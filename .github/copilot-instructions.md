# Copilot Code Review Instructions — GitHub Actions Templates

## Supply Chain Security & CI/CD Hardening

### 1. Action Security (CRITICAL)
- **SHA Pinning**
  - ALL third-party actions MUST use full commit SHA (not tags or branches)
  - Format: `actions/checkout@a81bbbf8298c0fa03ea29cdc473d45769f953675 # v3.5.2`
  - Flag any action using `@main`, `@v1`, or tag references
  - Verify SHAs are valid and match claimed versions
- **Supply Chain Hardening**
  - Use `step-security/harden-runner@...` as first step in jobs
  - Enable egress auditing: `egress-policy: audit` or `block`
  - Verify allowed-endpoints list is minimal
  - Check for network egress monitoring
- **Trusted Actions Only**
  - Prefer GitHub-verified actions (`actions/*`, `github/*`)
  - Flag unknown or low-star third-party actions
  - Require security audit for new dependencies

### 2. Secrets & Credentials (CRITICAL)
- **Secrets Management**
  - Never echo secrets: `echo "${{ secrets.TOKEN }}"` is FORBIDDEN
  - Use `secrets.*` only in workflow files, never in scripts
  - Check for accidental secret exposure in logs/artifacts
  - Verify OIDC token usage over long-lived credentials where possible
- **Environment Variables**
  - No hardcoded credentials in workflow files
  - Sensitive values must use `${{ secrets.* }}`
  - Check for secrets passed as plaintext parameters
  - Verify proper masking in logs
- **Token Permissions**
  - GitHub tokens must use least privilege
  - Explicitly set `permissions:` block on every job
  - Default should be `permissions: contents: read`
  - Only grant write permissions when required
  - Example:
    ```yaml
    permissions:
      contents: read
      pull-requests: write  # Only if needed
    ```

### 3. Input Validation & Injection Prevention
- **Command Injection**
  - Flag use of `run: echo ${{ github.event.issue.title }}`
  - User input must be passed via `env:` block
  - Use intermediate environment variables:
    ```yaml
    env:
      TITLE: ${{ github.event.issue.title }}
    run: echo "$TITLE"
    ```
  - Check for unquoted variables in shell commands
- **Script Injection**
  - Verify proper escaping in `run:` blocks
  - Flag `eval` or dynamic code execution
  - Check for SQL injection in database operations
  - Validate all workflow_dispatch inputs

### 4. Workflow Triggers & Conditions
- **Trigger Security**
  - `pull_request_target` is HIGH RISK - verify checkout safety
  - Check for `pull_request_target` + `actions/checkout@HEAD` (vuln combo)
  - Verify workflow_dispatch inputs have validation
  - Flag workflows triggered by forks without approval
- **Branch Protection**
  - Critical workflows should have `if:` conditions
  - Check for deployment protection rules
  - Verify required approvals for production deploys

### 5. Container & Docker Security
- **Image Security**
  - Base images MUST use digests: `ubuntu:22.04@sha256:...`
  - Never use `:latest` tag in production workflows
  - Check for known vulnerabilities in base images
  - Verify multi-stage builds minimize attack surface
- **Build Security**
  - Use `docker/build-push-action@...` with SHA pinning
  - Verify Docker Content Trust (DCT) where applicable
  - Check for secrets in Docker layers
  - Flag missing vulnerability scanning (Trivy, Snyk)

### 6. Artifact & Cache Security
- **Artifact Handling**
  - Verify artifact upload/download uses trusted paths
  - Check for sensitive data in artifacts
  - Ensure artifacts have retention policies
  - Flag public artifacts with credentials
- **Cache Security**
  - Cache keys should be deterministic and scoped
  - Verify cache restoration doesn't execute code
  - Check for cache poisoning risks

### 7. Dependency Management
- **Dependabot Integration**
  - Verify Dependabot is enabled for GitHub Actions
  - Check for automated PR creation on updates
  - Ensure version pinning is maintained
- **Vulnerability Scanning**
  - Check for `dependency-review-action` on PRs
  - Verify Trivy/Snyk scans are present
  - Flag missing SBOM generation
  - Check for license compliance scanning

### 8. Reusable Workflow Security
- **Workflow Inputs**
  - All inputs must have type and description
  - Required vs optional inputs clearly defined
  - Validation for critical inputs
- **Secrets Passing**
  - Document required secrets in README
  - Check for unnecessary secret inheritance
  - Verify secrets are scoped to specific jobs

### 9. Job Isolation & Least Privilege
- **Runner Security**
  - Verify jobs run on trusted runners only
  - Check for self-hosted runner security best practices
  - Flag jobs that modify repository without review
- **Permissions Scoping**
  - Permissions set per-job, not per-workflow (preferred)
  - Read-only by default
  - Write permissions justified in comments

### 10. Observability & Monitoring
- **Logging**
  - No secrets in logs (use `echo "::add-mask::$SECRET"`)
  - Sufficient logging for audit trails
  - Check for error handling in critical steps
- **Failure Handling**
  - Critical steps should have `continue-on-error: false`
  - Verify notifications on failure
  - Check for rollback procedures

## Code Quality Standards
- YAML syntax validation (`yamllint`)
- Consistent indentation (2 spaces)
- Descriptive job and step names
- Comments for complex logic
- README with usage examples

## Response Format
```
**[CRITICAL]**: Supply Chain Security - Action Not SHA-Pinned

**Location**: `.github/workflows/ci.yml:23`
**Problem**: Action uses tag reference instead of commit SHA
**Risk**: Tag can be moved to malicious code (supply chain attack vector)
**Fix**: 
\```yaml
# Before (vulnerable)
- uses: actions/checkout@v3

# After (hardened)
- uses: actions/checkout@8e5e7e5ab8b370d6c329ec480221332ada57f0ab # v3.5.2
\```
**Command to get SHA**:
\```bash
git ls-remote https://github.com/actions/checkout v3.5.2
\```
**Reference**: 
- https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#using-third-party-actions
- StepSecurity Harden Runner documentation
```

Severity: CRITICAL | HIGH | MEDIUM | LOW | ADVISORY

## Special Notes
- **CRITICAL findings in supply chain security block merge immediately**
- **All security findings should include remediation steps**
- **Reference SLSA framework for supply chain maturity**
- **Check OpenSSF Scorecard metrics where applicable**
