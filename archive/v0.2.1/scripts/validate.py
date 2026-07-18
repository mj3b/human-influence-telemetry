#!/usr/bin/env python3
"""Validate HIT schemas, evidence packs, evaluation artifacts, metadata, and releases."""

from __future__ import annotations

import copy
import json
import subprocess
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

VALIDATION_DIR = ROOT / "validation"
PROTOCOL_PATH = VALIDATION_DIR / "inter-rater-protocol.md"
PROTOCOL_LOCK_PATH = VALIDATION_DIR / "protocol-lock.json"
SUBMISSION_SCHEMA_PATH = VALIDATION_DIR / "scorer-submission.schema.json"
SUBMISSION_TEMPLATE_PATH = (
    VALIDATION_DIR / "submissions" / "scorer-submission.template.json"
)
PACKET_MANIFEST_PATH = VALIDATION_DIR / "frozen-packet" / "source-manifest.json"
TEST_VECTOR_A_PATH = VALIDATION_DIR / "test-vectors" / "rater-a.json"
TEST_VECTOR_B_PATH = VALIDATION_DIR / "test-vectors" / "rater-b.json"
COMPARISON_SCRIPT_PATH = ROOT / "scripts" / "compare_raters.py"
RESULTS_DIR = VALIDATION_DIR / "results"

MODEL_STRESS_DIR = VALIDATION_DIR / "model-stress-test"
MODEL_PROTOCOL_PATH = MODEL_STRESS_DIR / "protocol.md"
MODEL_SCHEMA_PATH = MODEL_STRESS_DIR / "model-submission.schema.json"
MODEL_TEMPLATE_PATH = MODEL_STRESS_DIR / "model-submission.template.json"
MODEL_RESULTS_DIR = MODEL_STRESS_DIR / "results"
FRICTION_REVIEW_PATH = VALIDATION_DIR / "adversarial-rubric-friction-review.md"
FRICTION_REGISTER_PATH = VALIDATION_DIR / "adversarial-rubric-friction-register.json"

RELEASE_VERSION = "0.2.1"
RELEASE_DATE = "2026-07-16"
CASE_EVIDENCE_RELEASE_VERSION = "0.2.0"
SPECIFICATION_VERSION = "0.1.0"
SCHEMA_VERSION = "0.1.0"
CATALOG_VERSION = "0.1.0"
ORIGINATING_CONCEPT_DOI = "10.5281/zenodo.21204892"

INTER_RATER_PROTOCOL_ID = "HIT-IRP-CIGNA-001"
INTER_RATER_PROTOCOL_VERSION = "1.0.0"
INTER_RATER_PACKET_ID = "HIT-IR-CIGNA-PXDX-001"
INTER_RATER_TARGET_RELEASE = "0.3.0"
EXPECTED_PACKET_SOURCE_IDS = {"S1", "S2", "S3"}

MODEL_STRESS_PROTOCOL_ID = "HIT-MST-CIGNA-001"
MODEL_STRESS_PROTOCOL_VERSION = "1.0.0"
FRICTION_REVIEW_ID = "HIT-ARFR-001"

