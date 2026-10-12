---
name: performance-audit
description: "Measure before you optimize. Use when latency, load time, or resource use is in question. Prefer evidence over guesses."
type: workflow
lifecycle: active
---

# Performance Audit — Measure Before Optimize

Do not optimize without a measurement that shows the problem.

## Process
1. Define the metric that matters (LCP, response time, memory, etc.).
2. Measure the current baseline.
3. Identify the dominant cost.
4. Make the smallest change that addresses it.
5. Re-measure and confirm improvement.
6. Stop if the gain is negligible.

## Verification
- [ ] Baseline measured
- [ ] Change targeted at measured bottleneck
- [ ] Post-change measurement shows improvement or is abandoned
