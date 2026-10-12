---
name: version-contracts
description: "Assess compatibility and plan migration when changing a published API, package surface, or externally consumed type."
---

# Version Contracts
Classify compatibility using real consumers and the project's versioning policy.

## Process
1. Identify public consumers and supported versions.
2. Check source, wire, and behavior compatibility, including errors, defaults, and ordering.
3. Add contract tests for existing consumers when feasible.
4. For a breaking change, document upgrade steps and follow the project's versioning/deprecation policy.
5. Define the compatibility window and removal condition; record the change in release notes.

## Example
Adding a required response field is usually additive for tolerant clients, but adding an enum variant can break exhaustive consumers. Inspect the consumers before classifying it.

## Stop conditions
Do not mandate a package major-version bump for every internal API or invent a deprecation window the project cannot support.

## Evidence
- [ ] Compatibility classification includes consumer evidence.
- [ ] Breaking changes have actionable migration steps.
- [ ] Release/version changes follow project policy.
