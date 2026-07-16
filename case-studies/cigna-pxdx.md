# Case Study 3: Cigna PxDx Claims-Review System

**Method:** Human Influence Telemetry 0.1.0  
**Status:** Public review draft for repository release 0.2.0  
**Assessment:** [`assessments/cigna-pxdx.json`](assessments/cigna-pxdx.json)  
**Author:** Mark Julius Banasihan

## Assessment boundary

- **Decision:** post-service determination that a submitted claim was not medically necessary using the PxDx procedure-to-diagnosis review workflow.
- **Institutional unit:** Cigna Corporation and Cigna Health and Life Insurance Company.
- **Period:** reported 2022 activity through the federal court order entered 31 March 2025.
- **Evidence boundary:** investigative reporting, Cigna's reported response, and the pleading-stage federal court order in *Kisting-Leung v. Cigna Corp.*
- **Terminology:** PxDx is described here as an algorithmic claims-review workflow. The assessment does not depend on classifying it as machine-learning AI.

Investigative reporting is treated as reporting. Allegations are treated as allegations. The court order is treated as a procedural ruling on a motion to dismiss, not as a merits judgment.

## Findings

| Dimension | Finding | Public-record basis | Material record still missing |
|---|---:|---|---|
| Counsel | `0` | Reporting based on internal spreadsheets and former-employee interviews describes denials processed without opening individual patient files. | Sampled file-access logs showing what each medical director opened before disposition |
| Judgment | `0` | Reporting describes batch sign-off; the court allowed a fiduciary-duty theory based on algorithmic delegation to proceed at the pleading stage. | Individual medical-director rationales showing patient-specific clinical judgment |
| Command | `0` | Reported throughput controls and batch processing are affirmative evidence that formal physician authority did not operate as individualized command in the described workflow. | Override, rejection, and stop-use records |
| Correction | `1` | Formal appeal and external-review mechanisms existed, with some evidence of individual effect but no demonstrated effect at scale. | PxDx-specific appeal, reversal, and interruption records |
| Repair | `IE` | No public artifact establishes systemic remediation for claims processed through PxDx. | Affected-claim identification, corrected records, reimbursement, notification, and named ownership |
| Reform | `0` | The assessed record includes continued defense of the workflow and no demonstrated architecture change through the evidence cutoff. | Authorized revision, suspension, or retirement records |

**Dominant pattern:** the visible record indicates compressed evidence access, judgment, and command; contestability remains mainly formal; systemic repair is not publicly reconstructable.

## Designed disagreement

Command is intentionally retained as an inter-rater test item.

- **Case for `0`:** the reported speed, batch workflow, and productivity controls are affirmative evidence that individualized authority was not practically operative.
- **Case for `1`:** licensed medical directors retained de jure authority and signatures, even where the workflow rendered that authority ceremonial.

The current assessment applies the handbook's downward ambiguity rule and records `0`. A second scorer may reasonably choose `1`. The disagreement should be measured, categorized, and adjudicated under the future inter-rater protocol.

Reform also contains a rival interpretation. A scorer may prefer `IE` because no public change record cannot prove no internal change occurred. The present `0` rests on the combination of continued public defense and no demonstrated architecture change within the bounded record.

## Telemetry Integrity

**Finding: `IE`.** The reporting and court order have traceable provenance, but the underlying operational record is incomplete and institution-controlled. Public sources do not provide a representative set of claim files, access logs, rationales, overrides, appeal outcomes, edit permissions, tamper controls, or retention records.

The process is legible because journalism, litigation, and regulatory scrutiny forced parts of the record into public view. That is different from an institution maintaining independent, audit-ready telemetry as a normal governance control.

## What this case contributes to HIT

1. It distinguishes human signature from evidence of counsel, judgment, and command.
2. It provides a designed disagreement for inter-rater testing.
3. It shows why litigation artifacts need an evidentiary tier: allegation, pleading-stage plausibility, or merits judgment.
4. It demonstrates that low `IE` frequency may reflect externally forced disclosure rather than strong institutional telemetry.

## Public sources

- Patrick Rucker of The Capitol Forum, with Maya Miller and David Armstrong of ProPublica, “How Cigna Saves Millions by Having Its Doctors Reject Claims Without Reading Them,” 25 March 2023: <https://www.propublica.org/article/cigna-pxdx-medical-health-insurance-rejection-claims>
- ProPublica follow-up reporting Cigna's response and regulatory scrutiny, 25 April 2023: <https://www.propublica.org/article/cigna-health-insurance-denials-pxdx-congress-investigation>
- *Kisting-Leung v. Cigna Corp.*, No. 2:23-cv-01477-DAD-CSK, order granting in part and denying in part the motion to dismiss, E.D. Cal., 31 March 2025, docket 55: <https://docs.justia.com/cases/federal/district-courts/california/caedce/2%3A2023cv01477/431351/55>

## Limitations

The assessment does not establish that Cigna violated law, that every PxDx decision followed the reported pattern, or that the reporting is equivalent to an institutional audit. The court order addresses pleading sufficiency and does not resolve liability. The period start is a conservative boundary derived from reported 2022 activity rather than a claim about the exact system launch date.
