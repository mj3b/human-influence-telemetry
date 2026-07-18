#!/usr/bin/env python3
"""Enforce canonical formatting for the three historical deterministic fixtures."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATHS = [
    ROOT / "fixtures" / "substantive-human-influence.json",
    ROOT / "fixtures" / "ceremonial-review.json",
    ROOT / "fixtures" / "insufficient-evidence.json",
]
CANONICAL_EXAMPLE = ROOT / "fixtures" / "v0.4.0-canonical-example.json"


def canonical_json(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    failures: list[str] = []

    for path in FIXTURE_PATHS:
        if not path.is_file():
            failures.append(f"{path.relative_to(ROOT)}: historical fixture is missing")
            continue
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

    if not CANONICAL_EXAMPLE.is_file():
        failures.append("fixtures/v0.4.0-canonical-example.json: canonical example is missing")
    else:
        try:
            json.loads(CANONICAL_EXAMPLE.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"fixtures/v0.4.0-canonical-example.json: cannot parse JSON: {exc}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print("Fixture formatting: PASS (3 historical fixtures; canonical example parseable)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
