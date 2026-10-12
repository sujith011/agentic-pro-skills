---
name: clarity-refactor
description: "Simplify proven behavior when control flow, duplication, or indirection increases understanding cost."
---

# Clarity Refactor
Remove concepts the reader must hold, rather than merely relocating code.

## Process
1. Establish the observable behavior and relevant passing baseline.
2. Identify one source of understanding cost: repeated branching, hidden state, misleading types, or pass-through abstraction.
3. Choose the smallest structural remedy and keep feature behavior unchanged.
4. Run relevant checks and review the diff for altered error, ordering, or state semantics.
5. Stop when further cleanup has no clear benefit.

## Example
Replace repeated branches on the same state with an explicit state model when it removes invalid combinations. Extracting each branch into another file may only move complexity.

## Stop conditions
Do not mix a feature change into cleanup or delete apparently unused public code without checking callers and compatibility.

## Evidence
- [ ] Baseline behavior is established.
- [ ] The change reduces concrete understanding cost.
- [ ] Observable behavior and compatibility remain unchanged.
