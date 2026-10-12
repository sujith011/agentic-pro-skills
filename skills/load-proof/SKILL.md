---
name: load-proof
description: "Prove performance under load before declaring a change ready. Use for any path that will see concurrent users."
type: workflow
lifecycle: active
---

# Load Proof — Measure Under Real Traffic

Unit tests do not prove capacity.

## Process
1. Define the expected load (requests per second, concurrent users).
2. Write or reuse a load test that hits the critical path.
3. Run it against a staging environment.
4. Confirm latency and error rate stay within the quality bar.
5. Only then allow the change to ship.

## Verification
- [ ] Load test exists
- [ ] Results meet the bar
- [ ] Bottlenecks identified if any
