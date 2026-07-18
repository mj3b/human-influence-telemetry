"""Deterministic complete-record conformance suite for HIT v0.5.0 development."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

from src.models.conformance import AssessmentConformanceResult
from src.validation.assessment import load_json, validate_assessment


def _tokens(pointer: str) -> list[str]:
    if not pointer.startswith("/"):
        raise ValueError(f"JSON pointer must start with '/': {pointer}")
    if pointer == "/":
        return []
    return [
        token.replace("~1", "/").replace("~0", "~")
        for token in pointer[1:].split("/")
    ]


def _resolve_parent(document: Any, pointer: str) -> tuple[Any, str]:
    tokens = _tokens(pointer)
    if not tokens:
        raise ValueError("root replacement is not supported")
    current = document
    for token in tokens[:-1]:
        current = current[int(token)] if isinstance(current, list) else current[token]
    return current, tokens[-1]


def apply_mutations(
    document: dict[str, Any], mutations: list[dict[str, Any]]
) -> dict[str, Any]:
    mutated = copy.deepcopy(document)
    for mutation in mutations:
        operation = mutation.get("op")
        pointer = str(mutation.get("path"))
        parent, token = _resolve_parent(mutated, pointer)
        key: int | str = int(token) if isinstance(parent, list) else token
        if operation == "set":
            parent[key] = copy.deepcopy(mutation.get("value"))
        elif operation == "delete":
            del parent[key]
        elif operation == "append":
            target = parent[key]
            if not isinstance(target, list):
                raise ValueError(f"append target is not a list: {pointer}")
            target.append(copy.deepcopy(mutation.get("value")))
        else:
            raise ValueError(f"unsupported mutation operation: {operation}")
    return mutated


def _digest(value: Any) -> str:
    payload = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def run_complete_record_suite(
    *,
    schema_path: Path,
    base_record_path: Path,
    suite_path: Path,
) -> dict[str, Any]:
    schema = load_json(schema_path)
    base_record = load_json(base_record_path)
    suite = load_json(suite_path)
    cases_out: list[dict[str, Any]] = []
    suite_valid = True

    for case in sorted(
        suite.get("cases", []), key=lambda item: str(item.get("case_id"))
    ):
        case_id = str(case.get("case_id"))
        record = apply_mutations(base_record, case.get("mutations", []))
        result: AssessmentConformanceResult = validate_assessment(
            record,
            schema,
            source=case_id,
        )
        actual_codes = sorted(
            {issue.code for issue in result.issues if issue.severity == "error"}
        )
        expected_codes = sorted(set(case.get("expected_error_codes", [])))
        expectation_met = result.valid is bool(case.get("expected_valid"))
        if expected_codes:
            expectation_met = expectation_met and all(
                code in actual_codes for code in expected_codes
            )
        suite_valid = suite_valid and expectation_met
        cases_out.append(
            {
                "case_id": case_id,
                "description": case.get("description"),
                "expected_valid": bool(case.get("expected_valid")),
                "expected_error_codes": expected_codes,
                "actual_valid": result.valid,
                "actual_error_codes": actual_codes,
                "expectation_met": expectation_met,
                "record_digest_sha256": _digest(record),
                "result": result.to_dict(),
            }
        )

    return {
        "suite_id": suite.get("suite_id"),
        "suite_version": suite.get("suite_version"),
        "contract": suite.get("contract"),
        "valid": suite_valid,
        "case_count": len(cases_out),
        "passed_case_count": sum(
            1 for item in cases_out if item["expectation_met"]
        ),
        "failed_case_count": sum(
            1 for item in cases_out if not item["expectation_met"]
        ),
        "base_record_digest_sha256": _digest(base_record),
        "cases": cases_out,
    }
