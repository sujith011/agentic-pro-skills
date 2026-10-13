---
name: authorization-design
description: "Design and verify server-side access rules for roles, tenants, resource ownership, and sensitive actions."
---

# Authorization Design

## Process
1. Build a small action/resource matrix from the product's rules. Distinguish identity, role, tenant membership, resource ownership, and elevated actions.
2. Locate enforcement on every entry point: API, bulk operations, download URLs, background workers, and administrative tools. Client visibility is only presentation.
3. Bind tenant and subject to trusted credentials/context. Scope reads and writes at persistence access where practical; do not trust a tenant identifier supplied in the body.
4. Define revocation and caching behavior. Permission changes and session invalidation must have an explicit propagation window.
5. Test the same operation as owner, other owner in the same tenant, another tenant, unauthenticated caller, and revoked caller. Cover nested identifiers and mass assignment.
6. Inspect refresh/session rotation and concurrent use when that boundary changes; token parsing and a successful login alone cannot establish authorization.

## Example
Support can view an invoice summary but cannot download its attachment. Verify denial through the direct attachment endpoint and any signed-URL issuance path.

## Stop conditions
If access policy is materially unspecified, ask for that policy while inspecting independent code. Do not grant broad access to unblock implementation.

## Evidence
- Access matrix and enforcement locations.
- Allow/deny cases including direct requests.
- Revocation window and unavailable checks.

## Reference
Workflow independently written after reviewing [auth-implementation-patterns](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/auth-implementation-patterns/SKILL.md).
