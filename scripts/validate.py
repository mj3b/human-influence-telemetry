#!/usr/bin/env python3
"""Validate the released HIT 0.4.0 contract, evidence, and governance artifacts."""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
RELEASE_VERSION = "0.4.0"
RELEASE_DATE = "2026-07-18"
SPECIFICATION_VERSION = "0.4.0"
SCHEMA_VERSION = "0.4.0"
CATALOG_VERSION = "0.4.0"
LEGACY_VERSION = "0.1.0"
ORIGINATING_DOI = "10.5281/zenodo.21204892"

SCHEMA_PATH = ROOT / "schema" / "hit-assessment.schema.json"
CATALOG_PATH = ROOT / "schema" / "hit-dimension-catalog.json"
EXAMPLE_PATH = ROOT / "fixtures" / "v0.4.0-canonical-example.json"
LEGACY_SCHEMA_PATH = ROOT / "archive" / "v0.1.0" / "schema" / "hit-assessment.schema.json"
MIGRATION_MANIFEST_PATH = ROOT / "case-studies" / "migrations" / "v0.4.0" / "migration-manifest.json"
PROTOCOL_LOCK_PATH = ROOT / "validation" / "protocol-lock.json"
CITATION_PATH = ROOT / "CITATION.cff"
ZENODO_PATH = ROOT / ".zenodo.json"

EXPECTED_DIMENSIONS = {"counsel", "judgment", "command", "correction", "repair", "reform"}
EXPECTED_EVIDENCE_STATES = {
    "affirmative_absence",
    "formal_presence",
    "operational_capability",
    "observed_exercise",
    "indeterminate",
}
EXPECTED_CASES = {
    "HIT-CASE-TOESLAGENAFFAIRE-HARM-2013-2019": (
        "case-studies/assessments/toeslagenaffaire-harm-period.json",
        "1f0a8099974ce0970df97d42cd4f10079e5e0e09",
    ),
    "HIT-CASE-OBERMEYER-DEPLOYERS-2019": (
        "case-studies/assessments/obermeyer-deployers.json",
        "2290b4504156a0eaff0c4c6939bd67f9ee269e00",
    ),
    "HIT-CASE-OBERMEYER-MANUFACTURER-2019": (
        "case-studies/assessments/obermeyer-manufacturer.json",
        "a0218f42e27afd8013af25c51ca3bc692ecab2a4",
    ),
    "HIT-CASE-CIGNA-PXDX-2022-2025": (
        "case-studies/assessments/cigna-pxdx.json",
        "e1a9458b656b103f0160d89c02fc6da5cacab746",
    ),
}

REQUIRED_FILES = {
    "README.md",
    "SPECIFICATION.md",
    "RESEARCH.md",
    "ROADMAP.md",
    "LIMITATIONS.md",
    "PROVENANCE.md",
    "CHANGELOG.md",
    "CITATION.cff",
    ".zenodo.json",
    "GOVERNANCE.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "LICENSE",
    "NOTICE",
    "docs/application-handbook.md",
    "docs/breaking-change-review-v0.4.0.md",
    "docs/migration-guide-v0.1.0-to-v0.4.0.md",
    "docs/adjacent-system-claim-audit-v0.4.0.md",
    "docs/releases/v0.4.0.md",
    "docs/decisions/ADR-0001-separate-semantic-versioning-from-research-maturity.md",
    "docs/decisions/ADR-0002-approve-v0.4.0-rubric-rules.md",
    "docs/decisions/ADR-0003-chronological-result-versioning.md",
    "schema/hit-assessment.schema.json",
    "schema/hit-dimension-catalog.json",
    "fixtures/v0.4.0-canonical-example.json",
    "fixtures/v0.4.0-boundaries/rubric-boundary-fixtures.json",
    "src/rubric/rules_v040.py",
    "case-studies/README.md",
    "case-studies/migrations/v0.4.0/migration-manifest.json",
    "validation/README.md",
    "validation/inter-rater-protocol.md",
    "validation/protocol-lock.json",
    "archive/v0.1.0/SPECIFICATION.md",
    "archive/v0.1.0/docs/application-handbook.md",
    "archive/v0.1.0/schema/hit-assessment.schema.json",
    "archive/v0.1.0/schema/hit-dimension-catalog.json",
    "archive/v0.2.1/scripts/validate.py",
}


def load_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise RuntimeError(f"cannot load {path}: {exc}") from exc


