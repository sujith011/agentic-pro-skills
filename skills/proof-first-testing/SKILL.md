---
name: proof-first-testing
description: "Red-Green-Refactor with strict seams and anti-patterns. Tests are proof. Use when implementing logic, fixing bugs, or changing behavior."
type: workflow
lifecycle: active
---

# Proof-First Testing — Tests Are the Specification

Write the failing test first. No production code without a failing test that describes the desired behavior.

## Process
1. Agree the public seam(s) under test with the user (or from the spec).
2. Write one failing test at that seam that names the behavior.
3. Run it and confirm it fails for the right reason.
4. Write the minimal code to make it pass.
5. Commit the cycle. Repeat for the next behavior.

## Rules of the Loop
- **Red before green.** The test must fail first.
- **One seam, one test, one implementation** per cycle.
- **Test at the public interface only.** Never test private methods or internals.
- **Do not weaken a test** to make code pass.
- **Refactoring is separate.** Do it after the tests are green, or in a later review.

## Anti-Patterns (Reject These)
| Pattern | Why it fails |
|---------|--------------|
| Implementation-coupled | Test breaks on refactor even when behavior is unchanged |
| Tautological | Assertion recomputes the expected value the same way the code does |
| Horizontal slicing | All tests written first, then all implementation — tests become insensitive |
| Coverage theater | Adding tests only to raise a percentage |

## Verification
- [ ] Seam was agreed before the test was written
- [ ] Test failed for the right reason before any production code
- [ ] Test lives at a public interface
- [ ] No tautological or implementation-coupled assertions
- [ ] Cycle committed before the next one starts
