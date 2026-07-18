# HIT Conformance Error Catalog

Error codes are stable machine-facing identifiers for the executable conformance implementation. A report may contain more than one code because one defect can violate both schema and cross-record rules.

| Code | Meaning | Typical repair |
|---|---|---|
| `HIT-SCHEMA` | The record violates the released JSON Schema. | Correct the field, type, enum, required value, or conditional schema state. |
| `HIT-DIMENSION-COVERAGE` | The six substantive dimensions do not each appear exactly once. | Add the missing dimension or remove the duplicate. |
| `HIT-ACTOR-ID-DUPLICATE` | Two actor objects use the same identifier. | Assign a unique stable actor identifier. |
| `HIT-CLAIM-ID-DUPLICATE` | Two evidence claims use the same identifier. | Assign a unique stable claim identifier. |
| `HIT-ACTOR-REFERENCE` | An actor reference points to an actor absent from the record. | Add the actor or correct the reference. |
| `HIT-CLAIM-REFERENCE` | A finding, actor, or integrity component cites an unknown claim. | Add the claim or correct the claim identifier. |
| `HIT-ACTOR-CLAIM-RECIPROCITY` | An actor lists a claim that does not attribute its proposition to that actor. | Correct either the actor evidence list or the claim actor attribution. |
| `HIT-CITATION-OTHER-NOTE` | A locator of type `other` lacks a reproducibility note. | Identify the smallest reproducible unit and explain the locator limitation. |
| `HIT-FINDING-STATE` | A finding is inconsistent with its evidence state. | Apply the published `0/1/2/IE` to evidence-state mapping. |
| `HIT-DETERMINATE-SUPPORT` | A determinate `0`, `1`, or `2` has no supporting claim. | Cite at least one supporting evidence proposition. |
| `HIT-IE-PROPOSITION` | `IE` lacks the unresolved proposition. | State the proposition that the evidence cannot resolve. |
| `HIT-IE-SEARCH` | `IE` lacks the search or request record. | Record what was requested or searched and why the evidence remains insufficient. |
| `HIT-CLAIM-RELATION` | A claim is cited as support, contradiction, or limitation under the wrong relation. | Align the claim relation with the reference list. |
| `HIT-CLAIM-DIMENSION` | A cited claim does not declare the dimension it is used to assess. | Add the dimension only when a distinct proposition and reasoning path support that use. |
| `HIT-REPAIR-TRIGGER` | An indeterminate Repair trigger coexists with a determinate finding. | Use Repair `IE` until the harm trigger is resolved. |
| `HIT-REPAIR-CAPABILITY` | Repair `2` is claimed without a triggered event or tested-capability basis. | Supply tested or previously exercised repair capability, or lower the finding. |
| `HIT-NONREPAIR-TRIGGER` | A non-Repair dimension carries a Repair trigger. | Set `repair_trigger` to `not_applicable`. |
| `HIT-INTEGRITY-DERIVATION` | Overall Telemetry Integrity does not follow `unreliable > IE > limited > adequate`. | Recompute the overall value from both component statuses. |
| `HIT-AGGREGATION-SCOPE` | Assessment scope and aggregation mode conflict. | Use event-specific aggregation for an event assessment and a period-compatible rule for a period assessment. |

The catalog describes implementation findings, not legal violations or empirical conclusions.
