---
name: test-driven-development
description: "Red-Green-Refactor. Tests are proof. Use when implementing logic, fixing bugs, or changing behavior."
type: workflow
lifecycle: active
---

# Test-Driven Development — Tests Are Proof

Write the failing test first. No production code without a failing test.

## Process
1. Write a failing test that describes the desired behavior.
2. Run it and confirm it fails for the right reason.
3. Write the minimal code to make it pass.
4. Refactor while keeping tests green.
5. Commit the cycle.

## Rules
- Prefer unit tests for pure logic.
- Integration tests for boundaries.
- Do not weaken a test to make code pass.
- Coverage is not the goal; behavioral proof is.

## Verification
- [ ] Test existed and failed before the implementation
- [ ] All tests pass
- [ ] No production code without a corresponding test for the change
