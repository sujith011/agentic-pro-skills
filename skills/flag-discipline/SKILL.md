---
name: flag-discipline
description: "Plan a controlled rollout for a risky behavior change when a runtime switch can meaningfully limit its effects."
---

# Flag Discipline
A flag controls execution; it does not undo writes or external effects.

## Process
1. Identify the blast radius and whether disabling the path actually mitigates failure.
2. Define owner, safe default, audience selection, expiry/removal condition, and access to the switch.
3. Verify both enabled and disabled behavior, including unavailable flag-service fallback.
4. Keep authorization server-side; a UI flag is not an access-control boundary.
5. Roll out to a limited cohort and expand only with measured evidence.
6. Remove the flag and obsolete path once the removal condition is met and removal is within scope.

## Example
Flagging a new billing calculation requires reconciling already-issued invoices separately; turning the flag off cannot reverse them.

## Stop conditions
Do not use a flag as the rollback plan for an irreversible migration or payment side effect.

## Evidence
- [ ] Both paths and fallback are tested.
- [ ] Switch access, owner, and expiry are recorded.
- [ ] Persistent effects have a separate recovery plan.
