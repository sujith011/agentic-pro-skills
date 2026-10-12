---
name: intent-extraction
description: "Extract true intent one question at a time until ~95% confidence. Use when the ask is underspecified or the user says interview me / grill me."
type: workflow
lifecycle: active
---

# Requirements Interrogation — Extract What Is Actually Wanted

Do not start work until intent is confirmed. Surface assumptions before any plan or code.

## Process
1. State hypothesis + confidence (0-100%) + what is still missing.
2. Ask one focused question with your best guess attached.
3. Update hypothesis after each answer.
4. Restate full intent (Outcome / User / Why now / Success / Constraint / Out of scope).
5. Require explicit "yes". Stop if confidence cannot reach ~95%.

## Rules
- One question per turn.
- Never accept "whatever you think" as confirmation.
- Probe "what would you actually want if you didn't have to justify it?" on vague answers.

## Verification
- [ ] Explicit hypothesis with confidence stated first
- [ ] Questions asked one at a time with guesses
- [ ] Concrete restate confirmed with explicit yes
- [ ] Out of scope declared
