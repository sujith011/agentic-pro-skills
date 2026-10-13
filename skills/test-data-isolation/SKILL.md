---
name: test-data-isolation
description: "Prepare integration or end-to-end test data with explicit environment safeguards, per-run ownership, parallel isolation, and bounded cleanup."
---

# Test Data Isolation

## Process
1. Identify the storage target and current test configuration before writing. Use a dedicated test database/namespace; require an unambiguous environment marker for destructive setup.
2. Create synthetic data with a unique run identifier and the minimum relationships needed. Never import production credentials or personal records to make a test realistic.
3. Separate identities/organizations for access-control tests. Use independent transactions/connections when testing concurrency; a single test transaction can conceal real races.
4. Choose rollback, truncation, or targeted deletion according to what the application actually touches. Background jobs and external effects may survive a test transaction.
5. Cleanup only resources owned by the run, respecting relationships and pending work. On setup/cleanup failure, report leftovers by synthetic identifier rather than deleting broadly.
6. Exercise parallel runs and verify no shared fixtures or global counters leak state. Distinguish sandbox setup failures from product behavior.

## Example
Two suites create organizations with distinct run IDs. Cleanup of suite A deletes only A's rows and queued tasks while suite B continues reading its data.

## Stop conditions
An uncertain database target blocks destructive setup, not independent source review. Never use an unrestricted DELETE or drop operation based only on a filename containing 'test'.

## Evidence
- Verified target identity and environment marker.
- Owned-resource list and cleanup result.
- Parallel/isolation checks and any residual test data.

## Reference
Workflow independently written after reviewing [test-driven-development](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/test-driven-development/SKILL.md).
