# Behavioral evaluation

These cases test observable agent decisions. They are a starting suite, not published evidence of superiority. No live agent results are included in this release.

## Run protocol

1. Choose a case from [scenarios.json](scenarios.json) and prepare its stated setup in an isolated workspace. Only tenant-isolation includes an executable fixture; prepare other environments separately.
2. Record agent/model version, settings, tools/permissions, base repository commit, skill commit, and exact prompt.
3. Run once without the skill and once with the relevant skill(s), using identical setup and separate fresh sessions. Do not give the tested agent the grader checks or previous answer.
4. Repeat at least three times per condition when comparing behavior; vary or randomize order. Include failed or blocked runs instead of discarding them.
5. Preserve transcript, commands/results, initial/final file diff, and Git state. A second reviewer should grade from these artifacts when feasible.
6. Score each observable check 0 or 1 with an evidence pointer. Any hard failure makes the run fail regardless of the numerical score. Report unavailable setup as not run, not pass.
7. Report pass rate, check scores, unnecessary clarification count, elapsed time, and tool/token cost when available. Discuss variance and trade-offs rather than relying on one favorable run.

## What structural CI establishes

The CI suite checks metadata, catalog consistency, supported local links, and helper safety. It does not execute a coding agent, measure instruction compliance, or prove that any generated product is safe.

## Suggested report

| Field | Record |
|-------|--------|
| Case and condition | ID; baseline or skill-enabled |
| Environment | Model/settings, tools, commit SHAs |
| Evidence | Transcript, command output, diff paths |
| Checks | Each check: 0/1 and evidence |
| Hard failures | None, or the observed failure |
| Limits | Missing tools, blocked actions, checks not run |
| Cost | Time, clarifications, calls/tokens if available |

Keep secrets and personal data out of stored artifacts. See [fixture instructions](fixtures/README.md).
