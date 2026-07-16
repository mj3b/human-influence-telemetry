# Deterministic HIT fixtures

This directory contains synthetic assessment records used to test the Human Influence Telemetry schema and scoring contract. They are not descriptions of actual institutions, people, or events.

Each JSON file is formatted for direct review in GitHub and validates against [`../schema/hit-assessment.schema.json`](../schema/hit-assessment.schema.json).

## Fixture index

| Fixture | Synthetic setting | Expected substantive pattern | Telemetry Integrity | Purpose |
|---|---|---|---|---|
| [`substantive-human-influence.json`](substantive-human-influence.json) | High-impact insurance-claim review | `2` for Counsel, Judgment, Command, Correction, Repair, and Reform | `adequate` | Demonstrates a record with observable and exercised human influence across all six dimensions |
| [`ceremonial-review.json`](ceremonial-review.json) | Public-benefit eligibility review | `1` for Counsel, Judgment, Command, and Correction; `0` for Repair and Reform | `limited` | Demonstrates formal human review that does not show practical capacity to change the decision path |
| [`insufficient-evidence.json`](insufficient-evidence.json) | AI-assisted hiring review | `IE` for five dimensions and `1` for Command | `unreliable` | Demonstrates why unavailable records must not be converted into findings of absence |

## Reading a fixture

The main fields are:

- `assessment_id`: stable identifier for the synthetic record;
- `schema_version`: assessment schema used by the record;
- `institutional_unit`, `decision_process`, and `period`: assessment boundary;
- `sampling_rule`: records included in the synthetic review;
- `substantive_findings`: one finding for each of the six HIT dimensions;
- `supporting_artifacts`: synthetic evidence supporting a finding;
- `requested_missing_artifacts`: evidence required but unavailable;
- `telemetry_integrity`: separate assessment of record trustworthiness;
- `limitations`: explicit boundary on what the fixture demonstrates.

## Interpretation rules

- `0` means the relevant capacity or practice is demonstrated as absent.
- `1` means the form of oversight exists but practical influence is not demonstrated.
- `2` means the records show substantive exercise or a credibly maintained capacity.
- `IE` means the available records cannot distinguish absence from missing evidence.

The fixtures test structural and semantic expectations. They do not establish inter-rater reliability, institutional effectiveness, legal compliance, or field validation.
