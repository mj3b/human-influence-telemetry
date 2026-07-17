# Adversarial Rubric-Friction Review

**Review ID:** `HIT-ARFR-001`  
**Version:** `1.0.0`  
**Status:** Non-empirical, coordinator-only  
**Method version reviewed:** HIT specification `0.1.0`  
**Related protocol:** `HIT-IRP-CIGNA-001`  
**Prepared:** 2026-07-16

## 1. Purpose

This review identifies places where two competent, independent scorers could reasonably apply the published Human Influence Telemetry rubric differently even when they receive the same assessment boundary and evidence packet.

It is a dry run of the method, not a dry run of the Cigna case.

## 2. Materials reviewed

- `SPECIFICATION.md`
- `docs/application-handbook.md`
- `validation/inter-rater-protocol.md`
- `validation/frozen-packet/decision-boundary.md`
- `validation/scorer-submission.schema.json`
- `validation/disagreement-taxonomy.md`

## 3. Exclusions

This review:

- did not read or evaluate sources S1, S2, or S3;
- did not assign any HIT finding;
- did not inspect or reproduce the author's Cigna findings;
- does not estimate the correct result for any dimension;
- does not satisfy claim H3;
- does not advance HIT beyond Maturity Level 1;
- must not be distributed to scorers before their submissions are locked.

The review is withheld from scorers because revealing predicted fault lines could prime their interpretation.

## 4. Executive assessment

The locked protocol is administrable, but the first human exercise is likely to be sensitive to construct interpretation rather than file-format error.

The highest-risk breakpoints are:

1. the evidentiary threshold separating `0` from `IE`;
2. whether formal authority without evidence of exercise supports `1` or `IE`;
3. the object and thresholds of Telemetry Integrity;
4. the trigger for Repair when harm is alleged, reported, acknowledged, or adjudicated;
5. actor and time-boundary decomposition.

These breakpoints matter because `IE` versus any determinate substantive finding is mechanically critical. A single such disagreement blocks the predeclared Level 2 gate even when the other six findings agree.

Ordinal disputes between `1` and `2` are less severe mechanically, but the six-of-seven rule permits only one exact mismatch. Two reasonable adjacent disagreements would therefore fail the gate without any critical disagreement.

## 5. Friction register

### `FR-01`: Affirmative absence versus missing evidence

**Construct:** all substantive dimensions

The specification defines `0` as absent. The handbook says `0` applies when the practice or artifact did not exist, while `IE` applies when records are missing or cannot distinguish absence from missing evidence.

- **Plausible reading A:** A detailed process description that omits a capacity may provide affirmative evidence that the capacity was absent.
- **Plausible reading B:** Only an explicit record of nonexistence or demonstrated impossibility supports `0`; documentary silence supports `IE`.
- **Likely disagreement:** `0` versus `IE`
- **Mechanical consequence:** Critical
- **Current resolution:** Partial
- **Candidate repair target:** Define affirmative evidence of absence and distinguish omission, failed production, explicit nonexistence, and structural impossibility.

### `FR-02`: Formal role evidence as `1` versus `IE`

**Construct:** Counsel, Judgment, Command, Correction, Repair, Reform

- **Plausible reading A:** A documented role, approval step, or authority statement establishes formal presence. Missing evidence of practical effect therefore supports `1`.
- **Plausible reading B:** A role statement without an independent operational artifact does not establish that the capacity existed in the assessed process. The result should remain `IE`.
- **Likely disagreement:** `1` versus `IE`
- **Mechanical consequence:** Critical
- **Current resolution:** Not explicit
- **Candidate repair target:** State the minimum artifact needed to establish formal presence before ceremoniality can be assessed.

### `FR-03`: Minimum evidence for a finding of `2`

**Construct:** all substantive dimensions

The specification permits `2` when capacity affected, or could credibly have affected, the path. The handbook emphasizes an observed instance or demonstrably maintained and exercised capacity.

- **Plausible reading A:** Credible documented authority and an operable mechanism can support `2` even when the sample contains no observed exercise.
- **Plausible reading B:** `2` requires an observed exercise or direct operational test; credible capacity alone supports at most `1`.
- **Likely disagreement:** `1` versus `2`
- **Mechanical consequence:** Noncritical, but consumes the only mismatch allowed by the gate
- **Current resolution:** Partial
- **Candidate repair target:** Define when capability evidence may substitute for an observed instance.

### `FR-04`: Counsel as access capability versus actual access

**Construct:** Counsel

