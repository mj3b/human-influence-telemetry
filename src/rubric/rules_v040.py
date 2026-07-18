"""Deterministic evaluators for HIT v0.4.0 candidate rubric boundary fixtures."""

from __future__ import annotations

from typing import Any, Callable

Result = dict[str, str | int | bool | None]
Facts = dict[str, Any]


def _bool(facts: Facts, key: str) -> bool:
    return bool(facts.get(key, False))


def evaluate_fr01(facts: Facts) -> Result:
    affirmative = any(
        _bool(facts, key)
        for key in (
            "explicit_nonexistence",
            "structural_impossibility",
            "complete_record_search_absent",
            "contemporaneous_exclusion",
            "consistent_nonexistence_records",
        )
    )
    return {"finding": 0 if affirmative else "IE"}


def evaluate_fr02(facts: Facts) -> Result:
    formal_presence = all(
        _bool(facts, key)
        for key in (
            "process_specific_artifact",
            "defined_or_assigned",
            "applies_to_unit",
            "applies_to_decision_type",
            "applies_to_period",
        )
    )
    return {"finding": 1 if formal_presence else "IE"}


def evaluate_fr03(facts: Facts) -> Result:
    if _bool(facts, "observed_exercise"):
        return {"finding": 2}
    operational = all(
        _bool(facts, key)
        for key in (
            "operational_capability",
            "named_authority",
            "mechanism_available",
            "consequence_identified",
            "no_material_barrier",
            "sample_does_not_permit_observed_exercise",
        )
    )
    if operational:
        return {"finding": 2}
    if _bool(facts, "formal_presence"):
        return {"finding": 1}
    return {"finding": "IE"}


def evaluate_fr04(facts: Facts) -> Result:
    if _bool(facts, "cannot_access_established"):
        return {"finding": 0}
    if all(
        _bool(facts, key)
        for key in ("actual_predecision_access", "relevant_underlying_evidence", "timing_known")
    ):
        return {"finding": 2}
    if _bool(facts, "formal_access_route") or _bool(facts, "only_compressed_output"):
        return {"finding": 1}
    return {"finding": "IE"}


def evaluate_fr05(facts: Facts) -> Result:
    if _bool(facts, "no_evaluation_step") or _bool(facts, "evaluation_structurally_prohibited"):
        return {"finding": 0}
    if _bool(facts, "direct_independent_reasoning"):
        return {"finding": 2}
    ceremonial = (
        _bool(facts, "formal_review")
        and int(facts.get("indirect_indicator_count", 0)) >= 2
        and _bool(facts, "process_specific")
        and not _bool(facts, "material_contrary_evidence")
    )
    if ceremonial:
        return {"finding": 1}
    return {"finding": "IE"}


def evaluate_fr06(facts: Facts) -> Result:
    if _bool(facts, "no_named_human_authority") or _bool(facts, "intervention_structurally_unavailable"):
        return {"finding": 0}
    exercised = _bool(facts, "observed_exercise") or _bool(facts, "operational_test")
    if (
        exercised
        and _bool(facts, "named_authority")
        and _bool(facts, "institution_controls_mechanism")
        and _bool(facts, "specified_consequence")
    ):
        return {"finding": 2}
    if _bool(facts, "formal_authority") or _bool(facts, "formal_mechanism"):
        return {"finding": 1}
    return {"finding": "IE"}


def evaluate_fr07(facts: Facts) -> Result:
    if _bool(facts, "no_channel"):
        return {"finding": 0}
    if (
        _bool(facts, "substantive_reconsideration")
        and _bool(facts, "practical_authority_to_alter")
    ):
        return {"finding": 2}
    if _bool(facts, "channel_exists") and any(
        _bool(facts, key)
        for key in ("intake_only", "routing_only", "template_disposition", "procedural_acknowledgment")
    ):
        return {"finding": 1}
    return {"finding": "IE"}


def evaluate_fr08(facts: Facts) -> Result:
    triggered = (
        _bool(facts, "adjudicated_harm")
        or _bool(facts, "formal_harm_acknowledgment")
        or (
            _bool(facts, "specific_contemporaneous_harm_evidence")
            and _bool(facts, "independent_corroboration")
        )
    )
    if triggered:
        trigger = "triggered"
    elif _bool(facts, "affirmative_no_qualifying_harm"):
        trigger = "not_triggered"
    else:
        trigger = "indeterminate"

    if trigger == "indeterminate":
        return {"trigger": trigger, "finding": "IE"}
    if trigger == "triggered":
        if _bool(facts, "no_named_repair_owner") or _bool(facts, "repair_structurally_excluded"):
            return {"trigger": trigger, "finding": 0}
        if _bool(facts, "delivered_person_level_remedy"):
            return {"trigger": trigger, "finding": 2}
        if _bool(facts, "formal_repair_owner") or _bool(facts, "process_correction_only"):
            return {"trigger": trigger, "finding": 1}
        return {"trigger": trigger, "finding": "IE"}

    if _bool(facts, "capability_testing_in_boundary"):
        if _bool(facts, "tested_repair_mechanism"):
            return {"trigger": trigger, "finding": 2}
        if _bool(facts, "formal_repair_owner"):
            return {"trigger": trigger, "finding": 1}
    return {"trigger": trigger, "finding": "IE"}


