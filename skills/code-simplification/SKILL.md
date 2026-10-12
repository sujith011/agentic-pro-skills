---
name: code-simplification
description: "Reduce complexity while preserving exact behavior. Use after a feature works but feels heavier than necessary. Clarity over cleverness."
type: workflow
lifecycle: active
---

# Code Simplification — Clarity Over Cleverness

Simplify only after behavior is proven. Preserve every observable outcome.

## Principles
- Preserve behavior exactly.
- Prefer explicit over clever.
- Remove duplication that increases understanding cost.
- Keep changes local.

## Process
1. Confirm tests pass and behavior is correct.
2. Identify the highest-complexity spots.
3. Apply the smallest simplification that improves clarity.
4. Re-run tests.
5. Stop when further changes add no clarity.

## Verification
- [ ] Behavior unchanged (tests still pass)
- [ ] Clarity improved (shorter mental model)
- [ ] No new cleverness introduced
