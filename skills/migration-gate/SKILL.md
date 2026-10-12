---
name: migration-gate
description: "Plan and verify a persistent schema or data change with compatibility and a realistic recovery strategy."
---

# Migration Gate
Distinguish rollback of code from recovery of data.

## Process
1. Classify the change as additive, transforming, or destructive. Estimate locks, runtime, storage, and affected rows.
2. Prefer expand -> backfill -> switch readers/writers -> contract when mixed application versions must coexist.
3. Define backup/restore or forward-repair strategy and rehearse it on production-like test data.
4. Make backfills resumable/idempotent, with batch limits and integrity checks.
5. Test old/new compatibility, interrupted migration, and validation queries.
6. Record environment, execution sequence, owner, monitoring, and abort conditions. Execute only within authorization for that environment.

## Example
Dropping a column after a new deployment is unsafe while older instances still read it. Delay contraction until all consumers are migrated.

## Stop conditions
Do not assume a down migration restores deleted data. Stop if required backup/recovery evidence or target authorization is missing.

## Evidence
- [ ] Compatibility and data-integrity checks pass.
- [ ] Recovery was rehearsed with outcome recorded.
- [ ] Execution is bounded and interruption behavior is known.
