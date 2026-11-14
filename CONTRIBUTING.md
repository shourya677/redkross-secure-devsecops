# Contributing

1. Create a feature branch; do not commit directly to the protected default branch.
2. Keep changes small and explain their security impact in the pull request.
3. Add or update tests for behavior changes.
4. Run `python -m unittest discover -s tests -v` and the available security checks before opening a PR.
5. Never include real secrets or personal data in source code, tests, logs, or screenshots.
6. Request review and wait for required CI checks before merging.

## Pull request checklist

- [ ] Tests added or updated and passing.
- [ ] Bandit and dependency audit reviewed.
- [ ] No secrets or sensitive data introduced.
- [ ] Dependencies are necessary and reviewed.
- [ ] README and security documentation updated.
