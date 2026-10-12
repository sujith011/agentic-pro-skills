---
name: vertical-slices
description: "Implement in thin vertical slices. One behavior, one commit. Use for any change touching more than one file."
type: workflow
lifecycle: active
---

# Vertical Slices — One Tracer Bullet at a Time

Finish one complete vertical slice (behavior + test + commit) before starting the next.

## Process
1. Pick the next acceptance criterion from the approved plan.
2. Implement the smallest change that satisfies it end-to-end.
3. Prove it with a test at the public seam.
4. Run the relevant test suite.
5. Commit with a message that names the behavior.
6. Only then start the next slice.

## Rules
- **One slice, one commit.** No mixed changes.
- **Never leave the codebase broken.** If the slice fails, fix it before proceeding.
- **Prefer flags or safe defaults** for anything that cannot be rolled back by a single commit.
- **Tracer bullet first.** The first slice should prove the path works, even if it is incomplete.

## Anti-Rationalizations
- “I’ll batch these small changes” → Batching hides failures and makes review harder.
- “The tests can come later” → Later is when the slice is already wrong.
- “This is too small to commit” → Small commits are the point.

## Verification
- [ ] Each slice has its own commit
- [ ] Tests for the slice pass
- [ ] The codebase is green after every commit
- [ ] No unrelated changes are mixed into the slice
