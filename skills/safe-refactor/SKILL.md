---
name: safe-refactor
description: "Change internal structure while preserving behavior, using characterization checks when existing coverage is insufficient."
---

# Safe Refactor
Establish a safety net before structural changes.

## Process
1. Identify public behavior, callers, and relevant baseline checks.
2. If coverage is missing, add characterization tests or a repeatable observational baseline before refactoring.
3. Make one coherent structural change without adding feature behavior.
4. Run affected checks after each step; run broader checks when dependencies or risk justify them.
5. Review compatibility and unintended changes. Commit coherent increments only when authorized.

## Example
Before replacing a parser, capture behavior for valid, malformed, and boundary inputs, including error messages relied on by callers.

## Stop conditions
Do not infer equivalent behavior solely from a successful build. Stop or reduce scope if a meaningful baseline cannot be established.

## Evidence
- [ ] Safety net existed before restructuring.
- [ ] Relevant observable outcomes remain equivalent.
- [ ] Diff contains only the intended structural change.
