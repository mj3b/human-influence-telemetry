#!/usr/bin/env python3
"""Validate HIT v0.4.0 public-case migration dispositions."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = (
    ROOT
    / "schema"
    / "candidates"
    / "hit-case-migration-manifest-0.4.0-candidate.schema.json"
)
MANIFEST_PATH = (
    ROOT / "case-studies" / "migrations" / "v0.4.0" / "migration-manifest.json"
)
README_PATH = ROOT / "case-studies" / "migrations" / "v0.4.0" / "README.md"

EXPECTED = {
    "HIT-CASE-TOESLAGENAFFAIRE-HARM-2013-2019": (
        "case-studies/assessments/toeslagenaffaire-harm-period.json",
        "1f0a8099974ce0970df97d42cd4f10079e5e0e09",
        "historical_version_bound",
    ),
    "HIT-CASE-OBERMEYER-DEPLOYERS-2019": (
        "case-studies/assessments/obermeyer-deployers.json",
        "2290b4504156a0eaff0c4c6939bd67f9ee269e00",
        "historical_version_bound",
    ),
    "HIT-CASE-OBERMEYER-MANUFACTURER-2019": (
        "case-studies/assessments/obermeyer-manufacturer.json",
        "a0218f42e27afd8013af25c51ca3bc692ecab2a4",
        "historical_version_bound",
    ),
    "HIT-CASE-CIGNA-PXDX-2022-2025": (
        "case-studies/assessments/cigna-pxdx.json",
        "e1a9458b656b103f0160d89c02fc6da5cacab746",
        "deferred_locked_protocol",
    ),
}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise RuntimeError(f"cannot load {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"cannot parse JSON {path}: {exc}") from exc


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    framed = f"blob {len(data)}\0".encode("utf-8") + data
    return hashlib.sha1(framed).hexdigest()


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    cases = manifest.get("cases", [])
    by_id = {
        case.get("assessment_id"): case
        for case in cases
        if isinstance(case, dict)
    }
    if set(by_id) != set(EXPECTED):
        failures.append("migration manifest must cover the four released assessment IDs exactly")
        return failures
    if manifest.get("case_count") != len(cases):
        failures.append("migration manifest case_count does not match cases")
    if len(cases) != len(by_id):
        failures.append("migration manifest contains duplicate assessment IDs")

    for assessment_id, (relative_path, blob_sha, disposition) in EXPECTED.items():
        case = by_id[assessment_id]
        if case.get("path") != relative_path:
            failures.append(f"{assessment_id}: historical path changed")
        if case.get("original_blob_sha") != blob_sha:
            failures.append(f"{assessment_id}: recorded historical blob SHA changed")
        if case.get("disposition") != disposition:
            failures.append(f"{assessment_id}: migration disposition changed")
        if case.get("candidate_record_path") is not None:
            failures.append(f"{assessment_id}: candidate record claimed without fresh migration")
        if case.get("findings_changed") is not False:
            failures.append(f"{assessment_id}: historical findings may not be changed")
        if case.get("release_exception") is not True:
            failures.append(f"{assessment_id}: explicit release exception is required")

        historical_path = ROOT / relative_path
        if not historical_path.is_file():
            failures.append(f"{assessment_id}: historical assessment is missing")
            continue
        actual_sha = git_blob_sha(historical_path)
        if actual_sha != blob_sha:
            failures.append(
                f"{assessment_id}: historical artifact changed; expected {blob_sha}, got {actual_sha}"
            )
        historical = load_json(historical_path)
        if historical.get("assessment_id") != assessment_id:
            failures.append(f"{assessment_id}: file contains a different assessment ID")
        if historical.get("schema_version") != "0.1.0":
            failures.append(f"{assessment_id}: historical schema version changed")

    return failures


def validate_mutation_detection(manifest: dict[str, Any]) -> list[str]:
    failures: list[str] = []

    wrong_sha = copy.deepcopy(manifest)
    wrong_sha["cases"][0]["original_blob_sha"] = "0" * 40
    if not validate_manifest(wrong_sha):
        failures.append("migration validator failed to detect changed historical SHA")

    missing_case = copy.deepcopy(manifest)
    missing_case["cases"] = missing_case["cases"][:-1]
    missing_case["case_count"] = len(missing_case["cases"])
    if not validate_manifest(missing_case):
        failures.append("migration validator failed to detect missing case disposition")

    claimed_candidate = copy.deepcopy(manifest)
    claimed_candidate["cases"][0]["candidate_record_path"] = (
        "case-studies/migrations/v0.4.0/candidate.json"
    )
    if not validate_manifest(claimed_candidate):
        failures.append("migration validator failed to detect unsupported candidate claim")

    return failures


def validate_readme() -> list[str]:
    text = README_PATH.read_text(encoding="utf-8")
    failures: list[str] = []
    for required in (
        "immutable historical artifacts",
        "historical_version_bound",
        "deferred_locked_protocol",
        "prevent silent reinterpretation",
    ):
        if required not in text:
            failures.append(f"case migration README is missing: {required}")
    return failures


def main() -> int:
    failures: list[str] = []
    for path in (SCHEMA_PATH, MANIFEST_PATH, README_PATH):
        if not path.is_file():
            failures.append(f"missing migration artifact: {path.relative_to(ROOT)}")
        elif path.stat().st_size == 0:
            failures.append(f"empty migration artifact: {path.relative_to(ROOT)}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    schema = load_json(SCHEMA_PATH)
    manifest = load_json(MANIFEST_PATH)
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # pragma: no cover
        failures.append(f"migration manifest schema is invalid: {exc}")
    else:
        validator = Draft202012Validator(schema)
        for error in sorted(validator.iter_errors(manifest), key=lambda item: list(item.path)):
            failures.append(f"migration manifest: {error.message}")

    failures.extend(validate_manifest(manifest))
    failures.extend(validate_mutation_detection(manifest))
    failures.extend(validate_readme())

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT v0.4.0 case migration validation passed")
    print("- historical assessments preserved: 4")
    print("- historical version bounds: 3")
    print("- locked-protocol deferrals: 1")
    print("- candidate case findings claimed: 0")
    print("- mutation checks: 3")
    return 0


if __name__ == "__main__":
    sys.exit(main())
