---
name: pre-ship-gate
description: "Assess release readiness immediately before an authorized production deployment or release."
---

# Pre-Ship Gate
Prepare a concrete go/no-go decision using applicable evidence.

## Process
1. Compare the final behavior with acceptance criteria and current release scope.
2. Gather relevant test/build, review, security, compatibility, and migration evidence.
3. Verify environment configuration, deployment target, rollback or forward-recovery procedure, and monitoring.
4. For risky changes, identify rollout cohort, abort thresholds, and an owner watching the release.
5. Record each applicable check as pass, fail, not run, or justified not applicable.
6. Deploy only within existing authorization. If approval is required, present the finished artifact, target, evidence, and remaining risks for the final decision.

## Example
A schema-changing release includes old/new application compatibility, restore rehearsal, and expected lock duration; a static documentation release does not need that machinery.

## Stop conditions
A failed required check or unavailable evidence needed to establish safety is a no-go. Do not mark every box passed merely because tests passed.

## Evidence
- [ ] Scope, target, and applicable checks are recorded.
- [ ] Recovery and monitoring are usable.
- [ ] Go/no-go and authorization are explicit.
