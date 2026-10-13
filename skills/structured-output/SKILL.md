---
name: structured-output
description: "Consume model-generated JSON or typed responses with schema validation, semantic checks, bounded repair, and independent authorization for actions."
---

# Structured Output

## Process
1. Define the consumer's required schema and business invariants: units, ranges, allowed transitions, references, and treatment of missing information.
2. Check the selected provider/model's current structured-output support in official documentation. Prefer supported constrained output when useful, while handling refusal, truncation, timeout, and transport errors distinctly.
3. Parse and validate at the trust boundary. Reject unexpected fields where appropriate and distinguish invalid syntax, schema mismatch, and semantically wrong values.
4. Validate claims against trusted context. A valid object may contain an invented identifier or wrong amount. Model-generated permission, destination, and action fields do not authorize execution.
5. Bound repair/retry by attempts, deadline, and cost. Keep side effects outside retries; ambiguous external results require reconciliation.
6. Test empty/refused/truncated output, missing/extra fields, invalid references, malicious instructions, and valid-looking business-rule violations. Log sanitized diagnostics rather than unrestricted prompts/responses.

## Example
An invoice extraction returns valid JSON with a negative payable amount and an invented bank account. Reject the business-rule violations and never initiate a transfer from those fields.

## Stop conditions
Do not turn parsing failure into a fabricated default value. Schema conformance is only one acceptance condition, not proof of correctness or authorization.

## Evidence
- Schema and independent semantic rules.
- Failure-category and repair-budget checks.
- Consumer behavior and privacy-aware diagnostics.

## Reference
Workflow independently written after reviewing [llm-structured-output](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/llm-structured-output/SKILL.md).
