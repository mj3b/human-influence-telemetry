"""Non-mutating migration planning for historical HIT assessments."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

from src.validation.assessment import load_json

RECONSTRUCTION_REQUIREMENTS = [
    "declare the 0.4.0 assessment boundary, sampling rule, and aggregation rule",
    "reconstruct the actor-authority matrix",
    "convert source material into bounded evidence claims with reproducible locators",
    "determine evidence state before assigning each substantive finding",
    "determine the Repair trigger",
    "separate institutional-record and assessment-packet integrity",
    "preserve the original 0.1.0 assessment without modification",
]


def build_migration_plan(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    instance = load_json(path)
    source_version = instance.get("schema_version")
    supported_source = source_version == "0.1.0"
    return {
        "plan_version": "0.1.0",
        "source": str(path),
        "source_assessment_id": instance.get("assessment_id"),
        "source_schema_version": source_version,
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "target_schema_version": "0.4.0",
        "automatic_migration": False,
        "source_preserved": True,
        "disposition": (
            "fresh_reassessment_required"
            if supported_source
            else "unsupported_source_contract"
        ),
        "requirements": RECONSTRUCTION_REQUIREMENTS if supported_source else [],
        "valid_plan": supported_source,
        "non_claim": (
            "This plan does not re-score the case or create a 0.4.0 assessment."
        ),
    }
