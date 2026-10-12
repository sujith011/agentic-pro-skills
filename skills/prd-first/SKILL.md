---
name: prd-first
description: "Define testable scope for a new feature or significant behavior change; use a brief acceptance note for a small settled fix."
---

# PRD First
Make the intended behavior reviewable before implementation. Scale the document to the change.

## Process
1. Inspect relevant behavior and existing specifications before creating another source of truth.
2. For a small fix, record the trigger, expected outcome, and verification in the task or PR. For substantial work, create or update SPEC.md.
3. Include objective, acceptance criteria, boundaries, compatibility requirements, failure cases, and actual build/test/run commands.
4. Resolve unknowns that change product scope or irreversible actions. A direct implementation request or delegated judgment already authorizes routine implementation.
5. Update the spec if scope changes; keep documentation and code in the same reviewable change. Commit only when authorized by the task or repository convention.

## Example
Password-reset acceptance criteria include token expiry, single use, generic account-discovery responses, and expected behavior after a second request.

## Stop conditions
Do not invent requirements or repeatedly require "yes" for decisions already authorized. Mark unavailable verification commands honestly.

## Evidence
- [ ] Criteria describe observable behavior and failure cases.
- [ ] Boundaries and compatibility are explicit.
- [ ] Commands are verified or marked unavailable.
- [ ] Implementation matches the current scope.
