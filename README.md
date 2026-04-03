# ⚙️ GitHub Actions Templates

> A curated collection of production-ready GitHub Actions workflow templates for DevOps automation — security scanning, Docker CI/CD, database migrations, static site deployments, and more.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![YAML](https://img.shields.io/badge/YAML-CB171E?logo=yaml&logoColor=white)](https://yaml.org/)

---

## 📋 Overview

This repository provides reusable, drop-in GitHub Actions workflow templates designed for real-world DevOps pipelines. Each template is thoroughly commented, follows CI/CD best practices, and is ready to be adapted with minimal configuration.

Templates cover four domains:
- 🔒 **Security** — secrets scanning, dependency vulnerabilities, license compliance
- 🐳 **Containers** — Docker image build and push
- 🗄️ **Database** — schema migration automation
- 🚀 **Deployment** — static site publishing
- 🧹 **Maintenance** — stale issue management

---

## 📁 Template Catalog

| Template | File | Trigger | Description |
|---|---|---|---|
| 🔐 Secrets Scanner | [`secrets-scanner.yml`](templates/secrets-scanner.yml) | Push, PR | Scans codebase for accidentally committed secrets, tokens, and credentials |
| 🛡️ Dependency Vulnerability Checker | [`dependency-vulnerability-checker.yml`](templates/dependency-vulnerability-checker.yml) | Push, PR, Schedule | Audits project dependencies for known CVEs and security advisories |
| 📜 License Compliance Checker | [`license-compliance-checker.yml`](templates/license-compliance-checker.yml) | Push, PR | Validates open-source license compatibility across dependencies |
| 🐳 Docker Build & Push | [`docker-build-push.yml`](templates/docker-build-push.yml) | Push, Release | Builds Docker images and pushes to a container registry (GHCR/DockerHub) |
| 🗄️ DB Schema Migrator | [`db-schema-migrator.yml`](templates/db-schema-migrator.yml) | Push, Manual | Runs database schema migrations in a controlled, environment-aware pipeline |
| 🌐 Static Site Deployment | [`static-site-deployment.yml`](templates/static-site-deployment.yml) | Push | Builds and deploys static sites to hosting platforms (GitHub Pages, S3, etc.) |
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

### 2. Configure required secrets

Each template lists the required secrets in its header comments. Add them via:

> **Settings → Secrets and variables → Actions → New repository secret**

### 3. Customize and push

Open the copied `.yml` file, update the environment variables and configuration blocks marked with `# TODO:` comments, then commit and push.

---

## 🔒 Security Templates

### Secrets Scanner
**File:** [`templates/secrets-scanner.yml`](templates/secrets-scanner.yml)

Detects accidentally committed secrets (API keys, tokens, passwords) before they reach production. Integrates with tools like `trufflesecurity/trufflehog` or `gitleaks`.

```yaml
# Required secrets: none
# Recommended: configure .gitleaks.toml or trufflehog config for allowlists
```

### Dependency Vulnerability Checker
**File:** [`templates/dependency-vulnerability-checker.yml`](templates/dependency-vulnerability-checker.yml)

Scans `requirements.txt`, `package.json`, `go.sum`, and other manifest files for known CVEs. Supports Python (Safety/pip-audit), Node.js (npm audit), and more.

```yaml
# Triggers: push, pull_request, scheduled weekly
# Configurable: severity threshold (low/medium/high/critical)
```

### License Compliance Checker
**File:** [`templates/license-compliance-checker.yml`](templates/license-compliance-checker.yml)

Ensures all dependencies use approved open-source licenses. Blocks GPL/AGPL licenses from entering commercial codebases if configured.

```yaml
# Configurable: allowed license list, fail-on-violation flag
```

---

## 🐳 Container Templates

### Docker Build & Push
**File:** [`templates/docker-build-push.yml`](templates/docker-build-push.yml)

Builds a Docker image with layer caching, tags it with the commit SHA and branch, and pushes to GitHub Container Registry (GHCR) or Docker Hub.

```yaml
# Required secrets:
#   REGISTRY_USERNAME  - Container registry username
#   REGISTRY_PASSWORD  - Container registry token/password

# Features: BuildKit cache, multi-platform support, image signing
```

---

## 🗄️ Database Templates

### DB Schema Migrator
**File:** [`templates/db-schema-migrator.yml`](templates/db-schema-migrator.yml)

Runs schema migrations (Flyway, Liquibase, Alembic, or raw SQL) against a target database. Supports environment-based promotion (dev → staging → prod).

```yaml
# Required secrets:
#   DB_HOST      - Database host
#   DB_PORT      - Database port
#   DB_NAME      - Database name
#   DB_USER      - Database username
#   DB_PASSWORD  - Database password
```

---

## 🌐 Deployment Templates

### Static Site Deployment
**File:** [`templates/static-site-deployment.yml`](templates/static-site-deployment.yml)

Builds a static site (React, Vue, Hugo, Jekyll, plain HTML) and deploys to GitHub Pages, AWS S3, or Netlify. Includes build caching and deployment previews for PRs.

```yaml
# Configurable: build_command, output_dir, deploy_target
# Optional secrets: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY (for S3)
```

---

## 🧹 Maintenance Templates

### Stale Issue Closer
**File:** [`templates/stale-issue-closer.yml`](templates/stale-issue-closer.yml)

Automatically labels issues and PRs as stale after a configurable period of inactivity, then closes them if no response is received.

```yaml
# Runs: daily via cron schedule
# Configurable: stale-after days, close-after days, exempt labels
```

---

## 🗂️ Repository Structure

```
github-actions-templates/
├── README.md
├── .gitignore
└── templates/
    ├── secrets-scanner.yml
    ├── dependency-vulnerability-checker.yml
    ├── license-compliance-checker.yml
    ├── docker-build-push.yml
    ├── db-schema-migrator.yml
    ├── static-site-deployment.yml
    └── stale-issue-closer.yml
```

---

## 🤝 Contributing

Contributions are welcome! To add a new template:

1. Fork this repository
2. Create a branch: `git checkout -b feat/my-new-template`
3. Add your template to `templates/` with inline comments explaining each block
4. Update the template catalog table in this README
5. Open a pull request

**Template standards:**
- Include a header block describing the template's purpose, triggers, and required secrets
- Mark all user-configurable values with `# TODO:` comments
- Use environment variables instead of hardcoded values
- Follow the principle of least privilege for `permissions:` blocks

---

## 📄 License

MIT © [donny-devops](https://github.com/donny-devops)

---

<p align="center">
  <sub>Built with ❤️ for DevOps engineers who automate everything that should never be manual.</sub>
</p>
