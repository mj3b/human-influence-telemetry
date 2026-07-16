#!/usr/bin/env python3
"""Compare two independent HIT scorer submissions deterministically."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "validation" / "scorer-submission.schema.json"
DIMENSIONS = (
    "counsel",
    "judgment",
    "command",
    "correction",
    "repair",
    "reform",
)
EXPECTED_SOURCE_IDS = {"S1", "S2", "S3"}
MINIMUM_EXACT_AGREEMENTS = 6
TOTAL_ITEMS = 7


class SubmissionError(ValueError):
    """Raised when a scorer submission is invalid for comparison."""


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise SubmissionError(f"cannot read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise SubmissionError(f"cannot parse JSON {path}: {exc}") from exc


def validate_submission(
    submission: Any,
    validator: Draft202012Validator,
    label: str,
) -> dict[str, Any]:
    if not isinstance(submission, dict):
        raise SubmissionError(f"{label}: submission must be a JSON object")

    schema_errors = sorted(
        validator.iter_errors(submission),
        key=lambda error: list(error.path),
    )
    if schema_errors:
        messages = "; ".join(
            f"{'.'.join(str(part) for part in error.path) or '<root>'}: {error.message}"
            for error in schema_errors
        )
        raise SubmissionError(f"{label}: schema validation failed: {messages}")

    findings = submission.get("substantive_findings", [])
    dimensions = [item.get("dimension") for item in findings]
    if set(dimensions) != set(DIMENSIONS) or len(dimensions) != len(set(dimensions)):
        raise SubmissionError(
            f"{label}: substantive findings must contain each dimension exactly once"
        )

    source_access = submission.get("source_access", [])
    source_ids = [item.get("source_id") for item in source_access]
    if set(source_ids) != EXPECTED_SOURCE_IDS or len(source_ids) != len(set(source_ids)):
        raise SubmissionError(
            f"{label}: source_access must contain S1, S2, and S3 exactly once"
        )
    if not all(item.get("access_complete") is True for item in source_access):
        raise SubmissionError(f"{label}: every frozen source must be accessed completely")

    return submission


def finding_map(submission: dict[str, Any]) -> dict[str, int | str]:
    return {
        str(item["dimension"]): item["finding"]
        for item in submission["substantive_findings"]
    }


def is_critical_substantive(a: int | str, b: int | str) -> tuple[bool, str | None]:
    if a == b:
        return False, None
    if (a == "IE") != (b == "IE"):
        return True, "IE versus determinate substantive finding"
    if {a, b} == {0, 2}:
        return True, "opposite substantive findings 0 versus 2"
    return False, None


def is_critical_integrity(a: str, b: str) -> tuple[bool, str | None]:
    if a == b:
        return False, None
    if (a == "IE") != (b == "IE"):
        return True, "Telemetry Integrity IE versus determinate status"
    return False, None


def cohens_kappa(values_a: list[int | str], values_b: list[int | str]) -> float | None:
    if len(values_a) != len(values_b) or not values_a:
        return None

    n = len(values_a)
    observed = sum(a == b for a, b in zip(values_a, values_b, strict=True)) / n
    counts_a = Counter(str(value) for value in values_a)
    counts_b = Counter(str(value) for value in values_b)
    categories = set(counts_a) | set(counts_b)
    expected = sum(
        (counts_a[category] / n) * (counts_b[category] / n)
        for category in categories
    )

    if expected == 1.0:
        return None
    return (observed - expected) / (1.0 - expected)


def compare_submissions(
    submission_a: dict[str, Any],
    submission_b: dict[str, Any],
) -> dict[str, Any]:
    if submission_a["protocol_id"] != submission_b["protocol_id"]:
        raise SubmissionError("submissions use different protocol IDs")
    if submission_a["protocol_version"] != submission_b["protocol_version"]:
        raise SubmissionError("submissions use different protocol versions")
    if submission_a["packet_id"] != submission_b["packet_id"]:
        raise SubmissionError("submissions use different packet IDs")

    scorer_a = submission_a["scorer"]["public_id"]
    scorer_b = submission_b["scorer"]["public_id"]
    if scorer_a == scorer_b:
        raise SubmissionError("scorer public IDs must be distinct")

    findings_a = finding_map(submission_a)
    findings_b = finding_map(submission_b)
    disagreements: list[dict[str, Any]] = []
    exact_agreements = 0

    for dimension in DIMENSIONS:
        value_a = findings_a[dimension]
        value_b = findings_b[dimension]
        if value_a == value_b:
            exact_agreements += 1
            continue
        critical, reason = is_critical_substantive(value_a, value_b)
        disagreements.append(
            {
                "dimension": dimension,
                "scorer_a_finding": value_a,
                "scorer_b_finding": value_b,
                "critical": critical,
                "mechanical_reason": reason,
            }
        )

    integrity_a = submission_a["telemetry_integrity"]["status"]
    integrity_b = submission_b["telemetry_integrity"]["status"]
    if integrity_a == integrity_b:
        exact_agreements += 1
    else:
        critical, reason = is_critical_integrity(integrity_a, integrity_b)
        disagreements.append(
            {
                "dimension": "telemetry_integrity",
                "scorer_a_finding": integrity_a,
                "scorer_b_finding": integrity_b,
                "critical": critical,
                "mechanical_reason": reason,
            }
        )

    critical_disagreements = [item for item in disagreements if item["critical"]]
    exact_proportion = exact_agreements / TOTAL_ITEMS
    kappa = cohens_kappa(
        [findings_a[dimension] for dimension in DIMENSIONS],
        [findings_b[dimension] for dimension in DIMENSIONS],
    )
    threshold_met = (
        exact_agreements >= MINIMUM_EXACT_AGREEMENTS
        and not critical_disagreements
    )

    return {
        "protocol_id": submission_a["protocol_id"],
        "protocol_version": submission_a["protocol_version"],
        "packet_id": submission_a["packet_id"],
        "scorer_a": scorer_a,
        "scorer_b": scorer_b,
        "items_compared": TOTAL_ITEMS,
        "exact_agreements": exact_agreements,
        "exact_agreement_proportion": round(exact_proportion, 4),
        "minimum_exact_agreements": MINIMUM_EXACT_AGREEMENTS,
        "critical_disagreement_count": len(critical_disagreements),
        "disagreements": disagreements,
        "substantive_dimension_cohens_kappa": (
            None if kappa is None else round(kappa, 4)
        ),
        "advancement_threshold_met": threshold_met,
        "interpretation_boundary": (
            "This comparison measures agreement for one frozen packet. "
            "It does not establish general reliability, causal validity, or legal correctness."
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    lines = [
        "# HIT Pre-adjudication Inter-rater Comparison",
        "",
        f"- Protocol: `{result['protocol_id']}` version `{result['protocol_version']}`",
        f"- Packet: `{result['packet_id']}`",
        f"- Scorers: `{result['scorer_a']}` and `{result['scorer_b']}`",
        f"- Exact agreement: {result['exact_agreements']} / {result['items_compared']} "
        f"(`{result['exact_agreement_proportion']:.4f}`)",
        f"- Critical disagreements: {result['critical_disagreement_count']}",
        f"- Supplementary substantive-dimension Cohen's kappa: "
        f"`{result['substantive_dimension_cohens_kappa']}`",
        f"- Advancement threshold met: **{'yes' if result['advancement_threshold_met'] else 'no'}**",
        "",
        "## Disagreements",
        "",
    ]

    disagreements = result["disagreements"]
    if not disagreements:
        lines.append("No finding disagreements.")
    else:
        lines.extend(
            [
                "| Item | Scorer A | Scorer B | Critical | Mechanical reason |",
                "|---|---:|---:|---|---|",
            ]
        )
        for item in disagreements:
            lines.append(
                f"| {item['dimension']} | `{item['scorer_a_finding']}` | "
                f"`{item['scorer_b_finding']}` | "
                f"{'yes' if item['critical'] else 'no'} | "
                f"{item['mechanical_reason'] or ''} |"
            )

    lines.extend(
        [
            "",
            "## Interpretation boundary",
            "",
            result["interpretation_boundary"],
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare two schema-valid independent HIT scorer submissions."
    )
    parser.add_argument("submission_a", type=Path)
    parser.add_argument("submission_b", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--require-threshold",
        action="store_true",
        help="Return exit status 1 when the advancement threshold is not met.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        schema = load_json(args.schema)
        if not isinstance(schema, dict):
            raise SubmissionError("submission schema must be a JSON object")
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())

        submission_a = validate_submission(
            load_json(args.submission_a), validator, str(args.submission_a)
        )
        submission_b = validate_submission(
            load_json(args.submission_b), validator, str(args.submission_b)
        )
        result = compare_submissions(submission_a, submission_b)
    except SubmissionError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    output = (
        json.dumps(result, indent=2, sort_keys=False) + "\n"
        if args.format == "json"
        else render_markdown(result)
    )

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")

    if args.require_threshold and not result["advancement_threshold_met"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
