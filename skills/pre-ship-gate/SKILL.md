---
name: pre-ship-gate
description: "Pre-launch verification. Use before any production deploy. Faster is safer only after the gates are passed."
type: workflow
lifecycle: active
---

# Ship Checklist — Verify Before You Deploy

Do not ship until every item is checked.

## Checklist
- [ ] Spec and plan still match what was built
- [ ] All tests pass (unit, integration, relevant e2e)
- [ ] Review completed and must-fix items resolved
- [ ] Constraints still met
- [ ] Rollback plan exists
- [ ] Monitoring / logs will catch failure
- [ ] Feature flag or staged rollout considered

## Process
1. Run the checklist.
2. Block ship on any unchecked item.
3. Record the go decision.

## Verification
- [ ] Checklist completed
- [ ] Explicit go/no-go decision recorded
