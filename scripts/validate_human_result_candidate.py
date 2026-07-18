#!/usr/bin/env python3
"""Validate the staged HIT-IRP-CIGNA-001 result candidate."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "validation" / "results" / "HIT-IRP-CIGNA-001"
SCHEMA = ROOT / "validation" / "scorer-submission.schema.json"
COMPARE = ROOT / "scripts" / "compare_raters.py"
REQUIRED = {
    "README.md",
    "adjudication-record.md",
    "claim-maturity-decision.md",
    "execution-record.json",
    "manual-originals-manifest.json",
    "pre-adjudication-comparison.json",
    "pre-adjudication-comparison.md",
    "preservation-manifest.json",
    "receipt-register.json",
    "transcription-verifications.json",
    "submissions/HIT-IR-SCORER-A.json",
    "submissions/HIT-IR-SCORER-B.json",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_compare_module():
    spec = importlib.util.spec_from_file_location("hit_compare", COMPARE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load compare_raters.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    failures: list[str] = []
    for relative in sorted(REQUIRED):
        path = PKG / relative
        if not path.is_file():
            failures.append(f"missing candidate artifact: {relative}")
        elif path.stat().st_size == 0:
            failures.append(f"empty candidate artifact: {relative}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    schema = load(SCHEMA)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    compare = load_compare_module()

    try:
        scorer_a = compare.validate_submission(
            load(PKG / "submissions" / "HIT-IR-SCORER-A.json"), validator, "A"
        )
        scorer_b = compare.validate_submission(
            load(PKG / "submissions" / "HIT-IR-SCORER-B.json"), validator, "B"
        )
        recomputed = compare.compare_submissions(scorer_a, scorer_b)
    except Exception as exc:
        failures.append(f"submission or comparison validation failed: {exc}")
        recomputed = {}

    published = load(PKG / "pre-adjudication-comparison.json")
    if recomputed != published:
        failures.append("published comparison differs from deterministic recomputation")

    expected = {
        "exact_agreements": 7,
        "items_compared": 7,
        "exact_agreement_proportion": 1.0,
        "critical_disagreement_count": 0,
        "advancement_threshold_met": True,
        "disagreements": [],
        "substantive_dimension_cohens_kappa": None,
    }
    for key, value in expected.items():
        if published.get(key) != value:
            failures.append(f"comparison field inconsistent: {key}")

    confirmations = {
        item.get("scorer_public_id"): item.get("confirmation")
        for item in load(PKG / "transcription-verifications.json").get("confirmations", [])
    }
    if confirmations != {
        "HIT-SCORER-A": "Confirmed exact.",
        "HIT-SCORER-B": "Confirmed exact.",
    }:
        failures.append("scorer transcription confirmations are incomplete")

    originals = load(PKG / "manual-originals-manifest.json")
    if originals.get("release_blocking") is not True:
        failures.append("manual-original publication gate must remain explicit")
    if len(originals.get("files", [])) != 3:
        failures.append("manual-original manifest must identify three files")

    preservation = load(PKG / "preservation-manifest.json")
    staged = set(preservation.get("text_artifacts", []))
    expected_staged = REQUIRED - {"preservation-manifest.json"}
    if staged != expected_staged:
        failures.append("candidate preservation manifest file set is inconsistent")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT human-result candidate validation passed")
    print("- verified scorer submissions: 2")
    print("- exact agreements: 7/7")
    print("- critical disagreements: 0")
    print("- advancement threshold: met")
    print("- release-blocking binary originals: 3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
