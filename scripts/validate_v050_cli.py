#!/usr/bin/env python3
"""Smoke-test the public HIT conformance and migration CLI commands."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.conformance.suite import apply_mutations
from src.validation.assessment import load_json

CANONICAL = ROOT / "fixtures" / "v0.4.0-canonical-example.json"
SUITE = ROOT / "fixtures" / "v0.5.0-conformance" / "complete-record-cases.json"
HISTORICAL = (
    ROOT
    / "case-studies"
    / "assessments"
    / "toeslagenaffaire-harm-period.json"
)


def run_cli(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "src.cli", *arguments],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def main() -> int:
    failures: list[str] = []

    first = run_cli(
        "conformance", "--path", str(CANONICAL), "--format", "json"
    )
    second = run_cli(
        "conformance", "--path", str(CANONICAL), "--format", "json"
    )
    if first.returncode != 0 or second.returncode != 0:
        failures.append("canonical assessment CLI did not return success")
    elif first.stdout != second.stdout:
        failures.append("canonical assessment CLI output is not byte-stable")
    else:
        report = json.loads(first.stdout)
        if report.get("valid") is not True:
            failures.append("canonical assessment CLI report is not valid")

    migration_first = run_cli(
        "migration-plan", "--path", str(HISTORICAL), "--format", "json"
    )
    migration_second = run_cli(
        "migration-plan", "--path", str(HISTORICAL), "--format", "json"
    )
    if migration_first.returncode != 0 or migration_second.returncode != 0:
        failures.append("historical migration CLI did not return success")
    elif migration_first.stdout != migration_second.stdout:
        failures.append("historical migration CLI output is not byte-stable")
    else:
        plan = json.loads(migration_first.stdout)
        if (
            plan.get("valid_plan") is not True
            or plan.get("automatic_migration") is not False
            or plan.get("source_preserved") is not True
        ):
            failures.append("historical migration CLI weakened preservation rules")

    base = load_json(CANONICAL)
    suite = load_json(SUITE)
    invalid_case = next(
        case
        for case in suite["cases"]
        if case["case_id"] == "CR-CLAIM-REFERENCE-001"
    )
    invalid = apply_mutations(base, invalid_case["mutations"])
    with tempfile.TemporaryDirectory() as directory:
        invalid_path = Path(directory) / "invalid-assessment.json"
        invalid_path.write_text(
            json.dumps(invalid, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        invalid_run = run_cli(
            "conformance", "--path", str(invalid_path), "--format", "json"
        )
    if invalid_run.returncode != 1:
        failures.append("invalid assessment CLI did not return exit code 1")
    else:
        report = json.loads(invalid_run.stdout)
        codes = {item.get("code") for item in report.get("issues", [])}
        if "HIT-CLAIM-REFERENCE" not in codes:
            failures.append("invalid assessment CLI omitted the expected error code")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT v0.5.0 CLI smoke tests passed")
    print("- valid assessment output: deterministic")
    print("- historical migration output: deterministic and non-mutating")
    print("- invalid assessment exit code and error code: enforced")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
