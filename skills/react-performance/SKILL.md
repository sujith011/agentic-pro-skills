---
name: react-performance
description: "Investigate measured React or Next.js interaction and loading bottlenecks while preserving rendering, accessibility, and data isolation."
---

# React Performance

## Process
1. Reproduce the slow route or interaction with a representative dataset and production-like build. Record timing, network waterfall, bundle cost, and render profile where available.
2. Locate whether the bottleneck is server work, sequential independent fetches, JavaScript transfer, repeated rendering, or expensive DOM work. Check framework/runtime versions before applying an API pattern.
3. Change the measured cause. Parallelize only independent requests, lazy-load nonessential heavy features, narrow subscriptions, or virtualize a large list when appropriate.
4. Use memoization when profiling and stable semantics justify it. Review dependencies, stale closures, cleanup, and existing compiler/framework optimization behavior.
5. Recheck data caching boundaries, hydration, keyboard/focus behavior, loading/error states, and small datasets. Virtualization can affect find-in-page and assistive technology.
6. Compare before/after under equivalent device, build, cache, and network conditions; report the distribution and dataset.

## Example
A dashboard awaits two unrelated read requests in sequence. Start both within the existing authorization scope and measure reduced load time without combining unrelated cache identities.

## Stop conditions
Do not claim improvement from fewer lines or a development render count alone. Avoid broad dependency or framework upgrades during a focused performance repair.

## Evidence
- Baseline profile and diagnosed cause.
- Comparable timing/profile after the change.
- Behavior/accessibility checks and measurement limits.

## Reference
Workflow independently written after reviewing [react-best-practices](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/react-best-practices/SKILL.md).
