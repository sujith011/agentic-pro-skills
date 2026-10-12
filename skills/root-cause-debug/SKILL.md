---
name: root-cause-debug
description: "Reproduce, localize, reduce, fix, guard. Use for any bug or unexpected behavior."
type: workflow
lifecycle: active
---

# Systematic Debugging — Five Steps, No Skipping

Do not guess. Follow the sequence.

## Process
1. Reproduce reliably (minimal steps).
2. Localize the failure (narrow the code path).
3. Reduce to the smallest failing case.
4. Fix the root cause.
5. Add a regression test that fails before the fix and passes after.

## Verification
- [ ] Reproduction steps documented
- [ ] Root cause identified (not just symptom)
- [ ] Regression test added
- [ ] Fix verified
