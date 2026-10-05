# Local ATS Auditor Project Plan

## Objective

Build a privacy-preserving resume quality tool that produces auditable evidence instead of a proprietary black-box score. The first release supports this job-search framework; later releases can become a public portfolio project after privacy and security review.

## Phase 1 Implemented

- Local PDF and DOCX text extraction.
- Standard-section and contact-field checks.
- DOCX table, text-box, header, footer, image, and minimum-font checks.
- PDF page and text-extraction checks.
- Reverse-chronological experience validation.
- Bullet action, quantification, length, and placeholder checks.
- Deterministic job-keyword coverage.
- JSON and Markdown reports.
- Unit tests for the core rules.

## Phase 2 Next

- Add a curated role-family vocabulary with aliases and proficiency boundaries.
- Add batch comparison across master resume variants.
- Import one job directly from the local application ledger by job ID. **Implemented.**
- Store scan results and resume hashes in the SQLite audit trail.
- Add regression fixtures for Greenhouse, Lever, Ashby, and Workday extraction behavior.

## Phase 3 Portfolio Release

- Add a small local web interface with no network requests.
- Add side-by-side extracted-text and rendered-page views.
- Add reproducible example resumes and job descriptions containing synthetic data only. **Implemented.**
- Add CI, packaging, documentation, and a public security statement. **Implemented.**
- Add screenshots after the local interface exists.
- Publish only after checking the repository for personal information and employer-confidential material. **Privacy review completed for the initial release.**

## Success criteria

- Every warning names the evidence and the corrective action.
- The scanner never rewrites or invents resume claims.
- The same input produces the same report.
- A resume with missing text, contact details, sections, or reverse chronology fails the strict check.
- No resume or job text leaves the machine.
