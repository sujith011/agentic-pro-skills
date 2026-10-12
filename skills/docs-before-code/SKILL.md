---
name: docs-before-code
description: "Document usage and failure behavior when adding or changing a public feature, API, or user workflow."
---

# Docs Before Code
Use documentation to clarify the public contract before substantial implementation.

## Process
1. Find the existing canonical documentation and update it in place.
2. Write a realistic usage example, prerequisites, parameters, outputs, and likely errors.
3. Check that the example reveals ambiguous behavior or missing requirements.
4. Implement and execute the example where practical; verify documented commands.
5. Document compatibility and migration steps when behavior changes.

## Example
A pagination example should show continuation, empty results, and whether concurrent inserts can cause duplicates.

## Stop conditions
Do not create a separate approval gate for settled details or claim an example was run when it was only inspected.

## Evidence
- [ ] Example reflects the implemented public behavior.
- [ ] Failure cases and prerequisites are accurate.
- [ ] Commands were checked and limitations recorded.
