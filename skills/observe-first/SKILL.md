---
name: observe-first
description: "Add diagnostic signals for a changed production path when failures, latency, or background work need operational visibility."
---

# Observe First
Choose signals that support a concrete decision without leaking data.

## Process
1. Identify success, failure, latency, and saturation signals for the changed path.
2. Reuse existing structured logging, metrics, and correlation/tracing conventions.
3. Include useful context while redacting secrets and sensitive payloads.
4. Bound label cardinality; do not use user IDs or raw URLs as unrestricted metric labels.
5. Verify a success and failure can be traced across the relevant boundary.
6. Document the dashboard/query and actionable alert threshold or explain why no new alert is needed.

## Example
For queued work, measure queue age and failed jobs and preserve a correlation ID; logging only "job started" cannot establish completion.

## Stop conditions
Do not instrument every routine UI change with a new metrics stack or log tokens, passwords, or personal data for convenience.

## Evidence
- [ ] Signals correspond to operational decisions.
- [ ] Success/failure visibility is checked.
- [ ] Redaction and label cardinality are considered.
