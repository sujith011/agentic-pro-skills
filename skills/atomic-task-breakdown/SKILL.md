---
name: atomic-task-breakdown
description: "Break an agreed substantial change into ordered, independently verifiable tasks without adding another routine approval gate."
---

# Atomic Task Breakdown
Make the next useful increment clear without creating unnecessary ceremony.

## Process
1. Use the current acceptance criteria and identify dependencies.
2. Split by observable behavior or risk, not arbitrary file counts or estimated hours.
3. Give each task an outcome, touched boundaries, dependencies, verification method, and completion condition.
4. Put risky assumptions or integration seams early so they fail cheaply.
5. Save a short plan in the task, or PLAN.md for sustained work. Continue under existing implementation authorization.

## Example
For file uploads: prove upload/storage integration, enforce size/type/access rules, then expose the user flow. Each task includes failure-path verification.

## Stop conditions
Ask before a newly discovered scope expansion or consequential unresolved choice. Do not ask for plan approval merely because a plan exists.

## Evidence
- [ ] Tasks map to acceptance criteria.
- [ ] Dependencies and risky assumptions are visible.
- [ ] Each task can be verified without claiming unfinished work is complete.
