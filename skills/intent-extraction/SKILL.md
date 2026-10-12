---
name: intent-extraction
description: "Clarify an underspecified outcome or conduct a requirements interview when material choices remain unresolved."
---

# Intent Extraction
Clarify what changes the implementation, then proceed within the user's authorized scope.

## Process
1. Read the request, relevant repository context, and decisions already made.
2. State the outcome, success criteria, constraints, and material unknowns. Avoid invented confidence percentages.
3. Ask one focused question at a time when different answers would change scope, cost, data handling, or behavior. Attach a reasonable recommendation.
4. Treat explicit delegation such as "use your judgment" as permission to decide routine details. Record the assumption and continue.
5. Restate the resulting scope briefly. Existing authorization is sufficient; request confirmation only for an unresolved consequential choice or a boundary requiring it.

## Example
"Add CSV export" may require asking which records the user can export. Delimiter choice can follow existing conventions without another approval.

## Stop conditions
Do not guess an access rule, destructive action, or materially different product outcome. Continue independent work while that question is pending.

## Evidence
- [ ] Outcome and acceptance criteria are concrete.
- [ ] Material unknowns are resolved or explicitly pending.
- [ ] Routine assumptions and existing authorization are preserved.
