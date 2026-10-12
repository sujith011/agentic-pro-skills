---
name: prd-first
description: "Write a complete, testable PRD before any code. Spec is the source of truth. Use when starting a feature, project, or significant change."
type: workflow
lifecycle: active
---

# PRD First — Spec Is the Contract

No implementation starts until the PRD is reviewed and explicitly approved.

## Required Sections
| Section | What it must contain |
|---------|----------------------|
| Objective | What and why, in one paragraph |
| Acceptance criteria | Numbered, testable statements |
| Out of scope | Explicit list of what will not be built |
| Commands | How to build, test, lint, and run |
| Boundaries | What the change may and may not touch |
| Success criteria | How we know it is done |

## Process
1. Draft every required section.
2. List open questions and resolve them with the user.
3. Require an explicit “yes” before any code or task breakdown.
4. Save as `SPEC.md` (or `docs/SPEC.md`) and commit it.
5. Only then allow planning or implementation.

## Anti-Rationalizations
- “I already know what to build” → Write it down anyway. Memory is not a contract.
- “We can refine the spec later” → Later is how scope creeps.
- “The acceptance criteria are obvious” → If they are not testable, they are not criteria.

## Verification
- [ ] Every required section is present
- [ ] Acceptance criteria are independently testable
- [ ] User gave an explicit approval
- [ ] SPEC.md is committed before any implementation commit
