#!/usr/bin/env python3
"""Validate HIT schema, catalog, and deterministic fixtures."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "hit-assessment.schema.json"
CATALOG_PATH = ROOT / "schema" / "hit-dimension-catalog.json"
FIXTURES_DIR = ROOT / "fixtures"
EXPECTED_DIMENSIONS = {"counsel", "judgment", "command", "correction", "repair", "reform"}


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"cannot load {path}: {exc}") from exc


def validate_fixture(validator: Draft202012Validator, path: Path) -> list[str]:
    instance = load_json(path)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    messages = [f"{path}: {error.message}" for error in errors]

    if not isinstance(instance, dict):
        return messages

    findings = instance.get("substantive_findings", [])
    dimensions = [item.get("dimension") for item in findings if isinstance(item, dict)]
    if set(dimensions) != EXPECTED_DIMENSIONS:
        messages.append(f"{path}: substantive findings must contain each of the six dimensions exactly once")
    if len(dimensions) != len(set(dimensions)):
        messages.append(f"{path}: duplicate substantive dimension finding")

    return messages


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    catalog = load_json(CATALOG_PATH)
    catalog_ids = {
        item["id"]
        for item in catalog.get("substantive_dimensions", [])
        if isinstance(item, dict) and "id" in item
    }
    failures: list[str] = []
    if catalog_ids != EXPECTED_DIMENSIONS:
        failures.append("dimension catalog does not contain exactly the six substantive dimensions")
    if catalog.get("cross_cutting_dimension", {}).get("id") != "telemetry_integrity":
        failures.append("dimension catalog must define Telemetry Integrity as the cross-cutting dimension")

    fixtures = sorted(FIXTURES_DIR.glob("*.json"))
    if len(fixtures) < 3:
        failures.append("at least three deterministic fixtures are required")

    for fixture in fixtures:
        failures.extend(validate_fixture(validator, fixture))

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print(f"HIT validation: PASS ({len(fixtures)} fixtures)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
