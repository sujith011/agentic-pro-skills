---
name: a11y-gate
description: "Verify accessibility before merge. Use for any user-facing UI change."
type: workflow
lifecycle: active
---

# Accessibility Gate — Inclusive by Default

Do not merge UI that fails basic accessibility checks.

## Process
1. Check keyboard navigation.
2. Verify screen-reader labels and roles.
3. Confirm color contrast meets the bar.
4. Test with a screen reader or automated checker.
5. Fix blockers before merge.

## Verification
- [ ] Keyboard works
- [ ] Labels present
- [ ] Contrast checked
