---
name: root-cause-debug
description: "Investigate a reproducible defect or unexpected behavior and verify the smallest supported root-cause fix."
---

# Root-Cause Debug
Maintain a falsifiable hypothesis, not a sequence of speculative patches.

## Process
1. Record expected versus actual behavior, the trigger, environment, and a minimal reproduction. Inspect the current diff and preserve unrelated work; a read-only investigation does not authorize a repair.
2. Run the reproduction before editing. Distinguish a product defect from a missing dependency, wrong working directory, permission failure, or invalid test setup. Correct the setup within scope or report the blocker; a setup error is not evidence for a product fix.
3. Inspect the relevant path and state a falsifiable hypothesis: suspected cause, predicted observation, and the smallest diagnostic that could disprove it. If evidence contradicts it, revise the hypothesis before another patch.
4. Reduce the reproduction and add a regression check that fails for the observed behavior. If it already passes, check the trigger, executed code, and assertion; do not weaken the expected behavior just to manufacture a red result. For timing bugs, use controlled ordering or a reliable runtime observation rather than arbitrary sleeps.
5. Fix the supported cause, rerun the original reproduction, then the targeted test and related checks. Explain how the changed behavior supports the diagnosis. Do not count an agent's proposed command as an executed check.

## When the defect cannot be reproduced
Separate observed facts from hypotheses. Inspect independent source evidence and identify the missing environment or trigger. If a source-supported repair is authorized, label it as unverified at runtime and specify the check needed to verify it. Do not claim a before/after failure sequence that did not occur.

## Example
For duplicate credits, call the same job ID twice and observe the ledger. If both calls append, test identical retries and conflicting payloads under that ID before repairing the effect boundary. A disabled client button does not address redelivery. An in-memory fixture cannot establish concurrent database or provider behavior.

## Stop conditions
If reproduction needs unavailable access, collect independent source evidence and mark the runtime conclusion unverified. Stop speculative patching when a diagnostic yields no new evidence. Keep failing checks visible; do not remove assertions, skip a failure, or claim a fix from a green test that misses the trigger.

## Evidence
- [ ] Trigger and environment are reproducible.
- [ ] Root cause is supported by a distinguishing observation.
- [ ] The regression check detects the defect and passes after repair.
- [ ] Original reproduction and relevant checks were rerun, with command, working directory, exit status, and actual result recorded.
- [ ] Missing checks, setup blockers, and runtime limits are explicit.
