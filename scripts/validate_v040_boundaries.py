#!/usr/bin/env python3
"""Validate HIT v0.4.0 candidate rubric boundary fixtures."""

from __future__ import annotations

import copy
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.rubric import evaluate_boundary_case

FIXTURE_SCHEMA_PATH = (
    ROOT
    / "schema"
    / "candidates"
    / "hit-rubric-boundary-fixture-0.4.0-candidate.schema.json"
)
FIXTURE_PATH = (
    ROOT / "fixtures" / "v0.4.0-boundaries" / "rubric-boundary-fixtures.json"
)
README_PATH = ROOT / "fixtures" / "v0.4.0-boundaries" / "README.md"

EXPECTED_FRICTIONS = {f"FR-{number:02d}" for number in range(1, 17)}
EXPECTED_ROLES = {"accepted", "rejected", "boundary"}
EXPECTED_CASE_COUNT = 48


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise RuntimeError(f"cannot load {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"cannot parse JSON {path}: {exc}") from exc


def schema_errors(
    validator: Draft202012Validator, instance: dict[str, Any]
) -> list[str]:
    return [
        error.message
        for error in sorted(
            validator.iter_errors(instance), key=lambda item: list(item.path)
        )
    ]


def validate_coverage(fixture_set: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    cases = fixture_set.get("cases", [])
    case_ids: list[str] = []
    roles_by_friction: dict[str, set[str]] = defaultdict(set)

    for case in cases:
        if not isinstance(case, dict):
            failures.append("boundary fixture case is not an object")
            continue
        case_id = str(case.get("case_id"))
        friction_id = str(case.get("friction_id"))
        role = str(case.get("role"))
        case_ids.append(case_id)
        roles_by_friction[friction_id].add(role)

        expected_suffix = {
            "accepted": "A",
            "rejected": "R",
            "boundary": "B",
        }.get(role)
        if expected_suffix and case_id != f"{friction_id}-{expected_suffix}":
            failures.append(
                f"{case_id}: case identifier does not match friction and role"
            )

    if len(case_ids) != len(set(case_ids)):
        failures.append("boundary fixture set contains duplicate case IDs")
    if len(cases) != EXPECTED_CASE_COUNT:
        failures.append(
            f"boundary fixture set must contain {EXPECTED_CASE_COUNT} cases"
        )
    if fixture_set.get("case_count") != len(cases):
        failures.append("boundary fixture case_count does not match cases")

    friction_ids = set(roles_by_friction)
    if friction_ids != EXPECTED_FRICTIONS:
        missing = sorted(EXPECTED_FRICTIONS - friction_ids)
        extra = sorted(friction_ids - EXPECTED_FRICTIONS)
        failures.append(
            f"boundary fixture friction coverage mismatch; missing={missing}, extra={extra}"
        )

    for friction_id in sorted(EXPECTED_FRICTIONS):
        roles = roles_by_friction.get(friction_id, set())
        if roles != EXPECTED_ROLES:
            failures.append(
                f"{friction_id}: expected roles {sorted(EXPECTED_ROLES)}, "
                f"got {sorted(roles)}"
            )

    return failures


def validate_expected_results(fixture_set: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    for case in fixture_set.get("cases", []):
        if not isinstance(case, dict):
            continue
        case_id = str(case.get("case_id"))
        friction_id = str(case.get("friction_id"))
        facts = case.get("facts", {})
        expected = case.get("expected", {})
        try:
            actual = evaluate_boundary_case(friction_id, facts)
        except (TypeError, ValueError) as exc:
            failures.append(f"{case_id}: evaluator failed: {exc}")
            continue
        if actual != expected:
            failures.append(
                f"{case_id}: expected {expected!r}, evaluator returned {actual!r}"
            )
    return failures


def validate_mutation_detection(fixture_set: dict[str, Any]) -> list[str]:
    """Confirm that changed expected output is detected by exact comparison."""
    failures: list[str] = []
    mutated = copy.deepcopy(fixture_set)
    first = mutated["cases"][0]
    original = first["expected"]
    first["expected"] = {"finding": "IE"} if original != {"finding": "IE"} else {"finding": 0}
    if not validate_expected_results(mutated):
        failures.append("boundary validator failed to detect a mutated expected result")

    missing_role = copy.deepcopy(fixture_set)
    missing_role["cases"] = [
        case for case in missing_role["cases"] if case["case_id"] != "FR-16-B"
    ]
    missing_role["case_count"] = len(missing_role["cases"])
    if not validate_coverage(missing_role):
        failures.append("boundary validator failed to detect missing role coverage")

    duplicate = copy.deepcopy(fixture_set)
    duplicate["cases"][-1]["case_id"] = duplicate["cases"][0]["case_id"]
    if not validate_coverage(duplicate):
        failures.append("boundary validator failed to detect duplicate case ID")

    return failures


def validate_readme() -> list[str]:
    failures: list[str] = []
    try:
        text = README_PATH.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"cannot load boundary fixture README: {exc}"]
    for required in (
        "exactly 48 cases",
        "one `accepted` case",
        "one `rejected` interpretation",
        "one `boundary` case",
        "do not establish empirical validity",
    ):
        if required not in text:
            failures.append(f"boundary fixture README is missing: {required}")
    return failures


def main() -> int:
    failures: list[str] = []
    for path in (FIXTURE_SCHEMA_PATH, FIXTURE_PATH, README_PATH):
        if not path.is_file():
            failures.append(f"missing boundary fixture artifact: {path.relative_to(ROOT)}")
        elif path.stat().st_size == 0:
            failures.append(f"empty boundary fixture artifact: {path.relative_to(ROOT)}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    schema = load_json(FIXTURE_SCHEMA_PATH)
    fixture_set = load_json(FIXTURE_PATH)

    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # pragma: no cover - diagnostic boundary
        failures.append(f"boundary fixture schema is invalid: {exc}")
    else:
        validator = Draft202012Validator(schema)
        for error in schema_errors(validator, fixture_set):
            failures.append(f"boundary fixture set: {error}")

    failures.extend(validate_coverage(fixture_set))
    failures.extend(validate_expected_results(fixture_set))
    failures.extend(validate_mutation_detection(fixture_set))
    failures.extend(validate_readme())

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT v0.4.0 boundary fixture validation passed")
    print("- friction classes: 16")
    print("- accepted cases: 16")
    print("- rejected cases: 16")
    print("- boundary cases: 16")
    print("- total executable cases: 48")
    print("- mutation checks: 3")
    return 0


if __name__ == "__main__":
    sys.exit(main())
