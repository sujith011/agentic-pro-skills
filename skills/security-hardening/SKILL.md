---
name: security-hardening
description: "Apply OWASP-style checks and harden inputs, auth, and secrets. Use when handling user input, authentication, or external data."
type: workflow
lifecycle: active
---

# Security Hardening — Prevent the Obvious Failures

Assume every external input is hostile until proven otherwise.

## Process
1. Identify all trust boundaries.
2. Validate and sanitize inputs at the boundary.
3. Check authn/authz on every protected path.
4. Ensure secrets are not logged or committed.
5. Review dependencies for known issues.
6. Add tests for abuse cases where practical.

## Verification
- [ ] Inputs validated
- [ ] Auth checks present on protected routes
- [ ] No secrets in code or logs
- [ ] Abuse cases considered
