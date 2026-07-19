#!/usr/bin/env python3
"""Validate HIT public release and v1-readiness status surfaces."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]

PUBLISHED_RELEASE = "0.6.0"
NORMATIVE_CONTRACT = "0.4.0"
CONFORMANCE_ENGINE = "0.5.0"
STABLE_TARGET = "1.0.0"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load_json(path: str) -> Any:
    return json.loads(read(path))


def require(failures: list[str], path: str, phrase: str) -> None:
    if phrase not in read(path):
        failures.append(f"{path}: missing public-status text: {phrase}")


def main() -> int:
    failures: list[str] = []

    required_files = (
        "README.md",
        "ROADMAP.md",
        "RESEARCH.md",
        "PROVENANCE.md",
        "LIMITATIONS.md",
        "CHANGELOG.md",
        "SECURITY.md",
        "GOVERNANCE.md",
        "CONTRIBUTING.md",
        "SPECIFICATION.md",
        "CITATION.cff",
        ".zenodo.json",
        "docs/releases/README.md",
        "docs/releases/v0.7.0-candidate.md",
        "docs/releases/v1.0.0-candidate.md",
        "docs/v1-readiness-plan.md",
        "release/v1.0.0/contract-freeze.candidate.json",
    )

    for relative in required_files:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            failures.append(f"missing or empty public-status file: {relative}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    required_phrases = {
        "README.md": (
            "**Current release:** 0.6.0",
            "**Stable target:** `1.0.0`, release prohibited",
            "**Active replication protocol:** `HIT-IRP-HIT040-002`, candidate, scoring prohibited",
            "Candidate and future-version documents in the repository are planning and release-control artifacts. They are not published releases.",
            "The citation and `.zenodo.json` metadata remain at `0.6.0` until a later release is actually published.",
        ),
        "ROADMAP.md": (
            "0.6.0: First human inter-rater result, current release",
            "1.0.0: Stable public contract",
            "Candidate documents do not create a tag, GitHub release, DOI archive, scorer activation, or maturity advancement.",
        ),
        "RESEARCH.md": (
            "Published repository release: `0.6.0`",
            "Stable public-contract target: `1.0.0`, gated candidate, release prohibited",
            "Supported for one frozen Cigna packet",
            "Level 2, Applicable",
            "HIT-CRI-V100-001",
        ),
        "PROVENANCE.md": (
            "Public repository release: 0.6.0",
            "Stable public-contract target: `1.0.0`, gated candidate, release prohibited",
            "Post-0.6.0 readiness work, unreleased",
            "Research maturity: Level 2, Applicable",
        ),
        "LIMITATIONS.md": (
            "Clean-room implementability untested",
            "Candidate `0.7.0`, `0.9.0`, and `1.0.0` materials do not establish that those versions are released or stable.",
        ),
        "CHANGELOG.md": (
            "Machine-readable `1.0.0` stable-contract gate ledger",
            "Release metadata remains pinned to `0.6.0` until a later version is actually tagged and published",
            "## [0.6.0] - 2026-07-18",
        ),
        "SECURITY.md": (
            "`0.6.0`, latest tagged release",
            "The stable `1.0.0` target remains under gated development and is not yet a supported published release.",
        ),
        "GOVERNANCE.md": (
            "pre-`1.0.0` research and stabilization phase",
            "Candidate release files, merged readiness controls, branch names, and roadmap milestones do not authorize a tag or GitHub release.",
        ),
        "CONTRIBUTING.md": (
            "pre-`1.0.0` research specification",
            "Candidate `1.0.0` work must not change published-release metadata",
        ),
        "SPECIFICATION.md": (
            "**Status:** Released pre-1.0 normative contract",
            "**Version:** 0.4.0",
            "**Stable target:** 1.0.0, gated candidate",
            "## 14. Version stability and research maturity",
        ),
        "docs/releases/README.md": (
            "Current published release",
            "`1.0.0`, release prohibited",
            "Candidate documents may describe future versions, but they must not overwrite published-release metadata.",
        ),
        "docs/releases/v0.7.0-candidate.md": (
            "**Status:** Active candidate, release prohibited",
            "**Stable target:** `1.0.0`",
            "selected cases: 0 of 3",
        ),
        "docs/releases/v1.0.0-candidate.md": (
            "**Status:** Candidate outline, release prohibited",
            "**GitHub release:** Not created",
            "This draft must not be copied to the GitHub Releases page until every gate passes.",
        ),
        "docs/v1-readiness-plan.md": (
            "**Current repository release:** `0.6.0`",
            "Version `1.0.0` is a compatibility and implementation claim",
            "Withhold `1.0.0`",
        ),
    }

    for path, phrases in required_phrases.items():
        for phrase in phrases:
            require(failures, path, phrase)

    citation = yaml.safe_load(read("CITATION.cff"))
    zenodo = load_json(".zenodo.json")
    v1_lock = load_json("release/v1.0.0/contract-freeze.candidate.json")

    if citation.get("version") != PUBLISHED_RELEASE:
        failures.append("CITATION.cff must identify the latest published release 0.6.0")
    if zenodo.get("version") != PUBLISHED_RELEASE:
        failures.append(".zenodo.json must identify the latest published release 0.6.0")
    if citation.get("date-released") != "2026-07-18":
        failures.append("CITATION.cff release date drifted")
    if zenodo.get("upload_type") != "software":
        failures.append(".zenodo.json upload type changed")

    if v1_lock.get("target_repository_release") != STABLE_TARGET:
        failures.append("v1 gate ledger target changed")
    if v1_lock.get("status") != "candidate":
        failures.append("v1 gate ledger must remain candidate")
    if v1_lock.get("release_permitted") is not False:
        failures.append("v1 gate ledger must continue to prohibit release")

    spec = read("SPECIFICATION.md")
    if f"**Version:** {NORMATIVE_CONTRACT}" not in spec:
        failures.append("specification contract version drifted")

    readme = read("README.md")
    if f"**Conformance engine version:** {CONFORMANCE_ENGINE}" not in readme:
        failures.append("README conformance-engine version drifted")

    prohibited_public_claims = {
        "README.md": (
            "**Current release:** 1.0.0",
            "**Current release:** `1.0.0`",
            "**Current maturity:** Level 3",
        ),
        "docs/releases/v1.0.0-candidate.md": (
            "**Status:** Published",
            "**GitHub release:** Published",
        ),
    }

    for path, phrases in prohibited_public_claims.items():
        text = read(path)
        for phrase in phrases:
            if phrase in text:
                failures.append(f"{path}: premature public claim: {phrase}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT public release-status validation passed")
    print("- published release: 0.6.0")
    print("- normative contract: 0.4.0")
    print("- conformance engine: 0.5.0")
    print("- research maturity: Level 2, Applicable")
    print("- active empirical package: 0.7.0 candidate")
    print("- stable target: 1.0.0 candidate, release prohibited")
    return 0


if __name__ == "__main__":
    sys.exit(main())
