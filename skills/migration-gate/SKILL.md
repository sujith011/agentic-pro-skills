---
name: migration-gate
description: "Plan and gate any data or schema migration. Use before changing persistent data structures."
type: workflow
lifecycle: active
---

# Migration Gate — Safe Data Changes

Never change schema or data without a reversible plan.

## Process
1. Write the migration steps and the rollback steps.
2. Test the migration on a copy of production-like data.
3. Confirm the application works against both old and new during the transition.
4. Schedule the migration with a monitoring window.
5. Only then execute.

## Verification
- [ ] Rollback documented and tested
- [ ] Dual-compatibility verified
- [ ] Monitoring plan exists
