---
name: python-service-design
description: "Implement or review Python HTTP service boundaries, request-scoped resources, async execution, and durable work using the installed framework."
---

# Python Service Design

## Process
1. Read the service's framework, validation library, ORM, Python version, and test conventions. Verify version-specific APIs against official documentation.
2. Separate request parsing, authorization, domain behavior, and persistence at existing seams. Define response schemas so internal or sensitive fields cannot leak through serialization.
3. Own database sessions and transactions at a clear request/job boundary; roll back on failure and close resources. Do not share mutable request sessions across concurrent tasks.
4. Trace blocking work inside async handlers. Use supported async clients or an appropriate bounded executor; async syntax alone does not make blocking I/O concurrent.
5. Bound external-call timeouts, streaming size, and cancellation. Durable business work needs a persistent worker/intent record rather than an in-process task that disappears on restart.
6. Use the existing dependency override/test setup. Check validation failures, access denial, transaction rollback, resource cleanup, and the actual HTTP serialization path.

## Example
An endpoint creates an order and then loses its outbound notification connection. Preserve the atomic order/outbox intent, return the contractually correct result, and let a durable worker handle delivery.

## Stop conditions
Do not switch frameworks or validation-library major versions during a local endpoint change. Mocked handler checks cannot establish database isolation or network timeout behavior.

## Evidence
- Version constraints and resource lifetime.
- Boundary and failure-path checks.
- Runtime/integration checks completed and remaining limits.

## Reference
Workflow independently written after reviewing [fastapi-pro](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/fastapi-pro/SKILL.md).
