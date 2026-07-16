# HIT Disagreement Taxonomy

This taxonomy classifies why two scorers reached different findings. It does not convert disagreement into agreement or determine which scorer is correct.

A disagreement may receive more than one category.

| Code | Category | Diagnostic question | Typical repair target |
|---|---|---|---|
| `D-EVIDENCE-SELECTION` | Evidence selection | Did scorers rely on different packet sources or different parts of the same source? | Source-use instructions or evidence index |
| `D-EVIDENCE-WEIGHT` | Evidentiary weight | Did scorers assign different weight to reporting, response statements, allegations, or a procedural ruling? | Evidentiary-tier rule |
| `D-BOUNDARY` | Assessment boundary | Did scorers evaluate different periods, actors, decisions, or workflow stages? | Boundary definition |
| `D-CONSTRUCT` | Construct interpretation | Did scorers understand Counsel, Judgment, Command, Correction, Repair, Reform, or Telemetry Integrity differently? | Specification or handbook |
| `D-ZERO-IE` | `0` versus `IE` | Did one scorer infer absence while the other treated the record as unable to distinguish absence from missing evidence? | Explicit absence rule |
| `D-ZERO-ONE` | `0` versus `1` | Did scorers differ on whether de jure form or ceremonial capacity remained observable? | Ceremonial-presence rule |
| `D-ONE-TWO` | `1` versus `2` | Did scorers differ on whether the evidence showed exercised practical effect rather than formal capacity? | Minimum evidence for `2` |
| `D-ZERO-TWO` | `0` versus `2` | Did scorers reach opposite conclusions about substantive capacity? | Critical rubric or evidence review |
| `D-INTEGRITY` | Telemetry Integrity | Did scorers differ on completeness, independence, provenance, tamper evidence, edit authority, or retention? | Integrity-status guidance |
| `D-SAMPLING` | Sampling inference | Did one scorer generalize from a limited instance or fail to separate process evidence from population inference? | Sampling guidance |
| `D-TEMPORAL` | Temporal inference | Did scorers treat later correction or reform as evidence about the earlier decision period? | Time-window rule |
| `D-ACTOR` | Actor attribution | Did scorers assign vendor, reviewer, insurer, regulator, or court conduct to the wrong institutional actor? | Actor decomposition |
| `D-CLERICAL` | Clerical or schema error | Was the mismatch caused by transcription, invalid JSON, duplicate dimensions, or a wrong source ID? | Submission correction |
| `D-OTHER` | Other | Is the disagreement not represented above? | New category with explanation |

## Criticality rule

The comparison tool identifies mechanically critical disagreements. The adjudication record may identify additional substantive importance, but it may not downgrade a mechanically critical disagreement merely to satisfy the advancement threshold.

## Required disagreement record

For every nonmatching item, record:

- dimension;
- scorer A finding;
- scorer B finding;
- mechanical criticality;
- one or more taxonomy codes;
- evidence passages or source IDs driving the difference;
- adjudicator analysis;
- whether a method change is proposed;
- proposed target version for that change.
