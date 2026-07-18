# HIT v0.7.0 Current-Contract Replication

This directory contains the candidate research design for independent application of the HIT `0.4.0` assessment contract.

The workstream exists because the completed Cigna exercise used the preserved `0.1.0` scorer contract. Release `0.6.0` supports reproducibility for one frozen packet. It does not establish independent application of the current contract.

## Status

- Protocol status: candidate
- Scoring status: prohibited
- Case-selection status: open
- Scorer recruitment: prohibited
- Target repository release: `0.7.0`
- Normative contract under test: `0.4.0`
- Conformance engine: `0.5.0`

The protocol becomes locked only after review, merge to `main`, and publication of the final protocol-lock digest. No scorer may receive a packet before that point.

## Files

- `replication-protocol-candidate.md`: research design, measures, thresholds, and publication rules
- `protocol-lock-candidate.json`: machine-readable candidate lock
- `case-selection-rule.md`: ex ante case-selection and category-variation requirements
- `packet-template.md`: required structure for each frozen scorer packet

## Research objective

The study asks whether independent reviewers can apply the `0.4.0` contract without private author explanation across three public cases that expose different evidence states and rating categories.

The design separates five outcomes:

1. exact categorical agreement;
2. weighted ordinal agreement;
3. Telemetry Integrity agreement;
4. source-reference overlap;
5. rationale divergence.

The separation matters because two scorers may reach the same finding through different evidence paths, or cite the same evidence while applying different thresholds.

## Advancement boundary

Release `0.7.0` freezes the protocol and packets. It does not report human results or advance research maturity. Human results belong in a later release after original submissions, verification records, pre-adjudication comparisons, and disagreement analysis exist.
