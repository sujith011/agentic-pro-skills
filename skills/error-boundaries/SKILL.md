---
name: error-boundaries
description: "Define clear error handling and failure modes. Use for any code that can fail."
type: workflow
lifecycle: active
---

# Error Boundaries — Fail Explicitly

Silent failures are bugs. Define how every failure surfaces.

## Process
1. List the failure modes for the change.
2. Decide which are user-facing, which are logged, and which are retried.
3. Use typed errors or clear error codes.
4. Never swallow exceptions without a reason.
5. Add tests for the failure paths.

## Verification
- [ ] Failure modes listed
- [ ] User-facing errors are clear
- [ ] Tests cover the error paths
