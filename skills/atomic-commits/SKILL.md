---
name: atomic-commits
description: "Prepare coherent Git commits when the user or repository workflow authorizes committing changes."
---

# Atomic Commits
Preserve user work and make each commit understandable on its own.

## Process
1. Inspect status and diff before staging; distinguish current task edits from existing work.
2. Group one logical behavior or repair with its necessary tests/docs.
3. Stage explicit paths or hunks and inspect the staged diff for unrelated edits and secrets.
4. Run appropriate checks and write an intent-focused message.
5. Commit when authorized; pushing, merging, and history rewriting require their own scope/authorization.

## Example
A validation fix and its regression test belong together. An unrelated dependency upgrade does not.

## Stop conditions
Do not stage everything blindly, reset user work, amend another person's commit, or rebase shared history without authorization. A read-only review never authorizes a commit.

## Evidence
- [ ] Staged changes match task scope.
- [ ] Message explains the behavioral change or reason.
- [ ] Verification is recorded and user work is preserved.
