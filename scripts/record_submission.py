#!/usr/bin/env python3
"""Create an immutable receipt record for one scorer submission."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("submission", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--received-at",
        help="ISO-8601 receipt time. Defaults to the current UTC time.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("submission must be a JSON object")
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    args = parse_args()
    try:
        submission = load_json(args.submission)
        received_at = args.received_at or datetime.now(timezone.utc).isoformat()
        receipt = {
            "receipt_version": "1.0.0",
            "submission_filename": args.submission.name,
            "submission_sha256": sha256_file(args.submission),
            "submission_size_bytes": args.submission.stat().st_size,
            "received_at": received_at,
            "submission_id": submission.get("submission_id"),
            "protocol_id": submission.get("protocol_id"),
            "protocol_version": submission.get("protocol_version"),
            "packet_id": submission.get("packet_id"),
            "scorer_public_id": submission.get("scorer", {}).get("public_id"),
            "preservation_statement": (
                "The receipt identifies the original file received by the coordinator. "
                "The referenced submission must not be substantively edited."
            ),
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"RECEIPT: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
