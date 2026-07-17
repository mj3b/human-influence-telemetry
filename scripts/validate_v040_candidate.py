#!/usr/bin/env python3
"""Validate the isolated HIT v0.4.0 candidate contract without changing released v0.1.0 validation."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_DIR = ROOT / "schema" / "candidates"
SCHEMA_PATH = CANDIDATE_DIR / "hit-assessment-0.4.0-candidate.schema.json"
CATALOG_PATH = CANDIDATE_DIR / "hit-dimension-catalog-0.4.0-candidate.json"
EXAMPLE_PATH = CANDIDATE_DIR / "hit-assessment-0.4.0-candidate.example.json"
SPECIFICATION_PATH = ROOT / "specification" / "HIT-SPECIFICATION-v0.4.0-candidate.md"
HANDBOOK_PATH = ROOT / "docs" / "application-handbook-v0.4.0-candidate.md"
ADR_PATH = ROOT / "docs" / "decisions" / "ADR-0002-approve-v0.4.0-rubric-rules.md"

EXPECTED_DIMENSIONS = {
    "counsel",
    "judgment",
    "command",
    "correction",
    "repair",
    "reform",
}
EXPECTED_EVIDENCE_STATES = {
    "affirmative_absence",
    "formal_presence",
    "operational_capability",
    "observed_exercise",
    "indeterminate",
}
EXPECTED_INTEGRITY_STATUSES = {"adequate", "limited", "unreliable", "IE"}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise RuntimeError(f"cannot load {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"cannot parse JSON {path}: {exc}") from exc


def require_file(path: Path, failures: list[str]) -> None:
    if not path.is_file():
        failures.append(f"missing candidate artifact: {path.relative_to(ROOT)}")
    elif path.stat().st_size == 0:
        failures.append(f"empty candidate artifact: {path.relative_to(ROOT)}")


def schema_errors(validator: Draft202012Validator, instance: dict[str, Any]) -> list[str]:
    return [
        error.message
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
    ]


def expect_rejected(
    failures: list[str],
    validator: Draft202012Validator,
    label: str,
    instance: dict[str, Any],
) -> None:
    if not schema_errors(validator, instance):
        failures.append(f"candidate negative test accepted: {label}")


def expected_integrity_status(institutional: str, packet: str) -> str:
    statuses = {institutional, packet}
    if "unreliable" in statuses:
        return "unreliable"
    if "IE" in statuses:
        return "IE"
    if "limited" in statuses:
        return "limited"
    return "adequate"


def validate_catalog(catalog: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if catalog.get("catalog_version") != "0.4.0-candidate":
        failures.append("candidate catalog version is inconsistent")
    if catalog.get("governing_decision") != "ADR-0002":
        failures.append("candidate catalog does not identify ADR-0002")

    dimensions = {
        item.get("id")
        for item in catalog.get("substantive_dimensions", [])
        if isinstance(item, dict)
    }
    if dimensions != EXPECTED_DIMENSIONS:
        failures.append("candidate catalog must contain the six dimensions exactly once")

    states = {
        item.get("id")
        for item in catalog.get("evidence_states", [])
        if isinstance(item, dict)
    }
    if states != EXPECTED_EVIDENCE_STATES:
        failures.append("candidate catalog evidence-state set is inconsistent")

    findings = set(catalog.get("findings", {}))
    if findings != {"0", "1", "2", "IE"}:
        failures.append("candidate catalog finding set is inconsistent")

    integrity = catalog.get("telemetry_integrity", {})
    statuses = set(integrity.get("statuses", {})) if isinstance(integrity, dict) else set()
    if statuses != EXPECTED_INTEGRITY_STATUSES:
        failures.append("candidate catalog integrity-status set is inconsistent")

    return failures


def validate_references(instance: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    actors = instance.get("actors", [])
    claims = instance.get("evidence_claims", [])
    findings = instance.get("substantive_findings", [])

    actor_ids = [item.get("actor_id") for item in actors if isinstance(item, dict)]
    claim_ids = [item.get("claim_id") for item in claims if isinstance(item, dict)]
    dimensions = [item.get("dimension") for item in findings if isinstance(item, dict)]

    if len(actor_ids) != len(set(actor_ids)):
        failures.append("candidate example contains duplicate actor IDs")
    if len(claim_ids) != len(set(claim_ids)):
        failures.append("candidate example contains duplicate evidence-claim IDs")
    if set(dimensions) != EXPECTED_DIMENSIONS or len(dimensions) != 6:
        failures.append("candidate example must contain each substantive dimension exactly once")

    actor_id_set = set(actor_ids)
    claim_id_set = set(claim_ids)

    for actor in actors:
        for claim_id in actor.get("evidence_claim_ids", []):
            if claim_id not in claim_id_set:
                failures.append(f"actor references unknown evidence claim: {claim_id}")

    for claim in claims:
        for actor_id in claim.get("actor_ids", []):
            if actor_id not in actor_id_set:
                failures.append(f"evidence claim references unknown actor: {actor_id}")

    for finding in findings:
        for field in (
            "supporting_claim_ids",
            "contradicting_claim_ids",
            "limiting_claim_ids",
        ):
            for claim_id in finding.get(field, []):
                if claim_id not in claim_id_set:
                    failures.append(
                        f"{finding.get('dimension')} finding references unknown claim: {claim_id}"
                    )

    integrity = instance.get("telemetry_integrity", {})
    for component_name in (
        "institutional_record_integrity",
        "assessment_packet_integrity",
    ):
        component = integrity.get(component_name, {})
        for claim_id in component.get("evidence_claim_ids", []):
            if claim_id not in claim_id_set:
                failures.append(
                    f"{component_name} references unknown evidence claim: {claim_id}"
                )

    institutional = integrity.get("institutional_record_integrity", {}).get("status")
    packet = integrity.get("assessment_packet_integrity", {}).get("status")
    overall = integrity.get("overall_status")
    if institutional in EXPECTED_INTEGRITY_STATUSES and packet in EXPECTED_INTEGRITY_STATUSES:
        expected = expected_integrity_status(institutional, packet)
        if overall != expected:
            failures.append(
                f"candidate integrity derivation is inconsistent: expected {expected}, got {overall}"
            )

    return failures


def validate_documentation() -> list[str]:
    failures: list[str] = []
    required_text = {
        SPECIFICATION_PATH: [
            "**Candidate version:** `0.4.0`",
            "## 4. Governing evidence states",
            "## 7. Telemetry Integrity",
            "## 9. Actor and authority attribution",
        ],
        HANDBOOK_PATH: [
            "## 5. Classify the evidence state",
            "## 7. Apply dimension-specific procedures",
            "## 10. Assess Telemetry Integrity separately",
        ],
        ADR_PATH: [
            "**Status:** Accepted",
            "Approve the candidate v0.4.0 normative rules",
        ],
    }
    for path, phrases in required_text.items():
        text = path.read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                failures.append(f"{path.relative_to(ROOT)} is missing required text: {phrase}")
    return failures


def validate_negative_cases(
    validator: Draft202012Validator, example: dict[str, Any]
) -> list[str]:
    failures: list[str] = []

    wrong_zero = copy.deepcopy(example)
    wrong_zero["substantive_findings"][0]["finding"] = 0
    expect_rejected(failures, validator, "0 without affirmative absence", wrong_zero)

    wrong_one = copy.deepcopy(example)
    wrong_one["substantive_findings"][0]["finding"] = 1
    wrong_one["substantive_findings"][0]["evidence_state"] = "indeterminate"
    expect_rejected(failures, validator, "1 with indeterminate evidence", wrong_one)

    wrong_two = copy.deepcopy(example)
    wrong_two["substantive_findings"][0]["finding"] = 2
    wrong_two["substantive_findings"][0]["evidence_state"] = "formal_presence"
    expect_rejected(failures, validator, "2 with formal presence only", wrong_two)

    incomplete_ie = copy.deepcopy(example)
    repair = next(
        item for item in incomplete_ie["substantive_findings"] if item["dimension"] == "repair"
    )
    repair["unresolved_proposition"] = None
    expect_rejected(failures, validator, "IE without unresolved proposition", incomplete_ie)

    wrong_trigger = copy.deepcopy(example)
    wrong_trigger["substantive_findings"][0]["repair_trigger"] = "triggered"
    expect_rejected(failures, validator, "non-repair trigger", wrong_trigger)

    wrong_repair = copy.deepcopy(example)
    repair = next(
        item for item in wrong_repair["substantive_findings"] if item["dimension"] == "repair"
    )
    repair["finding"] = 1
    repair["evidence_state"] = "formal_presence"
    expect_rejected(failures, validator, "indeterminate repair trigger with determinate finding", wrong_repair)

    missing_locator = copy.deepcopy(example)
    missing_locator["evidence_claims"][0]["locator"].pop("value")
    expect_rejected(failures, validator, "evidence claim without locator", missing_locator)

    wrong_integrity = copy.deepcopy(example)
    wrong_integrity["telemetry_integrity"]["assessment_packet_integrity"]["status"] = "limited"
    wrong_integrity["telemetry_integrity"]["overall_status"] = "adequate"
    expect_rejected(failures, validator, "incorrect integrity derivation", wrong_integrity)

    return failures


def main() -> int:
    failures: list[str] = []
    for path in (
        SCHEMA_PATH,
        CATALOG_PATH,
        EXAMPLE_PATH,
        SPECIFICATION_PATH,
        HANDBOOK_PATH,
        ADR_PATH,
    ):
        require_file(path, failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    schema = load_json(SCHEMA_PATH)
    catalog = load_json(CATALOG_PATH)
    example = load_json(EXAMPLE_PATH)

    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # pragma: no cover - diagnostic boundary
        failures.append(f"candidate schema is invalid: {exc}")
        validator = None
    else:
        validator = Draft202012Validator(schema, format_checker=FormatChecker())

    if validator is not None:
        for error in schema_errors(validator, example):
            failures.append(f"candidate example: {error}")
        failures.extend(validate_negative_cases(validator, example))

    failures.extend(validate_catalog(catalog))
    failures.extend(validate_references(example))
    failures.extend(validate_documentation())

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT v0.4.0 candidate validation passed")
    print("- candidate schema: 0.4.0-candidate")
    print("- candidate catalog: 0.4.0-candidate")
    print("- substantive dimensions: 6")
    print("- evidence states: 5")
    print("- negative cases: 8")
    print("- released v0.1.0 artifacts unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
