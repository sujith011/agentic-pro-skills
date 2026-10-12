---
name: understand-first
description: "Read and understand existing code before modifying it. Use before any non-trivial change to an existing system."
type: workflow
lifecycle: active
---

# Codebase Grounding — Understand Before You Change

Do not modify code you have not read and summarized.

## Process
1. Locate the relevant modules, entry points, and tests.
2. Read the key files.
3. Summarize current behavior, patterns, and invariants.
4. Identify risks of the proposed change.
5. Only then plan the modification.

## Verification
- [ ] Relevant files were read
- [ ] Current behavior summarized
- [ ] Risks listed before coding starts
