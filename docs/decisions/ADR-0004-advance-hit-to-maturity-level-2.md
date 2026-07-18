# ADR-0004: Advance HIT to Maturity Level 2 after the locked human exercise

**Status:** Accepted  
**Date:** 2026-07-18  
**Decision owner:** Mark Julius Banasihan  
**Related decisions:** ADR-0001, ADR-0002, ADR-0003  
**Protocol:** `HIT-IRP-CIGNA-001`

## Context

ADR-0001 separated semantic-version progression from research maturity. `RESEARCH.md` defined Level 2, Applicable, as the state in which a stranger can apply the method and the locked human exercise passes its declared independence and agreement rules.

The locked exercise required two eligible independent scorers, two complete submissions, at least 6 of 7 exact agreements, and zero critical disagreements. The protocol required publication of the result whether it passed or failed.

## Evidence

The completed pre-adjudication comparison reported:

- 7 of 7 exact agreements;
- exact-agreement proportion `1.0000`;
- zero critical disagreements;
- no categorical disagreements;
- advancement threshold met.

Both scorers confirmed that their final JSON files reproduced their manual submissions exactly.

## Decision

1. Claim H3 is supported for this one frozen packet under the locked `0.1.0` scorer contract.
2. HIT advances to Maturity Level 2, Applicable.
3. Repository release `0.6.0` publishes the original result package.
4. The `0.4.0` normative contract and `0.5.0` conformance engine remain unchanged.
5. This decision creates no claim of general inter-rater reliability.

## Limits

The exercise used two scorers, one retrospective case, and seven categorical items. All six substantive ratings fell in one category, so supplementary Cohen's kappa is undefined. Replication remains necessary across additional cases, sectors, scorer populations, and a compatible current contract.

## Consequences

Public metadata must distinguish repository release `0.6.0`, conformance engine `0.5.0`, normative contract `0.4.0`, and research maturity Level 2. The result artifacts, hashes, verification records, and pre-adjudication outputs must remain public and immutable.
