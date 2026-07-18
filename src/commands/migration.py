"""CLI command for non-mutating historical-assessment migration planning."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from src.conformance.migration import build_migration_plan


def _render_text(plan: dict[str, Any]) -> str:
    status = "PASS" if plan.get("valid_plan") else "FAIL"
    lines = [
        f"HIT migration plan: {status}",
        f"- source: {plan.get('source')}",
        f"- source schema: {plan.get('source_schema_version')}",
        f"- target schema: {plan.get('target_schema_version')}",
        f"- disposition: {plan.get('disposition')}",
        "- automatic migration: prohibited",
        "- original preservation: required",
    ]
    for requirement in plan.get("requirements", []):
        lines.append(f"- requirement: {requirement}")
    return "\n".join(lines)


def run(args: Any) -> int:
    plan = build_migration_plan(Path(args.path))
    rendered = (
        json.dumps(plan, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
        if args.format == "json"
        else _render_text(plan) + "\n"
    )
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0 if plan.get("valid_plan") else 1
