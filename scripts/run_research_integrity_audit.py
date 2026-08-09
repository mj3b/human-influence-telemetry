#!/usr/bin/env python3
"""Regenerate and verify the HIT v0.6.5 research-integrity audit and figures."""
from __future__ import annotations

import argparse
import copy
import csv
import io
import json
import re
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "evidence/claim-evidence-map.json"
SCHEMA_PATH = ROOT / "schemas/claim-evidence-map.schema.json"
CONTROLS_PATH = ROOT / "fixtures/research-integrity-negative-controls.json"
RESULT_PATH = ROOT / "audits/v0.6.5/audit-results.json"
REPORT_PATH = ROOT / "audits/v0.6.5/audit-report.md"
FIGURE_DATA_PATH = ROOT / "figures/data/claim-gates-v0.6.5.csv"
FIGURE_PATH = ROOT / "figures/generated/claim-gates-v0.6.5.svg"
FIGURE_MANIFEST_PATH = ROOT / "figures/v0.6.5-manifest.json"
FITNESS = ("directness", "contemporaneity", "independence", "completeness", "publication_authority")
GATES = ("traceability", "integrity", "human_support_review", "evidence_fitness", "dependency_closure")
EXCEPTIONS = (
    ("HIT-EX-01", "Current-contract external-rater replication is unresolved; PAPER-C04 remains blocked."),
    ("HIT-EX-02", "H4 and H7 lack complete external review; neither may enter the paper conclusion."),
    ("HIT-EX-03", "H5, H8, and H9 lack outcome, adoption, or clean-room evidence."),
    ("HIT-EX-04", "The responsible author supplied the recorded support review; no independent assessor reproduced the v0.6.5 fitness judgments."),
)


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def combine(states: list[str]) -> str:
    active = [state for state in states if state != "outside_scope"]
    if not active:
        return "outside_scope"
    if "fail" in active:
        return "fail"
    if "indeterminate" in active:
        return "indeterminate"
    return "pass"


def locator_resolves(path: Path, locator: str) -> bool:
    if not path.is_file():
        return False
    text = path.read_text(encoding="utf-8")
    return locator in text


def evaluate(data: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str]]:
    errors = [error.message for error in Draft202012Validator(load(SCHEMA_PATH)).iter_errors(data)]
    claims = {claim["claim_id"]: claim for claim in data.get("claims", [])}
    if len(claims) != len(data.get("claims", [])):
        errors.append("claim identifiers must be unique")
    rows: list[dict[str, Any]] = []
    provisional: dict[str, bool] = {}
    for claim in data.get("claims", []):
        evidence = claim["evidence"]
        traceability = "pass" if all(locator_resolves(ROOT / item["path"], item["locator"]) for item in evidence) else "fail"
        integrity = combine(["pass" if item["integrity"] in {"git_tracked", "locked_digest"} else "indeterminate" for item in evidence])
        support = combine(["pass" if item["support_review"] == "recorded" else ("outside_scope" if item["support_review"] == "outside_scope" else "indeterminate") for item in evidence])
        fitness = combine([claim["fitness"][name]["state"] for name in FITNESS])
        dependencies = claim["dependencies"]
        closure = "pass" if all(dependency in claims for dependency in dependencies) else "fail"
        computed = {"traceability": traceability, "integrity": integrity, "human_support_review": support, "evidence_fitness": fitness, "dependency_closure": closure}
        for gate in GATES:
            if claim["declared_gates"][gate] != computed[gate]:
                errors.append(f"{claim['claim_id']}: declared {gate} differs from computed state")
        provisional[claim["claim_id"]] = claim["status"] == "supported" and all(computed[gate] == "pass" for gate in GATES)
        rows.append({"claim_id": claim["claim_id"], **computed, "conclusion_eligible": False})
    changed = True
    while changed:
        changed = False
        for claim in data.get("claims", []):
            claim_id = claim["claim_id"]
            eligible = provisional[claim_id] and all(provisional.get(dep, False) for dep in claim["dependencies"])
            if eligible != provisional[claim_id]:
                provisional[claim_id] = eligible
                changed = True
    for row in rows:
        row["conclusion_eligible"] = provisional[row["claim_id"]]
        declared = claims[row["claim_id"]]["conclusion_eligible"]
        if declared != row["conclusion_eligible"]:
            errors.append(f"{row['claim_id']}: declared conclusion eligibility differs from computed state")
    return rows, errors


