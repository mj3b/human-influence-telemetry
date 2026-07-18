# H3 and Maturity Level 2 Decision

**Decision ID:** `HIT-DEC-H3-ML2-001`  
**Date:** 2026-07-18  
**Protocol:** `HIT-IRP-CIGNA-001`  
**Packet:** `HIT-IR-CIGNA-PXDX-001`  
**Status:** Accepted

## Decision

Claim H3 is supported for the completed locked exercise. HIT advances from Maturity Level 1, Defined, to Maturity Level 2, Applicable.

## Evidence

Two eligible independent scorers completed the same frozen Cigna PxDx packet under specification and schema `0.1.0`. Their verified submissions agreed on all six substantive dimensions and Telemetry Integrity.

The pre-adjudication comparison reported:

- 7 of 7 exact agreements;
- exact-agreement proportion `1.0000`;
- zero critical disagreements;
- advancement threshold met.

The predeclared gate required at least 6 of 7 exact agreements and zero critical disagreements.

## Scope of support

The result supports this claim:

> Two independent reviewers applied the published locked materials to one frozen packet and reached the predeclared agreement threshold.

The result does not support a population estimate of inter-rater reliability. It does not establish transfer across sectors, cases, evidence conditions, scorer populations, or the current `0.4.0` contract. It does not establish causal validity, evidence truth, legal correctness, field effectiveness, certification, or institutional adoption.

## Kappa

Supplementary Cohen's kappa is `null` because both scorers used one category across all six substantive dimensions. The data contain no category variance for chance-corrected estimation. The primary exact-agreement measure remains defined and passed.

## Consequences

1. `RESEARCH.md` records H3 as supported for one bounded exercise.
2. Repository research maturity advances to Level 2, Applicable.
3. The passing result is published under repository release `0.6.0`.
4. The specification, schema, catalog, handbook, and conformance engine remain at their prior versions.
5. Future replication should use additional cases, sectors, scorers, and a compatible current contract.

## Update condition

Revise or narrow this decision when replication produces material disagreement, when a compatible-contract exercise fails the threshold, or when evidence shows that the current maturity definition overstates reproducibility.