EXPECTED_DIMENSIONS = {
    "counsel",
    "judgment",
    "command",
    "correction",
    "repair",
    "reform",
}
EXPECTED_CASE_ASSESSMENT_IDS = {
    "HIT-CASE-TOESLAGENAFFAIRE-HARM-2013-2019",
    "HIT-CASE-OBERMEYER-DEPLOYERS-2019",
    "HIT-CASE-OBERMEYER-MANUFACTURER-2019",
    "HIT-CASE-CIGNA-PXDX-2022-2025",
}
CASE_STUDY_PATHS = {
    "case-studies/toeslagenaffaire.md",
    "case-studies/obermeyer.md",
    "case-studies/cigna-pxdx.md",
}
INTER_RATER_REQUIRED_FILES = {
    "validation/README.md",
    "validation/inter-rater-protocol.md",
    "validation/protocol-lock.json",
    "validation/frozen-packet/README.md",
    "validation/frozen-packet/decision-boundary.md",
    "validation/frozen-packet/source-manifest.json",
    "validation/scorer-submission.schema.json",
    "validation/submissions/scorer-submission.template.json",
    "validation/disagreement-taxonomy.md",
    "validation/adjudication-template.md",
    "validation/results/README.md",
    "validation/test-vectors/README.md",
    "validation/test-vectors/rater-a.json",
    "validation/test-vectors/rater-b.json",
    "scripts/compare_raters.py",
}
READINESS_REQUIRED_FILES = {
    "validation/adversarial-rubric-friction-review.md",
    "validation/adversarial-rubric-friction-register.json",
    "validation/model-stress-test/README.md",
    "validation/model-stress-test/protocol.md",
    "validation/model-stress-test/prompt.md",
    "validation/model-stress-test/model-submission.schema.json",
    "validation/model-stress-test/model-submission.template.json",
    "validation/model-stress-test/results/README.md",
    "coordinator/README.md",
    "coordinator/comparison-runbook.md",
    "recruitment/README.md",
    "recruitment/invitation.md",
    "recruitment/eligibility-screen.md",
    "recruitment/scorer-instructions.md",
    "scripts/validate_scorer_submission.py",
    "scripts/record_submission.py",
    "docs/doi-deadline-plan.md",
}
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
    *CASE_STUDY_PATHS,
    "docs/application-handbook.md",
    "docs/doi-and-release-strategy.md",
    "docs/releases/v0.1.0.md",
    "docs/releases/v0.2.0.md",
    "docs/releases/v0.2.1.md",
    *INTER_RATER_REQUIRED_FILES,
    *READINESS_REQUIRED_FILES,
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


def validate_finding_set(instance: dict[str, Any], label: str) -> list[str]:
    failures: list[str] = []
    findings = instance.get("substantive_findings", [])
    dimensions = [
        item.get("dimension")
        for item in findings
        if isinstance(item, dict)
    ]
    if set(dimensions) != EXPECTED_DIMENSIONS:
        failures.append(
            f"{label}: substantive findings must contain each dimension exactly once"
        )
    if len(dimensions) != len(set(dimensions)):
        failures.append(f"{label}: duplicate substantive dimension finding")
    return failures


def validate_assessment(
    validator: Draft202012Validator, path: Path
) -> tuple[list[str], dict[str, Any] | None]:
    instance = load_json(path)
    errors = sorted(
        validator.iter_errors(instance),
        key=lambda error: list(error.path),
    )
    failures = [f"{path}: {error.message}" for error in errors]

    if not isinstance(instance, dict):
        return failures, None

    failures.extend(validate_finding_set(instance, str(path)))
    return failures, instance


def is_rejected(
    validator: Draft202012Validator, instance: dict[str, Any]
) -> bool:
    return bool(
        list(validator.iter_errors(instance))
        or validate_finding_set(instance, "negative test")
    )


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

    wrong_schema_version = copy.deepcopy(source)
    wrong_schema_version["schema_version"] = "9.9.9"
    if not is_rejected(validator, wrong_schema_version):
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


def require_text(
    failures: list[str], path: str, expected: str, label: str
) -> None:
    text = load_text(ROOT / path)
    if expected not in text:
        failures.append(f"{path}: missing {label}: {expected}")


