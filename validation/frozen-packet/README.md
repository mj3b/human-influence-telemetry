# Frozen Scorer Packet: Cigna PxDx

**Packet ID:** `HIT-IR-CIGNA-PXDX-001`  
**Protocol:** `HIT-IRP-CIGNA-001`  
**Method:** HIT specification and assessment schema `0.1.0`

This packet supplies the common evidence surface for the blinded inter-rater exercise. It contains no author scores and does not identify an expected disagreement.

## Required reading

1. [`decision-boundary.md`](decision-boundary.md)
2. [`source-manifest.json`](source-manifest.json)
3. [`../../SPECIFICATION.md`](../../SPECIFICATION.md)
4. [`../../docs/application-handbook.md`](../../docs/application-handbook.md)
5. [`../scorer-submission.schema.json`](../scorer-submission.schema.json)
6. [`../submissions/scorer-submission.template.json`](../submissions/scorer-submission.template.json)

## Evidence rule

Use every source in the manifest and no additional case source. Source labels describe evidentiary posture rather than truth:

- investigative reporting is reporting;
- an institutional response is a response;
- allegations remain allegations;
- a pleading-stage order evaluates legal sufficiency and is not a merits judgment.

Do not infer that an unavailable institutional record never existed. Use `IE` when the packet cannot distinguish absence from unavailable evidence.

## Blinding rule

Before submission, do not inspect:

- `case-studies/cigna-pxdx.md`;
- `case-studies/assessments/cigna-pxdx.json`;
- `validation/test-vectors/`;
- public commentary discussing the author's Cigna findings;
- another scorer's notes or submission.

Because the repository is public, procedural blinding depends on scorer attestation. A false or materially unreliable attestation invalidates the exercise for maturity advancement.

## Source access record

For every manifest source, record:

- the source ID;
- access date;
- whether access was complete;
- any material access problem;
- an optional digest or archived-copy identifier.

Do not commit third-party source files to this repository unless redistribution rights are established.

## Submission

Return one JSON file conforming to `scorer-submission.schema.json`. The coordinator will not reveal either submission until both are locked.
