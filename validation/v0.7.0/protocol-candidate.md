# HIT Current-contract Multi-case Replication Protocol

**Protocol ID:** `HIT-IRP-HIT040-002`  
**Protocol version:** `0.1.0-candidate`  
**Target repository release:** `v0.7.0`  
**Method under test:** HIT specification, schema, catalog, and handbook `0.4.0`  
**Conformance engine:** `0.5.0`  
**Study status:** Candidate, scoring prohibited  
**Prepared:** 2026-07-18

## 1. Research question

Can three independent reviewers apply the current HIT contract to three frozen public-record packets and produce reproducible findings across distinct evidence conditions?

The exercise tests application of the `0.4.0` boundary rules, actor attribution, evidence states, six substantive dimensions, Repair trigger, sampling rules, aggregation rules, structured evidence claims, and split Telemetry Integrity.

## 2. Study objects

The study contains three packets selected before scoring:

- one exercise-rich packet containing direct evidence that a named human action changed a decision path;
- one constraint-rich packet containing a process-specific human role and at least two indicators of ceremonial operation;
- one evidence-limited packet in which a documented search leaves material propositions unresolved.

These labels govern case selection. Scorers do not receive the labels or any expected findings.

Each packet fixes:

- institutional unit and decision process;
- period and any follow-up period;
- AI-system role and stated human role;
- population or record universe;
- source boundary;
- sampling rule;
- aggregation rule;
- actor identity roster;
- known exclusions and selection effects.

Scorers evaluate authority, evidence states, findings, Repair trigger, and integrity under the frozen boundary.

## 3. Scorer design

Three eligible independent scorers assess all three packets. This creates nine submissions.

Each scorer must:

1. be someone other than the HIT author;
2. have made no material contribution to the `0.4.0` contract, packet findings, protocol, or source selection;
3. demonstrate competence in governance, assurance, law, policy, audit, socio-technical analysis, or a relevant applied discipline;
4. disclose organizational, financial, litigation, advocacy, and personal conflicts;
5. attest that they did not inspect author assessments, coordinator expectations, or another scorer's work;
6. work independently across all three packets;
7. use only frozen packet sources;
8. refrain from generative-model assistance for evidence interpretation, finding assignment, evidence selection, rationale drafting, or ambiguity analysis;
9. disclose every software tool used for document access, note-taking, hashing, schema validation, or formatting.

Deterministic schema validation and local text-processing tools are permitted. A generative model may not perform substantive scoring work.

## 4. Coordinator controls

The coordinator provides only:

- the frozen scorer packet;
- `SPECIFICATION.md` version `0.4.0`;
- `docs/application-handbook.md` version `0.4.0`;
- `schema/hit-assessment.schema.json` version `0.4.0`;
- `schema/hit-dimension-catalog.json` version `0.4.0`;
- submission instructions;
- technical validation instructions.

The coordinator may resolve access failures and schema-format questions. The coordinator may not interpret evidence, identify an expected finding, suggest an actor attribution, resolve ambiguity, reveal another scorer's work, or disclose the case-selection stratum.

Submissions remain sealed until all nine are received, preserved, hashed, validated, and verified by their scorers.

## 5. Submission contract

For each packet, each scorer submits:

1. one complete `0.4.0` assessment JSON;
2. one submission manifest;
3. any original manual worksheet or native working record used to create the JSON.

The assessment JSON must pass structural and executable conformance. Conformance does not establish substantive correctness.

The manifest records independence attestations, source access, tool use, file hashes, submission time, and conflict disclosure. Identity records used to establish eligibility remain separate from the public pseudonymous submission.

A coordinator transcription is allowed only when a scorer submits a manual record. The original remains immutable. The scorer verifies transcription accuracy without reconsidering any substantive judgment.

## 6. Primary comparison items

Each packet contains eight non-derived categorical comparison items.

For each substantive dimension, exact agreement requires:

- identical finding;
- identical evidence state;
- identical Repair trigger for Repair.

The six substantive composites are:

- Counsel;
- Judgment;
- Command;
- Correction;
- Repair;
- Reform.

The two integrity items are:

- institutional-record integrity status;
- assessment-packet integrity status.

The derived overall integrity status is checked for deterministic consistency and excluded from the primary denominator.

## 7. Primary agreement measures

Three scorers create three scorer pairs per packet. Eight items across three packets produce 72 pairwise comparisons.

The primary measures are:

1. pooled pairwise exact agreement: exact pairwise matches divided by 72;
2. packet-level pairwise exact agreement: exact pairwise matches divided by 24 for each packet;
3. item unanimity: packet-item units with identical values across all three scorers divided by 24.

