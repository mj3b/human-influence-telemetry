# HIT Inter-rater Validation Workstream

This directory contains the public materials for locked protocol `HIT-IRP-CIGNA-001`.

The exercise was originally planned for repository release `v0.3.0`. That release label is now superseded under ADR-0003 so semantic versions remain chronological. The eventual result must use the next available repository version when the result package is complete.

The protocol, frozen packet, scorer contract, threshold, critical-disagreement rules, adjudication controls, and pass/fail publication obligation are unchanged.

## Current status

| Gate | Status |
|---|---|
| Protocol drafted | Complete |
| Scorer packet defined | Complete |
| Submission schema defined | Complete |
| Comparison tooling implemented | Complete |
| Protocol reviewed and locked on `main` | Complete |
| Two eligible independent scorers enrolled | Pending |
| Two blinded submissions received | Pending |
| Pre-adjudication comparison published | Pending |
| Disagreement register and adjudication record published | Pending |
| Empirical result release | Pending; next available version |

No reliability result is claimed while the scorer and result gates remain pending.

## Contract boundary

The locked exercise uses specification and assessment schema `0.1.0`. Do not use the `0.4.0` handbook or schema to brief scorers, change original submissions, or reinterpret the pre-adjudication result.

## Directory map

| Path | Purpose |
|---|---|
| [`inter-rater-protocol.md`](inter-rater-protocol.md) | Locked study procedure, eligibility rules, threshold, and publication rules |
| [`protocol-lock.json`](protocol-lock.json) | Machine-readable protocol and packet identifiers |
| [`frozen-packet/`](frozen-packet/) | Fixed scorer-facing boundary and source manifest without author scores |
| [`scorer-submission.schema.json`](scorer-submission.schema.json) | Contract for independent scorer submissions |
| [`submissions/`](submissions/) | Template and future immutable submissions |
| [`test-vectors/`](test-vectors/) | Synthetic inputs for comparison-tool testing |
| [`disagreement-taxonomy.md`](disagreement-taxonomy.md) | Disagreement categories preserving original scores |
| [`adjudication-template.md`](adjudication-template.md) | Post-comparison adjudication structure |
| [`results/`](results/) | Original comparison and published result when available |
| [`../scripts/compare_raters.py`](../scripts/compare_raters.py) | Deterministic comparison command |

## Advancement rule

Publication and maturity advancement are separate decisions.

- The result release may report a passing or failing exercise.
- HIT advances to Maturity Level 2 only when the predeclared threshold and independence conditions are satisfied.
- Adjudication may explain disagreement and motivate later changes. It must not replace original submissions or retroactively manufacture agreement.
