# HIT v1.0.0 Clean-room Implementation Audit Protocol

**Protocol ID:** `HIT-CRI-V100-001`  
**Version:** `0.1.0-candidate`  
**Status:** Candidate, audit prohibited  
**Target release:** `v0.9.0`

## Research question

Can a technically competent external reviewer install, operate, and explain the public HIT package without private author explanation?

## Auditor eligibility

The auditor must:

- be someone other than the HIT author;
- have made no material contribution to the candidate implementation packet;
- have competence in software implementation, assurance, audit, data validation, or a related technical discipline;
- disclose conflicts and prior exposure;
- receive only the public implementation packet and ordinary public repository access;
- preserve commands, outputs, environment details, and original notes.

The auditor may be the same person as a future HIT scorer only when the eligibility record explains how implementation auditing remains separate from case scoring and no protected findings are disclosed.

## Coordinator boundary

The coordinator may:

- restore access to a public file;
- identify a documented installation command;
- confirm an exact version, filename, or hash;
- correct a packaging error through a public amendment.

The coordinator may not:

- explain a normative rule that the public artifacts fail to explain;
- interpret an assessment or case source;
- supply an undocumented command or hidden configuration;
- explain the intended meaning of an error code beyond public documentation;
- repair the auditor's output privately;
- omit a failed task from the published audit.

## Frozen inputs

Before audit activation, the protocol must record:

- exact repository commit;
- implementation-packet digest;
- package and dependency versions;
- required operating environment;
- canonical valid assessment ID and hash;
- invalid-vector IDs and hashes;
- migration input ID and hash;
- comparison input IDs and hashes;
- expected deterministic output hashes;
- public documentation paths.

## Required tasks

### Task 1. Fresh installation

The auditor records the operating system, Python version, dependency installation command, elapsed time, warnings, and failures.

### Task 2. Version reconstruction

Using public artifacts only, the auditor identifies:

- repository release;
- specification version;
- assessment-schema version;
- dimension-catalog version;
- handbook version;
- conformance-engine version;
- research maturity;
- supported historical versions.

### Task 3. Valid assessment

The auditor validates the canonical complete assessment and records the command, exit code, report, and output digest.

### Task 4. Invalid assessments

The auditor validates the declared invalid vectors and explains every error code using the public error catalog. Any code that cannot be explained publicly is a documentation defect.

### Task 5. Rule reconstruction

The auditor describes the public invariants for:

- actor and authority attribution;
- evidence-claim references;
- evidence states and findings;
- Repair trigger;
- sampling and aggregation;
- split Telemetry Integrity;
- overall integrity derivation;
- citation precision;
- component-version compatibility.

The auditor does not decide whether the rules are normatively correct. The task tests whether the rules can be reconstructed.

### Task 6. Migration planning

The auditor generates a migration plan for a preserved `0.1.0` assessment and explains why automatic migration is permitted or prohibited.

### Task 7. Comparison reproduction

The auditor reproduces one public inter-rater comparison, verifies the input hashes, and compares the output digest to the declared expected result.

### Task 8. Adjacent-system boundary

The auditor explains why HIT is a documentary assurance method and does not itself perform runtime governance, signed-receipt verification, policy-pack harmonization, compliance automation, or evidence portability.

### Task 9. Private-knowledge register

The auditor records each point where completion appears to require:

- undocumented author intent;
- hidden configuration;
- an absent artifact;
- an ambiguous rule;
- an unexplained error code;
- a contradictory version statement;
- an inaccessible source;
- a non-reproducible locator;
- a nondeterministic output.

### Task 10. Audit disposition

The auditor assigns one disposition:

- `pass_no_release_blocker`;
- `pass_with_nonblocking_findings`;
- `fail_release_blocking_defect`;
- `invalid_audit_integrity_failure`.

## Publication rule

All task results and failures are published. A failed audit does not disappear when the defect is repaired. The original audit remains preserved and a new audit or amendment records the later result.

## Release consequence

A `fail_release_blocking_defect` or `invalid_audit_integrity_failure` blocks `v0.9.0` promotion and `v1.0.0` release. A passing audit remains bounded to the exact frozen packet, environment, and commit.

## Current activation state

Audit activation is prohibited until the standalone implementation packet, exact hashes, expected outputs, and audit submission schema are final and the exact candidate commit passes validation.
