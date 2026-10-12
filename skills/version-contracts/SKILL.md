---
name: version-contracts
description: "Treat public interfaces as versioned contracts. Use when changing any API, library surface, or exported type."
type: workflow
lifecycle: active
---

# Version Contracts — Stable Surfaces

Breaking changes require an explicit version bump and migration path.

## Process
1. Identify all public consumers.
2. Decide if the change is additive, compatible, or breaking.
3. For breaking changes, write a migration guide and bump the major version.
4. Keep the old contract working for at least one release when possible.
5. Document the change in the changelog.

## Verification
- [ ] Change classified (additive / compatible / breaking)
- [ ] Migration path exists for breaking changes
- [ ] Changelog updated
