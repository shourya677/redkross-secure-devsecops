# RedKross Secure Repository Starter

**Task:** Secure Software Development & DevSecOps  
**Intern:** Shourya Singh  
**Internship ID:** 2430  
**Organization:** RedKross Research Foundation

## 1. Project overview

This repository is a reusable starter for Python projects. It demonstrates secure repository hygiene, a small example WSGI application with conservative defaults, automated tests, and a GitHub Actions pipeline that runs security checks on pushes and pull requests.

### Objectives

- Catch common insecure coding patterns early with Static Application Security Testing (SAST).
- Identify vulnerable third-party packages before merge.
- Detect accidentally committed credentials and tokens.
- Scan repository files for vulnerabilities, secrets, and configuration weaknesses.
- Establish repeatable tests and security review practices.

## 2. Security controls

| Control | Tool / file | Purpose |
|---|---|---|
| Unit tests | `pytest` | Verify expected application behavior |
| SAST | Bandit | Find common Python security issues |
| Dependency audit | `pip-audit` | Check installed/runtime dependencies against known advisories |
| Secret detection | Gitleaks | Detect likely secrets in repository history |
| Filesystem scan | Trivy | Scan files for vulnerabilities, secrets, and misconfiguration |
| Dependency updates | Dependabot | Propose dependency and GitHub Actions updates |
| Local pre-commit checks | `.pre-commit-config.yaml` | Catch formatting and private-key mistakes before commit |
| Security process | `SECURITY.md` | Explain responsible vulnerability reporting |

## 3. Repository structure

```text
redkross-secure-devsecops/
├── .github/
│   ├── workflows/security.yml
│   └── dependabot.yml
├── docs/
│   ├── TESTING.md
│   └── VIDEO_SCRIPT.md
├── scripts/run_security_checks.sh
├── src/secure_app/
│   ├── __init__.py
│   └── app.py
├── tests/test_app.py
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── requirements.txt
├── SECURITY.md
└── pyproject.toml
```

## 4. Requirements

- Python 3.10 or later
- Git
- GitHub account
- Optional local tools: Bandit, pip-audit, Gitleaks, pre-commit

The sample application uses only Python's standard library. `requirements.txt` intentionally has no runtime packages. CI installs test and scanning tools separately.

## 5. Setup and run

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -e . pytest bandit pip-audit
py -m unittest discover -s tests -v
```

### Linux / Kali / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e . pytest bandit pip-audit
python -m unittest discover -s tests -v
```

### Run the example server

To serve this app, use the following one-liner from the repository root:

```bash
python -c "from wsgiref.simple_server import make_server; from secure_app.app import application; make_server('127.0.0.1', 8000, application).serve_forever()"
```

Open `http://127.0.0.1:8000/health` or `http://127.0.0.1:8000/api/greeting`.

## 6. Run security checks locally

```bash
bandit -c pyproject.toml -r src -ll
pip-audit -r requirements.txt
```

Install Gitleaks separately to run a local secret scan:

```bash
gitleaks detect --source . --no-git --redact
```

Or run the helper script after installing Bandit and pip-audit:

```bash
bash scripts/run_security_checks.sh
```

## 7. CI workflow

The workflow at `.github/workflows/security.yml` runs on pushes to `main`/`master`, pull requests targeting those branches, and manual dispatch. It contains four jobs:

1. **Tests and SAST:** installs the project, runs unit tests, and executes Bandit.
2. **Dependency audit:** runs pip-audit against runtime requirements.
3. **Secret scan:** runs Gitleaks against repository history.
4. **Filesystem scan:** runs Trivy for vulnerabilities, secrets, and misconfiguration.

A failed check makes its job fail. Review findings, fix the root cause, and push a new commit. Do not suppress a finding just to make the pipeline green. If a finding is a false positive, document the rationale and use a narrow, reviewed exception.

## 8. GitHub repository setup

1. Create a new **public** repository named `redkross-secure-devsecops` (unless your supervisor requires private visibility).
2. Upload/push the complete contents of this folder to the repository's default branch.
3. In **Settings → Actions → General**, allow the required GitHub Actions to run.
4. In **Settings → Branches** or repository rulesets, protect `main` and require the `tests-and-sast`, `dependency-audit`, `secret-scan`, and `filesystem-scan` checks before merging (the exact displayed check names may include job labels).
5. Open **Actions** and verify that the workflow completes. Fix any failures before submission.
6. Add the repository URL and recorded video URL to the RedKross Task 2 submission sheet.

For stronger supply-chain hardening, pin third-party GitHub Actions to verified full commit SHAs and review action updates before merging. The starter uses version tags for readability and Dependabot update proposals.

## 9. Testing and evidence

See [`docs/TESTING.md`](docs/TESTING.md) for test cases, commands, and an evidence checklist. Only report CI results after running the workflow in your own GitHub repository. Do not describe local test results as GitHub Actions results.

## 10. Limitations and future improvements

- This is a minimal educational WSGI example, not a production service or complete secure application framework.
- The sample has no authentication, database, TLS termination, rate limiting, or deployment configuration.
- Trivy and Gitleaks depend on external GitHub Actions and their upstream services.
- Dependency audit covers the declared runtime requirements; extend it to all lockfiles and deployment images when adding components.
- Add CodeQL, container-image scanning, SBOM generation/signing, DAST, coverage thresholds, and environment-specific deployment gates for a larger production project.

## 11. References

- GitHub Actions documentation: https://docs.github.com/actions
- Bandit documentation: https://bandit.readthedocs.io/
- pip-audit: https://github.com/pypa/pip-audit
- Gitleaks: https://github.com/gitleaks/gitleaks
- Trivy: https://trivy.dev/
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP SAMM: https://owaspsamm.org/

## 12. Submission identity

- Name: Shourya Singh
- Internship ID: 2430
- Task: Secure Software Development & DevSecOps
- Organization: RedKross Research Foundation
