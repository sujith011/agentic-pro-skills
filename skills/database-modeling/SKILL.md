---
name: database-modeling
description: "Design relational entities, constraints, and transaction boundaries for new persisted behavior while preserving existing data semantics."
---

# Database Modeling

## Process
1. Start with actual reads/writes and domain invariants. Identify entity ownership, cardinality, identifiers, lifecycle, deletion, and retention requirements.
2. Put durable invariants in appropriate constraints: uniqueness, foreign keys, nullability, and valid values. Include tenant scope in uniqueness and references where the model requires it.
3. Define units, precision, timezone semantics, and representation of unknown values. Avoid floating-point money and distinguish missing from zero.
4. Determine which invariants span multiple rows and need transaction isolation, locking, or conditional updates. Application-side check-then-write alone can race.
5. Choose indexes from measured or expected query shapes, considering write cost and data growth. Document deliberate denormalization and how it stays consistent.
6. Apply the existing migration/recovery workflow for deployed data. Test concurrent writes, invalid relationships, and deletion behavior.

## Example
An organization-local invoice number is unique within the organization. A line item cannot reference an invoice from another organization, even if IDs are globally unique.

## Stop conditions
Do not change deployed schema or delete data during a design-only request. A syntactically valid migration is not evidence that existing records satisfy new constraints.

## Evidence
- Relationship sketch and invariants.
- Constraint and concurrency probes.
- Existing-data compatibility and migration limits.

## Reference
Workflow independently written after reviewing [database-design](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/database-design/SKILL.md).
