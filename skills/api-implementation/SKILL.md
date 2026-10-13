---
name: api-implementation
description: "Implement an HTTP endpoint from an agreed contract, including authorization, pagination, concurrency, and safe retry behavior."
---

# API Implementation

## Process
1. Read the existing routing, validation, authentication, error, and persistence conventions. Keep the agreed contract and framework versions visible.
2. Validate at the request boundary and derive identity from trusted authentication. Query resources within the caller's authorized scope; reject unexpected writable fields.
3. Bound list size and define stable ordering. For cursor pagination, include a unique tie breaker and document behavior during concurrent changes.
4. For mutations, define transaction boundaries, conditional updates, and duplicate-request handling. An idempotency record must bind the key to identity, operation, and payload; concurrent requests need atomic arbitration.
5. Map expected failures to the existing error format without returning internal details. Test allowed access, denial, malformed input, conflict, and retry after ambiguous success.

## Example
A retry of order creation returns the original result for the same caller/key/body. Reusing that key with a different body produces a conflict; two simultaneous requests cannot create two orders.

## Stop conditions
A valid token does not establish resource ownership. Do not invent a new error protocol or blanket retry mutations without reviewing the contract.

## Evidence
- Contract and relevant version references.
- Authorization and concurrency checks.
- Observed responses and explicitly unverified integrations.

## Reference
Workflow independently written after reviewing [api-design-principles](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/api-design-principles/SKILL.md).
