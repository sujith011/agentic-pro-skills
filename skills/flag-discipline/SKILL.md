---
name: flag-discipline
description: "Use feature flags for risky or incomplete changes. Use when a change cannot be fully rolled back by deploy alone."
type: workflow
lifecycle: active
---

# Feature Flag Discipline — Safe Rollouts

Ship behind a flag when the blast radius is large.

## Process
1. Decide if the change needs a flag.
2. Default the flag to off.
3. Implement the gated path and the old path.
4. Add a way to turn the flag on and off without a deploy.
5. Remove the flag after the change is proven.

## Verification
- [ ] Flag defaults to off
- [ ] Both paths work
- [ ] Removal plan exists
