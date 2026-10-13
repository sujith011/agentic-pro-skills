---
name: frontend-state
description: "Design or fix client, URL, and server state ownership, including request races, optimistic updates, and session changes."
---

# Frontend State

## Process
1. Classify each value: durable server data, shareable URL/navigation state, form draft, or temporary presentation state. Choose one authoritative owner.
2. Reuse the installed state/data-fetching tools. Keep local state near its consumers; introduce shared state only for a concrete coordination need.
3. Key server caches by all query and authorization dimensions. Clear or isolate them on logout, tenant switching, and identity changes.
4. Model loading, empty, error, and success states explicitly. For concurrent requests, cancellation can reduce work, but also guard result acceptance so an older response cannot replace a newer intent.
5. For optimistic mutations, reconcile with the server and define failure behavior. A rollback must not erase a newer successful mutation; track operations or use the library's supported concurrency pattern.
6. Verify back/forward navigation, retries, rapid input changes, failed mutations, and account switching.

## Example
Searching for A then B returns B first and A later. The displayed results remain B, and the URL reflects the current search rather than the response completion order.

## Stop conditions
Do not replace the state library to solve a local race. Duplicating the same server value into independent global stores creates a synchronization obligation.

## Evidence
- State ownership map and cache keys.
- Race/rollback/session-transition checks.
- Visible loading and recovery behavior.

## Reference
Workflow independently written after reviewing [react-state-management](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/react-state-management/SKILL.md).
