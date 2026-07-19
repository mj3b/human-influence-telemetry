#!/usr/bin/env python3
"""Validate the human-governed HIT v0.7.0 source-audit workstream."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "validation" / "v0.7.0" / "source-audit"
SCHEMA_PATH = BASE / "candidate-source-audit.schema.json"
DECISION_PATH = BASE / "human-selection-decision.md"

EXPECTED = {
    "HIT-CAND-A1-DUKE-SEPSIS": "exercise-rich",
    "HIT-CAND-A2-ALLEGHENY-AFST": "exercise-rich",
    "HIT-CAND-B1-HOUSTON-EVAAS": "constraint-rich",
    "HIT-CAND-B2-ROBODEBT": "constraint-rich",
    "HIT-CAND-C1-MOBLEY-WORKDAY": "evidence-limited",
    "HIT-CAND-C2-EPIC-SEPSIS": "evidence-limited",
}

PROHIBITED_TERMS = (
    '"expected_finding"',
    '"predicted_finding"',
    '"recommended_selection"',
    '"packet_id": "HIT-IR-HIT040-PKT-',
)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    failures: list[str] = []

    required = (BASE / "README.md", SCHEMA_PATH, DECISION_PATH)
    for path in required:
        if not path.is_file() or path.stat().st_size == 0:
            failures.append(f"missing or empty file: {path.relative_to(ROOT)}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    schema = load_json(SCHEMA_PATH)
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        failures.append(f"invalid source-audit schema: {exc}")
        validator = None
    else:
        validator = Draft202012Validator(schema, format_checker=FormatChecker())

    candidate_dir = BASE / "candidates"
    files = sorted(candidate_dir.glob("*.json"))
    records: dict[str, dict[str, Any]] = {}

    for path in files:
        raw = path.read_text(encoding="utf-8")
        for term in PROHIBITED_TERMS:
            if term in raw:
                failures.append(f"{path.relative_to(ROOT)} contains prohibited term: {term}")
        try:
            record = json.loads(raw)
        except Exception as exc:
            failures.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")
            continue
        candidate_id = record.get("candidate_id")
        if candidate_id in records:
            failures.append(f"duplicate candidate ID: {candidate_id}")
        records[candidate_id] = record
        if validator is not None:
            for error in sorted(validator.iter_errors(record), key=lambda item: list(item.path)):
                failures.append(f"{path.relative_to(ROOT)}: {error.message}")

    if set(records) != set(EXPECTED):
        failures.append("source audit must contain exactly the six declared candidates")

    slot_counts = {"exercise-rich": 0, "constraint-rich": 0, "evidence-limited": 0}
    for candidate_id, expected_slot in EXPECTED.items():
        record = records.get(candidate_id)
        if record is None:
            continue
        if record.get("slot") != expected_slot:
            failures.append(f"{candidate_id}: slot changed")
        slot_counts[expected_slot] += 1
        if record.get("decision_status") != "pending_human_selection":
            failures.append(f"{candidate_id}: automated selection is prohibited")
        if record.get("packet_id") is not None:
            failures.append(f"{candidate_id}: packet ID assigned before human selection")
        if record.get("expected_findings_recorded") is not False:
            failures.append(f"{candidate_id}: expected findings must not be recorded")
        human = record.get("human_decision", {})
        if human != {
            "decision": "pending",
            "rationale": None,
            "decided_by": None,
            "decided_at": None,
        }:
            failures.append(f"{candidate_id}: human decision must remain pending in this increment")
        sources = record.get("sources", [])
        if not sources:
            failures.append(f"{candidate_id}: at least one identified source is required")
        for source in sources:
            if source.get("source_status") != "identified_not_audited":
                failures.append(f"{candidate_id}/{source.get('source_id')}: source audit was completed without a human record")
            if source.get("human_audit_required") is not True:
                failures.append(f"{candidate_id}/{source.get('source_id')}: human audit flag weakened")

    if slot_counts != {"exercise-rich": 2, "constraint-rich": 2, "evidence-limited": 2}:
        failures.append(f"candidate slot distribution incorrect: {slot_counts}")

    decision = DECISION_PATH.read_text(encoding="utf-8")
    for phrase in (
        "Decision status:** Pending",
        "language model selected the cases",
        "Completing this record authorizes packet-ID allocation and packet construction only",
    ):
        if phrase not in decision:
            failures.append(f"human selection decision is missing required control text: {phrase}")

    protocol_lock = load_json(ROOT / "validation" / "v0.7.0" / "protocol-lock.candidate.json")
    if protocol_lock.get("status") != "candidate" or protocol_lock.get("scoring_permitted") is not False:
        failures.append("source-audit increment must not activate scoring")
    if protocol_lock.get("packet_ids") != []:
        failures.append("source-audit increment must not assign packet IDs")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT v0.7.0 source-audit staging validation passed")
    print("- candidates: 6")
    print("- slots: 2 exercise-rich, 2 constraint-rich, 2 evidence-limited")
    print("- human selection decisions: 0")
    print("- packet IDs assigned: 0")
    print("- scoring permitted: no")
    return 0


if __name__ == "__main__":
    sys.exit(main())
