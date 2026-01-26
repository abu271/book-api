# Security Tools in CI/CD Pipeline

This repository uses multiple free security tools integrated into GitHub Actions to ensure secure code and dependencies.

## Security Workflows

### 1. Security Scans (`security.yml`)
Comprehensive security scanning that runs on push, pull requests, and daily schedule:

- **Dependency Vulnerability Scan (pip-audit)**: Scans Python dependencies for known vulnerabilities
  - Reports CVEs in installed packages
  - Generates JSON reports stored as artifacts
  
- **SAST - Bandit Security Scan**: Static Application Security Testing for Python code
  - Identifies common security issues in Python code
  - Checks for hardcoded passwords, SQL injection risks, etc.
  
- **Secret Scanning (Gitleaks)**: Detects hardcoded secrets and credentials
  - Scans git history for exposed secrets
  - Prevents accidental credential commits
  
- **Container Image Scan (Trivy)**: Scans Docker images for vulnerabilities
  - Checks OS packages and application dependencies
  - Uploads results to GitHub Security tab (SARIF format)
  
- **Safety Check**: Additional Python dependency vulnerability scanner
  - Cross-validates dependency issues
  - Provides detailed vulnerability information
  
- **Semgrep SAST Scan**: Advanced static analysis for security vulnerabilities
  - Uses community security rules
  - Detects OWASP Top 10 vulnerabilities

### 2. CodeQL Analysis (`codeql.yml`)
GitHub's advanced semantic code analysis:

- Runs weekly and on code changes
- Uses security-extended and security-and-quality query packs
- Deep analysis for:
  - SQL injection
  - Command injection
  - Cross-site scripting (XSS)
  - Path traversal
  - And many more vulnerability types

### 3. Dependency Review (`dependency-review.yml`)
Automated dependency review for pull requests:

- Compares dependencies in PRs against the base branch
- Fails on moderate or higher severity vulnerabilities
- Posts summary comments on PRs with vulnerability details
- Prevents introducing vulnerable dependencies

### 4. Integrated Security Checks
Quick security checks integrated into existing workflows:

- **Pull Request Checks**: Runs Bandit and pip-audit on every PR
- **Main Build**: Includes security scanning before Docker push

## Security Reports

All security scan results are available as:
- **GitHub Security Tab**: CodeQL and Trivy results appear here
- **Workflow Artifacts**: Detailed JSON reports for pip-audit, Bandit, Safety, and Semgrep
- **Pull Request Comments**: Dependency review posts findings directly on PRs

## Running Security Scans Locally

### Bandit (Python SAST)
```bash
pip install bandit[toml]
bandit -r app/ -ll
```

### pip-audit (Dependency Vulnerabilities)
```bash
pip install pip-audit
pip-audit -r requirements.txt
```

### Safety (Dependency Vulnerabilities)
```bash
pip install safety
safety check
```

### Trivy (Container Scanning)
```bash
# Install trivy first: https://aquasecurity.github.io/trivy/
docker build -t bookapi:test .
trivy image bookapi:test
```

### Gitleaks (Secret Scanning)
```bash
# Install gitleaks first: https://github.com/gitleaks/gitleaks
gitleaks detect --source . --verbose
```

## Security Best Practices

1. **Never commit secrets**: Use GitHub Secrets or environment variables
2. **Keep dependencies updated**: Review Dependabot alerts regularly
3. **Fix critical/high vulnerabilities**: Address security findings promptly
4. **Review security scan results**: Check workflow runs for security issues
5. **Use the security tab**: Monitor CodeQL and Trivy findings

## Tools Summary

| Tool | Type | Frequency | Purpose |
|------|------|-----------|---------|
| **pip-audit** | SCA | Every push/PR + Daily | Python dependency vulnerabilities |
| **Safety** | SCA | Every push/PR + Daily | Python dependency vulnerabilities |
| **Bandit** | SAST | Every push/PR + Daily | Python code security issues |
| **Semgrep** | SAST | Every push/PR + Daily | Multi-language security patterns |
| **CodeQL** | SAST | Every push/PR + Weekly | Deep semantic code analysis |
| **Trivy** | Container | Every push/PR + Daily | Docker image vulnerabilities |
| **Gitleaks** | Secret Scan | Every push/PR + Daily | Exposed secrets detection |
| **Dependency Review** | SCA | Pull Requests | Dependency diff analysis |

## Cost

All tools used are **100% free** for public repositories and most are free for private repositories as well.

## Support

For questions or issues with security tools, please open an issue or contact the security team.
