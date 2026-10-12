---
name: proof-first-testing
description: "Use a failing behavior test before implementing logic, fixing a bug, or changing observable behavior."
---

# Proof-First Testing
A passing test is evidence for the behavior it exercises, not proof of all correctness.

## Process
1. Derive an observable behavior from the request or spec and choose the public seam.
2. Write one test with an independent expected outcome.
3. Run it before implementation; confirm it fails because the behavior is missing or wrong, not because setup is broken.
4. Implement the smallest fix, run the test, then relevant regression checks.
5. Refactor after green and rerun checks. Commit a coherent change only when authorized.

## Test design
- Cover relevant boundaries, failure paths, and concurrency, not private method names.
- Mock external dependencies when necessary; record which integration claims the mock cannot establish.
- Avoid assertions that recompute the answer using the implementation.
- Confirm a regression test detects the old defect by testing the prior behavior in an isolated copy when needed.
- Reuse project test commands and infrastructure.

## Example
For a single-use token, test the second use and concurrent consumption, not just a successful first request.

## Stop conditions
For static content or a change that cannot usefully be represented by an automated test, record the reason and a repeatable alternative. Do not invent test output or add a test merely to mirror implementation.

## Evidence
- [ ] Pre-fix failure and post-fix pass are recorded.
- [ ] Assertions establish the requested behavior independently.
- [ ] Relevant regression results and integration limits are explicit.
