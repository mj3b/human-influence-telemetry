# Roadmap to Human Influence Telemetry 1.0.0

This roadmap treats semantic versions as public compatibility claims. Research maturity remains an evidence claim governed by `RESEARCH.md`.

Dates are secondary. A milestone is complete only when its artifacts and tests exist publicly.

## Release principles

- `0.x` releases may change assessment semantics.
- `1.0.0` means the public assessment contract is stable enough for independent implementation.
- Research maturity is reported separately from repository and component versions.
- A stable contract may remain at Maturity Level 1 while human reliability evidence is pending.
- Missing evidence remains `IE`.
- Normative changes require migration notes, synchronized contracts, deterministic fixtures, and exact-commit validation.
- Release versions remain chronological. The earlier planned `v0.3.0` human-result label is superseded under ADR-0003.
- The locked human result uses the next available version when complete and must be published, passing or failing.
- Zenodo identifiers are recorded only after successful archival.

## 0.1.0: Foundation contract — complete

Established the six substantive dimensions, Telemetry Integrity, `0/1/2/IE`, the initial schema and catalog, basic fixtures, handbook, validator, and public release controls.

Research boundary: no independent scoring, prospective validation, conformity determination, or adoption claim.

## 0.2.0–0.2.1: Evidence and research-readiness infrastructure — complete

Added three public narratives, four actor-specific historical assessments, provenance controls, the locked inter-rater protocol and frozen packet, comparison tooling, coordinator and recruitment materials, the adversarial friction review, model stress-test protocol, and archival metadata.

The repository remained Maturity Level 1 and H3 remained unresolved.

## 0.4.0: Normative rubric stabilization — current release

Completed:

- governing rules for every `FR-01` through `FR-16` ambiguity;
- evidence-state model and explicit finding thresholds;
- dimension-specific Counsel, Judgment, Command, Correction, Repair, and Reform rules;
- Repair trigger;
- split Telemetry Integrity and deterministic derivation;
- actor-authority, sampling, aggregation, contradiction, reuse, and citation rules;
- canonical 0.4.0 schema, catalog, handbook, and synthetic example;
- 48 executable boundary fixtures;
- explicit historical-case migration dispositions;
- breaking-change review and migration guide;
- adjacent-system claim audit;
- chronological result-versioning decision.

Completion test: the canonical contract and all validation layers pass on the exact release commit.

Research status: Maturity Level 1; no independent human result.

## Human inter-rater research track — prepared, unresolved

Locked artifacts:

- protocol `HIT-IRP-CIGNA-001` version 1.0.0;
- frozen packet `HIT-IR-CIGNA-PXDX-001`;
- specification and schema 0.1.0 scorer contract;
- neutral submission template and schema;
- deterministic comparison tooling;
- disagreement taxonomy and adjudication controls.

Remaining empirical gates:

- two eligible human scorers independent of the author and each other;
- two complete, unchanged submissions;
- deterministic pre-adjudication comparison;
- publication of original submissions and all disagreements;
- at least six exact agreements across seven items;
- at least `0.8571` exact agreement;
- zero critical disagreements.

Cohen's kappa across the six substantive dimensions remains supplementary.

A passing or failing result must be released under the next available repository version. Only a passing predeclared result permits H3 and Maturity Level 2.

## 0.5.0: Executable assessment conformance

Required:

- promote boundary rules from fixture evaluator to reusable assessment-conformance checks;
- validate actor and evidence-claim references across complete assessment records;
- deterministic checks for integrity derivation, Repair triggers, evidence states, sampling, aggregation, contradictions, and citation precision;
- machine-readable compatibility manifest;
- migration tooling that preserves historical records;
- one-command conformance report.

Completion test: the repository rejects every known invalid complete-record state and produces deterministic results for included valid and boundary records.

## 0.9.0: Stable release candidate

Required:

- normative contract frozen for the release candidate;
- specification, schema, catalog, handbook, validator, and implementation package synchronized;
- at least three public `0.4.x` assessments, or documented evidence that migration requires unavailable records;
- public implementation package usable without private author explanation;
- clean-room implementation audit with original outputs preserved;
- citation and archival metadata synchronized;
- no release-blocking defect.

Completion test: an independent reader can implement the method, reproduce fixtures and included assessments, and identify all non-claims from public artifacts alone.

## 1.0.0: Stable public contract

Version `1.0.0` may be declared only when:

1. the six substantive dimensions and Telemetry Integrity have stable normative definitions;
2. the `0`, `1`, `2`, and `IE` decision rules govern known ambiguity classes;
3. schema, catalog, handbook, implementation, and validator are internally consistent;
4. deterministic fixtures cover valid, invalid, and boundary cases;
5. disagreement handling remains executable for future human scoring;
6. public applications and migration boundaries are documented;
7. limitations, claim statuses, provenance, migration notes, and non-claims are current;
8. the package requires no private author explanation;
9. one public release candidate has been completed;
10. exact-release validation passes.

`1.0.0` will not establish independent reviewer agreement, Maturity Level 2, causal effectiveness, legal conformity, certification, truthful reasoning, or independent adoption.

## Beyond 1.0.0

- **Maturity Level 2, Applicable:** locked human exercise completed and predeclared threshold passed.
- **Maturity Level 3, Evidenced:** Level 2 plus at least three public applications under a compatible contract.
- **Maturity Level 4, Validated:** preregistered prospective design and pilot result.
- **Maturity Level 5, Adopted:** independent institutional use and external reference.
- Compatible research results and profiles may use `1.x` releases.
- Breaking normative changes require `2.0.0`.
