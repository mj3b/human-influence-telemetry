#!/usr/bin/env python3
"""Validate HIT v0.4.0 candidate release-readiness documents."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "docs/decisions/ADR-0003-chronological-result-versioning.md": [
        "**Status:** Accepted",
        "`v0.3.0` is a superseded planning target",
        "next available repository version",
        "does not modify the protocol",
    ],
    "docs/breaking-change-review-v0.4.0.md": [
        "breaking normative and data-contract change",
        "all 16 ambiguity classes",
        "must not be described as conforming to `0.4.0`",
    ],
    "docs/migration-guide-v0.1.0-to-v0.4.0.md": [
        "fresh bounded reassessment",
        "Preserve the historical file",
        "deferred_locked_protocol",
    ],
    "docs/adjacent-system-claim-audit-v0.4.0.md": [
        "Microsoft Agent Governance Toolkit",
        "ScopeBlind/Acta",
        "Credo AI",
        "Decision Evidence Applicability Specification",
        "Passed for candidate artifacts",
    ],
    "docs/releases/v0.4.0-candidate.md": [
        "48 executable rubric boundary fixtures",
        "Maturity Level 1",
        "dedicated promotion pull request",
    ],
    "docs/v0.4.0-candidate-readiness-report.md": [
        "ready for canonical promotion",
        "Promotion work remaining",
        "Do not tag `v0.4.0`",
    ],
}


def main() -> int:
    failures: list[str] = []
    for relative_path, phrases in REQUIRED.items():
        path = ROOT / relative_path
        if not path.is_file():
            failures.append(f"missing release-readiness document: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            failures.append(f"empty release-readiness document: {relative_path}")
            continue
        for phrase in phrases:
            if phrase not in text:
                failures.append(f"{relative_path}: missing required text: {phrase}")

    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "**Current release:** 0.2.1" not in root_readme:
        failures.append("candidate branch must preserve released README version 0.2.1")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT v0.4.0 candidate release-readiness validation passed")
    print("- governance decisions: 3")
    print("- breaking-change review: present")
    print("- migration guide: present")
    print("- adjacent-system audit: passed")
    print("- candidate release notes: present")
    print("- canonical promotion: still required")
    return 0


if __name__ == "__main__":
    sys.exit(main())
