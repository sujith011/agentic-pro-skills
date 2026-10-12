---
name: root-cause-debug
description: "Investigate a reproducible defect or unexpected behavior and verify the smallest supported root-cause fix."
---

# Root-Cause Debug
Maintain a falsifiable hypothesis, not a sequence of speculative patches.

## Process
1. Record expected versus actual behavior, environment, and minimal reproduction.
2. Inspect the path and form a hypothesis with a predicted observation.
3. Run the smallest diagnostic that can distinguish competing causes.
4. Reduce the reproduction and add a regression check that fails before the fix.
5. Fix the cause, rerun the reproduction and related checks, and explain why the result supports the hypothesis.

## Example
For intermittent duplicate records, investigate retries and transaction boundaries before adding a client-side disabled button.

## Stop conditions
If reproduction needs unavailable access, collect independent source evidence and mark the runtime conclusion unverified. Do not repeatedly make changes without new evidence.

## Evidence
- [ ] Trigger and environment are reproducible.
- [ ] Root cause is supported by a distinguishing observation.
- [ ] The regression check detects the defect and passes after repair.
