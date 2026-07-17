# Human Influence Telemetry v1.0.0 Readiness Plan

**Target:** 31 July 2026  
**Governing decision:** `ADR-0001`  
**Current repository release:** `0.2.1`  
**Current component versions:** specification, assessment schema, and dimension catalog `0.1.0`  
**Current maturity:** Level 1, Defined

## Release claim

Version `1.0.0` will mean that HIT has a stable public assessment contract that can be implemented from public artifacts and checked through executable conformance tests.

It will not claim human inter-rater reliability. Claim H3 and Maturity Level 2 remain pending until two eligible independent human scorers complete the locked protocol.

The July 31 date is a target. The release gates control the decision.

## Workstream A: Normative rubric stabilization

**Candidate release:** `0.4.0`

Convert the adversarial rubric-friction review into explicit decision rules.

### Required rules

1. **Affirmative absence and `IE`.** Define the evidence needed for `0`, including explicit nonexistence, structural impossibility, complete negative search, and reliable process evidence. Documentary silence alone remains `IE`.
2. **Formal presence and ceremoniality.** Define the minimum artifact that establishes a practice existed before `1` can be assigned.
3. **Minimum evidence for `2`.** Separate observed exercise, tested capability, and asserted authority. Define when each can support substantive exercise.
4. **Actor and authority attribution.** Require one actor-authority matrix for multi-actor processes and prevent conduct from being assigned across institutional boundaries without evidence.
5. **Temporal admissibility.** Define how later correction, repair, and reform may inform an earlier assessment period.
6. **Repair trigger.** Define substantiated harm and the result when the harm trigger itself remains unresolved.
7. **Telemetry Integrity.** Separate integrity of the institutional record from integrity of the public evidence packet. Define thresholds for `adequate`, `limited`, `unreliable`, and `IE`.
8. **Contradictory evidence.** Define how source type, procedural posture, specificity, corroboration, institutional response, and unresolved conflict affect a finding.
9. **Sampling and aggregation.** Define whether a finding represents any demonstrated capacity, dominant practice, sampled frequency, or a specified worst-case condition.
10. **Citation precision.** Require source IDs plus passage, page, paragraph, event, or record locators when the source permits them.
11. **Adjacent-system terminology.** Define institutional decision, runtime policy decision, Governed Decision Record, HIT assessment record, documentary telemetry, assessment-contract conformance, cryptographic receipt, and evidence-applicability determination.
12. **Portfolio boundary.** Preserve the separate roles of Microsoft AGT, ScopeBlind/Acta, Credo AI, GDI, HIT, and DEAS. Prohibit claims that HIT performs runtime enforcement, receipt interoperability, policy-pack harmonization, compliance automation, or evidence portability.

### Required artifacts

- revised `SPECIFICATION.md`;
- revised application handbook;
- synchronized assessment schema and dimension catalog;
- normative decision tables;
- `docs/adjacent-system-boundaries.md`;
- migration notes from component version `0.1.0`;
- updated public cases or explicit migration exceptions;
- changelog and compatibility statement.

### Completion test

A reader can assign each finding without relying on private author interpretation for any ambiguity class recorded in `HIT-ARFR-001`, and can distinguish HIT from runtime governance, signed-receipt verification, policy-pack systems, decision-record infrastructure, and cross-regime evidence applicability.

## Workstream B: Executable conformance

**Candidate release:** `0.5.0`

Turn each normative rule into machine-checkable or review-checkable evidence.

### Test classes

- valid substantive assessment;
- valid ceremonial assessment;
- valid insufficient-evidence assessment;
- explicit absence versus missing evidence;
- formal authority with no exercise;
- tested capability with no observed use;
- conflicting source tiers;
- multi-actor attribution;
- later reform outside the assessment period;
- unresolved harm trigger;
- Telemetry Integrity packet-versus-record distinction;
- duplicate or missing dimensions;
- unsupported composite score;
- missing citation locator;
- inconsistent component versions;
- migration from the released `0.1.0` contract;
- prohibited unqualified use of `decision record`, `conformance`, `telemetry`, or `portability` in HIT public claims;
- unsupported claims of runtime enforcement, signed-receipt verification, policy-pack harmonization, compliance automation, or evidence portability.

