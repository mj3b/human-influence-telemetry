# Security Policy

## Supported versions

Security and integrity fixes are applied to the current working specification and the latest tagged release.

| Version | Supported |
|---|---|
| `main` | Yes |
| Latest tagged release | Yes |
| Earlier pre-release versions | Best effort |

## Reporting a vulnerability

Do not publish an exploit, sensitive institutional record, private decision data, or credential in a public issue.

Report vulnerabilities through GitHub private vulnerability reporting when it is enabled for this repository. When that channel is unavailable, contact the maintainer privately through the contact method listed on the maintainer's GitHub profile.

Include:

- affected version or commit;
- affected file, schema field, validator, workflow, or documentation rule;
- reproduction steps;
- expected and observed behavior;
- impact on integrity, confidentiality, availability, or evidentiary reliability;
- proposed mitigation, when known.

## Relevant vulnerability classes

This project is especially concerned with:

- schema bypasses that accept structurally invalid assessments;
- duplicate or omitted dimension findings that pass validation;
- path traversal or unsafe file handling in reference tooling;
- workflow dependency compromise;
- tampering with fixtures, provenance, or release metadata;
- misleading evidence-integrity claims;
- publication of confidential or personally identifying case material;
- silent version drift among the specification, schema, fixtures, and citation metadata.

## Response process

The maintainer will acknowledge a sufficiently detailed report, assess severity, determine whether coordinated disclosure is required, and prepare a tested correction. No fixed response-time guarantee is made during the working-specification phase.

A security fix does not by itself establish that HIT is suitable for high-stakes deployment. Implementers remain responsible for their own threat model, access controls, retention, privacy, and audit architecture.
