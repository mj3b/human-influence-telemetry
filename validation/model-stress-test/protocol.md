# HIT Model-based Rubric Stress-Test Protocol

**Protocol ID:** `HIT-MST-CIGNA-001`  
**Protocol version:** `1.0.0`  
**Related human protocol:** `HIT-IRP-CIGNA-001`  
**Packet:** `HIT-IR-CIGNA-PXDX-001`  
**Method under test:** HIT specification and assessment schema `0.1.0`

## 1. Research question

When two fresh language-model sessions independently apply HIT to the same frozen Cigna PxDx packet, where do their findings, rationales, and evidence use converge or diverge?

## 2. Design

Use two fresh model sessions. Prefer distinct model families or providers when available. Each session must:

1. begin without prior conversation context;
2. receive the same system-neutral task prompt;
3. receive the same HIT specification, handbook, decision boundary, source manifest, and source texts or stable archived copies;
4. have no access to the author's Cigna findings;
5. have no access to the other model's output;
6. return one schema-valid submission.

Record the model name, version or product label, provider, run date, access mode, and relevant settings.

## 3. Contamination rule

A session is contaminated when it has been exposed to the author's scores, prior discussion of a designed disagreement, another model's output, or substantive author coaching.

Contaminated outputs may be retained as demonstrations but must not be presented as protocol-conforming results.

## 4. Comparison

Compare:

- exact findings across six substantive dimensions and Telemetry Integrity;
- evidence references;
- rationale differences;
- `0` versus `IE` use;
- boundary adherence;
- unsupported legal or causal claims;
- hallucinated evidence;
- confidence or uncertainty language.

The human protocol's six-of-seven threshold may be reported descriptively for comparison, but it has no maturity consequence in this model exercise.

## 5. Publication

Publish both original outputs, run metadata, the comparison, disagreement classification, contamination assessment, and limitations.

## 6. Interpretation boundary

The result is an exploratory rubric stress test. It is not a human reliability study, legal analysis, certification, or validation of HIT.
