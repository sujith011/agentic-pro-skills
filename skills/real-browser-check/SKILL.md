---
name: real-browser-check
description: "Exercise critical interactive web flows in a real browser after a UI or integration change."
---

# Real Browser Check
Verify the user's observable flow and state transitions.

## Process
1. Select flows affected by the change, with expected outcomes and test data.
2. Run against the intended local or staging environment using an isolated test account when writes are involved.
3. Exercise success, validation/failure, keyboard use, and relevant responsive layout.
4. Inspect console and network results; distinguish existing errors from regressions.
5. Record browser, viewport, environment, steps, and evidence. Automated assertions are preferred for repeatable behavior; screenshots supplement them.

## Example
For checkout, verify totals, validation, a simulated declined payment, and successful completion using a test provider.

## Stop conditions
Do not perform purchases or alter production records without authorization. A mocked backend verifies UI behavior only; a screenshot alone does not verify an interactive flow.

## Evidence
- [ ] Critical flows have observed outcomes.
- [ ] Console/network findings are accounted for.
- [ ] Backend and environment limits are disclosed.
