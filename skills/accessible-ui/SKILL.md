---
name: accessible-ui
description: "Implement interactive frontend behavior with semantic structure, usable states, and component boundaries."
---

# Accessible UI
Design the interaction states together with the happy path.

## Process
1. Define component responsibility and states: loading, empty, success, invalid input, and failure as applicable.
2. Prefer native controls and semantic HTML; ensure labels, keyboard operation, visible focus, and useful error messages.
3. For dialogs, establish initial focus, contained tab order, Escape behavior, and focus return.
4. Keep expensive work out of render paths and measure suspected regressions.
5. Verify critical flows in a real browser, including a narrow viewport and keyboard-only use.

## Example
A save action prevents accidental duplicate submissions, exposes progress, preserves entered values on failure, and announces success without moving focus unexpectedly.

## Stop conditions
Do not replace controls with clickable nonsemantic elements without reproducing keyboard and accessibility behavior.

## Evidence
- [ ] Important states and keyboard paths work.
- [ ] Labels, errors, and focus behavior are verified.
- [ ] Browser evidence names viewport and tested flows.
