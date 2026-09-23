# ⚙️ GitHub Actions Templates

> A curated collection of production-ready GitHub Actions workflow templates for DevOps automation — security scanning, Docker CI/CD, Terraform IaC, AWS OIDC deployment, Kubernetes Helm releases, database migrations, static site deployments, and more.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![YAML](https://img.shields.io/badge/YAML-CB171E?logo=yaml&logoColor=white)](https://yaml.org/)

---

## 📋 Overview

This repository provides reusable, drop-in GitHub Actions workflow templates designed for real-world DevOps pipelines. Each template is thoroughly commented, adheres to least-privilege security permissions, follows CI/CD best practices, and is ready to be adapted with minimal configuration.

Templates cover seven core domains:
- 🔒 **Security & SecOps** — secrets scanning, dependency vulnerabilities, license compliance, CodeQL advanced static analysis, and PagerDuty/SIEM failure alerting
- 🐳 **Containers & Cloud** — Docker multi-platform builds, keyless AWS OIDC deployment, Kubernetes Helm releases
- 🏗️ **Infrastructure as Code** — Terraform / OpenTofu speculative plan commenting and automated apply
- 🗄️ **Database** — environment-aware schema migration automation
- 🚀 **Deployment & Releases** — static site publishing, automated semantic releases & changelogs
- 🔑 **Authentication** — GitHub OAuth app authorization verification
- 🧹 **Maintenance & Automation** — stale issue management
- 🧭 **AgentOps Foundation** — reusable fleet quality gates for Python, Node, Terraform, Docker, and package validation

---

## 📁 Template Catalog

| Template | File | Trigger | Description |
|---|---|---|---|
| 🔐 Secrets Scanner | [`secrets-scanner.yml`](templates/secrets-scanner.yml) | Push, PR | Scans codebase for accidentally committed secrets, tokens, and credentials |
| 🛡️ Dependency Vulnerability Checker | [`dependency-vulnerability-checker.yml`](templates/dependency-vulnerability-checker.yml) | Push, PR, Schedule | Audits project dependencies for known CVEs and security advisories |
| 📜 License Compliance Checker | [`license-compliance-checker.yml`](templates/license-compliance-checker.yml) | Push, PR | Validates open-source license compatibility across dependencies |
| 🔍 CodeQL Advanced Analysis | [`codeql-advanced-analysis.yml`](templates/codeql-advanced-analysis.yml) | Push, PR, Schedule | Deep static analysis and CWE vulnerability detection with SARIF upload |
| 🚨 SecOps SIEM & PagerDuty | [`pagerduty-siem-alerting.yml`](templates/pagerduty-siem-alerting.yml) | Workflow Run, Dispatch | Dispatches automated incident alerts to PagerDuty Events API v2 / SIEM on security failures |
| 🧭 Reusable AgentOps Fleet Gate | [`.github/workflows/reusable-agentops.yml`](.github/workflows/reusable-agentops.yml) | `workflow_call` | Detects repo stack and applies security/quality gates across organizations |
| 🐳 Docker Build & Push | [`docker-build-push.yml`](templates/docker-build-push.yml) | Push, Release | Builds multi-platform Docker images and pushes to GHCR or Docker Hub |
| ☁️ AWS OIDC Deployment | [`aws-oidc-deployment.yml`](templates/aws-oidc-deployment.yml) | Push, Dispatch | Keyless AWS deployment via OpenID Connect (S3 sync, CloudFront invalidation) |
| ☸️ Kubernetes Helm Deploy | [`kubernetes-helm-deploy.yml`](templates/kubernetes-helm-deploy.yml) | Push, PR, Dispatch | Helm chart linting, dry-run diffs, and atomic Kubernetes cluster releases |
| 🏗️ Terraform Plan & Apply | [`terraform-plan-apply.yml`](templates/terraform-plan-apply.yml) | Push, PR, Dispatch | Speculative plan output commented on PRs with auto-apply upon merge |
| 🗄️ DB Schema Migrator | [`db-schema-migrator.yml`](templates/db-schema-migrator.yml) | Push, Manual | Runs database schema migrations in a controlled, environment-aware pipeline |
| 🌐 Static Site Deployment | [`static-site-deployment.yml`](templates/static-site-deployment.yml) | Push | Builds and deploys static sites to hosting platforms (Pages, S3, Netlify) |
| 📦 Release & Changelog Automation | [`release-changelog-automation.yml`](templates/release-changelog-automation.yml) | Tag Push, Dispatch | Automated semantic release notes generation and GitHub Release publication |
| 🔑 GitHub OAuth Login Redirect | [`github-oauth-login.yml`](templates/github-oauth-login.yml) | Push, PR, Dispatch | Validates GitHub OAuth authorize URL construction and redirect flow |
| 🧹 Stale Issue Closer | [`stale-issue-closer.yml`](templates/stale-issue-closer.yml) | Schedule | Automatically labels and closes inactive issues and pull requests |

---

## 🚀 Quick Start

### 1. Copy a template

```bash
# Clone this repo
git clone https://github.com/donny-devops/github-actions-templates.git

# Copy the desired template into your project
cp github-actions-templates/templates/docker-build-push.yml \
   your-project/.github/workflows/docker-build-push.yml
```

### 2. Use as Organization Starter Workflows

If your team maintains an organization-level `.github` repository, copy the contents of `.github/workflow-templates/` into your organization repository. Members can then select these templates directly from the GitHub UI under **Actions → New workflow → Workflows created by your organization**.

### 3. Configure required secrets

Each template lists required secrets in its header comments. Add them via:

> **Settings → Secrets and variables → Actions → New repository secret**

### 4. Customize and push

Open the copied `.yml` file, update the environment variables and configuration blocks marked with `# TODO:` comments, then commit and push.

---

## 🔒 Security & SecOps Templates

### CodeQL Advanced Analysis
**File:** [`templates/codeql-advanced-analysis.yml`](templates/codeql-advanced-analysis.yml)

Executes GitHub CodeQL static code analysis across Python, TypeScript, Go, and compiled languages. Automatically scans on code pushes and a scheduled weekly basis for zero-day vulnerability signatures.

### SecOps SIEM & PagerDuty Dispatcher
**File:** [`templates/pagerduty-siem-alerting.yml`](templates/pagerduty-siem-alerting.yml)

Monitors upstream security workflows (`CodeQL`, `Secrets Scanner`, `Dependency Review`) via `workflow_run`. If any gate fails, it immediately constructs an event compliant with PagerDuty Events API v2 and dispatches an incident with branch and commit metadata.

### Secrets Scanner
**File:** [`templates/secrets-scanner.yml`](templates/secrets-scanner.yml)

Detects accidentally committed secrets (API keys, tokens, passwords) before they reach production. Integrates with tools like `trufflesecurity/trufflehog` or `gitleaks`.

### Dependency Vulnerability Checker
**File:** [`templates/dependency-vulnerability-checker.yml`](templates/dependency-vulnerability-checker.yml)

Scans `requirements.txt`, `package.json`, `go.sum`, and other manifest files for known CVEs. Supports Python (`pip-audit`), Node.js (`npm audit`), and more.

### License Compliance Checker
**File:** [`templates/license-compliance-checker.yml`](templates/license-compliance-checker.yml)

Ensures all dependencies use approved open-source licenses. Blocks copyleft GPL/AGPL licenses from entering commercial codebases if configured.

### Reusable AgentOps Fleet Gate
**File:** [`.github/workflows/reusable-agentops.yml`](.github/workflows/reusable-agentops.yml)

Promotes reusable quality gates across multiple repositories with stack auto-detection:
- Python gates (Ruff, pytest, Bandit, pip-audit)
- Node gates (install, lint, test, npm audit)
- Terraform gates (`fmt`, `validate`, optional `tflint`)
- Docker Compose validation
- Package validation (`twine check`, `npm pack --dry-run`)

---

## 🏗️ Infrastructure as Code (IaC)

### Terraform Plan & Apply
**File:** [`templates/terraform-plan-apply.yml`](templates/terraform-plan-apply.yml)

Enterprise Terraform & OpenTofu pipeline:
- Validates code formatting (`terraform fmt -check`) and configuration (`terraform validate`)
- Generates speculative `terraform plan` on Pull Requests and adds clean markdown diff summaries as PR comments
- Automatically runs `terraform apply` when PRs merge into `main` with concurrency group locks preventing state conflicts
- Authenticates securely via AWS OIDC (no long-lived keys)

---

## 🐳 Containers & Cloud Infrastructure

### AWS OIDC Deployment
**File:** [`templates/aws-oidc-deployment.yml`](templates/aws-oidc-deployment.yml)

Implements modern keyless AWS deployment using GitHub's OpenID Connect (OIDC) identity provider. Eliminates the risk of leaking permanent IAM access keys.

### Kubernetes Helm Deploy
**File:** [`templates/kubernetes-helm-deploy.yml`](templates/kubernetes-helm-deploy.yml)

Production-ready Kubernetes deployment pipeline using Helm:
- Lints and validates charts with `--strict`
- Runs non-destructive `--dry-run` diffs on pull requests
- Executes atomic upgrades with automatic rollback on failure (`--atomic --timeout 10m`)

### Docker Build & Push
**File:** [`templates/docker-build-push.yml`](templates/docker-build-push.yml)

Builds multi-platform container images with BuildKit layer caching and pushes to GitHub Container Registry (GHCR) or Docker Hub.

---

## 🗄️ Database Templates

### DB Schema Migrator
**File:** [`templates/db-schema-migrator.yml`](templates/db-schema-migrator.yml)

Runs schema migrations (Flyway, Liquibase, Alembic, or raw SQL) against target databases with environment promotion (dev → staging → prod).

---

## 🚀 Deployment & Releases

### Static Site Deployment
**File:** [`templates/static-site-deployment.yml`](templates/static-site-deployment.yml)

Builds static sites (Next.js export, React, Vue, Hugo, plain HTML) and publishes to GitHub Pages, AWS S3, or Netlify.

### Release & Changelog Automation
**File:** [`templates/release-changelog-automation.yml`](templates/release-changelog-automation.yml)

Extracts semantic release notes from merged PRs and commit history, tags releases (`vX.Y.Z`), and creates GitHub Releases with attached release assets.

---

## 🔑 Authentication Templates

### GitHub OAuth Login Redirect
**File:** [`templates/github-oauth-login.yml`](templates/github-oauth-login.yml)

Validates the construction and redirect endpoint behavior of GitHub OAuth applications, checking client ID, state generation, and redirect URI parameters.

---

## 🧹 Maintenance Templates

### Stale Issue Closer
**File:** [`templates/stale-issue-closer.yml`](templates/stale-issue-closer.yml)

Labels inactive issues and pull requests as stale and automatically closes them after a configurable grace period.

---

## 🗂️ Repository Structure

```
github-actions-templates/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflow-templates/                # GitHub Organization Starter Workflows
│   │   ├── aws-oidc-deployment.properties.json
│   │   ├── docker-build-push.properties.json
│   │   ├── kubernetes-helm-deploy.properties.json
│   │   └── secrets-scanner.properties.json
│   ├── workflows/
│   │   ├── ci.yml                          # Template validation CI & Gitleaks
│   │   └── reusable-agentops.yml          # Reusable fleet quality gate
│   └── dependabot.yml                     # Automated GitHub Actions version tracking
├── scripts/
│   └── validate_templates.py              # Zero-dependency template validator
├── templates/
│   ├── aws-oidc-deployment.yml            # Keyless AWS deployment (S3/CloudFront)
│   ├── codeql-advanced-analysis.yml       # CodeQL SAST scanning
│   ├── db-schema-migrator.yml             # Database migration pipeline
│   ├── dependency-vulnerability-checker.yml
│   ├── docker-build-push.yml              # Multi-arch container build & push
│   ├── github-oauth-login.yml             # OAuth redirect verification
│   ├── kubernetes-helm-deploy.yml         # Kubernetes Helm deploy & lint
│   ├── license-compliance-checker.yml     # License auditing
│   ├── pagerduty-siem-alerting.yml        # SecOps incident alerting
│   ├── release-changelog-automation.yml   # Semantic release & changelog
│   ├── secrets-scanner.yml                # Credential leakage detection
│   ├── stale-issue-closer.yml             # Issue triaging
│   ├── static-site-deployment.yml         # Static site publishing
│   └── terraform-plan-apply.yml           # Terraform IaC plan & apply pipeline
├── .gitleaks.toml
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── SECURITY.md
```

---

## 🤝 Contributing

Contributions are welcome! To add a new template:

1. Fork this repository
2. Create a branch: `git checkout -b feat/my-new-template`
3. Add your template to `templates/` with inline comments explaining each block
4. Run `python scripts/validate_templates.py` to ensure template syntax passes
5. Update the template catalog in `README.md`
6. Open a pull request

**Template standards:**
- Include a header block describing the template's purpose, triggers, and required secrets
- Mark all user-configurable values with `# TODO:` comments
- Follow the principle of least privilege for `permissions:` blocks
- Define explicit `timeout-minutes:` on all jobs

---

## 📄 License

MIT © [donny-devops](https://github.com/donny-devops)
