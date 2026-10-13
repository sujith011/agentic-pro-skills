# Showcase

Real task reports help people decide which workflow to try. Failed and mixed outcomes are useful too.

## Current evidence

No live-agent showcase reports or comparative results have been published here yet. Repository validation and installer tests check the collection's structure and helper behavior; they do not demonstrate agent effectiveness.

Start with the [duplicate-job walkthrough](../examples/duplicate-job.md). It provides a reproducible defect and verification steps, not a recorded successful agent run.

## Share a report

[Open a usage report](https://github.com/sujith011/agentic-pro-skills/issues/new?template=usage-report.yml) or submit a pull request with a public, reproducible case. Include:

| Field | What to record |
|-------|----------------|
| Task | Expected behavior, observed defect, and minimal setup |
| Environment | Agent/model version, OS, tools, settings, and relevant commit IDs |
| Skills | Exact skill names and evidence that they loaded |
| Before | Reproduction command, observed output, and initial test coverage |
| After | Resulting diff, commands run, and actual results |
| Evidence | Redacted transcript, tests, screenshots, or recording links |
| Limits | Checks not run, blocked actions, failures, and simulation boundaries |

Do not publish private code, credentials, or personal data. Distinguish maintainer reports from independent community reports. Link source artifacts and get the reporter's permission before featuring their words or identity.

## Report template

Copy this into a usage report. Replace placeholders with observations; do not present intended outcomes as completed work.

```text
Task/problem:
Agent/model and settings:
Repository commit and skill commit:
Skills loaded and loading evidence:
Before behavior and reproduction:
Commands actually run:
After behavior and diff:
Evidence links:
What helped / added friction / failed:
Checks not run and remaining limits:
```

For a baseline comparison, follow the [evaluation protocol](../evals/README.md). A single successful walkthrough is a demonstration of that run, not evidence of general superiority.
