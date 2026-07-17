# DOI Readiness Plan Through 31 July 2026

## Objective

Archive a citable HIT software release before 31 July 2026 without weakening the locked human protocol or overstating maturity.

## Release choice

Use repository version `0.2.1`.

This is a non-breaking maintenance and research-readiness release. It preserves `v0.3.0` for the eventual human inter-rater result and keeps the specification, schema, and dimension catalog at version `0.1.0`.

## Required sequence

1. Merge the `v0.2.1` release-preparation pull request.
2. Confirm CI passes on the exact `main` commit.
3. Create tag `v0.2.1` from that commit.
4. Publish GitHub release `Human Influence Telemetry v0.2.1`.
5. Confirm the repository is enabled in Zenodo's GitHub integration before publishing.
6. Wait for Zenodo processing.
7. Verify both the software concept DOI and version DOI.
8. Create a dedicated DOI-recording pull request.
9. Add the verified DOI badge and citation identifiers.
10. Do not move or recreate the tag after archival.

## Contingencies

- Processing: wait and recheck.
- Failed: diagnose the exact Zenodo error before changing repository metadata.
- Disabled: enable the repository and synchronize.
- Missing release entry: retain the tag, recreate only the GitHub release object, and select the existing tag.
- Do not create a new semantic version solely to retrigger a webhook.
- Do not invent or prepopulate a DOI.

## Research boundary

A DOI establishes archival identity for the software release. It does not establish inter-rater reliability, Maturity Level 2, certification, legal conformity, or institutional adoption.
