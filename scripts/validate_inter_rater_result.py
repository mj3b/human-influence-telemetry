#!/usr/bin/env python3
"""Validate the HIT-IRP-CIGNA-001 empirical result package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RESULT_DIR = ROOT / "research" / "inter-rater" / "HIT-IRP-CIGNA-001"
COMPARISON_JSON = RESULT_DIR / "pre-adjudication-comparison.json"
COMPARISON_MD = RESULT_DIR / "pre-adjudication-comparison.md"
SUMMARY = RESULT_DIR / "result-summary.md"
ADJUDICATION = RESULT_DIR / "no-disagreement-adjudication.md"
DECISION = RESULT_DIR / "h3-maturity-decision.md"
INDEX = RESULT_DIR / "preservation-index.json"
RELEASE_NOTES = ROOT / "docs" / "releases" / "v0.6.0.md"

EXPECTED_PROTOCOL = "HIT-IRP-CIGNA-001"
EXPECTED_PACKET = "HIT-IR-CIGNA-PXDX-001"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise RuntimeError(f"cannot read {path.relative_to(ROOT)}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"cannot parse {path.relative_to(ROOT)}: {exc}") from exc


def require_file(path: Path, failures: list[str]) -> None:
    if not path.is_file():
        failures.append(f"missing result artifact: {path.relative_to(ROOT)}")
    elif path.stat().st_size == 0:
        failures.append(f"empty result artifact: {path.relative_to(ROOT)}")


def require_text(path: Path, phrases: list[str], failures: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in text:
            failures.append(f"{path.relative_to(ROOT)} is missing required text: {phrase}")


def validate_comparison(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    expected = {
        "protocol_id": EXPECTED_PROTOCOL,
        "protocol_version": "1.0.0",
        "packet_id": EXPECTED_PACKET,
        "scorer_a": "HIT-SCORER-A",
        "scorer_b": "HIT-SCORER-B",
        "items_compared": 7,
        "exact_agreements": 7,
        "exact_agreement_proportion": 1.0,
        "minimum_exact_agreements": 6,
        "critical_disagreement_count": 0,
        "disagreements": [],
        "substantive_dimension_cohens_kappa": None,
        "advancement_threshold_met": True,
    }
    for key, value in expected.items():
        if data.get(key) != value:
            failures.append(
                f"comparison field {key!r} is inconsistent: expected {value!r}, got {data.get(key)!r}"
            )
    boundary = data.get("interpretation_boundary")
    if not isinstance(boundary, str) or "one frozen packet" not in boundary:
        failures.append("comparison interpretation boundary is missing or too broad")
    return failures


def validate_index(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if data.get("protocol_id") != EXPECTED_PROTOCOL:
        failures.append("preservation index protocol ID is inconsistent")
    if data.get("packet_id") != EXPECTED_PACKET:
        failures.append("preservation index packet ID is inconsistent")

    manual = data.get("manual_submissions", [])
    if len(manual) != 3:
        failures.append("preservation index must contain three manual-file records")
    roles = {item.get("role") for item in manual if isinstance(item, dict)}
    expected_roles = {
        "superseded_original_incomplete",
        "locked_corrected_manual_submission",
        "locked_original_manual_submission",
    }
    if roles != expected_roles:
        failures.append("preservation index manual-file roles are incomplete")

    verified = data.get("verified_json_submissions", [])
    if len(verified) != 2:
        failures.append("preservation index must contain two verified JSON records")

    for group_name in ("manual_submissions", "verified_json_submissions"):
        for index, item in enumerate(data.get(group_name, [])):
            digest = item.get("sha256") if isinstance(item, dict) else None
            if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
                failures.append(f"{group_name}[{index}] has an invalid SHA-256 digest")

    outputs = data.get("comparison_outputs", {})
    for key in ("json_sha256", "markdown_sha256"):
        digest = outputs.get(key) if isinstance(outputs, dict) else None
        if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
            failures.append(f"comparison_outputs.{key} has an invalid SHA-256 digest")

    note = data.get("publication_note")
    if not isinstance(note, str) or "exact-byte review" not in note:
        failures.append("preservation index must disclose the pending exact-byte review")
    return failures


def main() -> int:
    failures: list[str] = []
    artifacts = (
        COMPARISON_JSON,
        COMPARISON_MD,
        SUMMARY,
        ADJUDICATION,
        DECISION,
        INDEX,
        RELEASE_NOTES,
    )
    for path in artifacts:
        require_file(path, failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    failures.extend(validate_comparison(load_json(COMPARISON_JSON)))
    failures.extend(validate_index(load_json(INDEX)))

    require_text(
        SUMMARY,
        ["7 of 7", "1.0000", "zero critical disagreements", "Maturity Level 2"],
        failures,
    )
    require_text(
        ADJUDICATION,
        ["Closed without substantive adjudication", "No finding required classification"],
        failures,
    )
    require_text(
        DECISION,
        ["H3 is supported for this bounded exercise", "Maturity Level 2, Applicable"],
        failures,
    )
    require_text(
        RELEASE_NOTES,
        [
            "Repository release: `0.6.0`",
            "Conformance engine: `0.5.0`",
            "Specification: `0.4.0`",
            "Locked scorer contract used by this exercise: `0.1.0`",
        ],
        failures,
    )

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT inter-rater result validation passed")
    print("- protocol: HIT-IRP-CIGNA-001")
    print("- exact agreement: 7/7")
    print("- critical disagreements: 0")
    print("- H3 decision: supported for bounded exercise")
    print("- maturity decision: Level 2, Applicable")
    print("- raw evidence publication: pending exact-byte review")
    return 0


if __name__ == "__main__":
    sys.exit(main())
