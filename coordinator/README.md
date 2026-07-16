# HIT Coordinator Toolkit

This directory documents the coordinator-side infrastructure for receiving, validating, preserving, comparing, and adjudicating two independent HIT scorer submissions under `HIT-IRP-CIGNA-001`.

It is not part of the scorer packet and must not be shared before both submissions are locked. The repository's synthetic vectors and coordinator analysis materials could otherwise prime scorers.

## Existing repository components

- `scripts/compare_raters.py`: deterministic seven-item comparison
- `validation/scorer-submission.schema.json`: locked submission contract
- `validation/test-vectors/rater-a.json`
- `validation/test-vectors/rater-b.json`
- `validation/disagreement-taxonomy.md`
- `validation/adjudication-template.md`

## Added coordinator components

- `scripts/validate_scorer_submission.py`: validate one submission before the second arrives
- `scripts/record_submission.py`: create an immutable SHA-256 receipt record
- `coordinator/comparison-runbook.md`: exact commands and preservation sequence
- `validation/adversarial-rubric-friction-review.md`: coordinator-only non-scoring dry run

## Research boundary

The toolkit does not create human agreement evidence. It becomes empirically relevant only when two eligible independent human submissions are processed under the locked protocol.

The synthetic vectors test deterministic behavior only.