def mutate(source: dict[str, Any], control: dict[str, str]) -> dict[str, Any]:
    data = copy.deepcopy(source)
    claim = next(item for item in data["claims"] if item["claim_id"] == control["target_claim"])
    kind = control["mutation"]
    if kind == "missing_reference":
        claim["evidence"][0]["path"] = "fixtures/absent.json"
    elif kind == "pending_integrity":
        claim["evidence"][0]["integrity"] = "pending"
    elif kind == "support_review_removed":
        claim["evidence"][0]["support_review"] = "pending"
    elif kind == "fitness_failure":
        claim["fitness"]["directness"]["state"] = "fail"
    elif kind == "unresolved_dependency":
        claim["dependencies"] = ["PAPER-C99"]
    elif kind == "false_eligibility":
        claim["conclusion_eligible"] = True
    elif kind == "missing_locator":
        claim["evidence"][0]["locator"] = "CONTROLLED-MISSING-LOCATOR"
    elif kind == "replication_overclaim":
        claim["status"] = "supported"
        claim["conclusion_eligible"] = True
    else:
        raise ValueError(f"unknown mutation: {kind}")
    return data


def run_negative_controls(source: dict[str, Any]) -> list[dict[str, Any]]:
    output = []
    for control in load(CONTROLS_PATH)["controls"]:
        _, errors = evaluate(mutate(source, control))
        detected = bool(errors)
        output.append({"control_id": control["control_id"], "expected_gate": control["expected_gate"], "detected": detected, "message": errors[0] if errors else "controlled corruption escaped detection"})
    return output


def e5_errors() -> list[str]:
    targets = [ROOT / "paper", ROOT / "audits/v0.6.5", ROOT / "protocols/research-integrity-audit.md", ROOT / "docs/releases/v0.6.5.md"]
    prohibited = {
        "population-wide inter-rater reliability": "paper/PAPER-C04 boundary",
        "current-contract replication succeeded": "unresolved replication boundary",
        "proves meaningful human control": "H6 boundary",
        "independently adopted": "H8 boundary",
    }
    errors: list[str] = []
    for target in targets:
        paths = sorted(target.rglob("*.md")) if target.is_dir() else [target]
        for path in paths:
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for phrase, boundary in prohibited.items():
                for match in re.finditer(re.escape(phrase), text, re.IGNORECASE):
                    line = text[:match.start()].count("\n") + 1
                    context = text[max(0, match.start() - 100):match.end() + 120].lower()
                    if not any(marker in context for marker in ("does not", "has not", "blocked", "unsupported", "no ", "cannot", "prohibited")):
                        errors.append(f"{path.relative_to(ROOT)}:{line}: unbounded E5 phrase ({boundary})")
            if "—" in text:
                errors.append(f"{path.relative_to(ROOT)}: contains an em dash")
    return errors


def render_csv(rows: list[dict[str, Any]]) -> str:
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["claim_id", *GATES, "conclusion_eligible"])
    for row in rows:
        writer.writerow([row["claim_id"], *[row[gate] for gate in GATES], str(row["conclusion_eligible"]).lower()])
    return buffer.getvalue()


def render_svg(rows: list[dict[str, Any]]) -> str:
    colors = {"pass": "#24735b", "fail": "#b33a3a", "indeterminate": "#c48916", "outside_scope": "#78828c"}
    cell, label, top = 112, 95, 88
    width, height = label + cell * 6 + 24, top + len(rows) * 34 + 52
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">', '<rect width="100%" height="100%" fill="#fbfaf7"/>', '<style>text{font-family:Arial,sans-serif;fill:#17212b}.h{font-size:12px;font-weight:700}.c{font-size:12px}.s{font-size:11px;fill:white;font-weight:700}</style>', '<text x="16" y="24" class="h">HIT v0.6.5 claim-gate audit</text>']
    headers = ["Claim", "Traceability", "Integrity", "Support", "Fitness", "Closure", "Conclusion"]
    xs = [16, label, label + cell, label + cell * 2, label + cell * 3, label + cell * 4, label + cell * 5]
    for x, header in zip(xs, headers): out.append(f'<text x="{x}" y="58" class="h">{header}</text>')
    for index, row in enumerate(rows):
        y = top + index * 34
        out.append(f'<text x="16" y="{y + 18}" class="c">{row["claim_id"]}</text>')
        states = [row[gate] for gate in GATES] + (["pass"] if row["conclusion_eligible"] else ["fail"])
        for column, state in enumerate(states):
            x = label + column * cell
            out.append(f'<rect x="{x}" y="{y}" width="{cell - 5}" height="25" rx="3" fill="{colors[state]}"/>')
            label_text = "eligible" if column == 5 and row["conclusion_eligible"] else ("blocked" if column == 5 else state.replace("outside_scope", "n/a"))
            out.append(f'<text x="{x + 7}" y="{y + 17}" class="s">{label_text}</text>')
    out.append('</svg>\n')
    return "".join(out)


