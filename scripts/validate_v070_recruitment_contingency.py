#!/usr/bin/env python3
"""Validate HIT v0.7.0 recruitment contingency boundaries."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "validation" / "v0.7.0" / "recruitment-contingency.json"
DOC = ROOT / "validation" / "v0.7.0" / "recruitment-contingency.md"
LOCK = ROOT / "validation" / "v0.7.0" / "protocol-lock.candidate.json"

REQUIRED_PROHIBITIONS = {
    "author_as_independent_scorer",
    "same_person_as_multiple_scorers",
    "model_output_as_human_submission",
    "author_assessment_as_independent_submission",
    "consensus_without_preserved_independent_ratings",
    "threshold_change_after_unsealing",
    "packet_or_scorer_removal_for_low_agreement",
    "maturity_level_3_from_author_scored_cases_only",
    "schema_validity_as_human_reliability",
    "clean_room_usability_as_inter_rater_agreement",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    failures: list[str] = []
    for path in (RECORD, DOC, LOCK):
        if not path.is_file() or path.stat().st_size == 0:
            failures.append(f"missing or empty: {path.relative_to(ROOT)}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    record = load(RECORD)
    lock = load(LOCK)

    if record.get("record_id") != "HIT-IRP-HIT040-002-RECRUITMENT-CONTINGENCY-001":
        failures.append("contingency record ID changed")
    if record.get("protocol_id") != "HIT-IRP-HIT040-002":
        failures.append("contingency protocol ID changed")
    if record.get("status") != "candidate":
        failures.append("contingency must remain candidate")

    design = record.get("current_design", {})
    expected_design = {
        "packets": 3,
        "common_independent_scorers": 3,
        "required_submissions": 9,
        "scoring_permitted": False,
    }
    if design != expected_design:
        failures.append("current fixed design was weakened or changed")

    boundary = record.get("hard_boundary", {})
    for key in (
        "zero_rater_substitute_exists",
        "zero_independent_scorers_supports_h3_replication",
        "zero_independent_scorers_supports_maturity_level_3",
    ):
        if boundary.get(key) is not False:
            failures.append(f"hard zero-rater boundary weakened: {key}")

    tiers = {item.get("tier"): item for item in record.get("fallback_tiers", [])}
    if set(tiers) != {"A", "B", "C", "D", "E"}:
        failures.append("fallback tier set changed")
    else:
        for tier in ("B", "C", "D"):
            if tiers[tier].get("requires_protocol_change") is not True:
                failures.append(f"tier {tier} must require protocol change")
            if tiers[tier].get("permitted") is not False:
                failures.append(f"tier {tier} may not be activated by this record")

    prohibitions = set(record.get("prohibited_substitutions", []))
    if prohibitions != REQUIRED_PROHIBITIONS:
        failures.append("prohibited substitution set changed")

    activation = record.get("activation_rules", {})
    for key in (
        "substantive_scores_must_be_sealed_before_change",
        "numbered_amendment_or_new_protocol_required",
        "revised_estimands_and_denominators_required",
        "revised_thresholds_required",
        "recruitment_failure_must_be_published",
        "loss_of_generalizability_must_be_stated",
    ):
        if activation.get(key) is not True:
            failures.append(f"activation safeguard weakened: {key}")

    consequence = record.get("current_consequence", {})
    for key in (
        "changes_protocol",
        "assigns_cases",
        "assigns_packet_ids",
        "permits_recruitment",
        "permits_scoring",
    ):
        if consequence.get(key) is not False:
            failures.append(f"candidate contingency activated forbidden consequence: {key}")

    if lock.get("status") != "candidate":
        failures.append("protocol lock must remain candidate")
    if lock.get("scoring_permitted") is not False:
        failures.append("protocol must continue to prohibit scoring")
    if lock.get("required_scorers") != 3:
        failures.append("required scorer count changed")
    if lock.get("required_submissions") != 9:
        failures.append("required submission count changed")

    doc = DOC.read_text(encoding="utf-8")
    for phrase in (
        "does not have a zero-rater substitute",
        "zero independent scorers means no current-contract inter-rater result",
        "model outputs as human submissions",
        "Maturity Level 3 remains pending",
        "does not change `HIT-IRP-HIT040-002`",
    ):
        if phrase not in doc:
            failures.append(f"contingency document missing required boundary: {phrase}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT v0.7.0 recruitment contingency validation passed")
    print("- fixed design preserved: 3 scorers x 3 packets")
    print("- zero-rater substitute: none")
    print("- reduced designs activated: none")
    print("- recruitment permitted: no")
    print("- scoring permitted: no")
    return 0


if __name__ == "__main__":
    sys.exit(main())
