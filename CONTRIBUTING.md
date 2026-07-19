# Contributing

Human Influence Telemetry is a pre-`1.0.0` research specification with a published `0.6.0` release and a gated stable-contract target. Contributions are welcome when they improve testability, construct clarity, evidence discipline, interoperability, public implementability, or reproducibility.

## Suitable contributions

- schema corrections and stricter validation;
- deterministic positive and negative fixtures;
- scoring ambiguities with proposed adjudication rules;
- inter-rater protocols and replication results;
- public-record case studies with traceable sources;
- related-work comparisons that narrow or falsify novelty claims;
- clean-room implementation findings;
- migration and compatibility analysis;
- accessibility and documentation improvements;
- security or provenance controls.

## Current `1.0.0` contribution priorities

- identify instructions that still require private author explanation;
- test the candidate implementation packet in a clean environment;
- verify synchronization among the specification, schema, catalog, handbook, fixtures, CLI, and compatibility manifest;
- produce current-contract public applications with explicit provenance;
- identify release-blocking ambiguity or migration defects;
- improve the release audit and exact-commit validation surface.

Candidate `1.0.0` work must not change published-release metadata, activate scoring, or claim stable-contract completion before the declared gates pass.

## Contributions requiring particular care

Changes to dimensions, scoring anchors, aggregation, legal mappings, compatibility commitments, release status, or maturity claims are normative or claim-sensitive. Open an issue before implementing a large change.

A proposal should use this structure:

- **Claim:** What should change?
- **Mechanism:** Why would the change improve the method?
- **Evidence:** What record, study, test, or failure case supports it?
- **Rival explanation:** What alternative interpretation remains plausible?
- **Test:** How can the repository distinguish the proposals?
- **Update condition:** What result would reverse the recommendation?
- **Decision consequence:** Which schema, rubric, fixture, release gate, or claim changes?

## Development setup

```bash
python -m pip install --requirement requirements-dev.txt
python scripts/validate.py
python scripts/validate_v1_readiness.py
python scripts/validate_v1_implementation_packet.py
```

The complete validation workflow must pass before a pull request is ready for review.

## Pull-request requirements

A pull request should:

1. identify normative and informative changes;
2. update or add fixtures for changed behavior;
3. preserve the difference between `0` and `IE`;
4. avoid compliance, certification, causal-effectiveness, reliability, or adoption claims without the required evidence;
5. update `CHANGELOG.md` for user-visible changes;
6. document migration consequences for breaking schema changes;
7. preserve the distinction between a published release and a candidate release document;
8. state whether the change affects any `1.0.0` gate.

## Case-study requirements

A case study must distinguish:

- observed record content;
- interpretation under the HIT rubric;
- unavailable evidence;
- factual uncertainty;
- normative or legal inference.

Public sources must be cited precisely. An absent public record should usually produce `IE`, not `0`.

Author-scored or coordinator-scored applications must state their provenance and must not be represented as independent inter-rater evidence.

## Clean-room audit contributions

A clean-room implementation submission must preserve:

- exact repository commit;
- environment and dependency record;
- original commands and outputs;
- every point requiring private explanation;
- failed as well as successful tasks;
- the auditor's independence and conflict disclosure.

Model implementation audits may provide development evidence. They do not count as independent human reliability evidence.

## Licensing

By submitting a contribution, you agree that it may be distributed under the Apache License 2.0. Do not submit confidential, proprietary, restricted, or personally identifying material without authority to publish it.
