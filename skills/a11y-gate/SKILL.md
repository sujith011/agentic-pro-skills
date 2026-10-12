---
name: a11y-gate
description: "Verify accessibility for changed web interactions with automated checks plus manual keyboard and targeted assistive-technology testing."
---

# Accessibility Gate
Use WCAG 2.2 AA as the default web target unless the project specifies another target. This workflow is an affected-flow check, not a certification.

## Process
1. Identify changed controls, states, and applicable criteria.
2. Run an automated checker on affected pages and states; inspect findings.
3. Manually test keyboard operation, logical focus order, visible/unobscured focus, and absence of unintended traps.
4. Verify accessible names, roles, error identification, and dynamic announcements. Use a screen reader for changed interactions whose semantics or announcements matter.
5. Check normal text contrast at least 4.5:1, large text at least 3:1, and applicable UI/non-text contrast at least 3:1, accounting for criterion exceptions.
6. Check zoom/reflow, and target size against the applicable 24-by-24 CSS pixel minimum or allowed exceptions.
7. Fix confirmed blockers; record any untested criteria and explicitly justified exceptions.

## Example
For a modal, test focus entry, tab containment, Escape, focus return, and the announced dialog name. An automated scan cannot establish all of these.

## Stop conditions
An automated pass is not a substitute for manual interaction testing. Do not claim full WCAG conformance from this checklist.

## Evidence
- [ ] Tool output and manual steps identify the tested states.
- [ ] Focus, labels, errors, and applicable contrast are checked.
- [ ] Targeted screen-reader results and limitations are recorded.

Criterion reference: https://www.w3.org/TR/WCAG22/
