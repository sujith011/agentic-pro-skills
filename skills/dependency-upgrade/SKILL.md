---
name: dependency-upgrade
description: "Upgrade a dependency or framework through verified compatibility, migration guidance, reproducible installs, and relevant runtime checks."
---

# Dependency Upgrade

## Process
1. Record installed and target versions, runtime/toolchain requirements, direct/transitive dependents, and why the upgrade is needed.
2. Read the target's official release/migration notes and package metadata. Verify current support and known issues rather than assuming a newer version is compatible.
3. Choose the smallest coherent upgrade set. Framework peers or tightly coupled packages may need to move together; unrelated packages do not.
4. Preserve the existing lockfile workflow. Review codemods before running them, keep user edits intact, and inspect generated/configuration changes.
5. Check clean dependency resolution, type/build checks, changed behavior, and the relevant runtime/integration path. Audit output alone does not prove compatibility.
6. Document unavoidable contract/data changes and rollback feasibility. Compare package and lockfile changes for unexpected sources, scripts, or unrelated updates.

## Example
An ORM major upgrade changes transaction behavior. Update its required peer/runtime versions together and exercise a failed transaction followed by a valid request; a successful compile is insufficient.

## Stop conditions
Do not use force, ignore-peer flags, or a blanket latest upgrade to suppress unexplained conflicts. Release rollback may require data compatibility as well as the previous lockfile.

## Evidence
- Current/target versions and primary migration sources.
- Lockfile diff and clean install result.
- Relevant runtime checks and unresolved compatibility limits.

## Reference
Workflow independently written after reviewing [dependency-upgrade](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/dependency-upgrade/SKILL.md).
