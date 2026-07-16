# HIT Inter-rater Validation Workstream

This directory contains the public materials for the Human Influence Telemetry inter-rater exercise targeted for repository release `v0.3.0`.

## Current status

| Gate | Status |
|---|---|
| Protocol drafted | Complete |
| Scorer packet defined | Complete |
| Submission schema defined | Complete |
| Comparison tooling implemented | Complete |
| Protocol reviewed and locked on `main` | Pending |
| Two eligible independent scorers enrolled | Pending |
| Two blinded submissions received | Pending |
| Pre-adjudication comparison published | Pending |
| Disagreement register and adjudication record published | Pending |
| `v0.3.0` release decision | Pending |

No reliability result is claimed while the scorer and result gates remain pending.

## Directory map

| Path | Purpose |
|---|---|
| [`inter-rater-protocol.md`](inter-rater-protocol.md) | Normative study procedure, eligibility rules, threshold, and publication rules |
| [`protocol-lock.json`](protocol-lock.json) | Machine-readable protocol and packet identifiers |
| [`frozen-packet/`](frozen-packet/) | Scorer-facing decision boundary and fixed source manifest without author scores |
| [`scorer-submission.schema.json`](scorer-submission.schema.json) | Machine-readable contract for independent scorer submissions |
| [`submissions/`](submissions/) | Template and, after lock, immutable scorer submissions |
| [`test-vectors/`](test-vectors/) | Synthetic inputs used to test comparison tooling |
| [`disagreement-taxonomy.md`](disagreement-taxonomy.md) | Categories for classifying disagreements without erasing original scores |
| [`adjudication-template.md`](adjudication-template.md) | Required structure for the post-comparison adjudication record |
| [`results/`](results/) | Pre-adjudication comparison and final published result when available |
| [`../scripts/compare_raters.py`](../scripts/compare_raters.py) | Deterministic comparison command |

## Advancement rule

Publication of an exercise and advancement of the maturity level are separate decisions.

- A `v0.3.0` result release may report either a passing or failing exercise.
- HIT advances to Maturity Level 2 only when the predeclared threshold is met and the independence conditions are satisfied.
- Adjudication may explain disagreement and motivate later rubric changes. It must not replace the original submissions or retroactively manufacture agreement.