def load_json(path: Path) -> Any:
    try:
        return json.loads(load_text(path))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"cannot parse JSON {path}: {exc}") from exc


def load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(load_text(path))
    except yaml.YAMLError as exc:
        raise RuntimeError(f"cannot parse YAML {path}: {exc}") from exc


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    framed = f"blob {len(data)}\0".encode("utf-8") + data
    return hashlib.sha1(framed).hexdigest()


def schema_failures(validator: Draft202012Validator, instance: Any, label: str) -> list[str]:
    return [
        f"{label}: {error.message}"
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
    ]


def require_text(failures: list[str], relative_path: str, phrase: str) -> None:
    text = load_text(ROOT / relative_path)
    if phrase not in text:
        failures.append(f"{relative_path}: missing required text: {phrase}")


def validate_required_files() -> list[str]:
    failures: list[str] = []
    for relative_path in sorted(REQUIRED_FILES):
        path = ROOT / relative_path
        if not path.is_file():
            failures.append(f"required file is missing: {relative_path}")
        elif path.stat().st_size == 0:
            failures.append(f"required file is empty: {relative_path}")
    return failures


def validate_canonical_contract() -> list[str]:
    failures: list[str] = []
    schema = load_json(SCHEMA_PATH)
    catalog = load_json(CATALOG_PATH)
    example = load_json(EXAMPLE_PATH)

    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # pragma: no cover
        return [f"canonical schema is invalid: {exc}"]

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    failures.extend(schema_failures(validator, example, "canonical example"))

    if schema.get("properties", {}).get("schema_version", {}).get("const") != SCHEMA_VERSION:
        failures.append("canonical schema_version constant is inconsistent")
    if schema.get("properties", {}).get("specification_version", {}).get("const") != SPECIFICATION_VERSION:
        failures.append("canonical specification_version constant is inconsistent")
    if catalog.get("catalog_version") != CATALOG_VERSION:
        failures.append("dimension catalog version is inconsistent")
    if catalog.get("specification_version") != SPECIFICATION_VERSION:
        failures.append("dimension catalog specification version is inconsistent")

    dimensions = {item.get("id") for item in catalog.get("substantive_dimensions", []) if isinstance(item, dict)}
    if dimensions != EXPECTED_DIMENSIONS:
        failures.append("dimension catalog must contain each substantive dimension exactly once")
    states = {item.get("id") for item in catalog.get("evidence_states", []) if isinstance(item, dict)}
    if states != EXPECTED_EVIDENCE_STATES:
        failures.append("dimension catalog evidence states are inconsistent")

    findings = example.get("substantive_findings", [])
    finding_dimensions = [item.get("dimension") for item in findings if isinstance(item, dict)]
    if set(finding_dimensions) != EXPECTED_DIMENSIONS or len(finding_dimensions) != len(set(finding_dimensions)):
        failures.append("canonical example must contain each substantive dimension exactly once")

    claim_ids = {item.get("claim_id") for item in example.get("evidence_claims", []) if isinstance(item, dict)}
    actor_ids = {item.get("actor_id") for item in example.get("actors", []) if isinstance(item, dict)}
    for actor in example.get("actors", []):
        for claim_id in actor.get("evidence_claim_ids", []):
            if claim_id not in claim_ids:
                failures.append(f"actor references unknown evidence claim: {claim_id}")
        for actor_id in actor.get("related_actor_ids", []):
            if actor_id not in actor_ids:
                failures.append(f"actor references unknown related actor: {actor_id}")
    for claim in example.get("evidence_claims", []):
        for actor_id in claim.get("actor_ids", []):
            if actor_id not in actor_ids:
                failures.append(f"evidence claim references unknown actor: {actor_id}")
    for finding in findings:
        for field in ("supporting_claim_ids", "contradicting_claim_ids", "limiting_claim_ids"):
            for claim_id in finding.get(field, []):
                if claim_id not in claim_ids:
                    failures.append(f"finding references unknown evidence claim: {claim_id}")

    integrity = example.get("telemetry_integrity", {})
    statuses = {
        integrity.get("institutional_record_integrity", {}).get("status"),
        integrity.get("assessment_packet_integrity", {}).get("status"),
    }
    if "unreliable" in statuses:
        expected = "unreliable"
    elif "IE" in statuses:
        expected = "IE"
    elif "limited" in statuses:
        expected = "limited"
    else:
        expected = "adequate"
    if integrity.get("overall_status") != expected:
        failures.append("canonical example Telemetry Integrity derivation is inconsistent")

    negative = copy.deepcopy(example)
    negative["schema_version"] = "0.4.0-candidate"
    if not schema_failures(validator, negative, "negative candidate version"):
        failures.append("canonical schema accepted candidate schema_version")

    negative = copy.deepcopy(example)
    negative["substantive_findings"][0]["finding"] = 0
    negative["substantive_findings"][0]["evidence_state"] = "formal_presence"
    if not schema_failures(validator, negative, "negative zero state"):
        failures.append("canonical schema accepted finding 0 without affirmative absence")

    negative = copy.deepcopy(example)
    negative["substantive_findings"][4]["unresolved_proposition"] = None
    if not schema_failures(validator, negative, "negative IE proposition"):
        failures.append("canonical schema accepted IE without unresolved proposition")

    return failures


