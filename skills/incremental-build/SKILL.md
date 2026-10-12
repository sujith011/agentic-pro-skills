---
name: incremental-build
description: "Implement in thin vertical slices: code, test, verify, commit. Use for any change touching more than one file. One slice at a time."
type: workflow
lifecycle: active
---

# Incremental Build — One Slice at a Time

Do not batch large changes. Finish one vertical slice completely before starting the next.

## Process
1. Pick the next task from the approved plan.
2. Implement the minimal change that satisfies the acceptance criteria.
3. Write or update tests first when possible.
4. Run the full relevant test suite.
5. Commit with a clear message.
6. Only then move to the next slice.

## Rules
- Prefer feature flags or safe defaults for risky changes.
- Never leave the codebase in a broken state.
- If a slice fails verification, fix it before proceeding.

## Verification
- [ ] Each slice has its own commit
- [ ] Tests pass for the slice
- [ ] No partial broken state left behind
