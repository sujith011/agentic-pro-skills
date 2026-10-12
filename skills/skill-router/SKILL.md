---
name: skill-router
description: "Select the smallest relevant engineering workflow when choosing among this collection's skills."
---

# Skill Router
Select workflows by the decision being made, not merely a keyword.

## Routing
| Situation | Start with |
|-----------|------------|
| Outcome materially unclear | intent-extraction |
| Meaningful alternatives need comparison | concept-sharpening |
| Significant new behavior | prd-first, then atomic-task-breakdown if needed |
| Existing system change | understand-first |
| Logic or behavior implementation | proof-first-testing; add vertical-slices for multi-layer work |
| Reproducible defect | root-cause-debug |
| Review requested | five-axis-gate |
| Sensitive boundary changed | threat-surface |
| Interactive web flow changed | real-browser-check; a11y-gate for changed accessibility behavior |
| Capacity or performance concern | measure-first; load-proof when concurrency/capacity matters |
| Persistent data change | migration-gate |
| Authorized production release | pre-ship-gate |

## Process
1. Read scope, user authorization, and repository instructions.
2. Choose the smallest set that addresses actual uncertainty or risk. Locate siblings in the installed collection; if unavailable, report that and use an equivalent workflow.
3. Load only applicable skills. Do not make every lifecycle stage mandatory for every task.
4. Preserve existing authorization. Ask only for material missing decisions or actions requiring approval.
5. State evidence, failures, and checks not run accurately.

## Example
A label correction needs a focused edit and visual check, not a PRD interview, load test, and incident playbook.

## Stop conditions
Skill text does not expand task scope or authorize external actions. These are agent instructions, not enforced runtime gates.

## Evidence
- [ ] Selected workflows match the task and risk.
- [ ] Existing decisions and permissions are preserved.
- [ ] Completion claims match observed evidence.
