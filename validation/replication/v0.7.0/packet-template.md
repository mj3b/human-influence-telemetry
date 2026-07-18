# HIT v0.7.0 Frozen Packet Template

**Packet ID:** `HIT-IR-[CASE]-[NNN]`  
**Protocol ID:** `HIT-IRP-MULTICASE-002`  
**Packet version:** `0.1.0-candidate`  
**Contract:** HIT `0.4.0`  
**Status:** Candidate until final digest is recorded

## 1. Decision boundary

State:

- institution;
- decision process;
- named actor or actor class;
- system role;
- assessment period;
- affected population or record universe;
- decision stage;
- excluded processes and actors.

The boundary must be precise enough that two reviewers cannot silently evaluate different systems.

## 2. Sampling and aggregation declaration

Record:

- target record universe;
- available record universe;
- selection rule;
- dominant-pattern rule;
- treatment of rare interventions;
- treatment of missing records;
- limits on generalization.

## 3. Source manifest

For every source, record:

- source ID;
- title;
- issuing actor;
- publication or filing date;
- source type;
- procedural posture;
- stable public location or archived identifier;
- required pages, sections, paragraphs, or timestamps;
- SHA-256 when a frozen local copy is distributed;
- permitted use and redistribution status;
- proposition classes the source may support;
- claims the source cannot support.

## 4. Procedural-posture register

Every legal, regulatory, investigative, audit, or institutional source must be labeled. Examples include:

- allegation;
- pleading-stage ruling;
- merits judgment;
- settlement without admission;
- regulator finding;
- legislative investigation;
- internal policy statement;
- technical documentation;
- retrospective journalism;
- peer-reviewed empirical study.

The packet must prevent a source from carrying a stronger claim than its posture allows.

## 5. Actor-authority boundary

List the actors who may appear in the sources and state which actor the scorer must evaluate.

For the assessed actor, define possible authority over:

- evidence access;
- interpretation;
- independent judgment;
- approval or rejection;
- interruption or escalation;
- contestation and correction;
- remediation;
- system change.

Do not state whether the authority was exercised.

## 6. Evidence proposition index

Create neutral proposition identifiers before scoring. Each proposition states an observable question without assigning a finding.

Example form:

`P-CMD-01`: Records show whether the assessed actor could stop or reverse the system-mediated action before execution.

For each proposition, list:

- relevant dimension;
- eligible source IDs;
- required locator precision;
- possible support relations: supports, contradicts, limits, context only;
- known evidentiary gap.

## 7. Repair trigger materials

Provide the records needed to distinguish:

- `triggered`;
- `not_triggered`;
- `indeterminate`.

The packet must separate evidence of alleged harm, established harm, affected persons, remediation, restitution, and structural change.

## 8. Telemetry Integrity materials

### Institutional-record integrity

Include evidence relevant to completeness, provenance, authorship, timing, editability, auditability, selection, and institutional control of the underlying records.

### Assessment-packet integrity

Include the packet manifest, source hashes, locator checks, access notes, known omissions, selection method, and contradiction register.

## 9. Contradiction register

List known conflicts across sources without resolving them for the scorer.

For each conflict, record:

- contradiction ID;
- source IDs;
- propositions in conflict;
- procedural-posture difference;
- timing difference;
- unresolved question.

## 10. Scorer instructions

The scorer must:

1. use only the frozen packet and published `0.4.0` materials;
2. evaluate the declared actor and period;
3. record proposition-level evidence with precise locators;
4. distinguish evidence state from finding;
5. use `IE` when the record cannot resolve the proposition;
6. apply the Repair trigger before scoring Repair;
7. score both integrity components and derive overall Telemetry Integrity;
8. record contradictory evidence and weighting;
9. run complete-record conformance;
10. submit without consulting another scorer, the author, or prior HIT findings.

## 11. Coordinator-only annex

The scorer-facing packet must exclude:

- sampling-stratum label;
- expected category profile;
- author findings;
- comparison fixtures;
- disagreement predictions;
- adjudication guidance tied to the case;
- recruitment identities;
- another scorer's access or work status.

## 12. Freeze record

Before distribution, record:

- final packet ID and version;
- file list;
- byte size of each file;
- SHA-256 of each file;
- combined manifest digest;
- lock commit;
- lock timestamp;
- coordinator attestation that scorer-facing and coordinator-only materials are separated;
- validation result on the exact lock commit.
