"""Conformance orchestration for individual assessments and the repository suite."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Any

from src.config.paths import (
    CANONICAL_EXAMPLE_PATH,
    COMPATIBILITY_MANIFEST_PATH,
    COMPLETE_RECORD_SUITE_PATH,
    FORMAT_VALIDATOR_PATH,
    REPOSITORY_VALIDATOR_PATH,
    SCHEMA_PATH,
)
from src.conformance.compatibility import validate_compatibility_manifest
from src.conformance.selftest import run_self_tests
from src.conformance.suite import run_complete_record_suite
from src.validation.assessment import load_json, validate_assessment


def validate_file(path: Path) -> dict[str, Any]:
    schema = load_json(SCHEMA_PATH)
    instance = load_json(path)
    return validate_assessment(instance, schema, source=str(path)).to_dict()


def _run_command(path: Path) -> dict[str, Any]:
    root = path.parents[1]
    result = subprocess.run(
        [sys.executable, str(path)],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        "command": f"python {path.relative_to(root)}",
        "exit_code": result.returncode,
        "passed": result.returncode == 0,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def run_repository_conformance() -> dict[str, Any]:
    fixture_format = _run_command(FORMAT_VALIDATOR_PATH)
    release_validation = _run_command(REPOSITORY_VALIDATOR_PATH)
    compatibility = validate_compatibility_manifest(COMPATIBILITY_MANIFEST_PATH)
    complete_records = run_complete_record_suite(
        schema_path=SCHEMA_PATH,
        base_record_path=CANONICAL_EXAMPLE_PATH,
        suite_path=COMPLETE_RECORD_SUITE_PATH,
    )
    self_tests = run_self_tests(
        root=SCHEMA_PATH.parents[1],
        schema_path=SCHEMA_PATH,
        base_record_path=CANONICAL_EXAMPLE_PATH,
        suite_path=COMPLETE_RECORD_SUITE_PATH,
    )
    valid = (
        fixture_format["passed"]
        and release_validation["passed"]
        and compatibility["valid"]
        and complete_records["valid"]
        and self_tests["valid"]
    )
    return {
        "report_version": "0.1.0",
        "engine_version": "0.5.0",
        "contract": {
            "specification_version": "0.4.0",
            "schema_version": "0.4.0",
            "catalog_version": "0.4.0",
        },
        "valid": valid,
        "checks": {
            "fixture_format": fixture_format,
            "released_contract": release_validation,
            "compatibility_manifest": compatibility,
            "complete_record_suite": complete_records,
            "self_tests": self_tests,
        },
    }
