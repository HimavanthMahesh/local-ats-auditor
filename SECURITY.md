# Security and Privacy

## Supported versions

The latest commit on `main` is the supported development version. This project is an early portfolio release and has not undergone an independent security audit.

Local ATS Auditor performs no network requests and includes no analytics, telemetry, credentials, or model-provider integration.

Resume and job-description inputs can contain sensitive personal information. Keep generated reports local, review files before committing them, and never publish real candidate data without the candidate's explicit approval. The default `.gitignore` excludes the `reports/` directory.

## Reporting a vulnerability

Use the repository's **Security > Report a vulnerability** flow. Do not include a real resume, credentials, or private job-application data in a public issue.