- **Plausible reading A:** Evidence that the human role could retrieve underlying evidence establishes substantive access.
- **Plausible reading B:** Counsel concerns evidence actually presented or retrieved before the assessed decision, not general access permissions.
- **Likely disagreement:** `1` versus `2`, or `IE` versus determinate
- **Mechanical consequence:** Potentially critical
- **Candidate repair target:** Separate authorization, technical availability, actual retrieval, and timing.

### `FR-05`: Negative inference in Judgment

**Construct:** Judgment

Boilerplate acceptance, very short review time, and near-total recommendation adoption are listed as failure signs, but the rubric does not map each sign to `0`, `1`, or `IE`.

- **Plausible reading A:** Strong process indicators can affirmatively establish absence or ceremonial review.
- **Plausible reading B:** Without reviewer-level reasoning records, those indicators are suggestive but insufficient to distinguish `0`, `1`, and `IE`.
- **Likely disagreement:** `0`, `1`, or `IE`
- **Mechanical consequence:** Potentially critical
- **Candidate repair target:** Define when indirect process indicators are dispositive, corroborative, or insufficient.

### `FR-06`: Command as legal authority versus practical intervention

**Construct:** Command

Passing evidence includes authority to direct otherwise, with an exercised instance “where the sample permits.”

- **Plausible reading A:** A valid delegation instrument and usable override mechanism may support `2` when the sample is too narrow to include an exercise.
- **Plausible reading B:** Authority without an observed exercise supports `1`; a formal power may be practically unusable.
- **Likely disagreement:** `1` versus `2`
- **Mechanical consequence:** Noncritical, but gate-sensitive
- **Candidate repair target:** Define “where the sample permits” and the operational evidence required to show an override was usable.

### `FR-07`: Correction path versus effective reconsideration

**Construct:** Correction

- **Plausible reading A:** An operative appeal or escalation path establishes substantive Correction even without a reversal in the packet.
- **Plausible reading B:** The handbook and specification require evidence of reconsideration, interruption, or reversal; a path alone is ceremonial.
- **Third plausible reading:** The record cannot determine whether the path was operative, requiring `IE`.
- **Likely disagreement:** `1` versus `2`, or `IE` versus determinate
- **Mechanical consequence:** Potentially critical
- **Candidate repair target:** Distinguish channel existence, accessibility, procedural use, substantive reconsideration, and outcome change.

### `FR-08`: Repair trigger and “substantiated harm”

**Construct:** Repair

- **Plausible reading A:** Credible documentary evidence of harm is sufficient to activate the Repair inquiry.
- **Plausible reading B:** Harm must be adjudicated, formally acknowledged, or otherwise established by a defined institutional process before absence of repair can be scored.
- **Likely disagreement:** `0` versus `IE`, or different decisions about whether the dimension is triggered
- **Mechanical consequence:** Critical
- **Candidate repair target:** Define substantiation and specify the result when the trigger itself is unresolved.

### `FR-09`: Reform linkage and temporal leakage

**Construct:** Reform

- **Plausible reading A:** A later threshold, workflow, or governance change may demonstrate Reform when it responds to the assessed architecture.
- **Plausible reading B:** Later change counts only when a named authority links it to the assessed failure within the bounded period.
- **Additional ambiguity:** Externally compelled change may or may not demonstrate the institution’s own reform capacity.
- **Likely disagreement:** `1` versus `2`, or `IE` versus determinate
- **Mechanical consequence:** Potentially critical
- **Candidate repair target:** Define causal linkage, temporal admissibility, and externally compelled reform.

### `FR-10`: Object of Telemetry Integrity

**Construct:** Telemetry Integrity

- **Plausible reading A:** Assess the integrity of the institutional records that would support the six substantive findings.
- **Plausible reading B:** In a public-record reconstruction, assess the provenance and completeness of the evidence packet itself.
- **Plausible reading C:** Both objects matter and should be combined into one status.
- **Likely disagreement:** `IE` versus `limited`, `unreliable`, or another determinate status
- **Mechanical consequence:** Critical
- **Current resolution:** Not explicit
- **Candidate repair target:** Define the object of assessment and whether packet integrity and institutional-record integrity require separate fields.

### `FR-11`: Thresholds among Telemetry Integrity statuses

**Construct:** Telemetry Integrity

The schema permits `adequate`, `limited`, `unreliable`, and `IE`, but the specification and handbook do not provide decision thresholds for those statuses.

- **Plausible reading A:** Missing provenance or retention information makes integrity `limited`.
- **Plausible reading B:** The same omissions make integrity `IE` because the status cannot be determined.
- **Plausible reading C:** Material contradiction or dependence makes integrity `unreliable`.
- **Likely disagreement:** Any pair of integrity statuses
- **Mechanical consequence:** `IE` versus determinate is critical; other mismatches still consume the only allowed disagreement
- **Candidate repair target:** Publish a status decision tree with minimum conditions and failure signs.

