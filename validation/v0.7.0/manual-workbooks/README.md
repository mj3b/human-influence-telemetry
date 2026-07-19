# HIT v0.7.0 Manual Scorer Workbooks

**Protocol:** `HIT-IRP-HIT040-002`  
**Workbook version:** `0.1.0-draft`  
**Assessment contract:** `0.4.0`  
**Conformance engine:** `0.5.0`  
**Status:** Draft, scoring prohibited

## Purpose

This directory records the manual-workbook contract and exact candidate-asset hashes for three future independent scorers. The DOCX and PDF files are candidate release assets. They are not active scorer packets and are not committed as normative repository files.

Each scorer-specific workbook contains:

- activation controls and receipt fields;
- eligibility, independence, conflict, and tool-use declarations;
- a concise finding, evidence-state, Repair-trigger, and Telemetry Integrity reference;
- three complete manual assessment sections;
- boundary confirmation;
- frozen source-access log;
- actor and authority roster;
- proposition-level evidence-claim register;
- six substantive dimension records;
- institutional-record and assessment-packet integrity records;
- file and hash register;
- final attestation and transcription verification.

## Candidate assets

The candidate asset set contains:

- one DOCX and one PDF for `HIT-SCORER-A`;
- one DOCX and one PDF for `HIT-SCORER-B`;
- one DOCX and one PDF for `HIT-SCORER-C`;
- one unassigned master DOCX and PDF template;
- one machine-readable manifest;
- one ZIP bundle containing the full set.

Exact file sizes and SHA-256 hashes are recorded in `candidate-assets-manifest.json`.

## Activation boundary

The workbooks may be distributed for substantive scoring only when all conditions hold:

1. protocol `HIT-IRP-HIT040-002` has status `locked`;
2. the machine-readable lock states `scoring_permitted: true`;
3. exactly three packet IDs and versions are fixed;
4. each packet has a frozen decision boundary and source manifest;
5. each source is archived or has an approved stable identifier;
6. final scorer and coordinator instructions exist;
7. deterministic comparison code and synthetic vectors pass;
8. the exact release commit passes repository validation;
9. release `v0.7.0` is published.

Until then, every workbook must retain the visible label `DRAFT - SCORING PROHIBITED`.

## Finalization procedure

After the human case-selection record is signed and packets are frozen:

1. replace Packet 1, Packet 2, and Packet 3 placeholders with immutable packet IDs, versions, digests, decision-boundary paths, and source-manifest paths;
2. update the workbook version from `0.1.0-draft` to a locked version;
3. render every DOCX and inspect every page;
4. create print-ready PDFs from the exact locked DOCX files;
5. hash every file;
6. update the release-asset manifest;
7. validate that scorer-specific copies differ only in scorer public ID and document-level binary metadata;
8. publish the locked ZIP as a `v0.7.0` release asset.

## Preservation

The coordinator preserves the exact distributed workbook hash for each scorer. On receipt, the coordinator preserves the scorer's original working record unchanged. A later JSON transcription must be verified by the scorer and may correct transcription only. It may not replace or revise the original substantive judgment.

## Research boundary

These draft workbooks establish procedural readiness. They do not establish case selection, packet validity, independent application, inter-rater reliability, H3 replication, Maturity Level 3, legal correctness, or institutional adoption.
