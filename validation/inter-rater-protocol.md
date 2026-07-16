# HIT Inter-rater Protocol

**Protocol ID:** `HIT-IRP-CIGNA-001`  
**Protocol version:** `1.0.0`  
**Target repository release:** `v0.3.0`  
**Scorer packet:** `HIT-IR-CIGNA-PXDX-001`  
**Method under test:** HIT specification and assessment schema `0.1.0`  
**Prepared:** 2026-07-16

## 1. Research question

Can two independent reviewers apply the published HIT rubric to the same frozen public-record packet and produce sufficiently consistent findings across Counsel, Judgment, Command, Correction, Repair, Reform, and Telemetry Integrity?

The exercise tests reproducibility of rubric application under one bounded case. It does not test causal validity, legal correctness, field effectiveness, or institutional adoption.

## 2. Unit of analysis

The unit of analysis is the Cigna PxDx post-service claims-review workflow described in the frozen packet. The institutional unit, period, terminology, evidence boundary, and source list are fixed before scoring.

Scorers must evaluate the process described by the packet. They must not generalize findings to every Cigna claim, every insurer, or every algorithmic claims process.

## 3. Scorer eligibility

Each scorer must:

1. be someone other than the HIT author;
2. have made no material contribution to the HIT specification, public case findings, or this protocol;
3. be able to read governance, assurance, legal, policy, or socio-technical evidence with professional competence;
4. disclose relevant organizational, financial, litigation, or advocacy conflicts;
5. attest that they did not inspect the author's published Cigna findings or machine-readable assessment before locking their submission;
6. conduct the assessment without discussion with the other scorer or the author.

A scorer is excluded when an independence attestation is false, materially incomplete, or contradicted by the documented process.

## 4. Blinding and coordination controls

The coordinator provides only:

- the frozen packet;
- the public HIT specification `0.1.0`;
- the public application handbook;
- the scorer-submission template;
- technical instructions for producing a valid JSON submission.

The coordinator may resolve access failures or schema-format questions. The coordinator must not interpret case evidence, suggest a finding, identify an expected disagreement, or reveal another scorer's work.

Scorers submit separately. Neither submission is disclosed until both files are locked. The original files are then committed without substantive editing. Clerical corrections require a new file and a recorded reason; the superseded submission remains available.

## 5. Materials

Scorers use only the sources listed in `frozen-packet/source-manifest.json` and the boundary in `frozen-packet/decision-boundary.md`.

Scorers must not use:

- `case-studies/cigna-pxdx.md`;
- `case-studies/assessments/cigna-pxdx.json`;
- prior commentary describing a designed disagreement;
- unpublished annotations or author guidance;
- additional sources discovered independently.

The restriction is methodological, not a claim that the excluded materials are unreliable. It keeps both scorers on the same evidence surface.

## 6. Scoring procedure

Each scorer independently:

1. reads the specification and handbook;
2. reviews all frozen sources;
3. confirms the assessment boundary;
4. assigns one finding to each substantive dimension: `0`, `1`, `2`, or `IE`;
5. assigns one Telemetry Integrity status: `adequate`, `limited`, `unreliable`, or `IE`;
6. cites one or more source IDs for every finding;
7. records a rationale and any ambiguity;
8. completes all independence and source-access attestations;
9. validates the submission against `scorer-submission.schema.json`;
10. sends the locked JSON file to the coordinator without discussing results.

`IE` must not be used as a cautious substitute for an unfavorable finding. It applies when the packet cannot distinguish absence from unavailable evidence. Conversely, lack of a public artifact is not by itself evidence of absence.

## 7. Predeclared comparison measures

### 7.1 Primary measure

The primary measure is exact agreement across seven items:

- six substantive dimensions;
- Telemetry Integrity.

The exact-agreement proportion is:

`number of identical findings / 7`

### 7.2 Advancement threshold

The exercise meets the Level 2 agreement gate when:

1. at least six of seven findings agree exactly, yielding at least `0.8571` exact agreement;
2. there are no critical disagreements;
3. both submissions satisfy the eligibility, independence, completeness, and schema requirements.

The threshold is deliberately discrete. With seven items, five agreements would equal `0.7143`, while six equal `0.8571`.

### 7.3 Critical disagreement

A disagreement is critical when:

- one scorer assigns `IE` and the other assigns `0`, `1`, or `2` on a substantive dimension;
- one scorer assigns `0` and the other assigns `2`;
- one scorer assigns Telemetry Integrity `IE` and the other assigns a determinate status;
- the disagreement changes the assessment boundary or institutional actor rather than only the finding.

Adjacent ordinal disagreements such as `0` versus `1` or `1` versus `2` are material but not automatically critical.

### 7.4 Supplementary statistic

The comparison tool reports unweighted Cohen's kappa for the six substantive dimensions, treating `IE` as a distinct category. Kappa is supplementary because six observations are too few for a stable general reliability estimate and category prevalence may dominate the result.

No composite HIT score is calculated.

## 8. Disagreement classification

Every nonmatching item is classified using `disagreement-taxonomy.md`. Classification occurs after the original submissions are locked and the deterministic comparison is generated.

The classifier may identify multiple causes. The record must distinguish:

- evidence selection;
- evidentiary weight;
- boundary interpretation;
- construct interpretation;
- `0` versus `IE` logic;
- ordinal threshold interpretation;
- Telemetry Integrity interpretation;
- clerical or schema error.

## 9. Adjudication

Adjudication explains disagreements and determines whether the handbook, protocol, schema, or future rubric requires revision. It does not overwrite either score.

A third reviewer is preferred. When no third reviewer is available, the author may facilitate classification but must identify that limitation and may not recalculate pre-adjudication agreement after changing scores.

The public record must preserve:

- both original submissions;
- the deterministic comparison output;
- each disagreement category;
- the adjudicator's reasoning;
- any proposed normative change;
- the maturity decision based on the pre-adjudication result.

## 10. Failure handling

A failing result is publishable and informative.

When the threshold is not met:

- claim H3 remains unresolved or is updated as not demonstrated under this packet;
- the repository remains at Maturity Level 1;
- the failure and disagreements are published without selective omission;
- rubric revisions move to the `v0.4.0` stabilization workstream;
- a new exercise requires a new protocol or packet identifier.

No additional scorer may be added merely to replace an unfavorable result. A replication may be run, but the initial result remains part of the record.

## 11. Publication gate for v0.3.0

The result release requires:

- this protocol locked on `main` before scoring begins;
- two eligible independent submissions;
- successful schema validation;
- deterministic comparison output;
- disagreement register;
- adjudication record;
- updated `RESEARCH.md`, `README.md`, `CHANGELOG.md`, and release notes;
- repository validation passing on the exact release commit.

The release may report either pass or fail. Maturity Level 2 may be claimed only when the advancement threshold and independence conditions are met.