## 8. H3 replication threshold

The current-contract replication supports an extension of H3 when all conditions hold:

1. at least 60 of 72 pairwise comparisons agree exactly, yielding at least `0.8333`;
2. each packet has at least 19 of 24 pairwise exact matches, yielding at least `0.7917`;
3. at least 18 of 24 packet-item units are unanimous, yielding at least `0.7500`;
4. zero critical disagreements remain in the pre-adjudication result;
5. all nine submissions satisfy eligibility, independence, source-boundary, completeness, hash, verification, and conformance requirements.

The thresholds prevent one high-agreement packet from masking a low-agreement packet. The result remains bounded to this study.

## 9. Critical disagreements

A disagreement is critical when any of these conditions occurs:

- one scorer assigns `IE` and another assigns a determinate finding on a substantive dimension;
- one scorer assigns `0` and another assigns `2`;
- Repair trigger differs between `triggered` and `not_triggered`;
- one integrity component is `unreliable` and another scorer assigns `adequate`;
- one integrity component is `IE` and another scorer assigns a determinate status;
- a scorer changes the frozen unit, period, aggregation rule, or assessed actor identity;
- cross-institution authority is attributed without a documented relationship permitted by the contract;
- the disagreement changes whether a record can be treated as a conforming assessment of the frozen packet.

Adjacent ordinal disagreements remain material and enter the disagreement register.

## 10. Supplementary measures

The study reports:

- finding-only exact agreement;
- evidence-state agreement;
- Repair-trigger agreement;
- integrity-component agreement;
- pairwise weighted Cohen's kappa for determinate `0`, `1`, and `2` findings;
- Krippendorff's alpha using the declared nominal and ordinal treatments;
- source-ID set overlap for each packet-item unit;
- actor-authority vector agreement;
- disagreement causes under the public taxonomy;
- rationale divergence coded by human reviewers.

Chance-corrected statistics remain supplementary because category prevalence, `IE`, and the small packet count may distort them.

No composite HIT score is calculated.

## 11. Disagreement classification

Every nonmatching item is classified after the pre-adjudication comparison is frozen. Permitted causes include:

- source selection;
- locator interpretation;
- proposition construction;
- evidentiary weight;
- actor or authority attribution;
- boundary interpretation;
- evidence-state classification;
- ordinal threshold interpretation;
- Repair-trigger interpretation;
- sampling or aggregation interpretation;
- institutional-record integrity interpretation;
- assessment-packet integrity interpretation;
- clerical or schema error;
- contract ambiguity.

Multiple causes may apply. Classification does not alter the original scores.

## 12. Adjudication

Adjudication explains disagreement and identifies contract defects. It does not overwrite a submission or recalculate the pre-adjudication result.

The public record preserves:

- original working records;
- final scorer-verified JSON files;
- submission manifests;
- hashes and receipt times;
- pre-adjudication comparisons;
- disagreement classifications;
- adjudication reasoning;
- normative-change proposals;
- H3 and maturity decisions.

## 13. Maturity decision

Maturity Level 3 and the H3 replication result are separate decisions.

Level 3 may be considered when:

- three complete public `0.4.x` applications exist;
- nine independent submissions are preserved;
- every packet has a frozen boundary and source manifest;
- pre-adjudication comparisons and disagreement analysis are public;
- no unresolved protocol-integrity failure invalidates the applications;
- the repository passes exact-commit validation.

A failed H3 replication remains publishable evidence and does not erase valid current-contract applications. The maturity decision must explain the failure and its consequences.

## 14. Failure handling

All results are published. A failure may update H3 as unsupported under this protocol, reveal a contract ambiguity, identify an unusable packet, or expose a scorer-independence defect.

No scorer or packet may be removed because it lowers agreement. Replacement requires a new protocol amendment recorded before unsealing results, or a separate replication with a new identifier.

## 15. Protocol lock

Scoring is prohibited until `0.7.0` publishes:

- this protocol with status `locked`;
- a machine-readable lock record;
- three packet IDs and versions;
- three decision boundaries;
- three frozen source manifests;
- archived source hashes or stable source identifiers;
- final comparison code and synthetic test vectors;
- final submission schemas;
- scorer instructions and coordinator controls;
- pass, fail, and publication rules;
- exact-commit repository validation.

Changes after lock require a numbered amendment. The amendment must state whether the change affects eligibility, evidence surface, comparison, interpretation, or maturity consequences.
