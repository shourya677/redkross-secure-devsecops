# Local Test Results

Date: 14 November 2026

## Unit tests

Command executed:

```bash
python -m unittest discover -s tests -v
```

Result: **6 tests passed, 0 failures, 0 errors** in the provided build environment.

Covered tests:

- Health endpoint response
- Greeting endpoint response
- Unknown route handling
- Unsupported HTTP method handling
- Security response headers
- No reflection of query input in the greeting response

## Checks not yet executed

Bandit, pip-audit, Gitleaks, Trivy, and GitHub Actions have **not** been executed in the user's GitHub environment as part of this local build. Run the workflow after pushing the repository and record the actual results and run URL in `TESTING.md`. Do not represent these pending checks as passed.
