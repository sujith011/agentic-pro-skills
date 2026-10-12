---
name: incident-playbook
description: "Prepare a concise recovery runbook for a new critical path or an operationally risky release."
---

# Incident Playbook
Make detection and recovery executable for the person on call.

## Process
1. Identify likely failures and the observable signal for each.
2. Record impact, diagnostic query/dashboard, and initial mitigation.
3. Include exact environment-specific recovery commands only after verifying their target and expected effect.
4. State who owns escalation, how to verify recovery, and when to stop a failing mitigation.
5. Rehearse in a safe environment where practical and store beside existing runbooks.

## Example
For a queue backlog: inspect age/error metrics, identify a poisoned payload, pause the affected consumer if authorized, and verify age falls after mitigation.

## Stop conditions
Do not invent on-call contacts, publish secrets in commands, or execute destructive production recovery solely because a runbook describes it.

## Evidence
- [ ] Detection and mitigation are actionable.
- [ ] Owner, recovery verification, and abort conditions exist.
- [ ] Rehearsed steps and untested assumptions are distinguished.
