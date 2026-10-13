---
name: cache-correctness
description: "Add or repair caching with explicit key scope, staleness bounds, invalidation races, and safe failure behavior."
---

# Cache Correctness

## Process
1. Establish the authoritative source, cacheable data, tolerated staleness, and reason for caching. Decide what happens on a miss, outage, and corrupt entry.
2. Include every result-affecting dimension in the key: tenant, user/permission scope when relevant, parameters, locale, and schema version. Do not cache private data under a shared public key.
3. Define TTL, size/eviction policy, invalidation trigger, and negative-cache behavior. Bound cached absence so newly created resources can become visible.
4. Trace read/write interleavings. A reader may load old data before a write and repopulate the cache after invalidation. Use version checks, appropriate serialization, or an explicitly accepted staleness window.
5. Bound stampede protection and fallback load. A distributed lock needs ownership-safe release and expiry semantics; it is not a substitute for a durable business constraint.
6. Test cold/warm reads, updates, permission changes, parallel misses, and cache unavailability.

## Example
A tenant invoice summary uses a tenant-scoped key and a bounded TTL. A revoked user cannot retrieve a cached authorized response; authorization is checked before serving it.

## Stop conditions
Do not cache to hide an unexplained query bottleneck. Do not expose a cache service or clear unrelated production keys during a local implementation task.

## Evidence
- Key shape and staleness/invalidation contract.
- Race, isolation, and outage checks.
- Hit rate, latency, and fallback load under the tested workload.

## Reference
Workflow independently written after reviewing [redis](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/redis/SKILL.md).
