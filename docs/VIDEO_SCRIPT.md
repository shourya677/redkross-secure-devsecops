# 5–8 Minute Video Explanation Script

**Presenter:** Shourya Singh  
**Internship ID:** 2430  
**Project:** RedKross Secure Repository Starter — Secure Software Development & DevSecOps

Target duration: approximately 6 minutes. Record your real screen and show your own repository and actual test/CI results. Replace every bracketed instruction with genuine evidence. Do not claim a scan passed unless you ran it.

## 0:00–0:40 — Introduction and problem statement

"Hello, my name is Shourya Singh, and my internship ID is 2430. This is my Task 2 project for RedKross Research Foundation, titled Secure Software Development and DevSecOps.

The problem I am addressing is that security issues can enter a software repository through insecure code, vulnerable dependencies, accidentally committed credentials, or unsafe configuration. If these problems are discovered only near deployment, they become more expensive to fix.

My objective is to create a reusable secure-repository starter and automate important security checks in the development workflow."

**Show:** GitHub repository homepage and project title.

## 0:40–1:30 — Approach and technology choices

"I structured the project as a small Python starter with a GitHub Actions pipeline. I selected Bandit for Python static analysis, pip-audit for dependency vulnerability checks, Gitleaks for secret detection, and Trivy for filesystem and configuration scanning. Unit tests verify expected application behavior.

GitHub Actions runs these checks automatically on pushes and pull requests. This supports the shift-left security principle: detect issues as early as possible, before code is merged."

**Show:** `.github/workflows/security.yml` and briefly point to the four jobs.

## 1:30–2:25 — Repository structure and implementation

"The source code is under the `src` directory, and automated tests are under `tests`. The sample WSGI application exposes a health endpoint and a greeting endpoint. It uses fixed response content, rejects unsupported HTTP methods, returns generic errors, and adds defensive HTTP response headers such as `X-Content-Type-Options`, `X-Frame-Options`, and a restrictive Content Security Policy.

The repository also includes a `.gitignore` to exclude local environment files, an example environment file without real credentials, a security policy, contribution guidance, and Dependabot configuration."

**Show:** `src/secure_app/app.py`, `tests/test_app.py`, `.gitignore`, `SECURITY.md`.

## 2:25–3:35 — CI security workflow

"The first CI job runs the unit tests and Bandit. Bandit checks Python source code for common security weaknesses. The second job runs pip-audit against declared runtime dependencies to identify known vulnerable packages.

The third job runs Gitleaks to look for secrets in repository history. The fourth job uses Trivy to scan repository files for vulnerabilities, secrets, and configuration issues. The workflow uses read-only repository permissions by default and has time limits and concurrency controls.

When a check fails, the developer should inspect the finding, fix the root cause, and push an updated commit rather than simply suppressing the alert."

**Show:** Workflow YAML and the actual GitHub Actions run. If not yet run, say so and do not simulate a green result.

## 3:35–4:35 — Testing and results

"I included six unit tests covering the health endpoint, greeting endpoint, unknown routes, unsupported methods, security headers, and ensuring query input is not reflected in the response.

I ran the tests using [state the exact command] and obtained [state your actual result]. The Bandit result was [actual result], the pip-audit result was [actual result], and the GitHub Actions workflow result was [actual result]."

**Show:** Actual terminal output and Actions run summary. Do not use fabricated screenshots or results.

## 4:35–5:25 — Challenges and limitations

"One design consideration was keeping the starter reproducible and easy to understand without introducing unnecessary runtime dependencies. The example application therefore uses Python's standard library. The security tools are installed separately in CI.

This is a starter and educational reference, not a production security certification. A real production service would also need authentication and authorization, TLS, rate limiting, secure logging, deployment hardening, and application-specific threat modelling."

**Show:** README limitations and future improvements.

## 5:25–6:10 — Improvements and conclusion

"Future improvements could include CodeQL, container image scanning, software bill of materials generation, dynamic application security testing, and deployment security gates. Branch protection can also require all security checks to pass before a pull request is merged.

To conclude, this project provides a reusable repository structure, secure development guidance, automated tests, and CI security checks for code, dependencies, secrets, and configuration. Thank you."

**Show:** README summary and repository URL.

## Recording checklist

- [ ] Video is between 5 and 8 minutes.
- [ ] Show your own GitHub repository and actual workflow run.
- [ ] Show real test and scan output.
- [ ] Replace all bracketed result placeholders with real results.
- [ ] Explain the project in your own words; do not merely read the script.
- [ ] Make the repository and video link accessible to the reviewers.
