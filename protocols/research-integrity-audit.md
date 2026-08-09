# HIT Research-Integrity Audit

**Protocol version:** 0.6.5

**Audit scope:** `HIT-COE-V0.6.5`

**Decision:** determine which mapped claims may enter a research-paper conclusion

## Problem

A file path proves that an artifact exists. It does not prove that the artifact supports a claim, fits the claim's evidentiary demand, or closes every dependency behind a conclusion. This protocol tests those propositions separately.

## Five gates

Each claim receives five states: `pass`, `fail`, `indeterminate`, or `outside_scope`.

1. Traceability checks that every path exists and every declared locator resolves.
2. Integrity checks that evidence is git-tracked or protected by a preserved locked digest.
3. Human support review records whether a person has accepted the claim-to-evidence relation. Automation cannot supply this judgment.
4. Evidence fitness combines directness, contemporaneity, independence, completeness, and publication authority.
5. Dependency closure requires every prerequisite claim to exist and qualify for the proposed conclusion.

A failed required dimension makes fitness fail. An indeterminate required dimension makes fitness indeterminate when no required dimension fails. Dimensions may be outside scope only when the rationale states why the claim does not require them.

## Conclusion rule

A claim may enter a conclusion when its status is `supported`, all five gates pass, every dependency is conclusion-eligible, and the declared eligibility matches the computed state. A failed or indeterminate gate preserves the observation and blocks conclusion use.

## Negative controls

The audit mutates in-memory copies of the map. It tests a missing reference, pending integrity, removed support review, failed fitness dimension, unresolved dependency, false eligibility, missing locator, and current-contract replication overclaim. Every corruption must produce an error. The committed map remains unchanged.

## E5 prose rule

Empirical prose must identify the population, protocol, contract, case count, scorer count, item count, and unresolved evidence that limit the claim. The validator rejects unbounded assertions of current-contract replication, population reliability, causal or legal proof, and independent adoption in v0.6.5 research and paper surfaces.

## Preserved boundaries

This audit adds no scoring rule. The normative contract remains 0.4.0. The executable conformance engine remains 0.5.0. The preserved human result remains the bounded 0.6.0 result. The software concept DOI remains 10.5281/zenodo.21204892, the v0.6.4 DOI remains bound to its exact archive, and the v0.6.5 DOI remains pending archival.

`HIT-IRP-HIT040-002` remains a separate candidate protocol. Recruitment and scoring remain prohibited until its existing gates authorize them. v0.6.5 creates no new independent-rater evidence.

## Audit state

`PASS_WITH_EXCEPTIONS` means every deterministic control passed and every mapped unresolved claim remained blocked. It does not establish source truth, external validity, population reliability, legal conformity, causal validity, current-contract replication, or institutional adoption.
