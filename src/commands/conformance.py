"""CLI command for HIT assessment and repository conformance."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from src.conformance.runner import run_repository_conformance, validate_file


def _render_text(report: dict[str, Any]) -> str:
    if "checks" in report:
        suite = report["checks"]["complete_record_suite"]
        status = "PASS" if report["valid"] else "FAIL"
        return "\n".join(
            [
                f"HIT repository conformance: {status}",
                f"- released contract: {'PASS' if report['checks']['released_contract']['passed'] else 'FAIL'}",
                f"- fixture formatting: {'PASS' if report['checks']['fixture_format']['passed'] else 'FAIL'}",
                f"- compatibility manifest: {'PASS' if report['checks']['compatibility_manifest']['valid'] else 'FAIL'}",
                f"- complete-record cases: {suite['passed_case_count']}/{suite['case_count']}",
                f"- deterministic report: {'PASS' if report['checks']['self_tests']['deterministic_report']['valid'] else 'FAIL'}",
                f"- protected migration plans: {'PASS' if all(item['valid'] for item in report['checks']['self_tests']['historical_migration_plans']) else 'FAIL'}",
                "- specification/schema/catalog: 0.4.0",
                "- research maturity: unchanged",
            ]
        )
    status = "PASS" if report.get("valid") else "FAIL"
    lines = [
        f"HIT assessment conformance: {status}",
        f"- source: {report.get('source')}",
    ]
    for issue in report.get("issues", []):
        lines.append(f"- {issue['code']} {issue['path']}: {issue['message']}")
    return "\n".join(lines)


def run(args: Any) -> int:
    report = run_repository_conformance() if args.all else validate_file(Path(args.path))
    rendered = (
        json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
        if args.format == "json"
        else _render_text(report) + "\n"
    )
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0 if report.get("valid") else 1
