---
name: dep-audit
description: "Assess necessity, supply-chain exposure, licensing, and compatibility before adding or upgrading a dependency."
---

# Dependency Audit
Review the resolved dependency graph, not only the requested package name.

## Process
1. Check whether existing packages or the standard library meet the need.
2. Verify exact package identity, source, maintenance, license, and install scripts.
3. Inspect affected lockfile changes and transitive dependencies.
4. Run the ecosystem's supported audit against the resolved versions and record date/tool. Read advisories for applicability and exploitability.
5. For upgrades, read release/migration notes and run affected behavior tests.
6. Record accepted risks with owner and remediation plan; keep the lockfile consistent.

## Example
A vulnerable transitive development tool and an exposed production parser have different impact. Neither a clean audit nor a package's popularity establishes safety.

## Stop conditions
Do not run blanket forced upgrades, blindly execute install scripts, or claim "no vulnerabilities" when the advisory check was unavailable.

## Evidence
- [ ] Necessity and exact package identity are checked.
- [ ] Audit scope/results and license are recorded.
- [ ] Upgrade compatibility and lockfile changes are verified.
