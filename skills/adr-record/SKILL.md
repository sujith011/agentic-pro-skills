---
name: adr-record
description: "Record a durable architecture decision when choosing among alternatives that affect system boundaries, compatibility, or operations."
---

# ADR Record
Capture why a lasting decision is appropriate for this system.

## Process
1. Locate existing ADRs and follow their numbering and format.
2. Record status, context, constraints, alternatives, decision, consequences, and evidence.
3. Include reversal cost and conditions that would justify revisiting the decision.
4. Link from the relevant specification or design document.
5. Supersede an older ADR explicitly instead of silently rewriting history.

## Example
An ADR selecting a queue should state required delivery semantics, retry/idempotency design, operational cost, and the alternatives rejected.

## Stop conditions
Do not create an ADR for every routine implementation choice or present an untested assumption as a benchmark.

## Evidence
- [ ] Decision follows stated constraints.
- [ ] Alternatives and consequences are specific.
- [ ] Status and revisit conditions are recorded.
