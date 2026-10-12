---
name: quality-bar
description: "Decide the quality bar once and enforce it on every change. Use when setting or checking performance, security, test coverage, or style floors."
type: workflow
lifecycle: active
---

# Constraint Enforcement — Decide Once, Enforce Everywhere

Write the bar. Do not let it drift.

## Process
1. Interview for the dimensions that matter (coverage, latency, security, a11y, etc.).
2. Set numeric thresholds where possible.
3. Write CONSTRAINTS.md with the rules and how to check them.
4. On every change, run the checks before declaring done.
5. Refuse to lower a constraint without explicit justification and update to the file.

## Verification
- [ ] CONSTRAINTS.md exists with measurable rules
- [ ] Checks are runnable (commands or scripts)
- [ ] No silent lowering of the bar
