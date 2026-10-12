---
name: five-axis-gate
description: "Review a proposed change for correctness, readability, architecture, security, and performance with evidence appropriate to risk."
---

# Five-Axis Gate
Lead with consequential findings and give a concrete remedy.

## Process
1. Read the request, acceptance criteria, diff, and relevant surrounding code.
2. Check tests and whether they would detect the defect or behavior change.
3. Review each axis using the table below. Distinguish observed evidence from inference.
4. Categorize findings as critical, required, or optional; cite location, trigger, impact, and fix.
5. Record resolved items and explicitly accepted deferrals with owner and reason.
6. Give a verdict bounded by the checks actually performed.

| Axis | Evidence to seek |
|------|------------------|
| Correctness | Behavior and failure paths match criteria; appropriate tests or reproducible checks pass. |
| Readability | Names, control flow, and boundaries make the behavior understandable without hidden assumptions. |
| Architecture | Ownership and dependencies fit the system; new abstractions earn their cost. |
| Security | Relevant trust boundaries, authorization, input handling, and secret exposure were inspected. |
| Performance | Affected hot paths and resource risks were assessed; measure when a regression is plausible. |

## Example
An authorization finding names the endpoint and unauthorized caller that can read another tenant's data, with a suggested ownership check and regression case.

## Stop conditions
Do not approve a known exploitable defect or data-loss issue based on an unspecified future fix. Mark an axis not applicable with a reason when it truly has no affected surface. Do not mutate code during a read-only review.

## Evidence
- [ ] Each applicable axis has supporting evidence.
- [ ] Findings separate blockers from suggestions.
- [ ] Verdict includes test and runtime limitations.
