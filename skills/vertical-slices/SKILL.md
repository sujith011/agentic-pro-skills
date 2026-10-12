---
name: vertical-slices
description: "Deliver a multi-layer behavior change in small end-to-end increments with a consistent test-first verification sequence."
---

# Vertical Slices
Complete one observable behavior before starting the next.

## Process
1. Select the next acceptance criterion and identify the public seam.
2. Write a failing behavior test and run it to confirm failure for the expected reason.
3. Implement the smallest end-to-end change that passes it.
4. Run relevant regression checks; verify integration when mocks cannot establish the criterion.
5. Refactor after green and rerun checks.
6. Record evidence and, when committing is authorized, make one coherent commit before the next slice.

## Example
For a protected export endpoint, first prove an authorized user gets the expected file; then prove another tenant cannot export those records.

## Stop conditions
If a failing automated test cannot represent the change, record why and use a repeatable baseline/recheck (for example a visual review). Never invent a red result or force a meaningless test for static content.

## Evidence
- [ ] Failing check precedes implementation for changed behavior.
- [ ] The slice satisfies an observable criterion.
- [ ] Relevant checks pass or unresolved limits are explicit.
- [ ] Unrelated changes are excluded.
