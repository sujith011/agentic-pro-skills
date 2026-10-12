---
name: five-axis-gate
description: "Five-axis review gate before merge. Correctness, readability, architecture, security, performance. Use before any merge."
type: workflow
lifecycle: active
---

# Five-Axis Gate — No Merge Without Evidence

Review is a hard gate. Do not approve until every axis has evidence.

## Axes and What to Score
| Axis | Pass condition |
|------|----------------|
| **Correctness** | Matches the approved spec and existing tests. No silent behavior changes. |
| **Readability** | A new engineer can understand the change in under 5 minutes. Names reveal intent. |
| **Architecture** | Fits existing patterns or explicitly records a new decision (ADR). |
| **Security** | No new trust-boundary violations, secret leaks, or unvalidated inputs. |
| **Performance** | No measurable regression, or the regression is measured and accepted. |

## Process
1. Diff against the approved task or spec.
2. For each axis, write one sentence of evidence (or “fails because…”).
3. List must-fix items. Defer only with an explicit reason and owner.
4. Do not mark the review complete until must-fix items are resolved or deferred.

## Anti-Rationalizations
- “It’s small, skip review” → Size does not remove risk.
- “Tests passed, so it’s fine” → Tests do not cover architecture or security.
- “I’ll fix it later” → Later is how debt accumulates.

## Verification
- [ ] All five axes have written evidence
- [ ] Must-fix items resolved or explicitly deferred
- [ ] Review recorded in the PR or commit message
