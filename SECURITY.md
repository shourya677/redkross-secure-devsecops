# Security Policy

## Supported versions

The latest version on the default branch is the only version currently supported.

## Reporting a vulnerability

Do not publish exploitable vulnerability details in a public issue. Contact the repository maintainer privately through the security contact configured in the GitHub repository's **Security** tab. Include affected files, impact, reproduction steps, and a suggested mitigation where possible.

This starter is an educational reference implementation. It is not a security certification or a guarantee that an application built from it is secure.

## Secret handling

- Never commit credentials, tokens, private keys, or production `.env` files.
- Store CI credentials in GitHub Actions secrets or a managed secret store.
- Rotate any credential that may have been exposed; deleting a commit does not invalidate a leaked credential.
