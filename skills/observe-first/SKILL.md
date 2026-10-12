---
name: observe-first
description: "Add logging, metrics, and tracing before the feature is considered done. Use for any user-facing or long-running change."
type: workflow
lifecycle: active
---

# Observability First — See It in Production

Do not ship a change you cannot observe.

## Process
1. Identify the key signals (errors, latency, success rate).
2. Add structured logs at decision points.
3. Emit metrics for the critical path.
4. Confirm traces or correlation IDs exist.
5. Document what to watch after deploy.

## Verification
- [ ] Logs present at key points
- [ ] Metrics defined
- [ ] What to alert on is written down
