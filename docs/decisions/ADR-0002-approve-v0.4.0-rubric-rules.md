# ADR-0002: Approve the HIT v0.4.0 normative rubric rules

**Status:** Accepted  
**Decision date:** 2026-07-17  
**Decision authority:** Repository owner and method author  
**Applies to:** Prospective HIT `0.4.0` development  
**Supersedes:** No released artifact

## Context

The adversarial rubric-friction review `HIT-ARFR-001` identified 16 ambiguity classes capable of producing reasonable scorer divergence under specification `0.1.0`.

The v0.4.0 development branch converted those classes into a candidate evidence-state model, findings rules, dimension-specific thresholds, integrity logic, actor-attribution rules, sampling rules, conflict handling, evidence-reuse constraints, and citation requirements.

The candidate rules passed repository validation as documentation-only additions. They did not alter the released specification, schema, public cases, locked human protocol, or research-maturity claim.

## Decision

Approve the candidate v0.4.0 normative rules as the fixed design target for schema, catalog, fixture, validator, and case-migration work.

The approved evidence-state sequence is:

1. affirmative absence;
2. formal presence;
3. operational capability;
4. observed exercise.

The approved findings logic is:

- `0` requires affirmative evidence of absence;
- `1` requires process-specific formal presence without established substantive capability or effect;
- `2` requires observed exercise or directly demonstrated operational capability under bounded conditions;
- `IE` records unresolved evidentiary state and may not be converted to zero.

The approved contract also requires:

- dimension-specific decision rules;
- Repair trigger states;
- separate institutional-record and assessment-packet integrity components;
- deterministic overall Telemetry Integrity derivation;
- dominant-pattern aggregation by default for period-level assessments;
- an actor-authority matrix;
- explicit treatment of contradictory evidence;
- proposition-specific cross-dimensional evidence reuse;
- precise locators and bounded evidence propositions.

## Implementation consequence

The following files become the normative development targets:

- `specification/HIT-SPECIFICATION-v0.4.0-candidate.md`;
- `docs/application-handbook-v0.4.0-candidate.md`;
- `docs/normative-decision-rules-v0.4.0-draft.md` as the friction-to-rule traceability source.

Schema and catalog work must conform to those files. Where machine representation exposes an inconsistency or impossible requirement, the issue must be returned to normative review rather than silently resolved in code.

## Protected boundaries

This decision does not alter:

- released specification `0.1.0`;
- released schema or dimension catalog `0.1.0`;
- historical public case findings;
- protocol `HIT-IRP-CIGNA-001`;
- the frozen Cigna packet;
- the pre-adjudication threshold or critical-disagreement rules;
- claim H3;
- Maturity Level 1 status.

## Rejected alternatives

### Lower the inter-rater threshold

Rejected. The first human result must remain governed by the locked protocol.

### Treat missing evidence as absence

Rejected. This would collapse an epistemic limitation into a substantive failure claim.

### Require observed exercise for every `2`

Rejected. Some assessment designs reasonably test operational capability without containing a naturally occurring exercise. Capability-only `2` therefore remains available under strict conditions.

### Treat a single exceptional exercise as the period-level pattern

Rejected. Period-level assessments default to the dominant operational pattern unless another aggregation rule was predeclared.

### Collapse packet integrity and institutional-record integrity

Rejected. The assessor's packet and the institution's record system are different objects with different failure mechanisms.

## Update conditions

Reopen this decision only when at least one of the following occurs:

- schema design demonstrates an internal contradiction;
- deterministic fixtures cannot distinguish a required boundary;
- independent scorers expose a new ambiguity not governed by the approved rules;
- repeated clean-room implementation audits produce the same interpretive divergence;
- external methodological review identifies a specific failure mechanism and repair.

Any later change applies prospectively and must not rewrite historical results.
