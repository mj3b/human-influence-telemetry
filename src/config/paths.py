"""Repository paths used by the HIT conformance implementation."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schema" / "hit-assessment.schema.json"
CATALOG_PATH = ROOT / "schema" / "hit-dimension-catalog.json"
CANONICAL_EXAMPLE_PATH = ROOT / "fixtures" / "v0.4.0-canonical-example.json"
COMPLETE_RECORD_SUITE_PATH = (
    ROOT / "fixtures" / "v0.5.0-conformance" / "complete-record-cases.json"
)
COMPATIBILITY_MANIFEST_PATH = ROOT / "compatibility" / "hit-compatibility-manifest.json"
REPOSITORY_VALIDATOR_PATH = ROOT / "scripts" / "validate.py"
FORMAT_VALIDATOR_PATH = ROOT / "scripts" / "check_fixture_format.py"
