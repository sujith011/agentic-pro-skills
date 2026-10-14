---
name: proof-first-testing
description: "Use a failing behavior test before implementing logic, fixing a bug, or changing observable behavior."
---

# Proof-First Testing
A passing test is evidence for the behavior it exercises, not proof of all correctness.

## Process
1. Derive an observable behavior from the request or spec and choose the public seam. Inspect existing tests and repository commands; preserve unrelated changes.
2. Write the smallest test with an independent expected outcome. Assert the important result or side effect, including its absence when that is the requirement.
3. Run the targeted test before implementation. Record the command, working directory, exit status, and assertion failure. A collection error, missing dependency, permission failure, or unrelated failure does not establish the required red result.
4. If the test already passes, confirm it exercises the trigger and relevant code. Strengthen missing coverage from the requirement, not from implementation details. If the behavior is already correct, report that instead of inventing a fix. When the repair predates the test, test the original defect in an isolated copy and label the chronology accurately.
5. Implement the smallest supported fix. Rerun the same test, the original reproduction, and relevant regression checks. Keep assertions intact unless the agreed behavior changes; explain any necessary expectation change.
6. Refactor only after green and rerun checks affected by the refactor. Commit only when authorized; a request for test evidence does not itself authorize publishing.

## Test design
- Cover relevant boundaries, failure paths, and concurrency, not private method names.
- Mock external dependencies when necessary; record which integration claims the mock cannot establish.
- Avoid assertions that recompute the answer using the implementation.
- Confirm a regression test detects the old defect by testing the prior behavior in an isolated copy when needed.
- Reuse project test commands and infrastructure.
- Make races reproducible with controlled ordering or barriers. Repeated retries and sleeps alone do not establish concurrency correctness.
- Keep grading checks outside a tested agent's workspace during blind evaluations. An agent that has seen the expected checks can demonstrate a repair, but that run is not a blind comparison.

## Example
For a retried job, assert one ledger credit after two identical calls, the original returned credit, and rejection when the same ID carries a different amount. The new-job happy path alone misses the defect. For a single-use token, test second use and controlled concurrent consumption when the environment supports it.

## Stop conditions
For static content or a change that cannot usefully be represented by an automated test, record the reason and a repeatable alternative. Do not invent test output or add a test merely to mirror implementation.

When tests cannot execute, report the exact blocker and distinguish source inspection from runtime evidence. Do not mark red, green, or integration verification complete. Do not modify production data or discard user changes to recreate a baseline.

## Evidence
- [ ] Pre-fix failure and post-fix pass are recorded.
- [ ] Assertions establish the requested behavior independently.
- [ ] Relevant regression results and integration limits are explicit.
- [ ] Already-green checks and tests added after a repair have accurate chronology.
