# Case Study 2: Obermeyer Population-Health Algorithm

**Method:** Human Influence Telemetry 0.1.0  
**Status:** Public review draft for repository release 0.2.0  
**Assessments:** [`assessments/obermeyer-deployers.json`](assessments/obermeyer-deployers.json) and [`assessments/obermeyer-manufacturer.json`](assessments/obermeyer-manufacturer.json)  
**Author:** Mark Julius Banasihan

## Assessment boundary

- **Decision:** selection of patients for additional high-risk care-management attention using an algorithmic risk score.
- **Actors:** deploying health systems and the manufacturer are assessed separately.
- **Evidence cutoff:** 25 October 2019, the publication date of the principal peer-reviewed study and the contemporaneous New York regulatory letter.
- **Evidence boundary:** the *Science* article and public regulatory material. The public sources do not expose a complete institutional decision record.

The actor split is essential. A manufacturer may document a technical reform while deploying institutions leave no public record of evidence access, override, appeal, repair, or workflow change. Combining them would assign one actor's conduct to the entire decision chain.

## Mechanism

The studied system used healthcare cost as a proxy for health need. Because spending and access were unequal, patients with comparable illness could receive different risk rankings. The paper reports that correcting the proxy would increase the share of Black patients receiving additional help from 17.7 percent to 46.5 percent and that a reformulated target reduced measured bias by 84 percent.

HIT does not score the predictive model itself. It asks what the institutional record shows about human evidence access, judgment, authority, correction, repair, and reform around that allocation process.

## Actor A: deploying health systems

| Dimension | Finding | Public-record basis | Material record still missing |
|---|---:|---|---|
| Counsel | `IE` | The study explains the allocation mechanism, not what evidence an enrolling reviewer could access. | Reviewer access logs and evidence packets |
| Judgment | `IE` | No public record distinguishes individualized clinical judgment from routine acceptance of the score. | Clinical rationales, exception records, and disagreement logs |
| Command | `IE` | No public artifact identifies an operative authority to reject, modify, or stop the score-driven path. | Authority matrix and exercised override records |
| Correction | `IE` | The public record does not establish a patient or reviewer contestability channel. | Notice, appeal, escalation, and reversal records |
| Repair | `IE` | No deployer-side remediation record is public. | Identification, review, notification, and remediation of under-selected patients |
| Reform | `IE` | The public record does not show whether deploying institutions changed their workflows. | Suspension, retirement, threshold revision, or workflow-redesign records |

**Dominant pattern:** the public record is rich on model effects and sparse on deployer-side governance. Six `IE` findings are not a scoring failure. They identify the absence of publicly reproducible evidence about the oversight layer.

## Actor B: manufacturer

| Dimension | Finding | Public-record basis | Material record still missing |
|---|---:|---|---|
| Counsel | `IE` | The sources explain the proxy failure but not the evidence considered when cost was selected as the target. | Design-stage evidence register |
| Judgment | `IE` | No public record reconstructs pre-publication deliberation about proxy validity. | Alternatives, dissent, or internal review records |
| Command | `IE` | The public record does not identify who could reject the proxy choice before external intervention. | Internal authority and stop-use records |
| Correction | `IE` | No manufacturer-level channel for contesting an individual score is documented. | Customer or patient challenge and reversal records |
| Repair | `IE` | The technical revision concerns future scoring, not documented remediation of prior allocation effects. | Patient identification and remediation records |
| Reform | `2` | The published record documents a material redesign of the target and a substantial reduction in measured bias. | None required for the finding; trigger provenance remains relevant |

**Dominant pattern:** one documented act of Reform is visible because outside researchers produced the evidence. The broader internal governance record remains unavailable.

## Telemetry Integrity

Both actor assessments return `IE`. The study and regulatory letter have traceable provenance, but they do not establish the completeness, edit authority, independence, tamper evidence, or retention of the operational records used by either actor.

## Rival interpretations

- A reviewer may argue that externally prompted reform should score lower than institution-initiated reform. The current rubric scores whether architecture change occurred, not who triggered it.
- A reviewer may treat the evidence cutoff as too narrow for a deployment-period assessment. The JSON records therefore state explicitly that the date represents a public-evidence cutoff, not the full product lifespan.

## What this case contributes to HIT

1. Multi-actor systems must be assessed by actor rather than averaged into one profile.
2. A near-total `IE` profile can be a discriminating governance result.
3. Reform needs a provenance qualifier distinguishing institution-initiated change from externally forced change.
4. Technical correction does not by itself establish repair for previously affected persons.

## Public sources

- Ziad Obermeyer, Brian Powers, Christine Vogeli, and Sendhil Mullainathan, “Dissecting racial bias in an algorithm used to manage the health of populations,” *Science* 366, no. 6464 (2019): 447–453, <https://doi.org/10.1126/science.aax2342>
- New York State Department of Financial Services and Department of Health, joint letter to UnitedHealth Group, 25 October 2019: <https://www.dfs.ny.gov/reports-and-publications/comment-letters/dfs-doh-joint-letter-uhgi-20191025>

## Limitations

The assessment does not infer that oversight was absent merely because records were not public. It does not characterize the studied system as a direct denial-of-care mechanism. It evaluates the documentary visibility of institutional influence around allocation to additional care-management resources.
