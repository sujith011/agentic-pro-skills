---
name: threat-surface
description: "Review changed trust boundaries involving authentication, authorization, untrusted input, external requests, or sensitive data."
---

# Threat Surface
Trace an attacker-controlled input to its sensitive effect.

## Process
1. Map actors, assets, trust boundaries, and new data flows.
2. Enumerate concrete abuse cases for affected paths rather than applying every check indiscriminately.
3. Verify server-side authentication and resource/tenant authorization, including denied requests and cross-tenant identifiers.
4. Validate shape, type, size, and allowed values. Use parameterized queries and contextual output encoding; input sanitization alone is insufficient.
5. For outbound requests, restrict destinations and account for redirects and resolved addresses. For uploads, check size, type/content, storage, and execution exposure.
6. Inspect secret handling, logging/redaction, session/token lifecycle, and dependencies where touched.
7. Add focused abuse tests and record unresolved exposure with severity.

## Example
A supplier endpoint taking an invoice ID needs ownership enforcement even when the caller has a valid supplier token. Test another supplier's ID and assert no protected data is returned.

## Stop conditions
Do not test attacks against third-party or production systems without authorization. A checklist is not a penetration test; scanners and tests cover only their stated scope.

## Evidence
- [ ] Changed trust boundaries and attacker inputs are mapped.
- [ ] Applicable abuse cases have checks and outcomes.
- [ ] Authorization and sensitive-data handling are verified.
- [ ] Residual risks and coverage limits are explicit.
