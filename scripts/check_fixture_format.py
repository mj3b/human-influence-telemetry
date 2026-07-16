#!/usr/bin/env python3
"""Reject minified or non-canonical JSON in deterministic HIT fixtures."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FIXTURES_DIR = ROOT / "fixtures"


def canonical_json(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    failures: list[str] = []
    fixture_paths = sorted(FIXTURES_DIR.glob("*.json"))

    if not fixture_paths:
        failures.append("no fixture JSON files were found")

    for path in fixture_paths:
        try:
            text = path.read_text(encoding="utf-8")
            value = json.loads(text)
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"{path.relative_to(ROOT)}: cannot parse JSON: {exc}")
            continue

        if text != canonical_json(value):
            failures.append(
                f"{path.relative_to(ROOT)}: use two-space indented canonical JSON with a final newline"
            )

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print(f"Fixture formatting: PASS ({len(fixture_paths)} readable JSON files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
