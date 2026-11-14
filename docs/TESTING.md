# Testing Plan and Evidence Record

## Test environment

Record the actual environment used before submission:

- OS: [enter your OS and version]
- Python: [enter `python --version` output]
- Git: [enter `git --version` output]
- Repository commit: [enter commit SHA]
- GitHub Actions run: [paste workflow run URL]

## Unit test cases

| ID | Test | Expected result |
|---|---|---|
| UT-01 | `GET /health` | HTTP 200 and `{"status":"ok"}` |
| UT-02 | `GET /api/greeting` | HTTP 200 and a fixed greeting message |
| UT-03 | Unknown path | HTTP 404 and generic error |
| UT-04 | POST to `/health` | HTTP 405 |
| UT-05 | Security headers | `nosniff`, `DENY`, no-store, restrictive CSP are present |
| UT-06 | Query string contains script-like text | User-controlled query is not reflected in the response |

## Security checks

| Check | Command / workflow | Pass condition |
|---|---|---|
| Unit tests | `python -m unittest discover -s tests -v` | All tests pass |
| Bandit | `bandit -c pyproject.toml -r src -ll` | No high-severity findings requiring remediation |
| Dependency audit | `pip-audit -r requirements.txt` | No known vulnerable declared runtime dependencies |
| Gitleaks | `gitleaks detect --source . --no-git --redact` or CI job | No real secrets detected |
| Trivy | `filesystem-scan` CI job | No unaccepted HIGH/CRITICAL findings |

## Evidence to capture for the final submission

1. Terminal output showing all unit tests passing.
2. Bandit output showing the scan completed and its findings summary.
3. pip-audit output showing the audit completed.
4. GitHub Actions page showing all four security jobs completed successfully.
5. Repository page showing README, workflow, SECURITY.md, and tests.

Paste actual results below after running the commands. Do not leave placeholders in the submitted evidence document.

### Actual results

- Unit tests: [replace with actual result]
- Bandit: [replace with actual result]
- pip-audit: [replace with actual result]
- Gitleaks: [replace with actual result]
- Trivy: [replace with actual result]
- GitHub Actions run URL: [paste URL]
