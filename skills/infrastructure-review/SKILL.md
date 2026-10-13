---
name: infrastructure-review
description: "Review Terraform or OpenTofu changes against the intended environment, state, plan, replacement risk, and authorized apply scope."
---

# Infrastructure Review

## Process
1. Identify provider/tool versions, lockfile, backend, workspace, account/project, region, and environment. Confirm the target before operations that contact infrastructure.
2. Review configuration and static validation first. Explain whether plan generation refreshes remote state, invokes external data sources, or needs credentials; plan is not always an offline operation.
3. Protect state and plan artifacts as potentially sensitive. Inspect locking, recovery, and concurrent-change behavior for the actual backend.
4. Read the plan for deletes/replacements, address moves, permission changes, public exposure, quotas/cost, and unknown values. A smaller textual diff may still destroy a large resource.
5. Separate code review from apply. If apply is authorized, verify the final plan matches the authorized target and revision, and avoid a stale plan after intervening changes.
6. Define service/data recovery for failures. Reapplying old configuration may not restore destroyed data; record post-apply checks if execution is in scope.

## Example
Renaming a resource address schedules destruction and recreation of a database. Use the tool's supported move/import approach and verify the resulting plan preserves the intended resource identity.

## Stop conditions
Do not force-unlock, rewrite state, or apply changes to escape a mismatch without resolving ownership and authorization. Redacting display output does not remove secrets from stored artifacts.

## Evidence
- Environment/revision and tool/provider versions.
- Reviewed plan effects and sensitive artifact handling.
- Recovery expectations and checks actually executed.

## Reference
Workflow independently written after reviewing [terraform-specialist](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/terraform-specialist/SKILL.md).
