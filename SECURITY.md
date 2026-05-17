# Security Policy

## Supported Versions

Security updates are provided for the actively maintained `main` branch and the latest tagged workflow-template release.

| Version | Supported |
| --- | --- |
| `main` | Yes |
| latest stable release | Yes |
| older releases | No |

## Reporting a Vulnerability

Please do not open public issues for workflow-template vulnerabilities.

Report privately through GitHub private vulnerability reporting if enabled, or contact the maintainer directly.

Please include:

- affected workflow template or reusable workflow
- risky permission, secret, dependency, or deployment behavior
- reproduction steps
- expected secure behavior
- suggested fix, if available

## Scope

In scope:

- excessive `GITHUB_TOKEN` permissions
- unsafe pull request workflow triggers
- secrets exposed to untrusted forks
- unpinned third-party Actions in sensitive workflows
- deployment workflows using long-lived credentials where OIDC is possible
- missing security scanning in reusable CI/CD templates

Out of scope:

- downstream repositories that modified templates after copying them
- cosmetic workflow changes without security impact
- denial-of-service issues without a practical exploit path

## Security Expectations

- Default to `permissions: contents: read`.
- Grant write permissions only per job when needed.
- Prefer GitHub Actions OIDC over long-lived cloud credentials.
- Pin sensitive third-party Actions by commit SHA.
- Never echo secrets or deployment credentials in logs.
