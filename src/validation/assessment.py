"""Complete-record conformance checks for HIT specification and schema 0.4.0."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

from src.models.conformance import AssessmentConformanceResult, ConformanceIssue

EXPECTED_DIMENSIONS = {
    "counsel",
    "judgment",
    "command",
    "correction",
    "repair",
    "reform",
}
REFERENCE_FIELDS = {
    "supporting_claim_ids": "supports",
    "contradicting_claim_ids": "contradicts",
    "limiting_claim_ids": "limits",
}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise RuntimeError(f"cannot load {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"cannot parse JSON {path}: {exc}") from exc


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _issue(code: str, path: str, message: str) -> ConformanceIssue:
    return ConformanceIssue(code=code, path=path, message=message)


def _derive_integrity(institutional: str | None, packet: str | None) -> str:
    statuses = {institutional, packet}
    if "unreliable" in statuses:
        return "unreliable"
    if "IE" in statuses:
        return "IE"
    if "limited" in statuses:
        return "limited"
    return "adequate"


def validate_assessment(
    instance: dict[str, Any],
    schema: dict[str, Any],
    *,
    source: str,
) -> AssessmentConformanceResult:
    """Validate one complete HIT assessment structurally and semantically."""

    issues: list[ConformanceIssue] = []
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    schema_errors = sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
    for error in schema_errors:
        issues.append(_issue("HIT-SCHEMA", _pointer(error.path), error.message))

    findings = instance.get("substantive_findings", [])
    actors = instance.get("actors", [])
    claims = instance.get("evidence_claims", [])

    finding_dimensions = [item.get("dimension") for item in findings if isinstance(item, dict)]
    if len(finding_dimensions) != 6 or set(finding_dimensions) != EXPECTED_DIMENSIONS:
        issues.append(
            _issue(
                "HIT-DIMENSION-COVERAGE",
                "/substantive_findings",
                "each substantive dimension must appear exactly once",
            )
        )

    actor_ids = [item.get("actor_id") for item in actors if isinstance(item, dict)]
    claim_ids = [item.get("claim_id") for item in claims if isinstance(item, dict)]
    if len(actor_ids) != len(set(actor_ids)):
        issues.append(_issue("HIT-ACTOR-ID-DUPLICATE", "/actors", "actor IDs must be unique"))
    if len(claim_ids) != len(set(claim_ids)):
        issues.append(
            _issue("HIT-CLAIM-ID-DUPLICATE", "/evidence_claims", "claim IDs must be unique")
        )

    actor_map = {
        item.get("actor_id"): item
        for item in actors
        if isinstance(item, dict) and isinstance(item.get("actor_id"), str)
    }
    claim_map = {
        item.get("claim_id"): item
        for item in claims
        if isinstance(item, dict) and isinstance(item.get("claim_id"), str)
    }

    for index, actor in enumerate(actors):
        if not isinstance(actor, dict):
            continue
        actor_id = actor.get("actor_id")
        for related in actor.get("related_actor_ids", []):
            if related not in actor_map:
                issues.append(
                    _issue(
                        "HIT-ACTOR-REFERENCE",
                        f"/actors/{index}/related_actor_ids",
                        f"unknown related actor: {related}",
                    )
                )
        for claim_id in actor.get("evidence_claim_ids", []):
            claim = claim_map.get(claim_id)
            if claim is None:
                issues.append(
                    _issue(
                        "HIT-CLAIM-REFERENCE",
                        f"/actors/{index}/evidence_claim_ids",
                        f"unknown evidence claim: {claim_id}",
                    )
                )
            elif actor_id not in claim.get("actor_ids", []):
                issues.append(
                    _issue(
                        "HIT-ACTOR-CLAIM-RECIPROCITY",
                        f"/actors/{index}/evidence_claim_ids",
                        f"claim {claim_id} does not attribute its proposition to actor {actor_id}",
                    )
                )

    for index, claim in enumerate(claims):
        if not isinstance(claim, dict):
            continue
        for actor_id in claim.get("actor_ids", []):
            if actor_id not in actor_map:
                issues.append(
                    _issue(
                        "HIT-ACTOR-REFERENCE",
                        f"/evidence_claims/{index}/actor_ids",
                        f"unknown actor: {actor_id}",
                    )
                )
        locator = claim.get("locator", {})
        if (
            isinstance(locator, dict)
            and locator.get("locator_type") == "other"
            and not locator.get("reproducibility_note")
        ):
            issues.append(
                _issue(
                    "HIT-CITATION-OTHER-NOTE",
                    f"/evidence_claims/{index}/locator/reproducibility_note",
                    "locator_type 'other' requires a reproducibility note",
                )
            )

    for index, finding in enumerate(findings):
        if not isinstance(finding, dict):
            continue
        dimension = finding.get("dimension")
        value = finding.get("finding")
        state = finding.get("evidence_state")

        expected_states: dict[Any, set[str]] = {
            0: {"affirmative_absence"},
            1: {"formal_presence"},
            2: {"operational_capability", "observed_exercise"},
            "IE": {"indeterminate"},
        }
        if value in expected_states and state not in expected_states[value]:
            issues.append(
                _issue(
                    "HIT-FINDING-STATE",
                    f"/substantive_findings/{index}/evidence_state",
                    f"finding {value!r} is inconsistent with evidence state {state!r}",
                )
            )
        if value in {0, 1, 2} and not finding.get("supporting_claim_ids"):
            issues.append(
                _issue(
                    "HIT-DETERMINATE-SUPPORT",
                    f"/substantive_findings/{index}/supporting_claim_ids",
                    "a determinate finding requires at least one supporting evidence claim",
                )
            )
        if value == "IE":
            if not finding.get("unresolved_proposition"):
                issues.append(
                    _issue(
                        "HIT-IE-PROPOSITION",
                        f"/substantive_findings/{index}/unresolved_proposition",
                        "IE requires an unresolved proposition",
                    )
                )
            if not finding.get("search_or_request_summary"):
                issues.append(
                    _issue(
                        "HIT-IE-SEARCH",
                        f"/substantive_findings/{index}/search_or_request_summary",
                        "IE requires a search or request summary",
                    )
                )

        for field, expected_relation in REFERENCE_FIELDS.items():
            for claim_id in finding.get(field, []):
                claim = claim_map.get(claim_id)
                if claim is None:
                    issues.append(
                        _issue(
                            "HIT-CLAIM-REFERENCE",
                            f"/substantive_findings/{index}/{field}",
                            f"unknown evidence claim: {claim_id}",
                        )
                    )
                    continue
                if claim.get("relation") != expected_relation:
                    issues.append(
                        _issue(
                            "HIT-CLAIM-RELATION",
                            f"/substantive_findings/{index}/{field}",
                            f"claim {claim_id} has relation {claim.get('relation')!r}, expected {expected_relation!r}",
                        )
                    )
                if dimension not in claim.get("dimensions", []):
                    issues.append(
                        _issue(
                            "HIT-CLAIM-DIMENSION",
                            f"/substantive_findings/{index}/{field}",
                            f"claim {claim_id} does not declare dimension {dimension!r}",
                        )
                    )

        trigger = finding.get("repair_trigger")
        if dimension == "repair":
            if trigger == "indeterminate" and value != "IE":
                issues.append(
                    _issue(
                        "HIT-REPAIR-TRIGGER",
                        f"/substantive_findings/{index}",
                        "an indeterminate Repair trigger requires finding IE",
                    )
                )
            if (
                trigger == "not_triggered"
                and value == 2
                and finding.get("aggregation_basis") != "tested_capability"
            ):
                issues.append(
                    _issue(
                        "HIT-REPAIR-CAPABILITY",
                        f"/substantive_findings/{index}/aggregation_basis",
                        "Repair 2 without a triggered event requires tested-capability evidence",
                    )
                )
        elif trigger != "not_applicable":
            issues.append(
                _issue(
                    "HIT-NONREPAIR-TRIGGER",
                    f"/substantive_findings/{index}/repair_trigger",
                    "non-Repair dimensions must use repair_trigger 'not_applicable'",
                )
            )

    integrity = instance.get("telemetry_integrity", {})
    if isinstance(integrity, dict):
        institutional = integrity.get("institutional_record_integrity", {})
        packet = integrity.get("assessment_packet_integrity", {})
        expected_overall = _derive_integrity(
            institutional.get("status") if isinstance(institutional, dict) else None,
            packet.get("status") if isinstance(packet, dict) else None,
        )
        if integrity.get("overall_status") != expected_overall:
            issues.append(
                _issue(
                    "HIT-INTEGRITY-DERIVATION",
                    "/telemetry_integrity/overall_status",
                    f"overall status must be {expected_overall!r}",
                )
            )
        for component_name, component in (
            ("institutional_record_integrity", institutional),
            ("assessment_packet_integrity", packet),
        ):
            if not isinstance(component, dict):
                continue
            for claim_id in component.get("evidence_claim_ids", []):
                claim = claim_map.get(claim_id)
                if claim is None:
                    issues.append(
                        _issue(
                            "HIT-CLAIM-REFERENCE",
                            f"/telemetry_integrity/{component_name}/evidence_claim_ids",
                            f"unknown evidence claim: {claim_id}",
                        )
                    )
                elif "telemetry_integrity" not in claim.get("dimensions", []):
                    issues.append(
                        _issue(
                            "HIT-CLAIM-DIMENSION",
                            f"/telemetry_integrity/{component_name}/evidence_claim_ids",
                            f"claim {claim_id} does not declare telemetry_integrity",
                        )
                    )

    scope = instance.get("assessment_scope")
    aggregation = instance.get("aggregation", {})
    mode = aggregation.get("mode") if isinstance(aggregation, dict) else None
    if scope == "event_specific" and mode != "event_specific":
        issues.append(
            _issue(
                "HIT-AGGREGATION-SCOPE",
                "/aggregation/mode",
                "event-specific assessments require event-specific aggregation",
            )
        )
    if scope == "period_level" and mode == "event_specific":
        issues.append(
            _issue(
                "HIT-AGGREGATION-SCOPE",
                "/aggregation/mode",
                "period-level assessments cannot use event-specific aggregation as the assessment rule",
            )
        )

    schema_valid = not schema_errors
    semantic_errors = [
        issue
        for issue in issues
        if issue.code != "HIT-SCHEMA" and issue.severity == "error"
    ]
    return AssessmentConformanceResult(
        source=source,
        schema_valid=schema_valid,
        semantic_valid=not semantic_errors,
        issues=issues,
    )
