---
name: curated-context
description: "Feed the agent the right information at the right time. Use at session start, task switch, or when output quality drops."
type: workflow
lifecycle: active
---

# Context Packing — Right Information, Right Time

Do not dump the entire codebase. Curate what the agent needs for the current task.

## Process
1. Identify the task scope.
2. Load only: relevant files, conventions, recent decisions, open constraints.
3. Prefer summaries and pointers over full pastes when possible.
4. Update context when the task changes.
5. Explicitly drop irrelevant context.

## Verification
- [ ] Context matches current task
- [ ] No unnecessary large files loaded
- [ ] Key conventions and constraints are present