def validate_release_text() -> list[str]:
    failures: list[str] = []

    require_text(
        failures,
        "README.md",
        f"**Current release:** {RELEASE_VERSION}",
        "repository release version",
    )
    require_text(
        failures,
        "README.md",
        f"**Specification version:** {SPECIFICATION_VERSION}",
        "specification version",
    )
    require_text(
        failures,
        "README.md",
        f"**Assessment schema version:** {SCHEMA_VERSION}",
        "schema version",
    )
    require_text(
        failures,
        "README.md",
        "**Development workstream:** v0.3.0 human inter-rater result",
        "human inter-rater development status",
    )
    require_text(
        failures,
        "SPECIFICATION.md",
        f"**Version:** {SPECIFICATION_VERSION}",
        "specification version",
    )
    require_text(
        failures,
        "PROVENANCE.md",
        f"- Public repository release: {RELEASE_VERSION}",
        "release provenance",
    )
    require_text(
        failures,
        "CHANGELOG.md",
        f"## [{RELEASE_VERSION}] - {RELEASE_DATE}",
        "release changelog entry",
    )
    require_text(
        failures,
        f"docs/releases/v{RELEASE_VERSION}.md",
        f"# Human Influence Telemetry v{RELEASE_VERSION}",
        "release-note title",
    )

    expected_status = (
        f"**Status:** Released with repository version "
        f"{CASE_EVIDENCE_RELEASE_VERSION}"
    )
    for relative_path in sorted(CASE_STUDY_PATHS):
        text = load_text(ROOT / relative_path)
        if expected_status not in text:
            failures.append(
                f"{relative_path}: case-study release provenance must remain "
                f"{CASE_EVIDENCE_RELEASE_VERSION}"
            )
        if "Public review draft" in text:
            failures.append(
                f"{relative_path}: public-review marker remains in release artifact"
            )

    return failures


def validate_metadata(
    schema: dict[str, Any], catalog: dict[str, Any]
) -> list[str]:
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
    if citation.get("version") != RELEASE_VERSION:
        failures.append("CITATION.cff repository release version is inconsistent")
    if citation.get("date-released") != RELEASE_DATE:
        failures.append("CITATION.cff release date is inconsistent")
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
    if zenodo.get("version") != RELEASE_VERSION:
        failures.append(".zenodo.json repository release version is inconsistent")
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
        failures.append(
            ".zenodo.json must relate the software to the originating research DOI"
        )

    schema_version = (
        schema.get("properties", {})
        .get("schema_version", {})
        .get("const")
    )
    if schema_version != SCHEMA_VERSION:
        failures.append("assessment schema component version is inconsistent")
    if catalog.get("catalog_version") != CATALOG_VERSION:
        failures.append("dimension catalog component version is inconsistent")

    return failures


def validate_scorer_submission_shape(
    submission: dict[str, Any], label: str
) -> list[str]:
    failures: list[str] = []
    failures.extend(validate_finding_set(submission, label))

    source_access = submission.get("source_access", [])
    source_ids = [
        item.get("source_id")
        for item in source_access
        if isinstance(item, dict)
    ]
    if set(source_ids) != EXPECTED_PACKET_SOURCE_IDS:
        failures.append(f"{label}: source_access must contain S1, S2, and S3")
    if len(source_ids) != len(set(source_ids)):
        failures.append(f"{label}: duplicate source_access entry")
    if not all(
        isinstance(item, dict) and item.get("access_complete") is True
        for item in source_access
    ):
        failures.append(f"{label}: every frozen source must be accessed completely")

    return failures


