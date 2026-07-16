# Project Governance

Human Influence Telemetry is an open research artifact maintained by Mark Julius Banasihan through Node & Norm.

## Decision authority

The maintainer holds final release authority during the working-specification phase. This authority covers:

- normative changes to the specification;
- schema and rubric changes;
- release acceptance;
- claim and maturity status;
- provenance and publication boundaries;
- security and responsible-disclosure decisions.

Maintainer authority does not convert unresolved empirical questions into settled findings. Claim status advances only when the evidence conditions in `RESEARCH.md` are met.

## Contribution process

Substantive changes should enter through a pull request. A normative change should state:

1. the problem being corrected;
2. the affected construct, field, rubric rule, or claim;
3. supporting evidence;
4. rival interpretations;
5. backward-compatibility consequences;
6. test or fixture changes;
7. the condition under which the change should be reconsidered.

## Normative and informative material

Normative material includes:

- `SPECIFICATION.md`;
- `schema/hit-assessment.schema.json`;
- the scoring definitions in `schema/hit-dimension-catalog.json`;
- release-tagged migration notes.

Informative material includes:

- examples and fixtures;
- application guidance;
- related-work discussion;
- retrospective case studies;
- framework mappings.

Informative material may explain the method but cannot silently change normative behavior.

## Release approval

A release requires:

- passing automated validation on the release commit;
- synchronized version values across normative artifacts and metadata;
- an updated changelog and release note;
- an accurate maturity statement;
- no unresolved security issue affecting the release;
- explicit migration guidance for breaking changes.

## Conflicts of interest

Contributors should disclose institutional, commercial, litigation, standards, or publication interests that could materially affect a proposed scoring rule, case interpretation, or external-framework mapping.

## Stewardship transition

Broader governance may be introduced after sustained external contribution or institutional adoption. Any transition must preserve public version history, attribution, license continuity, and the distinction between evidence and aspiration.
