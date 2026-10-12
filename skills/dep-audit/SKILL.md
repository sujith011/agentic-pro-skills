---
name: dep-audit
description: "Audit dependencies for known vulnerabilities and unnecessary packages. Use before adding or upgrading any dependency."
type: workflow
lifecycle: active
---

# Dependency Audit — Know What You Ship

Do not add a dependency without checking its risk and necessity.

## Process
1. List the proposed dependency and its transitive tree.
2. Check for known CVEs and license compatibility.
3. Confirm no existing package already solves the need.
4. Prefer the smallest, most maintained option.
5. Record the decision.

## Verification
- [ ] CVE check completed
- [ ] License compatible
- [ ] Necessity justified
