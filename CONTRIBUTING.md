# Contributing

Human Influence Telemetry is a working research specification. Contributions are welcome when they improve testability, construct clarity, evidence discipline, interoperability, or reproducibility.

## Suitable contributions

- schema corrections and stricter validation;
- deterministic positive and negative fixtures;
- scoring ambiguities with proposed adjudication rules;
- inter-rater protocols and replication results;
- public-record case studies with traceable sources;
- related-work comparisons that narrow or falsify novelty claims;
- accessibility and documentation improvements;
- security or provenance controls.

## Contributions requiring particular care

Changes to dimensions, scoring anchors, aggregation, legal mappings, or maturity claims are normative or claim-sensitive. Open an issue before implementing a large change.

A proposal should use this structure:

- **Claim:** What should change?
- **Mechanism:** Why would the change improve the method?
- **Evidence:** What record, study, test, or failure case supports it?
- **Rival explanation:** What alternative interpretation remains plausible?
- **Test:** How can the repository distinguish the proposals?
- **Update condition:** What result would reverse the recommendation?
- **Decision consequence:** Which schema, rubric, fixture, or claim changes?

## Development setup

```bash
python -m pip install --requirement requirements-dev.txt
python scripts/validate.py
```

The validation command must pass before a pull request is ready for review.

## Pull-request requirements

A pull request should:

1. identify normative and informative changes;
2. update or add fixtures for changed behavior;
3. preserve the difference between `0` and `IE`;
4. avoid compliance, certification, causal-effectiveness, or adoption claims without the required evidence;
5. update `CHANGELOG.md` for user-visible changes;
6. document migration consequences for breaking schema changes.

## Case-study requirements

A case study must distinguish:

- observed record content;
- interpretation under the HIT rubric;
- unavailable evidence;
- factual uncertainty;
- normative or legal inference.

Public sources must be cited precisely. An absent public record should usually produce `IE`, not `0`.

## Licensing

By submitting a contribution, you agree that it may be distributed under the Apache License 2.0. Do not submit confidential, proprietary, restricted, or personally identifying material without authority to publish it.
