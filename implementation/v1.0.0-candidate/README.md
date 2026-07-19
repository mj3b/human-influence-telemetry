# HIT v1.0.0 Candidate Implementation Packet

**Status:** Candidate, incomplete  
**Target release path:** `v0.9.0` clean-room release candidate, then `v1.0.0` stable contract  
**Private explanation permitted:** No

## Purpose

This directory defines the standalone public packet that a technically competent external implementer must be able to use without private author explanation.

The packet is complete only when every listed artifact is copied or referenced at an exact validated commit and the clean-room audit protocol can be executed from a fresh environment.

## Required normative artifacts

- `SPECIFICATION.md`;
- `docs/application-handbook.md`;
- `schema/hit-assessment.schema.json`;
- `schema/hit-dimension-catalog.json`;
- `docs/adjacent-system-boundaries.md`;
- current compatibility manifest;
- migration guide;
- current claim register and limitations.

## Required implementation artifacts

- public package entry point;
- conformance command documentation;
- migration-plan command documentation;
- stable error-code catalog;
- one canonical valid complete assessment;
- invalid complete-assessment vectors;
- boundary fixtures;
- deterministic comparison example;
- expected output digests;
- installation and environment instructions.

## Auditor tasks

The auditor must, without private explanation:

1. install the package in a fresh environment;
2. identify the current specification, schema, catalog, handbook, and engine versions;
3. validate one complete conforming assessment;
4. run at least three invalid vectors and explain every returned error code;
5. identify the actor, evidence-claim, finding, Repair-trigger, sampling, aggregation, and Telemetry Integrity invariants;
6. generate a migration plan for one preserved `0.1.0` assessment;
7. reproduce one deterministic inter-rater comparison from public inputs;
8. distinguish HIT from runtime governance, signed-receipt verification, policy-pack harmonization, compliance automation, and evidence portability;
9. record every point where the public packet is ambiguous, incomplete, or requires private author knowledge;
10. produce a signed audit record with environment details, commands, outputs, and unresolved defects.

## Evidence boundary

A clean-room audit evaluates public implementability and documentation sufficiency. It does not establish inter-rater reliability, evidence truth, causal effectiveness, legal correctness, certification, or institutional adoption.

## Current stop condition

The packet remains incomplete until:

- the current-contract application path is resolved;
- final target component versions are selected;
- exact artifact hashes are recorded;
- the comparison implementation and reproducible example are final;
- the audit protocol is run by an independent external reviewer;
- every release-blocking defect is repaired or explicitly accepted.
