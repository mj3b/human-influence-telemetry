"""Validation for the machine-readable HIT compatibility manifest."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from src.validation.assessment import load_json

REQUIRED_TOP_LEVEL = {
    "manifest_version",
    "engine_version",
    "supported_contracts",
    "historical_contracts",
    "migration_rules",
    "commands",
    "non_claims",
}


def validate_compatibility_manifest(path: Path) -> dict[str, Any]:
    manifest = load_json(path)
    errors: list[str] = []
    missing = sorted(REQUIRED_TOP_LEVEL - set(manifest))
    if missing:
        errors.append(f"missing top-level fields: {missing}")

    supported = manifest.get("supported_contracts", [])
    if not any(
        isinstance(item, dict)
        and item.get("specification_version") == "0.4.0"
        and item.get("schema_version") == "0.4.0"
        and item.get("conformance_mode") == "full"
        for item in supported
    ):
        errors.append("0.4.0 must be declared as a fully supported contract")

    historical = manifest.get("historical_contracts", [])
    if not any(
        isinstance(item, dict)
        and item.get("schema_version") == "0.1.0"
        and item.get("conformance_mode") == "historical_validation_only"
        for item in historical
    ):
        errors.append("0.1.0 must be restricted to historical validation")

    rules = manifest.get("migration_rules", [])
    if not any(
        isinstance(item, dict)
        and item.get("from_schema_version") == "0.1.0"
        and item.get("to_schema_version") == "0.4.0"
        and item.get("automatic") is False
        and item.get("preserve_original") is True
        and item.get("method") == "fresh_reassessment"
        for item in rules
    ):
        errors.append(
            "0.1.0-to-0.4.0 must require a preserved fresh reassessment"
        )

    return {
        "valid": not errors,
        "manifest_version": manifest.get("manifest_version"),
        "engine_version": manifest.get("engine_version"),
        "errors": errors,
        "manifest": manifest,
    }
