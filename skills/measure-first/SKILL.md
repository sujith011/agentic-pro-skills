---
name: measure-first
description: "Diagnose a suspected performance or resource regression using a repeatable baseline before optimization."
---

# Measure First
Optimize the dominant measured cost and preserve correctness.

## Process
1. Define the metric, representative workload, environment, and acceptance target.
2. Warm up when appropriate and collect repeated baseline measurements.
3. Profile to localize the dominant cost rather than guessing.
4. Make one targeted change and rerun the same workload.
5. Compare distributions and resource usage, not a single best run. Recheck behavior.
6. Retain the change only if the measured benefit justifies complexity.

## Example
For slow list rendering, compare render duration and interaction latency on the same dataset/device before introducing memoization.

## Stop conditions
Do not claim a tiny improvement that is within measurement noise or compare different workloads as if they were equivalent.

## Evidence
- [ ] Baseline and candidate use comparable conditions.
- [ ] Profiling supports the targeted change.
- [ ] Results, variability, and correctness checks are recorded.
