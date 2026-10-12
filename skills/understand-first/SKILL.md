---
name: understand-first
description: "Inspect affected behavior and dependencies before making a non-trivial change to an existing system."
---

# Understand First
Establish what the system currently does before deciding how to change it.

## Process
1. Locate repository instructions, affected entry points, callers, and tests.
2. Trace the successful path and at least the relevant failure path.
3. Summarize invariants, ownership boundaries, persistence effects, and compatibility.
4. Run the smallest baseline check that can distinguish an existing failure from a regression.
5. Choose the smallest change consistent with those findings.

## Example
Before changing refresh tokens, inspect issuance, consumption, persistence, and concurrent refresh callers rather than only the controller.

## Stop conditions
Do not infer backend correctness from a mocked UI or a successful compile. If source or runtime is unavailable, identify that limit.

## Evidence
- [ ] Relevant source and callers were inspected.
- [ ] Current behavior and invariants are stated.
- [ ] Baseline and implementation risks are recorded.
