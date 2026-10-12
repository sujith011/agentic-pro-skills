---
name: real-browser-check
description: "Verify UI behavior in a real browser. Use for any user-facing change that cannot be fully proven by unit tests."
type: workflow
lifecycle: active
---

# Browser Verification — Real Browser Proof

Unit tests are not enough for interactive UI.

## Process
1. Identify the critical user flows.
2. Exercise them in a real browser (or headless with screenshots).
3. Check console errors, network failures, and layout.
4. Confirm the change works as specified.
5. Capture evidence (screenshots or notes).

## Verification
- [ ] Critical flows exercised in browser
- [ ] No new console or network errors
- [ ] Behavior matches spec
