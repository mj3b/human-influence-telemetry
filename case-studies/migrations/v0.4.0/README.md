# HIT v0.4.0 Public-Case Migration Dispositions

The four public case assessments released under HIT specification and schema `0.1.0` remain immutable historical artifacts.

Version `0.4.0` changes the assessment contract materially. It adds evidence states, structured evidence propositions and locators, an actor-authority matrix, a Repair trigger, explicit sampling and aggregation, and two Telemetry Integrity components. Existing findings are therefore not relabeled or copied into the candidate schema without a fresh source review.

`migration-manifest.json` records one explicit disposition for every released assessment:

- `historical_version_bound`: the original remains a valid historical `0.1.0` artifact, but no `0.4.0` candidate record is claimed;
- `deferred_locked_protocol`: migration is prohibited until the locked human protocol has published its original result.

These dispositions are release exceptions, not evidence that the cases conform to the candidate contract. They preserve historical findings and prevent silent reinterpretation.
