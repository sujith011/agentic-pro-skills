---
name: contract-first
description: "Specify inputs, outputs, compatibility, and failure semantics before changing a public API or module boundary."
---

# Contract First
Resolve ambiguities at the boundary rather than hiding them in implementation.

## Process
1. Identify consumers and the authoritative contract (types, schema, protocol, or docs).
2. Define valid input, output, error codes, authorization, and invariants.
3. For state-changing calls, decide idempotency, concurrency, and partial-failure semantics where applicable.
4. Include examples for success, invalid input, and compatibility with existing callers.
5. Implement against the contract and verify it through the public interface.

## Example
An order-creation API defines the idempotency-key scope and what happens when the same key is reused with a different payload.

## Stop conditions
Do not use silent fallbacks or broad optional types to hide an unresolved invariant. Ask if it changes public behavior.

## Evidence
- [ ] Consumers and error semantics are explicit.
- [ ] Contract tests exercise applicable edge cases.
- [ ] Existing callers remain compatible or have a migration path.