def validate_historical_cases() -> list[str]:
    failures: list[str] = []
    legacy_schema = load_json(LEGACY_SCHEMA_PATH)
    try:
        Draft202012Validator.check_schema(legacy_schema)
    except Exception as exc:  # pragma: no cover
        return [f"archived 0.1.0 schema is invalid: {exc}"]
    validator = Draft202012Validator(legacy_schema, format_checker=FormatChecker())
    manifest = load_json(MIGRATION_MANIFEST_PATH)
    manifest_cases = {
        item.get("assessment_id"): item
        for item in manifest.get("cases", [])
        if isinstance(item, dict)
    }
    if set(manifest_cases) != set(EXPECTED_CASES):
        failures.append("migration manifest must cover the four historical assessments exactly")
        return failures

    for assessment_id, (relative_path, expected_sha) in EXPECTED_CASES.items():
        path = ROOT / relative_path
        instance = load_json(path)
        failures.extend(schema_failures(validator, instance, relative_path))
        if instance.get("assessment_id") != assessment_id:
            failures.append(f"{relative_path}: assessment ID changed")
        if instance.get("schema_version") != LEGACY_VERSION:
            failures.append(f"{relative_path}: historical schema version changed")
        actual_sha = git_blob_sha(path)
        if actual_sha != expected_sha:
            failures.append(f"{relative_path}: historical blob changed; expected {expected_sha}, got {actual_sha}")
        manifest_item = manifest_cases[assessment_id]
        if manifest_item.get("original_blob_sha") != expected_sha:
            failures.append(f"{relative_path}: migration manifest SHA is inconsistent")
        if manifest_item.get("candidate_record_path") is not None:
            failures.append(f"{relative_path}: unsupported 0.4.0 candidate record claimed")
        if manifest_item.get("findings_changed") is not False:
            failures.append(f"{relative_path}: historical findings marked as changed")

    return failures


def validate_protocol() -> list[str]:
    failures: list[str] = []
    lock = load_json(PROTOCOL_LOCK_PATH)
    expected = {
        "protocol_id": "HIT-IRP-CIGNA-001",
        "protocol_version": "1.0.0",
        "target_repository_release": "0.3.0",
        "method_specification_version": "0.1.0",
        "assessment_schema_version": "0.1.0",
        "packet_id": "HIT-IR-CIGNA-PXDX-001",
        "status": "locked",
        "minimum_exact_agreements": 6,
        "minimum_exact_agreement_proportion": 0.8571,
        "critical_disagreements_allowed": 0,
        "required_scorers": 2,
        "author_may_score": False,
        "post_adjudication_rescoring_changes_primary_result": False,
        "failure_result_must_be_published": True,
    }
    for key, value in expected.items():
        if lock.get(key) != value:
            failures.append(f"protocol lock field changed: {key}")

    require_text(failures, "validation/README.md", "superseded under ADR-0003")
    require_text(failures, "validation/README.md", "next available repository version")
    require_text(failures, "docs/decisions/ADR-0003-chronological-result-versioning.md", "does not modify the protocol")

    results_dir = ROOT / "validation" / "results"
    unexpected = [path for path in results_dir.glob("*.json") if path.is_file()]
    if unexpected:
        failures.append("human result JSON exists before the locked exercise is complete")

    return failures


