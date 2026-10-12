---
name: atomic-commits
description: "Small, meaningful commits with clear messages. Use on every change. Keep history readable."
type: workflow
lifecycle: active
---

# Git Discipline — Clean History

One logical change per commit. Messages explain why.

## Process
1. Stage only the files that belong to the current slice.
2. Write a message that states the intent (not just "fix").
3. Commit.
4. Do not mix unrelated changes.
5. Prefer rebasing or clean history over merge commits for personal work.

## Verification
- [ ] Commit is atomic
- [ ] Message describes intent
- [ ] No unrelated files included
