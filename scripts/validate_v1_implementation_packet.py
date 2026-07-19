#!/usr/bin/env python3
"""Validate the candidate HIT v1 clean-room implementation packet."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "implementation" / "v1.0.0-candidate"
README = BASE / "README.md"
PROTOCOL = BASE / "audit-protocol.md"
MANIFEST = BASE / "manifest.candidate.json"


def main() -> int:
    failures: list[str] = []

    for path in (README, PROTOCOL, MANIFEST):
        if not path.is_file() or path.stat().st_size == 0:
            failures.append(f"missing or empty file: {path.relative_to(ROOT)}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("packet_id") != "HIT-IMPLEMENTATION-V100-CANDIDATE-001":
        failures.append("implementation packet ID changed")
    if manifest.get("status") != "candidate_incomplete":
        failures.append("implementation packet must remain candidate_incomplete")
    if manifest.get("audit_protocol_id") != "HIT-CRI-V100-001":
        failures.append("implementation packet audit protocol ID changed")
    if manifest.get("audit_permitted") is not False:
        failures.append("clean-room audit must remain prohibited")
    if manifest.get("target_release") != "0.9.0":
        failures.append("implementation packet must target v0.9.0")
    if manifest.get("target_stable_release") != "1.0.0":
        failures.append("implementation packet stable target must remain 1.0.0")
    if manifest.get("exact_repository_commit") is not None:
        failures.append("candidate implementation packet must not claim a frozen commit")
    if manifest.get("packet_digest") is not None:
        failures.append("candidate implementation packet must not claim a final digest")
    if manifest.get("private_author_explanation_allowed") is not False:
        failures.append("private author explanation must be prohibited")
    if manifest.get("model_audit_counts_as_human_reliability_evidence") is not False:
        failures.append("model audit must not count as human reliability evidence")
    if manifest.get("failed_audit_must_be_published") is not True:
        failures.append("failed clean-room audits must be publishable evidence")

    required_tasks = {
        "fresh_install",
        "version_reconstruction",
        "valid_assessment_validation",
        "invalid_vector_error_explanation",
        "rule_reconstruction",
        "migration_plan_generation",
        "comparison_reproduction",
        "adjacent_system_boundary_explanation",
        "private_knowledge_register",
        "audit_disposition",
    }
    if set(manifest.get("required_runtime_tasks", [])) != required_tasks:
        failures.append("clean-room task set changed")

    missing = set(manifest.get("missing_before_activation", []))
    required_missing = {
        "exact_repository_commit",
        "packet_digest",
        "dependency_lock_or_exact_environment_record",
        "expected_output_hashes",
        "audit_submission_schema",
        "independent_auditor_eligibility_record",
        "exact_commit_validation",
    }
    if not required_missing.issubset(missing):
        failures.append("implementation packet is missing required activation blockers")

    readme = README.read_text(encoding="utf-8")
    for phrase in (
        "Status:** Candidate, incomplete",
        "Private explanation permitted:** No",
        "install the package in a fresh environment",
        "record every point where the public packet is ambiguous",
        "does not establish inter-rater reliability",
    ):
        if phrase not in readme:
            failures.append(f"implementation README missing control text: {phrase}")

    protocol = PROTOCOL.read_text(encoding="utf-8")
    for phrase in (
        "Protocol ID:** `HIT-CRI-V100-001`",
        "Status:** Candidate, audit prohibited",
        "Can a technically competent external reviewer install, operate, and explain",
        "private author knowledge",
        "fail_release_blocking_defect",
        "blocks `v0.9.0` promotion and `v1.0.0` release",
    ):
        if phrase not in protocol:
            failures.append(f"audit protocol missing control text: {phrase}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT v1 clean-room implementation packet candidate validation passed")
    print("- packet status: candidate_incomplete")
    print("- audit permitted: no")
    print("- target release: 0.9.0")
    print("- stable target: 1.0.0")
    print("- private author explanation: prohibited")
    return 0


if __name__ == "__main__":
    sys.exit(main())
