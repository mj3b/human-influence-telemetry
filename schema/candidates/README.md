# HIT Candidate Data Contracts

This directory contains development contracts that are not part of the current released HIT schema.

## v0.4.0 candidate

- `hit-assessment-0.4.0-candidate.schema.json` — candidate JSON Schema;
- `hit-dimension-catalog-0.4.0-candidate.json` — candidate machine-readable rubric catalog;
- `hit-assessment-0.4.0-candidate.example.json` — canonical synthetic example.

The candidate contract implements the design approved in `ADR-0002` and the candidate specification.

It adds:

- evidence-state classification;
- structured evidence claims and locators;
- actor-authority attribution;
- sampling and aggregation declarations;
- Repair trigger states;
- separate institutional-record and assessment-packet integrity;
- deterministic overall Telemetry Integrity;
- migration declarations.

The released `schema/hit-assessment.schema.json` and `schema/hit-dimension-catalog.json` remain at `0.1.0` until the candidate contract, boundary fixtures, validator, case migrations, and release metadata are complete.

Run candidate validation with:

```bash
python scripts/validate_v040_candidate.py
```

A passing candidate validation does not establish human inter-rater reliability, field effectiveness, legal compliance, certification, or independent adoption.
