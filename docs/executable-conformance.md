# Executable Assessment Conformance

HIT executable conformance engine version `0.5.0` evaluates whether a complete assessment record satisfies the released contract `0.4.0`: specification, schema, catalog, handbook, and cross-record consistency rules.

## Commands

Validate the repository and all deterministic suites:

```bash
python -m src conformance --all
```

Validate one complete `0.4.0` assessment:

```bash
python -m src conformance --path assessment.json
```

Produce a JSON report:

```bash
python -m src conformance \
  --path assessment.json \
  --format json \
  --output hit-conformance-report.json
```

Produce a non-mutating plan for reconstructing a historical `0.1.0` assessment under `0.4.0`:

```bash
python -m src migration-plan \
  --path case-studies/assessments/toeslagenaffaire-harm-period.json
```

`python -m src.cli` remains a compatible direct harness invocation, but `python -m src` is the public package entry point.

## Exit codes

- `0`: the requested validation or migration-plan operation succeeded;
- `1`: the assessment is nonconforming, the repository suite failed, or the migration source is unsupported;
- `2`: argument parsing failed before evaluation.

## Validation layers

The assessment command performs:

1. JSON Schema validation;
2. exact six-dimension coverage;
3. identifier uniqueness;
4. actor, related-actor, and evidence-claim reference checks;
5. actor-to-claim attribution reciprocity;
6. claim relation and dimension checks;
7. finding-to-evidence-state checks;
8. determinate-support and `IE` documentation checks;
9. Repair-trigger checks;
10. Telemetry Integrity derivation;
11. scope and aggregation checks;
12. citation handling for nonstandard locators.

The repository command additionally runs the `0.5.0` release validator, the compatibility-manifest check, sixteen complete-record cases, report-determinism tests, protected migration plans for all four historical assessments, and the existing 48 isolated rubric-boundary fixtures.

## Determinism

Repository reports contain no runtime timestamp. Cases are ordered by `case_id`; issues are ordered by severity, code, path, and message. Derived records receive SHA-256 digests over canonical JSON. Two executions over identical inputs must produce byte-identical JSON.

## Compatibility

The conformance engine fully supports specification, schema, and catalog `0.4.0`. Contract `0.1.0` is supported only for historical validation and non-mutating migration planning. Automatic conversion from `0.1.0` to `0.4.0` is prohibited because the later contract requires evidence states, actor decomposition, structured evidence propositions, a Repair trigger, explicit aggregation, and split Telemetry Integrity.

See [`../compatibility/hit-compatibility-manifest.json`](../compatibility/hit-compatibility-manifest.json).

## Interpretation boundary

A passing report establishes assessment-contract conformance for the supplied record. It does not establish that the underlying evidence is truthful, complete, legally sufficient, or correctly interpreted. It does not establish human inter-rater reliability, legal compliance, certification, institutional effectiveness, runtime enforcement, signed-receipt verification, or evidence portability.
