---
name: interface-design
description: "Design clean APIs and interfaces before implementation. Use when creating or changing public contracts, endpoints, or module boundaries."
type: workflow
lifecycle: active
---

# Interface Design — Contracts First

Define the interface. Then implement it.

## Process
1. List consumers of the interface.
2. Define inputs, outputs, errors, and invariants.
3. Prefer small, stable surfaces.
4. Document the contract (types, examples, error cases).
5. Implement against the documented contract.
6. Do not leak internals.

## Verification
- [ ] Contract documented before implementation
- [ ] Error cases explicit
- [ ] No unnecessary surface area
