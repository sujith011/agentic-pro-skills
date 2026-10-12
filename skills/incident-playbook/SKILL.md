---
name: incident-playbook
description: "Write the incident response steps before the feature ships. Use for any change that can cause user-visible failure."
type: workflow
lifecycle: active
---

# Incident Playbook — Know How to Recover

Do not ship something you do not know how to fix at 2 a.m.

## Process
1. List the most likely failure modes.
2. Write the detection signal for each.
3. Write the immediate mitigation (rollback, flag off, etc.).
4. Note who to page and what data to collect.
5. Store the playbook next to the code.

## Verification
- [ ] Failure modes listed
- [ ] Mitigation steps written
- [ ] Playbook accessible
