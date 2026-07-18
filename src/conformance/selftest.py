"""Determinism and migration-preservation checks for the HIT conformance engine."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from src.conformance.migration import build_migration_plan
from src.conformance.suite import run_complete_record_suite

HISTORICAL_PATHS = (
    "case-studies/assessments/toeslagenaffaire-harm-period.json",
    "case-studies/assessments/obermeyer-deployers.json",
    "case-studies/assessments/obermeyer-manufacturer.json",
    "case-studies/assessments/cigna-pxdx.json",
)


def _canonical_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    ).encode("utf-8")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_self_tests(
    *,
    root: Path,
    schema_path: Path,
    base_record_path: Path,
    suite_path: Path,
) -> dict[str, Any]:
    first = run_complete_record_suite(
        schema_path=schema_path,
        base_record_path=base_record_path,
        suite_path=suite_path,
    )
    second = run_complete_record_suite(
        schema_path=schema_path,
        base_record_path=base_record_path,
        suite_path=suite_path,
    )
    first_bytes = _canonical_bytes(first)
    second_bytes = _canonical_bytes(second)
    deterministic = first_bytes == second_bytes

    migrations: list[dict[str, Any]] = []
    migrations_valid = True
    for relative_path in HISTORICAL_PATHS:
        path = root / relative_path
        before = _sha256(path)
        plan = build_migration_plan(path, source_label=relative_path)
        after = _sha256(path)
        case_valid = (
            plan.get("valid_plan") is True
            and plan.get("automatic_migration") is False
            and plan.get("source_preserved") is True
            and plan.get("disposition") == "fresh_reassessment_required"
            and before == after
        )
        migrations_valid = migrations_valid and case_valid
        migrations.append(
            {
                "source": relative_path,
                "valid": case_valid,
                "before_sha256": before,
                "after_sha256": after,
                "plan": plan,
            }
        )

    unsupported = build_migration_plan(
        base_record_path,
        source_label="fixtures/v0.4.0-canonical-example.json",
    )
    unsupported_valid = (
        unsupported.get("valid_plan") is False
        and unsupported.get("disposition") == "unsupported_source_contract"
        and unsupported.get("automatic_migration") is False
    )

    return {
        "valid": deterministic and migrations_valid and unsupported_valid,
        "deterministic_report": {
            "valid": deterministic,
            "first_sha256": hashlib.sha256(first_bytes).hexdigest(),
            "second_sha256": hashlib.sha256(second_bytes).hexdigest(),
        },
        "historical_migration_plans": migrations,
        "unsupported_source_check": {
            "valid": unsupported_valid,
            "plan": unsupported,
        },
    }
