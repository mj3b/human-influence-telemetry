# HIT v0.4.0 Breaking-Change Review

**Status:** Candidate release review  
**Governing decisions:** ADR-0001, ADR-0002, ADR-0003  
**Predecessor contract:** specification, schema, and catalog `0.1.0`  
**Target contract:** `0.4.0`

## Classification

The candidate is a breaking normative and data-contract change. Existing `0.1.0` assessment records do not conform automatically to `0.4.0`.

## Breaking changes

1. Findings must be supported through the evidence-state sequence: affirmative absence, formal presence, operational capability, observed exercise, or indeterminate.
2. `0` requires affirmative evidence of absence; silence or nonproduction is insufficient.
3. `1` requires process-specific formal presence and may not be inferred from a generic policy or role description.
4. `2` requires observed exercise or directly demonstrated operational capability under the published bounded conditions.
5. `IE` requires an unresolved proposition, missing or conflicting artifacts, and a recorded search or request.
6. Every assessment must declare scope, sampling, aggregation, exclusions, and likely selection effects.
7. Every material actor must appear in an actor-authority matrix.
8. Evidence must be represented as bounded propositions with precise locators and `supports`, `contradicts`, or `limits` relations.
9. Repair requires a separate trigger state before a finding is assigned.
10. Telemetry Integrity is split into institutional-record integrity and assessment-packet integrity, with a deterministic overall status.
11. Contradictory evidence and cross-dimensional evidence reuse require explicit reasoning records.
12. Historical case assessments remain version-bound and are not silently rewritten.
13. The planned `v0.3.0` result label is superseded; empirical results use the next available version.

## Compatibility boundary

A `0.1.0` record remains a valid historical artifact when its version and provenance are preserved. It must not be described as conforming to `0.4.0`, passed through the candidate validator, or upgraded by changing only its version field.

## Migration risk

The primary risks are unsupported conversion of `0` from silence, automatic elevation of formal authority to `2`, actor collapse, loss of contradictory evidence, and false integrity precision. The migration guide prohibits mechanical scoring conversion.

## Decision

The breaking changes are justified because they directly resolve all 16 ambiguity classes in `HIT-ARFR-001`. Release remains blocked until canonical promotion, metadata synchronization, and exact-commit CI are complete.
