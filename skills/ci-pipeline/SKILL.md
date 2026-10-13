---
name: ci-pipeline
description: "Create or repair repository CI with deterministic installs, meaningful failure propagation, safe trust boundaries, and verified required checks."
---

# CI Pipeline

## Process
1. Read supported runtimes, local commands, existing workflows, and repository rules. Select a useful OS/runtime matrix rather than every possible combination.
2. Install from the committed lockfile using the existing package manager. Key caches by relevant environment and lockfile inputs; do not treat cached output as fresh validation.
3. Run checks with preserved exit status and bounded timeouts. Publication must depend on the required validation result; do not hide failures with unconditional success or continue-on-error.
4. Separate untrusted pull-request validation from privileged publication. Inspect token scopes, action versions, runner trust, artifact paths, and commands that interpolate contributor-controlled text.
5. Pin third-party actions to reviewed commit SHAs when repository policy calls for it. Verify actual environment/branch protections; naming an environment does not configure approval.
6. Exercise the passing path and a deliberate failure on a safe topic branch when changing orchestration. Confirm the failed prerequisite blocks publication.

## Example
A Windows-only defect fails one matrix job. The aggregate required check fails and the publishing job cannot run, even though Linux passed.

## Stop conditions
Do not introduce deployment credentials into untrusted jobs. A workflow file that parses or an echo of 'deployed' is not evidence of a completed deployment.

## Evidence
- Exact commands and runtime matrix.
- Observed job/failure propagation.
- Trust/permissions model and unverified repository settings.

## Reference
Workflow independently written after reviewing [github-actions-templates](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/github-actions-templates/SKILL.md).
