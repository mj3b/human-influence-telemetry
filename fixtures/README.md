# Deterministic HIT fixtures

This directory contains synthetic records used to test different generations of the Human Influence Telemetry contract. They do not describe actual institutions, people, or events.

## Released 0.4.0 artifacts

| Artifact | Contract | Purpose |
|---|---|---|
| [`v0.4.0-canonical-example.json`](v0.4.0-canonical-example.json) | Schema and specification `0.4.0` | Canonical complete assessment with mixed findings, actor references, structured evidence claims, Repair trigger, and split Telemetry Integrity |
| [`v0.4.0-boundaries/`](v0.4.0-boundaries/) | Approved `0.4.0` rubric rules | Forty-eight accepted, rejected, and boundary cases covering `FR-01` through `FR-16` |

## Historical 0.1.0 fixtures

The following records remain immutable historical fixtures and are interpreted under the archived schema in [`../archive/v0.1.0/`](../archive/v0.1.0/):

| Fixture | Synthetic setting | Historical pattern | Historical Telemetry Integrity |
|---|---|---|---|
| [`substantive-human-influence.json`](substantive-human-influence.json) | High-impact insurance-claim review | `2` across all six dimensions | `adequate` |
| [`ceremonial-review.json`](ceremonial-review.json) | Public-benefit eligibility review | `1` for Counsel, Judgment, Command, and Correction; `0` for Repair and Reform | `limited` |
| [`insufficient-evidence.json`](insufficient-evidence.json) | AI-assisted hiring review | `IE` for five dimensions and `1` for Command | `unreliable` |

These historical files do not validate against the canonical `0.4.0` schema without a fresh migration. They are retained for reproducibility and formatting checks.

## Interpretation boundary

The `0.4.0` fixture suite demonstrates deterministic implementation of approved rules. It does not establish human inter-rater reliability, institutional effectiveness, legal compliance, field validity, or empirical correctness.

Synthetic fixture results must not be cited as findings about real institutions.