def render_report(result: dict[str, Any]) -> str:
    lines = ["# HIT v0.6.5 Research-Integrity Audit", "", f"**Audit date:** {result['audit_date']}", "", f"**State:** `{result['status']}`", "", f"**Scope:** {result['scope']}", "", "## Decision", "", "The mapped claim set passes the executable controls with published exceptions. H1, H2, H3, and three bounded paper claims may enter a conclusion. The audit blocks current-contract replication, causal, legal, adoption, outcome, and clean-room claims whose required evidence is absent or indeterminate.", "", "## Claim gates", "", "| Claim | Traceability | Integrity | Human review | Fitness | Closure | Conclusion |", "|---|---|---|---|---|---|---|"]
    for row in result["claim_results"]:
        lines.append(f"| {row['claim_id']} | {row['traceability']} | {row['integrity']} | {row['human_support_review']} | {row['evidence_fitness']} | {row['dependency_closure']} | {'eligible' if row['conclusion_eligible'] else 'blocked'} |")
    lines.extend(["", "## Negative controls", "", "| Control | Expected gate | Detected |", "|---|---|---|"])
    for row in result["negative_controls"]:
        lines.append(f"| {row['control_id']} | {row['expected_gate']} | {'yes' if row['detected'] else 'no'} |")
    lines.extend(["", "## Published exceptions", ""])
    lines.extend([f"- `{identifier}`: {text}" for identifier, text in EXCEPTIONS])
    lines.extend(["", "## Interpretation", "", "`PASS_WITH_EXCEPTIONS` means the committed controls behaved as declared and every blocked claim remains blocked. It does not establish source truth, population reliability, current-contract replication, causal validity, legal conformity, or independent adoption.", ""])
    return "\n".join(lines)


def build() -> tuple[dict[str, Any], str, str, str, str]:
    source = load(MAP_PATH)
    rows, errors = evaluate(source)
    errors.extend(e5_errors())
    controls = run_negative_controls(source)
    escaped = [row for row in controls if not row["detected"]]
    status = "FAIL" if errors or escaped else "PASS_WITH_EXCEPTIONS"
    result = {"version": "0.6.5", "audit_id": "HIT-COE-AUDIT-V0.6.5", "audit_date": "2026-08-09", "scope": source["scope"], "status": status, "errors": errors, "exceptions": [item[0] for item in EXCEPTIONS], "negative_controls": controls, "claim_results": rows}
    csv_text, svg_text = render_csv(rows), render_svg(rows)
    manifest = {"version": "0.6.5", "figure_id": "HIT-FIG-COE-01", "title": "Claim-gate audit states", "source": "audits/v0.6.5/audit-results.json", "derived_data": str(FIGURE_DATA_PATH.relative_to(ROOT)), "generated_figure": str(FIGURE_PATH.relative_to(ROOT)), "generator": "scripts/run_research_integrity_audit.py", "reproduction_command": "python scripts/run_research_integrity_audit.py"}
    return result, render_report(result), csv_text, svg_text, json.dumps(manifest, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result, report, csv_text, svg_text, manifest = build()
    outputs = ((RESULT_PATH, json.dumps(result, indent=2) + "\n"), (REPORT_PATH, report), (FIGURE_DATA_PATH, csv_text), (FIGURE_PATH, svg_text), (FIGURE_MANIFEST_PATH, manifest))
    if args.check:
        stale = [str(path.relative_to(ROOT)) for path, content in outputs if not path.is_file() or path.read_text(encoding="utf-8") != content]
        if stale:
            print("stale generated outputs: " + ", ".join(stale))
            return 1
    else:
        for path, content in outputs:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    print(f"research-integrity audit: {result['status']} ({len(result['claim_results'])} claims; {sum(row['detected'] for row in result['negative_controls'])}/{len(result['negative_controls'])} controls detected)")
    return 0 if result["status"] != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
