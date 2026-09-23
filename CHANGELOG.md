# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-09-23

### Added
- **14 Production Workflow Templates**:
  - `aws-oidc-deployment.yml` — Keyless AWS deployment using OpenID Connect (S3 sync, CloudFront invalidation).
  - `codeql-advanced-analysis.yml` — GitHub CodeQL deep SAST static security analysis with SARIF uploads.
  - `db-schema-migrator.yml` — Environment-promoted database schema migrations.
  - `dependency-vulnerability-checker.yml` — Automated CVE audits across Python, Node.js, Go dependencies.
  - `docker-build-push.yml` — Multi-platform Docker builds with BuildKit caching and Trivy vulnerability scanning.
  - `github-oauth-login.yml` — GitHub OAuth authorization URL parameter and redirect flow validation.
  - `kubernetes-helm-deploy.yml` — Strict Helm chart linting, PR dry-run diffs, and atomic Kubernetes cluster releases.
  - `license-compliance-checker.yml` — Open-source license compatibility checker.
  - `pagerduty-siem-alerting.yml` — PagerDuty Events API v2 incident dispatcher for security pipeline failures.
  - `release-changelog-automation.yml` — Automated semantic release notes generation and GitHub Release publisher.
  - `secrets-scanner.yml` — Repository credential and API secret leakage scanner.
  - `stale-issue-closer.yml` — Automated issue and pull request lifecycle triage.
  - `static-site-deployment.yml` — Multi-provider static site deployment pipeline (Pages, S3, Netlify).
  - `terraform-plan-apply.yml` — Infrastructure-as-Code pipeline with speculative PR plan comments and auto-apply.
- **Enterprise Features & Tooling**:
  - `reusable-agentops.yml` — Centralized multi-stack fleet quality gate for organization-wide adoption.
  - `scripts/validate_templates.py` — Zero-dependency cross-platform template syntax and catalog validator.
  - `ci.yml` — Automated CI testing templates, running Gitleaks secret detection and Actionlint.
  - `.github/dependabot.yml` — Automated weekly dependency tracking for GitHub Actions.
  - `.github/workflow-templates/` — GitHub Organization Starter Workflows descriptors and properties.
- **Documentation**:
  - Comprehensive documentation cataloging all templates, triggers, required permissions, and configuration options.
  - Contributing guidelines, security policy, and code of conduct.

---

[1.0.0]: https://github.com/donny-devops/github-actions-templates/releases/tag/v1.0.0
