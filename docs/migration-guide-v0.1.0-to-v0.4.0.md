# Migration Guide: HIT 0.1.0 to 0.4.0

## Migration principle

Migration is a fresh bounded reassessment, not a schema-only transformation. Preserve the original `0.1.0` file unchanged and create a separate `0.4.0` record.

## Required sequence

1. Preserve the historical file and record its Git blob SHA.
2. Reconfirm the institutional unit, decision process, period, scope, and sample.
3. Declare the aggregation rule before reviewing findings.
4. Build the actor-authority matrix.
5. Rewrite every material citation as a bounded evidence proposition with a precise locator and relation.
6. Classify the evidence state for each substantive dimension.
7. Reapply the `0`, `1`, `2`, and `IE` rules without carrying forward the old finding by default.
8. Determine the Repair trigger separately.
9. Assess institutional-record and assessment-packet integrity separately and derive the overall status.
10. Record contradictions, reused evidence, limitations, exclusions, and selection effects.
11. Validate the new record against the `0.4.0` schema.
12. Publish a migration comparison that identifies every changed field and finding.

## Prohibited shortcuts

Do not:

- replace `schema_version` and retain the old body;
- convert every old `0` to `IE` mechanically;
- preserve an old `2` without testing the new operational-capability threshold;
- infer actor relationships from corporate affiliation alone;
- reuse a source across dimensions without separate propositions;
- combine the two integrity components;
- overwrite or delete the historical assessment.

## Current public cases

The migration manifest provides explicit release exceptions for all four released assessments. Three remain `historical_version_bound`. Cigna is `deferred_locked_protocol` until the locked human exercise publishes its original result.

## Result-release versioning

Historical references to a planned `v0.3.0` human-result release are superseded. When the locked exercise is completed, its package must use the next available repository version and preserve the original protocol identity.