### `FR-12`: Period aggregation and rare exercised capacity

**Construct:** all substantive dimensions

- **Plausible reading A:** One verified exercise can establish that a capacity existed and was substantive during the bounded period.
- **Plausible reading B:** A rare exception does not establish the dominant decision architecture and should not determine the period-level finding.
- **Likely disagreement:** `1` versus `2`
- **Mechanical consequence:** Noncritical, but gate-sensitive
- **Candidate repair target:** Declare whether HIT scores any demonstrated capacity, the dominant pattern, a defined sample proportion, or a worst-case condition.

### `FR-13`: Actor decomposition

**Construct:** all dimensions

The institutional unit includes related corporate entities, while the human role is a physician or medical director. Vendors, regulators, courts, and corporate leadership may also affect the process.

- **Plausible reading A:** Score the institution as a combined decision architecture.
- **Plausible reading B:** Score each authority-bearing actor separately and avoid attributing one actor’s conduct to another.
- **Likely disagreement:** Boundary or actor disagreement
- **Mechanical consequence:** Critical under the locked protocol
- **Candidate repair target:** Add an actor-authority matrix and attribution rules.

### `FR-14`: Contradictory evidence and evidentiary weight

**Construct:** all dimensions

- **Plausible reading A:** A detailed, corroborated account can support a determinate finding despite an institutional denial.
- **Plausible reading B:** Material conflict between reporting, institutional response, and procedural allegations prevents a determinate finding.
- **Likely disagreement:** `IE` versus determinate, or adjacent ordinal findings
- **Mechanical consequence:** Potentially critical
- **Candidate repair target:** Define how source tiers, corroboration, specificity, and contradiction affect findings without turning the method into a merits adjudication.

### `FR-15`: Cross-dimensional reuse of evidence

**Construct:** dimension boundaries

- **Plausible reading A:** One artifact may support multiple dimensions when it has distinct implications for each.
- **Plausible reading B:** Evidence should not be reused unless it separately establishes each construct; otherwise dimensions collapse into one another.
- **Likely disagreement:** Multiple adjacent or `IE` mismatches
- **Mechanical consequence:** Gate-sensitive
- **Candidate repair target:** Add construct-separation examples and rules for multi-dimensional evidence.

### `FR-16`: Citation precision

**Construct:** auditability rather than finding substance

The schema requires source IDs but not page, paragraph, quotation, or record locator.

- **Risk:** Two scorers may cite the same source ID while relying on different passages. The comparison will detect the finding mismatch but not reconstruct the evidentiary crux efficiently.
- **Mechanical consequence:** No direct threshold effect
- **Candidate repair target:** Require passage locators or structured evidence claims in a later schema version.

## 6. Gate sensitivity

The gate is intentionally strict:

- one adjacent ordinal disagreement may still pass;
- two adjacent disagreements fail;
- one `IE` versus determinate disagreement fails;
- one actor or boundary disagreement fails;
- one Telemetry Integrity `IE` versus determinate disagreement fails.

Therefore, construct ambiguity can dominate the result even when scorers agree on the broad institutional pattern.

This is not an argument to lower the gate after observing a result. It is an argument to interpret failure diagnostically and to preserve the initial exercise.

## 7. Controls that may be applied without changing the locked protocol

Before scoring:

1. Freeze identical source files and record their SHA-256 digests.
2. Give both scorers the same file set and filenames.
3. Keep this friction review coordinator-only.
4. Answer only access and schema-format questions.
5. Record every coordinator communication.
6. When one scorer reports a broken link or file defect, issue the same neutral correction to both.
7. Do not answer construct or evidence-interpretation questions.
8. Do not revise the specification, handbook, threshold, or packet after the first scorer begins.
9. Preserve all questions that expose ambiguity as inputs to `v0.4.0`.
10. Run the deterministic comparison before any adjudication.

## 8. Update conditions

A friction hypothesis should become a normative rubric change only when supported by at least one of:

- an actual independent-scorer disagreement;
- repeated divergence across separate model stress-test runs;
- a demonstrated contradiction between specification, handbook, schema, and validator;
- evidence that the current rule makes a construct impossible to apply consistently;
- an external methodological review with a stated mechanism and repair.

The initial human result must remain unchanged after any later update.

## 9. Decision consequence

Proceed with:

- the coordinator tooling;
- the separate model-based rubric stress test;
- a maintenance software release and DOI;
- continued recruitment when qualified scorers become available.

Do not claim human inter-rater reliability or Maturity Level 2 until `HIT-IRP-CIGNA-001` is completed under its locked rules.
