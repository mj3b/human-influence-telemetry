# HIT Inter-rater Validation Workstream

This directory contains the public materials for locked protocol `HIT-IRP-CIGNA-001`.

The exercise was originally planned for repository release `v0.3.0`. ADR-0003 superseded that label so release versions remain chronological. The completed result is published in `v0.6.0`.

The protocol, frozen packet, scorer contract, threshold, critical-disagreement rules, adjudication controls, and pass/fail publication obligation were not changed.

## Current status

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

## Contract boundary

The exercise used specification and assessment schema `0.1.0`. The current `0.4.0` handbook and schema were not used to brief scorers, change submissions, or reinterpret the primary result.

## Directory map

| Path | Purpose |
|---|---|
| [`inter-rater-protocol.md`](inter-rater-protocol.md) | Locked study procedure, eligibility rules, threshold, and publication rules |
| [`protocol-lock.json`](protocol-lock.json) | Machine-readable protocol and packet identifiers |
| [`frozen-packet/`](frozen-packet/) | Fixed scorer-facing boundary and source manifest |
| [`scorer-submission.schema.json`](scorer-submission.schema.json) | Contract for independent scorer submissions |
| [`submissions/`](submissions/) | Verified immutable scorer JSON |
| [`receipts/`](receipts/) | Intake, correction, transcription, and verification records |
| [`results/`](results/) | Comparison, decisions, preservation manifest, and release-asset manifest |
| [`../scripts/compare_raters.py`](../scripts/compare_raters.py) | Deterministic comparison command |

## Advancement rule

Publication and maturity advancement are separate decisions. The exercise passed both gates:

- the empirical result is publishable under release `0.6.0`;
- H3 is supported for this bounded exercise;
- HIT advances to Maturity Level 2 because the independence and agreement conditions were satisfied.

Adjudication did not alter any score or recalculate the primary result.
