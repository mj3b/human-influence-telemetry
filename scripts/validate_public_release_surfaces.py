#!/usr/bin/env python3
"""Validate synchronized public release and v1 readiness surfaces."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
RESEARCH = ROOT / "RESEARCH.md"
CITATION = ROOT / "CITATION.cff"
RELEASE_INDEX = ROOT / "docs" / "releases" / "README.md"
V1_CANDIDATE = ROOT / "docs" / "releases" / "v1.0.0-candidate.md"
V1_GATE = ROOT / "release" / "v1.0.0" / "contract-freeze.candidate.json"


def require(path: Path, failures: list[str]) -> str:
    if not path.is_file() or path.stat().st_size == 0:
        failures.append(f"missing or empty file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def main() -> int:
    failures: list[str] = []

    readme = require(README, failures)
    changelog = require(CHANGELOG, failures)
    research = require(RESEARCH, failures)
    citation = require(CITATION, failures)
    release_index = require(RELEASE_INDEX, failures)
    v1_candidate = require(V1_CANDIDATE, failures)
    require(V1_GATE, failures)

    for phrase in (
        "**Current public release:** `0.6.0`",
        "**Stable-release target:** `1.0.0`, readiness work active, release prohibited",
        "Version `1.0.0` is a compatibility and implementation claim",
        "The immediate blocking gate is a signed human selection",
        "The citation file remains at `0.6.0` until a later numbered release is actually published",
    ):
        if phrase not in readme:
            failures.append(f"README missing release control text: {phrase}")

    for phrase in (
        "Candidate `v0.7.0` current-contract replication architecture",
        "Machine-readable `v1.0.0` gate ledger",
        "`v1.0.0`: release prohibited until all gate-ledger conditions pass",
        "does not establish new human reliability",
    ):
        if phrase not in changelog:
            failures.append(f"CHANGELOG missing v1 readiness statement: {phrase}")

    for phrase in (
        "## v1 readiness claim boundary",
        "do not add E5 evidence",
        "may remain at Level 2",
        "Candidate documents, readiness plans, and release outlines do not authorize tag creation",
    ):
        if phrase not in research:
            failures.append(f"RESEARCH missing claim boundary text: {phrase}")

    for phrase in (
        "## Published releases",
        "## Active release train",
        "Public repository release | `0.6.0`",
        "`v1.0.0` | Stable public assessment contract suitable for independent implementation | Release prohibited",
    ):
        if phrase not in release_index:
            failures.append(f"release index missing status text: {phrase}")

    for phrase in (
        "**Status:** Candidate outline, release prohibited",
        "**Current public repository release:** `0.6.0`",
        "## Future GitHub release record",
        "does not authorize version promotion, tag creation, release publication",
    ):
        if phrase not in v1_candidate:
            failures.append(f"v1 candidate notes missing publication control: {phrase}")

    version_match = re.search(r'^version:\s*"([^"]+)"', citation, flags=re.MULTILINE)
    if version_match is None or version_match.group(1) != "0.6.0":
        failures.append("CITATION.cff must remain at published version 0.6.0")

    date_match = re.search(r'^date-released:\s*"([^"]+)"', citation, flags=re.MULTILINE)
    if date_match is None or date_match.group(1) != "2026-07-18":
        failures.append("CITATION.cff release date must remain synchronized with v0.6.0")

    forbidden_readme_claims = (
        "**Current public release:** `1.0.0`",
        "v1.0.0 is released",
        "v1.0.0 has been published",
        "Current maturity:** Level 3",
    )
    for phrase in forbidden_readme_claims:
        if phrase in readme:
            failures.append(f"README contains premature public claim: {phrase}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT public release-surface validation passed")
    print("- current published release: 0.6.0")
    print("- stable-release target: 1.0.0")
    print("- v1 publication permitted: no")
    print("- citation version: 0.6.0")
    print("- public release index: synchronized")
    return 0


if __name__ == "__main__":
    sys.exit(main())
