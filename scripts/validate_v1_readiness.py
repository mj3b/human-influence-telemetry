#!/usr/bin/env python3
"""Validate HIT v1 readiness staging and draft manual-workbook controls."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANUAL_DIR = ROOT / "validation" / "v0.7.0" / "manual-workbooks"
ASSET_MANIFEST = MANUAL_DIR / "candidate-assets-manifest.json"
WORKBOOK_CONTRACT = MANUAL_DIR / "manual-workbook-contract.json"
V1_LOCK = ROOT / "release" / "v1.0.0" / "contract-freeze.candidate.json"
V1_PLAN = ROOT / "docs" / "v1-readiness-plan.md"
V1_RELEASE = ROOT / "docs" / "releases" / "v1.0.0-candidate.md"
ACTIVE_PROTOCOL = ROOT / "validation" / "v0.7.0" / "protocol-lock.candidate.json"

EXPECTED_SCORERS = ["HIT-SCORER-A", "HIT-SCORER-B", "HIT-SCORER-C"]
EXPECTED_FILENAMES = {
    "HIT-SCORER-A-HIT040-manual-workbook-draft.docx",
    "HIT-SCORER-A-HIT040-manual-workbook-draft.pdf",
    "HIT-SCORER-B-HIT040-manual-workbook-draft.docx",
    "HIT-SCORER-B-HIT040-manual-workbook-draft.pdf",
    "HIT-SCORER-C-HIT040-manual-workbook-draft.docx",
    "HIT-SCORER-C-HIT040-manual-workbook-draft.pdf",
    "HIT-IRP-HIT040-002-manual-scorer-workbook-template.docx",
    "HIT-IRP-HIT040-002-manual-scorer-workbook-template.pdf",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def require_file(path: Path, failures: list[str]) -> None:
    if not path.is_file() or path.stat().st_size == 0:
        failures.append(f"missing or empty file: {path.relative_to(ROOT)}")


def main() -> int:
    failures: list[str] = []

    for path in (
        MANUAL_DIR / "README.md",
        ASSET_MANIFEST,
        WORKBOOK_CONTRACT,
        V1_LOCK,
        V1_PLAN,
        V1_RELEASE,
        ACTIVE_PROTOCOL,
    ):
        require_file(path, failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    assets = load_json(ASSET_MANIFEST)
    if assets.get("protocol_id") != "HIT-IRP-HIT040-002":
        failures.append("manual asset manifest protocol ID changed")
    if assets.get("status") != "draft_scoring_prohibited":
        failures.append("manual assets must remain draft and scoring prohibited")
    if assets.get("assessment_contract_version") != "0.4.0":
        failures.append("manual assets must target assessment contract 0.4.0")
    if assets.get("conformance_engine_version") != "0.5.0":
        failures.append("manual assets must identify conformance engine 0.5.0")
    if assets.get("packet_ids") != []:
        failures.append("manual assets may not assign packet IDs before human selection and freeze")
    if assets.get("rendered_page_count_per_workbook") != 31:
        failures.append("manual workbook page count must remain recorded as 31")
    if assets.get("visual_review_status") != "passed_all_pages":
        failures.append("manual workbook visual review must cover every page")
    if assets.get("activation_requires_locked_protocol") is not True:
        failures.append("manual assets must require locked protocol activation")
    if assets.get("activation_requires_three_packet_ids") is not True:
        failures.append("manual assets must require three packet IDs")
    if assets.get("activation_requires_v070_publication") is not True:
        failures.append("manual assets must require v0.7.0 publication")

    bundle = assets.get("bundle", {})
    if bundle.get("publication_status") != "candidate_asset_not_published":
        failures.append("manual workbook ZIP must remain an unpublished candidate asset")
    if not isinstance(bundle.get("size_bytes"), int) or bundle.get("size_bytes", 0) <= 0:
        failures.append("manual workbook ZIP size missing")
    if not isinstance(bundle.get("sha256"), str) or len(bundle.get("sha256", "")) != 64:
        failures.append("manual workbook ZIP hash invalid")

    files = assets.get("files", [])
    filenames = {item.get("filename") for item in files}
    if filenames != EXPECTED_FILENAMES:
        failures.append("manual asset manifest must contain exactly eight declared files")
    for item in files:
        if not isinstance(item.get("size_bytes"), int) or item.get("size_bytes", 0) <= 0:
            failures.append(f"invalid size for {item.get('filename')}")
        if not isinstance(item.get("sha256"), str) or len(item.get("sha256", "")) != 64:
            failures.append(f"invalid SHA-256 for {item.get('filename')}")

    binary_files = [
        path for path in MANUAL_DIR.iterdir()
        if path.suffix.lower() in {".docx", ".pdf", ".zip"}
    ]
    if binary_files:
        failures.append("candidate workbook binaries belong in release assets, not the repository tree")

    contract = load_json(WORKBOOK_CONTRACT)
    if contract.get("contract_id") != "HIT-MANUAL-WORKBOOK-HIT040-001":
        failures.append("manual workbook contract ID changed")
    if contract.get("status") != "candidate":
        failures.append("manual workbook contract must remain candidate")
    if contract.get("scoring_permitted") is not False:
        failures.append("manual workbook contract must not permit scoring")
    if contract.get("required_scorer_public_ids") != EXPECTED_SCORERS:
        failures.append("manual workbook contract must require scorer IDs A, B, and C")
    if contract.get("required_packet_count") != 3:
        failures.append("manual workbook contract must require three packets")
    if contract.get("required_packet_ids") != []:
        failures.append("manual workbook contract must not preassign packet IDs")
    if contract.get("generative_ai_substantive_assistance_allowed") is not False:
        failures.append("manual workbook contract must prohibit generative AI substantive assistance")
    if contract.get("original_working_record_preserved") is not True:
        failures.append("manual workbook contract must preserve original records")
    if contract.get("adjudication_may_overwrite_original") is not False:
        failures.append("adjudication may not overwrite original scorer records")

    active = load_json(ACTIVE_PROTOCOL)
    if active.get("status") != "candidate":
        failures.append("active v0.7.0 protocol must remain candidate in this increment")
    if active.get("scoring_permitted") is not False:
        failures.append("active v0.7.0 protocol must continue to prohibit scoring")
    if active.get("required_scorers") != 3 or active.get("required_submissions") != 9:
        failures.append("active protocol must retain the three-scorer, nine-submission design")
    if active.get("packet_ids") != []:
        failures.append("active protocol must not assign packet IDs in this increment")

    v1 = load_json(V1_LOCK)
    if v1.get("target_repository_release") != "1.0.0":
        failures.append("v1 target release changed")
    if v1.get("status") != "candidate" or v1.get("release_permitted") is not False:
        failures.append("v1 contract freeze must remain a non-releasable candidate")
    if v1.get("research_maturity_is_separate") is not True:
        failures.append("v1 semantic stability must remain separate from research maturity")
    if v1.get("current_repository_release") != "0.6.0":
        failures.append("v1 readiness baseline must identify repository release 0.6.0")
    current = v1.get("current_component_versions", {})
    expected_current = {
        "specification": "0.4.0",
        "assessment_schema": "0.4.0",
        "dimension_catalog": "0.4.0",
        "application_handbook": "0.4.0",
        "conformance_engine": "0.5.0",
    }
    if current != expected_current:
        failures.append("v1 readiness current component map is inconsistent")
    target = v1.get("target_component_versions", {})
    if set(target.values()) != {"1.0.0"}:
        failures.append("all stable target components must be 1.0.0")
    blockers = set(v1.get("blocking_gates", []))
    required_blockers = {
        "signed_human_case_selection",
        "three_frozen_current_contract_packets",
        "v0.7.0_locked_protocol_publication",
        "standalone_implementation_packet",
        "clean_room_implementation_audit",
        "public_v0.9.0_release_candidate",
        "exact_release_commit_validation",
    }
    if not required_blockers.issubset(blockers):
        failures.append("v1 readiness ledger is missing mandatory blockers")

    plan = V1_PLAN.read_text(encoding="utf-8")
    for phrase in (
        "Current repository release:** `0.6.0`",
        "Current research maturity:** Level 2, Applicable",
        "Version `1.0.0` is a compatibility and implementation claim",
        "Draft manual workbooks now exist",
        "Withhold `1.0.0`",
        "Publish `v0.9.0`",
    ):
        if phrase not in plan:
            failures.append(f"v1 readiness plan missing required statement: {phrase}")

    release = V1_RELEASE.read_text(encoding="utf-8")
    for phrase in (
        "Status:** Candidate outline, release prohibited",
        "Current normative contract:** `0.4.0`",
        "Current conformance engine:** `0.5.0`",
        "public `v0.9.0` release candidate",
        "DRAFT - SCORING PROHIBITED",
    ):
        if phrase not in release:
            failures.append(f"v1 candidate release outline missing required statement: {phrase}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print("HIT v1 readiness staging validation passed")
    print("- current repository release: 0.6.0")
    print("- current normative contract: 0.4.0")
    print("- current conformance engine: 0.5.0")
    print("- manual workbooks: 3 scorer-specific plus 1 master, DOCX and PDF")
    print("- manual workbook status: draft, scoring prohibited")
    print("- v1 release permitted: no")
    print("- active protocol: candidate, 3 scorers, 9 submissions, 0 packet IDs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
