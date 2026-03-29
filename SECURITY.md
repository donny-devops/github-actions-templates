# Security Policy for github-actions-templates

This policy covers the github-actions-templates repository, which provides reusable GitHub Actions workflows, composite actions, and CI/CD templates for secure DevOps pipelines. Security is paramount for workflows handling builds, deploys, and secrets.

## Supported Versions

Templates are actively maintained on the `main` branch. Use pinned commits/tags for production. Older branches receive security updates only.

| Branch/Tag | Supported          |
|------------|--------------------|
| `main`     | ✅ Yes             |
| `*` tags   | ✅ Yes (pinned)    |
| Others     | ❌ No              |

## Reporting a Vulnerability

Report responsibly to maintain trust in these templates:

- **Preferred**: Open a private [security advisory](https://github.com/donny-devops/github-actions-templates/security/advisories/new) on GitHub. This creates a draft advisory for triage/fix before public disclosure.
- **Email**: donny.dev@outlook.com for sensitive issues.
- **Do not**: Open public issues/PRs for vulns; file in other repos using these templates.

We triage within 7 days, aim for patches in 30 days, and coordinate disclosure.

## Security Expectations for Users

When forking/using these templates:

- Set repo Actions to **read-only** default permissions (Settings > Actions > General). [web:13]
- Pin third-party actions to full SHA (e.g., `actions/checkout@692973e3`), allowlist in org settings. [web:13][web:16]
- Use OIDC for cloud auth; never hardcode secrets. Environment secrets with required reviews for prod. [web:13][web:20]
- Avoid `pull_request_target`; run sensitive jobs only on `main` post-review. Require branch protection with status checks. [web:20]
- Enable CodeQL/dependency review in workflows; use Scorecard action. [web:11]
- Self-hosted runners: Ephemeral, private repos only. [cite:5]

## Scope and Disclaimers

This applies only to templates in this repo. Vulnerabilities in downstream user workflows (e.g., secret misconfigs) are user responsibility. No warranties; use at own risk.
