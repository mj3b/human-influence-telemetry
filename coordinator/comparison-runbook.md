# Coordinator Comparison Runbook

This directory is coordinator-only. Do not include it in either scorer packet.

## 1. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jsonschema
```

On Windows PowerShell, activate with:

```powershell
.venv\Scripts\Activate.ps1
```

## 2. Run the synthetic self-test

Validate both vectors:

```bash
python scripts/validate_scorer_submission.py validation/test-vectors/rater-a.json
python scripts/validate_scorer_submission.py validation/test-vectors/rater-b.json
```

Generate JSON:

```bash
python scripts/compare_raters.py \
  validation/test-vectors/rater-a.json \
  validation/test-vectors/rater-b.json \
  --format json \
  --output validation/results/synthetic-comparison.json
```

Generate Markdown:

```bash
python scripts/compare_raters.py \
  validation/test-vectors/rater-a.json \
  validation/test-vectors/rater-b.json \
  --format markdown \
  --output validation/results/synthetic-comparison.md
```

Expected result:

- exact agreement: `6 / 7`
- exact-agreement proportion: `0.8571`
- critical disagreements: `0`
- substantive-dimension Cohen's kappa: `0.76`
- advancement threshold met: `yes`

The vectors are synthetic and create no empirical reliability claim.

## 3. Receive one human submission

Copy the unchanged file into a private working directory. Do not commit it publicly while waiting for the second scorer.

Validate it:

```bash
python scripts/validate_scorer_submission.py HIT-IR-SCORER-A.json
```

Create a receipt:

```bash
python scripts/record_submission.py \
  HIT-IR-SCORER-A.json \
  --received-at 2026-07-16T19:30:00-04:00 \
  --output HIT-IR-SCORER-A.receipt.json
```

Repeat separately for Scorer B.

Do not disclose the first submission while waiting for the second.

## 4. Generate the pre-adjudication result

After both original files are locked and validated:

```bash
python scripts/compare_raters.py \
  HIT-IR-SCORER-A.json \
  HIT-IR-SCORER-B.json \
  --format json \
  --output pre-adjudication-comparison.json
```

```bash
python scripts/compare_raters.py \
  HIT-IR-SCORER-A.json \
  HIT-IR-SCORER-B.json \
  --format markdown \
  --output pre-adjudication-comparison.md
```

The script uses `--format` and `--output`. It does not support `--json-output` or `--markdown-output`.

## 5. Interpret exit codes

- `0`: inputs were valid and comparison completed.
- `1`: returned only when `--require-threshold` is used and the valid comparison failed the advancement threshold.
- `2`: invalid input, schema failure, missing source access, or another comparison error.

A threshold failure is a valid research result. Do not treat exit code `1` as corrupt data.

## 6. Preserve before adjudication

Before discussion:

1. preserve both original submissions;
2. preserve both receipt files;
3. preserve the JSON and Markdown comparisons;
4. record the comparison command and software commit;
5. verify that neither scorer changed a finding after disclosure.

## 7. Adjudicate

Copy `validation/adjudication-template.md` into the results directory.

Classify every disagreement using `validation/disagreement-taxonomy.md`.

Adjudication may explain disagreement and propose later changes. It may not:

- overwrite either original submission;
- recalculate the pre-adjudication result after changing scores;
- downgrade a mechanically critical disagreement;
- suppress a failing result.

## 8. Publication

The result branch should contain:

- original submissions;
- receipts and SHA-256 digests;
- deterministic comparison outputs;
- disagreement register;
- adjudication record;
- claim and maturity decision;
- updated repository documentation.

Release `v0.3.0` whether the exercise passes or fails.
