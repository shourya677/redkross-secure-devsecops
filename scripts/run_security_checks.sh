#!/usr/bin/env bash
set -euo pipefail

python -m unittest discover -s tests -v

if ! command -v bandit >/dev/null 2>&1; then
  echo "Bandit is required. Install with: python -m pip install bandit" >&2
  exit 2
fi
bandit -c pyproject.toml -r src -ll

if ! command -v pip-audit >/dev/null 2>&1; then
  echo "pip-audit is required. Install with: python -m pip install pip-audit" >&2
  exit 2
fi
pip-audit -r requirements.txt

if command -v gitleaks >/dev/null 2>&1; then
  gitleaks detect --source . --no-git --redact
else
  echo "Gitleaks not installed locally; CI runs Gitleaks on pushes and pull requests."
fi
