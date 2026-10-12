---
name: atomic-task-breakdown
description: "Decompose a spec into small, verifiable, ordered tasks. Use after a spec is approved and before any implementation."
type: workflow
lifecycle: active
---

# Task Planning — Small Atomic Units

Tasks must be completable and verifiable in one focused session.

## Process
1. Read the approved spec.
2. Break into tasks of 1-4 hours each.
3. Each task has: title, acceptance criteria, dependencies, verification steps.
4. Order by dependency.
5. Save as PLAN.md or tasks/*.md.
6. Require user approval of the plan before coding.

## Verification
- [ ] Every task has explicit acceptance criteria
- [ ] Dependencies declared
- [ ] Plan approved by user
- [ ] No task larger than ~4 hours
