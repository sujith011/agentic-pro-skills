---
name: load-proof
description: "Measure capacity or concurrency-sensitive behavior when a backend change affects throughput, resource use, or latency under load."
---

# Load Proof
Use load testing where capacity or contention is a material risk.

## Process
1. Define representative request mix, data size, concurrency, arrival rate, and duration.
2. Set acceptance thresholds for latency percentiles, errors, saturation, and recovery before running.
3. Use an isolated local or staging environment with synthetic data and a bounded workload.
4. Establish baseline, ramp up gradually, and stop at the agreed error/saturation boundary.
5. Observe database connections, queue depth, CPU/memory, and downstream pressure as relevant.
6. Compare against baseline and confirm recovery after load ends.

## Example
A token refresh change may need a targeted concurrent-request test rather than a broad high-volume service benchmark.

## Stop conditions
Do not load-test production or third-party services without explicit authorization. Do not prescribe a load test for changes with no capacity impact. Stop if test traffic threatens shared resources.

## Evidence
- [ ] Workload, duration, environment, and thresholds are recorded.
- [ ] Latency distribution, error rate, and saturation are measured.
- [ ] Recovery and any bottlenecks are documented.
