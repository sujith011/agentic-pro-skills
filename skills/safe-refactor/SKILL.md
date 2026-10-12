---
name: safe-refactor
description: "Refactor only with a safety net of tests and small steps. Use when improving structure without changing behavior."
type: workflow
lifecycle: active
---

# Safe Refactor — Change Structure, Not Behavior

Refactoring without tests is just rewriting.

## Process
1. Confirm tests cover the current behavior.
2. Make the smallest structural change.
3. Run the full test suite.
4. Commit.
5. Repeat until the structure is clean.

## Verification
- [ ] Tests existed before the refactor
- [ ] Behavior unchanged
- [ ] Each step is small and committed
