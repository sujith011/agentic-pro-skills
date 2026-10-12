---
name: multi-axis-review
description: "Five-axis review before merge: correctness, readability, architecture, security, performance. Use before any merge."
type: workflow
lifecycle: active
---

# Multi-Axis Review — Improve Code Health

Review is a gate, not optional polish.

## Axes
1. Correctness — does it match the spec and tests?
2. Readability — can a new engineer understand it quickly?
3. Architecture — does it fit existing patterns?
4. Security — any new risks?
5. Performance — any measurable regressions?

## Process
1. Diff against the approved task.
2. Score each axis with evidence.
3. List must-fix items.
4. Do not approve until must-fix items are resolved.

## Verification
- [ ] All five axes addressed
- [ ] Must-fix items resolved or explicitly deferred with reason
- [ ] Review recorded
