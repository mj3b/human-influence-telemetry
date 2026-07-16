#!/usr/bin/env python3
"""Validate one HIT independent-scorer submission."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from compare_raters import DEFAULT_SCHEMA, SubmissionError, load_json, validate_submission


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("submission", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        schema = load_json(args.schema)
        if not isinstance(schema, dict):
            raise SubmissionError("submission schema must be a JSON object")
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        submission = validate_submission(
            load_json(args.submission), validator, str(args.submission)
        )
    except (SubmissionError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    scorer_id = submission["scorer"]["public_id"]
    print(f"VALID: {args.submission} ({scorer_id})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