def evaluate_fr09(facts: Facts) -> Result:
    if _bool(facts, "no_reform_authority") or _bool(facts, "change_structurally_impossible"):
        return {"finding": 0}
    admissible_change = all(
        _bool(facts, key)
        for key in (
            "followup_period_declared",
            "change_identifiable",
            "change_linked_to_assessed_failure",
            "implementing_actor_identified",
            "operative_change",
        )
    )
    if admissible_change and (
        not _bool(facts, "externally_compelled")
        or _bool(facts, "institution_substantively_implemented_or_extended")
    ):
        return {"finding": 2}
    if _bool(facts, "formal_reform_authority") or _bool(facts, "formal_change_process"):
        return {"finding": 1}
    return {"finding": "IE"}


def evaluate_fr10(facts: Facts) -> Result:
    separate = (
        _bool(facts, "institutional_component_present")
        and _bool(facts, "packet_component_present")
        and not _bool(facts, "combined_only")
    )
    return {"valid": separate}


def evaluate_fr11(facts: Facts) -> Result:
    institutional = str(facts.get("institutional_status"))
    packet = str(facts.get("packet_status"))
    statuses = {institutional, packet}
    if "unreliable" in statuses:
        overall = "unreliable"
    elif "IE" in statuses:
        overall = "IE"
    elif "limited" in statuses:
        overall = "limited"
    else:
        overall = "adequate"
    return {"overall_status": overall}


def evaluate_fr12(facts: Facts) -> Result:
    boundary_type = str(facts.get("boundary_type", "period"))
    if boundary_type == "event":
        return {
            "finding": facts.get("event_finding", "IE"),
            "scope": "event_specific",
        }
    if _bool(facts, "exception_generally_available"):
        return {
            "finding": facts.get("exception_finding", "IE"),
            "scope": "period_general_capability",
        }
    return {
        "finding": facts.get("dominant_pattern_finding", "IE"),
        "scope": "dominant_pattern",
    }


def evaluate_fr13(facts: Facts) -> Result:
    if not _bool(facts, "combined_finding_requested"):
        return {"valid": True}
    valid_relation = (
        _bool(facts, "same_decision_architecture_explained")
        or _bool(facts, "delegation_or_control_evidenced")
        or _bool(facts, "shared_decision_rights_evidenced")
    )
    if _bool(facts, "actor_authorities_differ") and not valid_relation:
        return {"valid": False}
    return {"valid": valid_relation}


def evaluate_fr14(facts: Facts) -> Result:
    if _bool(facts, "unresolved_conflict_could_change_finding") or _bool(
        facts, "actor_attribution_affected"
    ):
        return {"disposition": "IE"}
    if _bool(facts, "materially_better_supported_account") and _bool(
        facts, "weighting_explanation_recorded"
    ):
        return {"disposition": "determinate"}
    return {"disposition": "IE"}


def evaluate_fr15(facts: Facts) -> Result:
    valid = (
        _bool(facts, "same_artifact")
        and _bool(facts, "distinct_dimension_propositions")
        and _bool(facts, "separate_reasoning")
        and not _bool(facts, "automatic_cross_dimension_inference")
    )
    return {"valid": valid}


def evaluate_fr16(facts: Facts) -> Result:
    base = (
        _bool(facts, "source_identifier")
        and _bool(facts, "bounded_proposition")
        and _bool(facts, "relation_recorded")
    )
    if not base:
        return {"valid": False}
    if _bool(facts, "stable_locator_available"):
        return {"valid": _bool(facts, "locator_provided")}
    return {
        "valid": (
            _bool(facts, "smallest_reproducible_unit_identified")
            and _bool(facts, "locator_limitation_explained")
        )
    }


_HANDLERS: dict[str, Callable[[Facts], Result]] = {
    "FR-01": evaluate_fr01,
    "FR-02": evaluate_fr02,
    "FR-03": evaluate_fr03,
    "FR-04": evaluate_fr04,
    "FR-05": evaluate_fr05,
    "FR-06": evaluate_fr06,
    "FR-07": evaluate_fr07,
    "FR-08": evaluate_fr08,
    "FR-09": evaluate_fr09,
    "FR-10": evaluate_fr10,
    "FR-11": evaluate_fr11,
    "FR-12": evaluate_fr12,
    "FR-13": evaluate_fr13,
    "FR-14": evaluate_fr14,
    "FR-15": evaluate_fr15,
    "FR-16": evaluate_fr16,
}


def evaluate_boundary_case(friction_id: str, facts: Facts) -> Result:
    """Evaluate one boundary fixture under the approved candidate rules."""
    try:
        handler = _HANDLERS[friction_id]
    except KeyError as exc:
        raise ValueError(f"unknown friction ID: {friction_id}") from exc
    return handler(facts)
