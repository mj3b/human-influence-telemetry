#!/usr/bin/env python3
"""Validate the HIT 0.7.0 current-contract replication candidate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "validation" / "v0.7.0"

REQUIRED = {
    BASE / "README.md",
    BASE / "protocol-candidate.md",
    BASE / "protocol-lock.candidate.json",
    BASE / "submission-manifest.schema.json",
    BASE / "comparison-plan.md",
    BASE / "case-selection-register.md",
    BASE / "frozen-packet" / "source-manifest.schema.json",
    BASE / "frozen-packet" / "decision-boundary-template.md",
    ROOT / "docs" / "releases" / "v0.7.0-candidate.md",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def require_text(failures: list[str], path: Path, phrases: tuple[str, ...]) -> None:
    content = path.read_text(encoding="utf-8")
    for phrase in phrases:
        if phrase not in content:
            failures.append(f"{path.relative_to(ROOT)}: missing text: {phrase}")


def main() -> int:
    failures: list[str] = []

    for path in sorted(REQUIRED):
        if not path.is_file():
            failures.append(f"missing file: {path.relative_to(ROOT)}")
        elif path.stat().st_size == 0:
            failures.append(f"empty file: {path.relative_to(ROOT)}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    for schema_path in (
        BASE / "submission-manifest.schema.json",
        BASE / "frozen-packet" / "source-manifest.schema.json",
    ):
        try:
            Draft202012Validator.check_schema(load_json(schema_path))
        except Exception as exc:
            failures.append(f"invalid schema {schema_path.relative_to(ROOT)}: {exc}")

    lock = load_json(BASE / "protocol-lock.candidate.json")
    expected = {
        "protocol_id": "HIT-IRP-HIT040-002",
        "protocol_version": "0.1.0-candidate",
        "target_repository_release": "0.7.0",
        "status": "candidate",
        "scoring_permitted": False,
        "method_specification_version": "0.4.0",
        "assessment_schema_version": "0.4.0",
        "dimension_catalog_version": "0.4.0",
        "application_handbook_version": "0.4.0",
        "conformance_engine_version": "0.5.0",
        "required_scorers": 3,
        "required_packets": 3,
        "required_submissions": 9,
        "primary_items_per_packet": 8,
        "packet_item_units": 24,
        "pairwise_comparisons": 72,
        "minimum_pooled_pairwise_exact_agreements": 60,
        "minimum_packet_pairwise_exact_agreements": 19,
        "minimum_unanimous_packet_items": 18,
        "critical_disagreements_allowed": 0,
        "author_may_score": False,
        "generative_ai_substantive_assistance_allowed": False,
        "post_adjudication_changes_primary_result": False,
        "failure_result_must_be_published": True,
    }
    for key, value in expected.items():
        if lock.get(key) != value:
            failures.append(f"protocol lock field {key!r} is {lock.get(key)!r}; expected {value!r}")

    if lock.get("packet_ids") != []:
        failures.append("candidate lock must not contain packet IDs before case selection")
    remaining = lock.get("lock_conditions_remaining")
    if not isinstance(remaining, list) or len(remaining) < 5:
        failures.append("candidate lock must name unresolved lock conditions")

    computed = {
        "required_submissions": lock.get("required_scorers", 0) * lock.get("required_packets", 0),
        "packet_item_units": lock.get("required_packets", 0) * lock.get("primary_items_per_packet", 0),
        "pairwise_comparisons": (
            lock.get("required_packets", 0)
            * lock.get("primary_items_per_packet", 0)
            * (lock.get("required_scorers", 0) * (lock.get("required_scorers", 0) - 1) // 2)
        ),
    }
    for key, value in computed.items():
        if lock.get(key) != value:
            failures.append(f"protocol arithmetic mismatch for {key}: {lock.get(key)} != {value}")

    require_text(
        failures,
        BASE / "protocol-candidate.md",
        (
            "three independent reviewers",
            "nine submissions",
            "72 pairwise comparisons",
            "generative-model assistance",
            "All results are published",
            "Maturity Level 3 and the H3 replication result are separate decisions",
            "Scoring is prohibited",
        ),
    )
    require_text(
        failures,
        BASE / "comparison-plan.md",
        (
            "pooled pairwise exact agreement",
            "packet-level pairwise exact agreement",
            "item unanimity",
            "Krippendorff's alpha",
            "No threshold is recalculated after adjudication",
        ),
    )
    require_text(
        failures,
        BASE / "case-selection-register.md",
        (
            "exercise-rich",
            "constraint-rich",
            "evidence-limited",
            "No case has been selected",
            "Scorer recruitment and scoring remain blocked",
        ),
    )
    require_text(
        failures,
        ROOT / "docs" / "releases" / "v0.7.0-candidate.md",
        (
            "full study contract before any scorer begins",
            "scoring_permitted: true",
            "does not itself establish new human agreement evidence",
        ),
    )

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT 0.7.0 current-contract replication candidate validation passed")
    print("- protocol: HIT-IRP-HIT040-002")
    print("- status: candidate; scoring prohibited")
    print("- design: 3 scorers x 3 packets = 9 submissions")
    print("- primary comparison: 24 packet-items and 72 pairwise comparisons")
    print("- selected packets: 0 of 3")
    return 0


if __name__ == "__main__":
    sys.exit(main())
