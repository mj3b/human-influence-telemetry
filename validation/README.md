# HIT Validation Workstreams

This directory contains both the completed first human exercise and the active current-contract replication candidate.

## Completed human exercise

Locked protocol `HIT-IRP-CIGNA-001` was originally planned for repository release `v0.3.0`. ADR-0003 superseded that label so release versions remain chronological. The completed result is published in `v0.6.0`.

The protocol, frozen packet, scorer contract, threshold, critical-disagreement rules, adjudication controls, and pass/fail publication obligation were not changed.

### Completed status

| Gate | Status |
|---|---|
| Protocol drafted and locked | Complete |
| Frozen scorer packet | Complete |
| Two eligible independent scorers | Complete |
| Two manual submissions received and preserved | Complete |
| Two schema-valid JSON transcriptions verified by scorers | Complete |
| Pre-adjudication comparison | Complete |
| Exact agreement | 7 / 7 |
| Critical disagreements | 0 |
| Advancement threshold | Met |
| Disagreement adjudication | No substantive adjudication required |
| H3 decision | Supported for one frozen packet |
| Maturity decision | Level 2, Applicable |
| Empirical result release | 0.6.0 |

### Contract boundary

The completed exercise used specification and assessment schema `0.1.0`. The current `0.4.0` handbook and schema were not used to brief scorers, change submissions, or reinterpret the primary result.

## Active current-contract replication candidate

Protocol `HIT-IRP-HIT040-002` is staged under [`v0.7.0/`](v0.7.0/). It is intended to test independent application of the current `0.4.0` contract across three evidence conditions.

| Field | Current state |
|---|---|
| Target release | `0.7.0` |
| Cases selected | 0 of 3 |
| Packet IDs assigned | 0 |
| Required scorers | 3 |
| Required submissions | 9 |
| Protocol status | Candidate |
| Recruitment | Prohibited |
| Scoring | Prohibited |
| Draft manual workbooks | Complete for A, B, C, and master template |

The candidate protocol, source-audit controls, recruitment contingency, and manual workbooks are readiness artifacts. They do not create a new empirical result or advance research maturity.

## Relationship to stable `1.0.0`

The current-contract replication is one evidence path toward the stable public contract. The separate clean-room implementation work under [`../implementation/v1.0.0-candidate/`](../implementation/v1.0.0-candidate/) tests whether the public package can be used without private author explanation.

Human agreement evidence and public implementability remain separate estimands. Neither may be substituted for the other.

## Directory map

| Path | Purpose |
|---|---|
| [`inter-rater-protocol.md`](inter-rater-protocol.md) | Completed locked Cigna study procedure |
| [`protocol-lock.json`](protocol-lock.json) | Completed Cigna protocol and packet identifiers |
| [`frozen-packet/`](frozen-packet/) | Completed Cigna scorer-facing boundary and source manifest |
| [`scorer-submission.schema.json`](scorer-submission.schema.json) | Contract for completed Cigna scorer submissions |
| [`submissions/`](submissions/) | Verified immutable Cigna scorer JSON |
| [`receipts/`](receipts/) | Intake, correction, transcription, and verification records |
| [`results/`](results/) | Published comparison, decisions, preservation, and asset manifests |
| [`v0.7.0/`](v0.7.0/) | Current-contract replication candidate, source audit, and manual-workbook controls |
| [`../scripts/compare_raters.py`](../scripts/compare_raters.py) | Deterministic completed-exercise comparison command |

## Advancement rule

Publication and maturity advancement are separate decisions. The completed exercise passed both gates:

- the empirical result is publishable under release `0.6.0`;
- H3 is supported for this bounded exercise;
- HIT advances to Maturity Level 2 because the independence and agreement conditions were satisfied.

Adjudication did not alter any score or recalculate the primary result.

The active `0.7.0` candidate has passed no new empirical gate. It remains blocked on human case selection, packet freeze, protocol lock, and scorer activation.