def validate_metadata_and_text() -> list[str]:
    failures: list[str] = []
    citation = load_yaml(CITATION_PATH)
    zenodo = load_json(ZENODO_PATH)

    if citation.get("version") != RELEASE_VERSION:
        failures.append("CITATION.cff version is inconsistent")
    if citation.get("date-released") != RELEASE_DATE:
        failures.append("CITATION.cff release date is inconsistent")
    if citation.get("license") != "Apache-2.0":
        failures.append("CITATION.cff license is inconsistent")
    identifiers = citation.get("identifiers", [])
    doi_values = {str(item.get("value")) for item in identifiers if isinstance(item, dict) and item.get("type") == "doi"}
    if doi_values != {ORIGINATING_DOI}:
        failures.append("CITATION.cff must contain only the originating research DOI until a software DOI exists")

    if zenodo.get("version") != RELEASE_VERSION:
        failures.append(".zenodo.json version is inconsistent")
    if zenodo.get("upload_type") != "software":
        failures.append(".zenodo.json upload_type is inconsistent")
    if zenodo.get("license") != "Apache-2.0":
        failures.append(".zenodo.json license is inconsistent")

    required_phrases = {
        "README.md": [
            "**Current release:** 0.4.0",
            "**Specification version:** 0.4.0",
            "**Assessment schema version:** 0.4.0",
            "**Current maturity:** Level 1, Defined",
            "No `0.4.0` case finding is claimed",
        ],
        "SPECIFICATION.md": [
            "**Version:** 0.4.0",
            "Affirmative absence",
            "Operational capability",
            "assessment-packet integrity",
            "next available repository version",
        ],
        "RESEARCH.md": ["H3", "Unresolved", "Release `0.4.0` remains Level 1"],
        "ROADMAP.md": ["0.4.0: Normative rubric stabilization", "0.5.0: Executable assessment conformance", "1.0.0: Stable public contract"],
        "PROVENANCE.md": ["Public repository release: 0.4.0", "No `0.4.0` public-case findings are claimed"],
        "CHANGELOG.md": ["## [0.4.0] - 2026-07-18", "breaking normative and data-contract release"],
        "docs/releases/v0.4.0.md": ["# Human Influence Telemetry v0.4.0", "Maturity Level 1"],
        "docs/adjacent-system-claim-audit-v0.4.0.md": ["Audit status:** Passed", "Microsoft Agent Governance Toolkit", "ScopeBlind/Acta", "Credo AI"],
    }
    for relative_path, phrases in required_phrases.items():
        for phrase in phrases:
            require_text(failures, relative_path, phrase)

    current_docs = ["README.md", "ROADMAP.md", "RESEARCH.md", "CHANGELOG.md", "validation/README.md"]
    for relative_path in current_docs:
        text = load_text(ROOT / relative_path)
        if "Release v0.3.0" in text or "targeted for repository release `v0.3.0`" in text:
            failures.append(f"{relative_path}: contains unsuperseded future v0.3.0 language")

    for relative_path in ("SPECIFICATION.md", "schema/hit-assessment.schema.json", "schema/hit-dimension-catalog.json", "docs/application-handbook.md"):
        text = load_text(ROOT / relative_path)
        if "0.4.0-candidate" in text or "not yet released" in text:
            failures.append(f"{relative_path}: candidate marker remains in canonical contract")

    return failures


def run_subvalidator(relative_path: str) -> list[str]:
    result = subprocess.run(
        [sys.executable, str(ROOT / relative_path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0:
        return []
    output = (result.stdout + "\n" + result.stderr).strip()
    return [f"{relative_path} failed:\n{output}"]


def main() -> int:
    failures: list[str] = []
    failures.extend(validate_required_files())
    if not failures:
        failures.extend(validate_canonical_contract())
        failures.extend(validate_historical_cases())
        failures.extend(validate_protocol())
        failures.extend(validate_metadata_and_text())
        failures.extend(run_subvalidator("scripts/validate_v040_boundaries.py"))
        failures.extend(run_subvalidator("scripts/validate_v040_migrations.py"))

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT 0.4.0 validation passed")
    print("- canonical specification/schema/catalog: 0.4.0")
    print("- canonical synthetic assessments: 1")
    print("- executable rubric boundary cases: 48")
    print("- historical 0.1.0 assessments preserved: 4")
    print("- locked human protocol: unchanged and pending")
    print("- research maturity: Level 1, Defined")
    print("- software DOI: pending")
    return 0


if __name__ == "__main__":
    sys.exit(main())
