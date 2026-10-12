---
name: quality-bar
description: "Define or check measurable acceptance thresholds for a project or a change with concrete reliability, security, or performance requirements."
---

# Quality Bar
Use the repository's existing bar first. Add thresholds only where they inform a decision.

## Process
1. Identify applicable constraints and the owner of each decision.
2. Record metric, workload or scope, threshold, measurement command, and evidence location in CONSTRAINTS.md or an existing equivalent.
3. Separate required checks from recommendations. Explain any justified not-applicable check.
4. Run affected checks and distinguish pass, fail, not run, and not applicable.
5. Change a threshold only with a recorded reason and the authorization required by the project.

## Example
"Search p95 below 300 ms at 20 requests/second on the staging dataset" is testable. "Fast search" is not. These numbers are examples, not universal defaults.

## Stop conditions
Do not lower a bar silently or replace behavior coverage with an arbitrary coverage percentage.

## Evidence
- [ ] Each required threshold has a repeatable method.
- [ ] Measured results identify environment and workload.
- [ ] Exceptions have reason, owner, and follow-up.
