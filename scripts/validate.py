#!/usr/bin/env python3
"""Validate HIT schemas, fixtures, public cases, metadata, and release files."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "hit-assessment.schema.json"
CATALOG_PATH = ROOT / "schema" / "hit-dimension-catalog.json"
FIXTURES_DIR = ROOT / "fixtures"
CASE_STUDIES_DIR = ROOT / "case-studies"
CASE_ASSESSMENTS_DIR = CASE_STUDIES_DIR / "assessments"
CITATION_PATH = ROOT / "CITATION.cff"
ZENODO_PATH = ROOT / ".zenodo.json"
EXPECTED_VERSION = "0.1.0"
EXPECTED_DIMENSIONS = {"counsel", "judgment", "command", "correction", "repair", "reform"}
EXPECTED_CASE_ASSESSMENT_IDS = {
    "HIT-CASE-TOESLAGENAFFAIRE-HARM-2013-2019",
    "HIT-CASE-OBERMEYER-DEPLOYERS-2019",
    "HIT-CASE-OBERMEYER-MANUFACTURER-2019",
    "HIT-CASE-CIGNA-PXDX-2022-2025",
}
ORIGINATING_CONCEPT_DOI = "10.5281/zenodo.21204892"
REQUIRED_RELEASE_FILES = {
    "README.md",
    "SPECIFICATION.md",
    "RESEARCH.md",
    "ROADMAP.md",
    "PROVENANCE.md",
    "LIMITATIONS.md",
    "CHANGELOG.md",
    "GOVERNANCE.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "LICENSE",
    "NOTICE",
    "CITATION.cff",
    ".zenodo.json",
    "case-studies/README.md",
    "case-studies/toeslagenaffaire.md",
    "case-studies/obermeyer.md",
    "case-studies/cigna-pxdx.md",
    "docs/application-handbook.md",
    "docs/doi-and-release-strategy.md",
    "docs/releases/v0.1.0.md",
}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"cannot load {path}: {exc}") from exc


def load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise RuntimeError(f"cannot load {path}: {exc}") from exc


def validate_finding_set(instance: dict[str, Any], label: str) -> list[str]:
    messages: list[str] = []
    findings = instance.get("substantive_findings", [])
    dimensions = [item.get("dimension") for item in findings if isinstance(item, dict)]
    if set(dimensions) != EXPECTED_DIMENSIONS:
        messages.append(f"{label}: substantive findings must contain each dimension exactly once")
    if len(dimensions) != len(set(dimensions)):
        messages.append(f"{label}: duplicate substantive dimension finding")
    return messages


def validate_assessment(
    validator: Draft202012Validator, path: Path
) -> tuple[list[str], dict[str, Any] | None]:
    instance = load_json(path)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    messages = [f"{path}: {error.message}" for error in errors]

    if not isinstance(instance, dict):
        return messages, None

    messages.extend(validate_finding_set(instance, str(path)))
    return messages, instance


def is_rejected(validator: Draft202012Validator, instance: dict[str, Any]) -> bool:
    return bool(list(validator.iter_errors(instance)) or validate_finding_set(instance, "negative test"))


def validate_negative_cases(
    validator: Draft202012Validator, source: dict[str, Any]
) -> list[str]:
    failures: list[str] = []

    duplicate_dimension = copy.deepcopy(source)
    duplicate_dimension["substantive_findings"][-1]["dimension"] = "counsel"
    if not is_rejected(validator, duplicate_dimension):
        failures.append("negative test: duplicate substantive dimension was accepted")

    missing_integrity = copy.deepcopy(source)
    missing_integrity.pop("telemetry_integrity", None)
    if not is_rejected(validator, missing_integrity):
        failures.append("negative test: missing Telemetry Integrity was accepted")

    wrong_version = copy.deepcopy(source)
    wrong_version["schema_version"] = "9.9.9"
    if not is_rejected(validator, wrong_version):
        failures.append("negative test: wrong schema version was accepted")

    invalid_finding = copy.deepcopy(source)
    invalid_finding["substantive_findings"][0]["finding"] = 3
    if not is_rejected(validator, invalid_finding):
        failures.append("negative test: out-of-range finding was accepted")

    return failures


def validate_release_files() -> list[str]:
    failures: list[str] = []
    for relative_path in sorted(REQUIRED_RELEASE_FILES):
        path = ROOT / relative_path
        if not path.is_file():
            failures.append(f"required release file is missing: {relative_path}")
        elif path.stat().st_size == 0:
            failures.append(f"required release file is empty: {relative_path}")
    return failures


def validate_metadata(schema: dict[str, Any], catalog: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    citation = load_yaml(CITATION_PATH)
    zenodo = load_json(ZENODO_PATH)

    if not isinstance(citation, dict):
        return ["CITATION.cff must contain a YAML mapping"]
    if not isinstance(zenodo, dict):
        return [".zenodo.json must contain a JSON object"]

    if citation.get("cff-version") != "1.2.0":
        failures.append("CITATION.cff must use CFF 1.2.0")
    if citation.get("title") != "Human Influence Telemetry":
        failures.append("CITATION.cff title is inconsistent")
    if citation.get("version") != EXPECTED_VERSION:
        failures.append("CITATION.cff version is inconsistent")
    if citation.get("license") != "Apache-2.0":
        failures.append("CITATION.cff license is inconsistent")

    identifiers = citation.get("identifiers", [])
    citation_dois = {
        str(identifier.get("value"))
        for identifier in identifiers
        if isinstance(identifier, dict) and identifier.get("type") == "doi"
    }
    if ORIGINATING_CONCEPT_DOI not in citation_dois:
        failures.append("CITATION.cff must identify the originating research DOI")

    if zenodo.get("title") != "Human Influence Telemetry":
        failures.append(".zenodo.json title is inconsistent")
    if zenodo.get("version") != EXPECTED_VERSION:
        failures.append(".zenodo.json version is inconsistent")
    if zenodo.get("upload_type") != "software":
        failures.append(".zenodo.json upload_type must be software")
    if zenodo.get("license") != "Apache-2.0":
        failures.append(".zenodo.json license is inconsistent")

    related_identifiers = zenodo.get("related_identifiers", [])
    related_values = {
        str(identifier.get("identifier"))
        for identifier in related_identifiers
        if isinstance(identifier, dict)
    }
    if f"https://doi.org/{ORIGINATING_CONCEPT_DOI}" not in related_values:
        failures.append(".zenodo.json must relate the software to the originating research DOI")

    schema_version = schema.get("properties", {}).get("schema_version", {}).get("const")
    if schema_version != EXPECTED_VERSION:
        failures.append("assessment schema version is inconsistent")
    if catalog.get("catalog_version") != EXPECTED_VERSION:
        failures.append("dimension catalog version is inconsistent")

    return failures


def main() -> int:
    failures = validate_release_files()

    schema = load_json(SCHEMA_PATH)
    if not isinstance(schema, dict):
        raise RuntimeError("assessment schema must be a JSON object")
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    catalog = load_json(CATALOG_PATH)
    if not isinstance(catalog, dict):
        raise RuntimeError("dimension catalog must be a JSON object")

    catalog_ids = {
        item["id"]
        for item in catalog.get("substantive_dimensions", [])
        if isinstance(item, dict) and "id" in item
    }
    if catalog_ids != EXPECTED_DIMENSIONS:
        failures.append("dimension catalog does not contain exactly the six substantive dimensions")
    if catalog.get("cross_cutting_dimension", {}).get("id") != "telemetry_integrity":
        failures.append("dimension catalog must define Telemetry Integrity as cross-cutting")

    fixtures = sorted(FIXTURES_DIR.glob("*.json"))
    if len(fixtures) < 3:
        failures.append("at least three deterministic fixtures are required")

    valid_fixtures: list[dict[str, Any]] = []
    for fixture in fixtures:
        fixture_failures, instance = validate_assessment(validator, fixture)
        failures.extend(fixture_failures)
        if instance is not None and not fixture_failures:
            valid_fixtures.append(instance)

    case_assessments = sorted(CASE_ASSESSMENTS_DIR.glob("*.json"))
    if len(case_assessments) < 4:
        failures.append("at least four actor-specific public case assessments are required")

    observed_case_ids: set[str] = set()
    for case_path in case_assessments:
        case_failures, instance = validate_assessment(validator, case_path)
        failures.extend(case_failures)
        if instance is not None:
            assessment_id = instance.get("assessment_id")
            if isinstance(assessment_id, str):
                if assessment_id in observed_case_ids:
                    failures.append(f"duplicate public case assessment_id: {assessment_id}")
                observed_case_ids.add(assessment_id)

    if observed_case_ids != EXPECTED_CASE_ASSESSMENT_IDS:
        failures.append("public case assessment IDs do not match the expected evidence pack")

    if valid_fixtures:
        failures.extend(validate_negative_cases(validator, valid_fixtures[0]))
    else:
        failures.append("negative tests could not run because no valid fixture was available")

    failures.extend(validate_metadata(schema, catalog))

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print(
        "HIT validation: PASS "
        f"({len(fixtures)} fixtures, {len(case_assessments)} public case assessments, "
        "4 negative tests, release metadata synchronized)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
