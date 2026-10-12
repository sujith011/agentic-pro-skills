---
name: error-boundaries
description: "Design failure handling for operations involving retries, external services, persistence, or user-visible recovery."
---

# Error Boundaries
Make failures distinguishable and recovery intentional.

## Process
1. Enumerate expected failure categories and their effect on state.
2. Map each to user behavior, typed error/code, logging, and retry policy.
3. Retry transient failures only with a bound, timeout, backoff, and idempotency where side effects exist.
4. Preserve original causes internally while excluding secrets and internals from public errors.
5. Test failure paths, cancellation, and partial success where applicable.

## Example
A payment timeout may mean "outcome unknown." Query by idempotency key before retrying rather than risking another charge.

## Stop conditions
Do not silently swallow failures, retry indefinitely, or report success after an incomplete operation.

## Evidence
- [ ] Failure categories and state effects are explicit.
- [ ] Retry bounds and duplicate-effect prevention are tested.
- [ ] Users have an actionable recovery path.
