---
name: e2e-journeys
description: "Test a complete user journey through a real application boundary using stable selectors, isolated state, and observable final outcomes."
---

# End-to-End Journeys

## Process
1. Define the user-visible outcome and real boundaries under test: browser, service, persistence, and external provider. Choose a controlled environment and identify which parts are simulated.
2. Provision isolated identities/data through supported setup interfaces. Give each run its own identifiers and clean up only the resources it owns.
3. Discover the rendered UI. Use role/name or deliberate test selectors and wait for observable state transitions; fixed sleeps hide races.
4. Exercise one critical success path and relevant denial/failure paths. Assert persisted business outcome as well as visible feedback when access permits.
5. For asynchronous work, wait within a bounded deadline for completion evidence. Retrying an assertion is different from repeatedly performing a side-effecting action.
6. Preserve sanitized traces/screenshots/logs on failure. Classify product defects, test defects, and environment failures before rerunning.

## Example
A buyer submits a draft request. Confirm its success message, resulting identifier, and visibility to the authorized buyer; verify a different organization cannot open it directly.

## Stop conditions
A mocked provider limits the claim to that simulated boundary. Do not make real purchases, send live notifications, or reuse production customer records without authorization.

## Evidence
- Environment, data ownership, and mocked boundaries.
- Action-to-persisted-outcome trace.
- Failure artifacts and checks not run.

## Reference
Workflow independently written after reviewing [webapp-testing](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/webapp-testing/SKILL.md).
