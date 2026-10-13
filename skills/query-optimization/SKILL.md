---
name: query-optimization
description: "Diagnose a slow database query using workload evidence and execution plans, then verify a bounded change without altering result semantics."
---

# Query Optimization

## Process
1. Capture the exact query shape, parameters, cardinality, concurrency, latency distribution, and database/version. Inspect ORM-generated SQL and repeated queries.
2. Obtain an estimated plan first. Actual-plan tools such as EXPLAIN ANALYZE execute the statement; use an authorized safe environment and a bounded workload. A rollback cannot undo every external or sequence side effect.
3. Compare estimated and actual row counts, scanned rows, joins, sorts/spills, index usage, lock waits, and network/materialization cost. A sequential scan may be correct for a broad result.
4. Change one cause: query shape, unnecessary columns, batching, index, or statistics. Account for index write/storage cost and deployment lock behavior.
5. Re-measure with representative data, several parameter distributions, and comparable cache conditions. Confirm identical ordering, null handling, and authorization.

## Example
A list endpoint makes one customer query per row. Fetch the required customer summaries in a bounded batch and compare query count and latency while preserving pagination order.

## Stop conditions
Do not run heavy plans or index operations against production without target authorization. Do not force index usage solely because a scan appears in a plan.

## Evidence
- Before/after SQL, plans, and dataset context.
- Latency/query-count measurements.
- Result-equivalence checks and rollout cost.

## Reference
Workflow independently written after reviewing [postgresql-optimization](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/postgresql-optimization/SKILL.md).