### Required artifacts

- positive and negative fixtures;
- boundary assessment cases;
- validator rules;
- fixture index;
- conformance report format;
- machine-readable compatibility manifest;
- adjacent-system claim-audit checklist;
- one-command repository validation.

### Completion test

The repository rejects every known invalid state, produces deterministic results for every included boundary case, and detects public language that collapses HIT into an adjacent system layer.

## Workstream C: Clean-room implementation audit

**Candidate release:** `0.9.0`

Test whether the public package can be used without private explanation.

### Procedure

1. Build a standalone implementation packet containing only public normative artifacts.
2. Run two fresh model sessions as implementation auditors, not human scorers.
3. Ask each session to reconstruct the finding rules, identify required fields, validate the included fixtures, and report ambiguous instructions.
4. Ask each session to classify HIT against Microsoft AGT, ScopeBlind/Acta, Credo AI, GDI, and DEAS using only the public boundary document.
5. Preserve both original outputs and classify discrepancies.
6. Resolve release-blocking documentation or conformance defects.
7. Keep the model result separate from H3 and the maturity model.

### Release-candidate gates

- component versions frozen;
- all public cases validate under the candidate contract;
- migration guide complete;
- no known ambiguity can systematically change a finding without a documented rule;
- implementation packet complete;
- adjacent-system claim audit passes;
- the public package distinguishes documentary telemetry from runtime observability and cryptographic receipt evidence;
- README, research register, limitations, provenance, citation, and release metadata synchronized;
- one public `v0.9.0` release candidate published;
- no release-blocking defect remains open.

## Workstream D: Stable public contract

**Release:** `1.0.0`

### Required release artifacts

- stable specification `1.0.0`;
- assessment schema `1.0.0`;
- dimension catalog `1.0.0`;
- application handbook `1.0.0`;
- terminology and adjacent-system boundary contract;
- conformance suite and report;
- migration guide from `0.1.0`;
- breaking-change review;
- implementation packet;
- revalidated public cases;
- adjacent-system claim-audit report;
- current claim register and limitations;
- release notes and citation metadata;
- exact release commit with passing CI.

### Mandatory release language

The release must state:

- HIT is at Maturity Level 1;
- H3 remains unresolved;
- the locked human protocol remains pending;
- model stress tests are development evidence only;
- HIT is a documentary assurance method, not a runtime governor, signed-receipt protocol, policy-pack platform, compliance engine, or evidence-portability mechanism;
- the stable contract does not establish legal compliance, causal validity, certification, or independent adoption.

## Parallel DOI path

The DOI path is independent of semantic versioning.

A manual Zenodo software upload of the `v0.2.1` GitHub source archive can establish a citable software record while the v1 work continues. The upload must contain one compressed source archive, use Resource type `Software`, identify version `0.2.1`, and preserve the same title, author, ORCID, license, description, and related identifiers used in the repository metadata.

The resulting DOI must be added only after the public Zenodo record exists.

## Proposed schedule

| Date | Decision target |
|---|---|
| 17 to 21 July | Complete `0.4.0` normative rules, terminology boundary, and migration design |
| 22 to 24 July | Complete `0.5.0` conformance fixtures, claim audit, and validator coverage |
| 25 to 27 July | Publish `0.9.0` release candidate and run clean-room implementation audit |
| 28 to 30 July | Correct release-blocking defects and perform release audit |
| 31 July | Publish `1.0.0` only when every stable-contract gate passes |

## Stop conditions

Withhold `1.0.0` when any of the following remains true:

- a known friction class can change a finding without a governing rule;
- schema, catalog, handbook, fixtures, cases, or validator disagree;
- public cases cannot migrate cleanly;
- the implementation packet requires private explanation;
- HIT public language implies runtime enforcement, signed-receipt interoperability, policy-pack harmonization, compliance automation, or evidence portability;
- overloaded terms such as `decision record`, `telemetry`, `conformance`, or `portability` remain unqualified where they can change system interpretation;
- a release-blocking defect remains open;
- release metadata implies H3, Level 2, validation, certification, or adoption.