def run_comparison(
    submission_a: Path, submission_b: Path
) -> tuple[list[str], dict[str, Any] | None]:
    completed = subprocess.run(
        [
            sys.executable,
            str(COMPARISON_SCRIPT_PATH),
            str(submission_a),
            str(submission_b),
            "--schema",
            str(SUBMISSION_SCHEMA_PATH),
            "--format",
            "json",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        return [
            "comparison tool failed: "
            + (completed.stderr.strip() or completed.stdout.strip())
        ], None

    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        return [f"comparison tool returned invalid JSON: {exc}"], None
    if not isinstance(result, dict):
        return ["comparison tool output must be a JSON object"], None
    return [], result


def validate_inter_rater_artifacts() -> tuple[list[str], str]:
    failures: list[str] = []

    protocol_lock = load_json(PROTOCOL_LOCK_PATH)
    if not isinstance(protocol_lock, dict):
        return ["validation/protocol-lock.json must contain a JSON object"], "unknown"

    expected_lock_values = {
        "protocol_id": INTER_RATER_PROTOCOL_ID,
        "protocol_version": INTER_RATER_PROTOCOL_VERSION,
        "target_repository_release": INTER_RATER_TARGET_RELEASE,
        "method_specification_version": SPECIFICATION_VERSION,
        "assessment_schema_version": SCHEMA_VERSION,
        "packet_id": INTER_RATER_PACKET_ID,
        "required_scorers": 2,
        "author_may_score": False,
        "post_adjudication_rescoring_changes_primary_result": False,
        "failure_result_must_be_published": True,
    }
    for key, expected in expected_lock_values.items():
        if protocol_lock.get(key) != expected:
            failures.append(
                f"validation/protocol-lock.json: {key} must equal {expected!r}"
            )

    protocol_status = str(protocol_lock.get("status", "unknown"))
    if protocol_status != "locked":
        failures.append("validation/protocol-lock.json: status must be locked")
    if protocol_lock.get("minimum_exact_agreements") != 6:
        failures.append("protocol lock must require six exact agreements")
    if protocol_lock.get("minimum_exact_agreement_proportion") != 0.8571:
        failures.append("protocol lock exact-agreement proportion is inconsistent")
    if protocol_lock.get("critical_disagreements_allowed") != 0:
        failures.append("protocol lock must allow zero critical disagreements")

    protocol_text = load_text(PROTOCOL_PATH)
    for required_text in (
        INTER_RATER_PROTOCOL_ID,
        INTER_RATER_PROTOCOL_VERSION,
        INTER_RATER_PACKET_ID,
        "at least six of seven findings agree exactly",
        "A failing result is publishable and informative",
    ):
        if required_text not in protocol_text:
            failures.append(
                f"validation/inter-rater-protocol.md: missing {required_text}"
            )

    manifest = load_json(PACKET_MANIFEST_PATH)
    if not isinstance(manifest, dict):
        failures.append("frozen packet source manifest must be a JSON object")
    else:
        if manifest.get("packet_id") != INTER_RATER_PACKET_ID:
            failures.append("frozen packet ID is inconsistent")
        if manifest.get("protocol_id") != INTER_RATER_PROTOCOL_ID:
            failures.append("frozen packet protocol ID is inconsistent")
        sources = manifest.get("sources", [])
        source_ids = {
            item.get("source_id")
            for item in sources
            if isinstance(item, dict)
        }
        if source_ids != EXPECTED_PACKET_SOURCE_IDS:
            failures.append("frozen packet must contain source IDs S1, S2, and S3")
        if len(sources) != 3:
            failures.append("frozen packet must contain exactly three sources")
        for item in sources:
            if not isinstance(item, dict):
                failures.append("frozen packet source entries must be objects")
                continue
            if item.get("required") is not True:
                failures.append(
                    f"frozen packet source {item.get('source_id')} must be required"
                )
            for key in ("citation", "url", "evidentiary_tier", "use_constraint"):
                if not isinstance(item.get(key), str) or not item.get(key):
                    failures.append(
                        f"frozen packet source {item.get('source_id')} lacks {key}"
                    )

        excluded = set(manifest.get("excluded_repository_paths", []))
        expected_exclusions = {
            "case-studies/cigna-pxdx.md",
            "case-studies/assessments/cigna-pxdx.json",
        }
        if not expected_exclusions.issubset(excluded):
            failures.append("frozen packet does not exclude the author-scored Cigna files")

    submission_schema = load_json(SUBMISSION_SCHEMA_PATH)
    if not isinstance(submission_schema, dict):
        failures.append("scorer-submission schema must be a JSON object")
        return failures, protocol_status

    try:
        Draft202012Validator.check_schema(submission_schema)
    except Exception as exc:
        failures.append(f"invalid scorer-submission schema: {exc}")
        return failures, protocol_status

    submission_validator = Draft202012Validator(
        submission_schema,
        format_checker=FormatChecker(),
    )

    template = load_json(SUBMISSION_TEMPLATE_PATH)
    if not isinstance(template, dict):
        failures.append("scorer submission template must be a JSON object")
    else:
        if template.get("protocol_id") != INTER_RATER_PROTOCOL_ID:
            failures.append("scorer template protocol ID is inconsistent")
        if template.get("packet_id") != INTER_RATER_PACKET_ID:
            failures.append("scorer template packet ID is inconsistent")
        template_dimensions = {
            item.get("dimension")
            for item in template.get("substantive_findings", [])
            if isinstance(item, dict)
        }
        if template_dimensions != EXPECTED_DIMENSIONS:
            failures.append("scorer template does not contain all six dimensions")

    test_submissions: list[dict[str, Any]] = []
    for path in (TEST_VECTOR_A_PATH, TEST_VECTOR_B_PATH):
        instance = load_json(path)
        errors = sorted(
            submission_validator.iter_errors(instance),
            key=lambda error: list(error.path),
        )
        failures.extend(f"{path}: {error.message}" for error in errors)
        if isinstance(instance, dict):
            failures.extend(validate_scorer_submission_shape(instance, str(path)))
            if not errors:
                test_submissions.append(instance)

    if len(test_submissions) == 2:
        scorer_ids = {
            item.get("scorer", {}).get("public_id")
            for item in test_submissions
            if isinstance(item.get("scorer"), dict)
        }
        if len(scorer_ids) != 2:
            failures.append("synthetic test-vector scorer IDs must be distinct")

    comparison_failures, comparison = run_comparison(
        TEST_VECTOR_A_PATH,
        TEST_VECTOR_B_PATH,
    )
    failures.extend(comparison_failures)
    if comparison is not None:
        expected_results = {
            "items_compared": 7,
            "exact_agreements": 6,
            "exact_agreement_proportion": 0.8571,
            "critical_disagreement_count": 0,
            "advancement_threshold_met": True,
        }
        for key, expected in expected_results.items():
            if comparison.get(key) != expected:
                failures.append(
                    f"comparison test vector: {key} must equal {expected!r}"
                )
        disagreements = comparison.get("disagreements", [])
        if not isinstance(disagreements, list) or len(disagreements) != 1:
            failures.append("comparison test vector must produce one disagreement")

    result_files = {
        path.name
        for path in RESULTS_DIR.iterdir()
        if path.is_file() and path.name != "README.md"
    }
    if not result_files:
        pending_text = load_text(RESULTS_DIR / "README.md")
        if "No inter-rater result is currently available." not in pending_text:
            failures.append("pending human results boundary is missing")
    else:
        required_result_files = {
            "scorer-a.json",
            "scorer-b.json",
            "pre-adjudication-comparison.json",
            "pre-adjudication-comparison.md",
            "disagreement-register.md",
            "adjudication.md",
            "result-summary.md",
        }
        if result_files != required_result_files:
            failures.append(
                "empirical result directory does not contain the exact required result set"
            )

    return failures, protocol_status


def validate_readiness_artifacts() -> list[str]:
    failures: list[str] = []

    friction_text = load_text(FRICTION_REVIEW_PATH)
    for required_text in (
        FRICTION_REVIEW_ID,
        "did not assign any HIT finding",
        "must not be distributed to scorers",
    ):
        if required_text not in friction_text:
            failures.append(
                f"validation/adversarial-rubric-friction-review.md: missing {required_text}"
            )

    friction_register = load_json(FRICTION_REGISTER_PATH)
    if not isinstance(friction_register, dict):
        failures.append("rubric-friction register must be a JSON object")
    else:
        if friction_register.get("review_id") != FRICTION_REVIEW_ID:
            failures.append("rubric-friction review ID is inconsistent")
        if friction_register.get("case_sources_reviewed") is not False:
            failures.append("rubric-friction review must declare no case-source review")
        if friction_register.get("case_findings_assigned") is not False:
            failures.append("rubric-friction review must declare no case findings")
        if friction_register.get("maturity_consequence") != "none":
            failures.append("rubric-friction review must have no maturity consequence")

    model_protocol_text = load_text(MODEL_PROTOCOL_PATH)
    for required_text in (
        MODEL_STRESS_PROTOCOL_ID,
        MODEL_STRESS_PROTOCOL_VERSION,
        INTER_RATER_PROTOCOL_ID,
        INTER_RATER_PACKET_ID,
    ):
        if required_text not in model_protocol_text:
            failures.append(
                f"validation/model-stress-test/protocol.md: missing {required_text}"
            )

    model_schema = load_json(MODEL_SCHEMA_PATH)
    if not isinstance(model_schema, dict):
        failures.append("model stress-test schema must be a JSON object")
    else:
        try:
            Draft202012Validator.check_schema(model_schema)
        except Exception as exc:
            failures.append(f"invalid model stress-test schema: {exc}")

    model_template = load_json(MODEL_TEMPLATE_PATH)
    if not isinstance(model_template, dict):
        failures.append("model stress-test template must be a JSON object")
    else:
        if model_template.get("protocol_id") != MODEL_STRESS_PROTOCOL_ID:
            failures.append("model stress-test template protocol ID is inconsistent")
        if model_template.get("packet_id") != INTER_RATER_PACKET_ID:
            failures.append("model stress-test template packet ID is inconsistent")
        dimensions = {
            item.get("dimension")
            for item in model_template.get("substantive_findings", [])
            if isinstance(item, dict)
        }
        if dimensions != EXPECTED_DIMENSIONS:
            failures.append("model stress-test template lacks the six dimensions")

    model_result_files = {
        path.name
        for path in MODEL_RESULTS_DIR.iterdir()
        if path.is_file() and path.name != "README.md"
    }
    if model_result_files:
        failures.append(
            "v0.2.1 must not contain model stress-test result files; use a separate result branch"
        )
    else:
        pending_text = load_text(MODEL_RESULTS_DIR / "README.md")
        if "No protocol-conforming model stress-test result is currently available." not in pending_text:
            failures.append("pending model stress-test result boundary is missing")

    coordinator_text = load_text(ROOT / "coordinator" / "comparison-runbook.md")
    for required_text in ("--format", "--output", "Do not disclose"):
        if required_text not in coordinator_text:
            failures.append(
                f"coordinator/comparison-runbook.md: missing {required_text}"
            )

    return failures


def main() -> int:
    failures = validate_release_files()
    failures.extend(validate_release_text())

    schema = load_json(SCHEMA_PATH)
    if not isinstance(schema, dict):
        raise RuntimeError("assessment schema must be a JSON object")
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )

    catalog = load_json(CATALOG_PATH)
    if not isinstance(catalog, dict):
        raise RuntimeError("dimension catalog must be a JSON object")

    catalog_ids = {
        item["id"]
        for item in catalog.get("substantive_dimensions", [])
        if isinstance(item, dict) and "id" in item
    }
    if catalog_ids != EXPECTED_DIMENSIONS:
        failures.append(
            "dimension catalog does not contain exactly the six substantive dimensions"
        )
    if catalog.get("cross_cutting_dimension", {}).get("id") != "telemetry_integrity":
        failures.append(
            "dimension catalog must define Telemetry Integrity as cross-cutting"
        )

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
                    failures.append(
                        f"duplicate public case assessment_id: {assessment_id}"
                    )
                observed_case_ids.add(assessment_id)

    if observed_case_ids != EXPECTED_CASE_ASSESSMENT_IDS:
        failures.append(
            "public case assessment IDs do not match the expected evidence pack"
        )

    if valid_fixtures:
        failures.extend(validate_negative_cases(validator, valid_fixtures[0]))
    else:
        failures.append(
            "negative tests could not run because no valid fixture was available"
        )

    failures.extend(validate_metadata(schema, catalog))
    inter_rater_failures, protocol_status = validate_inter_rater_artifacts()
    failures.extend(inter_rater_failures)
    failures.extend(validate_readiness_artifacts())

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print(
        "HIT validation: PASS "
        f"(release {RELEASE_VERSION}; specification {SPECIFICATION_VERSION}; "
        f"schema {SCHEMA_VERSION}; catalog {CATALOG_VERSION}; "
        f"case evidence release {CASE_EVIDENCE_RELEASE_VERSION}; "
        f"{len(fixtures)} fixtures; {len(case_assessments)} public case assessments; "
        f"inter-rater protocol {protocol_status}; readiness artifacts present; "
        "4 negative tests)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
