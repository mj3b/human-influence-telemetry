# HIT Inter-rater Adjudication Record

**Protocol ID:** `HIT-IRP-CIGNA-001`  
**Packet ID:** `HIT-IR-CIGNA-PXDX-001`  
**Comparison artifact:** `pre-adjudication-comparison.json`  
**Record date:** 2026-07-18  
**Adjudication status:** No substantive adjudication required

## Integrity checks

- [x] Both verified scorer JSON submissions are committed unchanged.
- [x] Both submissions validate against `scorer-submission.schema.json`.
- [x] Scorer public IDs are distinct.
- [x] Required independence attestations are true.
- [x] Both scorers reported complete access to S1, S2, and S3.
- [x] Both manual submissions were preserved and hashed.
- [x] Both scorers confirmed their JSON transcriptions exactly reproduced their manual submissions.
- [x] The deterministic comparison was generated before this record.
- [x] No scorer revised a finding after seeing the other submission.

## Pre-adjudication result

- Exact agreements: 7 / 7
- Exact-agreement proportion: 1.0000
- Critical disagreements: 0
- Supplementary substantive-dimension Cohen's kappa: `null`
- Predeclared threshold met: yes

The maturity decision uses this pre-adjudication result.

## Dimension-level disagreements

None.

## Agreement without adjudication

Both scorers assigned `1` to Counsel, Judgment, Command, Correction, Repair, and Reform. Both assigned `limited` to Telemetry Integrity.

The scorers relied on different primary source references in their structured submissions. Scorer A cited S1 for all seven findings. Scorer B cited S2 for all seven findings. Their rationales also used different analytical vocabularies. Those differences did not produce a categorical disagreement and do not change the primary measure.

## Method-update consequences

No normative change is authorized by this record. The exercise used the locked `0.1.0` scorer contract. The current `0.4.0` specification, schema, catalog, handbook, and scoring semantics remain unchanged.

## Claim and maturity decision

- H3 status: supported for this one frozen packet under the locked protocol.
- Maturity level: Level 2, Applicable.
- Basis: two eligible independent scorers produced complete verified submissions, reached 7 of 7 exact agreements, and produced zero critical disagreements.
- Remaining uncertainty: the result covers two scorers, seven categorical items, one retrospective case, one sector, and the `0.1.0` scorer contract. It does not estimate general inter-rater reliability.

## Preservation statement

The scorer submissions and pre-adjudication comparison remain the authoritative evidence of this exercise. This record does not alter either scorer's findings or recalculate the primary result.
