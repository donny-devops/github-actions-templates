# github-actions-templates

Reusable GitHub Actions workflow library for Docker, Terraform, Python, Node.js/TypeScript, and security scanning. Call these workflows from any repo with a single `uses:` reference.

[![CI](https://github.com/donny-devops/github-actions-templates/actions/workflows/ci.yml/badge.svg)](https://github.com/donny-devops/github-actions-templates/actions/workflows/ci.yml)
[![YAML Lint](https://img.shields.io/badge/YAML-lint%20passing-brightgreen?style=flat-square)](https://github.com/donny-devops/github-actions-templates)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

---

## Available Workflows

| Workflow | File | Purpose |
|---|---|---|
| Docker Build · Scan · Push | `workflows/docker-build-push.yml` | Multi-platform build, Trivy scan, GHCR push |
| Terraform Plan / Apply | `workflows/terraform-plan-apply.yml` | OIDC AWS auth, plan on PR, apply on merge |
| Python CI | `workflows/python-ci.yml` | ruff lint, pytest + coverage |
| Node.js / TypeScript CI | `workflows/node-ts-ci.yml` | eslint, tsc, jest + coverage |
| Security Scan | `workflows/security-scan.yml` | CodeQL, dependency review, Trivy |

---

## Usage

### Docker Build & Push

```yaml
jobs:
  docker:
    uses: donny-devops/github-actions-templates/workflows/docker-build-push.yml@main
    with:
      image_name: my-api
      dockerfile_path: ./Dockerfile
      context: .
    secrets: inherit
```

### Terraform (Plan on PR, Apply on main)

```yaml
jobs:
  terraform:
    uses: donny-devops/github-actions-templates/workflows/terraform-plan-apply.yml@main
    with:
      working_directory: ./infra
      terraform_version: "1.7.5"
      aws_region: us-east-1
      aws_role_arn: arn:aws:iam::123456789012:role/github-actions-terraform
      apply: ${{ github.ref == 'refs/heads/main' }}
    secrets: inherit
```

### Python CI

```yaml
jobs:
  python-ci:
    uses: donny-devops/github-actions-templates/workflows/python-ci.yml@main
    with:
      python_version: "3.12"
      requirements_file: requirements.txt
      coverage_threshold: "85"
```

### Node.js / TypeScript CI

```yaml
jobs:
  node-ci:
    uses: donny-devops/github-actions-templates/workflows/node-ts-ci.yml@main
    with:
      node_version: "20"
      coverage_threshold: "80"
```

### Security Scan

```yaml
jobs:
  security:
    uses: donny-devops/github-actions-templates/workflows/security-scan.yml@main
    with:
      language: python
      fail_on_severity: HIGH
```

---

## Repository Structure


---

## Requirements

- Workflows use **OIDC** for AWS authentication — no long-lived access keys stored as secrets.
- The Terraform workflow requires an IAM role with a trust policy allowing GitHub OIDC.
- GHCR push uses `GITHUB_TOKEN` by default — no additional secrets needed for public repos.

---

## License

MIT — see [LICENSE](LICENSE).
