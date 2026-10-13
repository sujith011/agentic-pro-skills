# Contributing

Changes should improve a specific decision or failure mode rather than add generic advice.

## Where to start

- Try the [duplicate-job walkthrough](examples/duplicate-job.md) and report the actual result, including failed or blocked steps.
- Reproduce an installation or discovery issue on your OS and agent version.
- Clarify a confusing skill trigger or example with a concrete task where it caused a poor decision.
- Add an isolated fixture for an existing evaluation scenario that does not yet have one.

Use the [bug report](https://github.com/sujith011/agentic-pro-skills/issues/new?template=bug-report.yml), [skill proposal](https://github.com/sujith011/agentic-pro-skills/issues/new?template=skill-proposal.yml), or [usage report](https://github.com/sujith011/agentic-pro-skills/issues/new?template=usage-report.yml). Search existing issues first. A usage report can describe a failure; a favorable testimonial is not required.

Before adding a skill, identify the distinct task and explain why an existing skill cannot handle it. Prefer improving a relevant workflow over duplicating it. Include no secrets, private project code, or personal data in issues or evaluation artifacts.

## Skill format

Each directory under skills/ contains SKILL.md with portable frontmatter: a lowercase name matching its folder and a JSON-quoted description. This repository intentionally uses only those two required fields so its dependency-free validator can check them deterministically. Additional YAML structures require extending the validator and tests first.

Descriptions explain when the skill applies. Keep the body self-contained and concise; add local references only when progressive disclosure has a concrete benefit. Do not add external-action permission, forced commits, or repeated approvals to unrelated work.

Include decision criteria, a realistic example, stop conditions proportional to risk, and observable evidence. A runnable test, browser observation, source inspection, and mocked integration are different forms of evidence; name the actual one.

## Validation

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

Local link checking supports simple inline links and Markdown headings, including duplicate heading suffixes. External links, reference-style links, HTML anchors, and arbitrary Markdown rendering are outside its scope.

Add regression tests when changing helpers. Test safety behavior such as collision refusal and dry-run effects, not merely generated wording. Update the README catalog and count when adding/removing skills. The validator also checks release-version consistency and evaluation case schemas/skill references.

For changed behavioral guidance, select relevant cases from [the evaluation protocol](evals/README.md), run them in an isolated workspace where feasible, and report results or explicitly mark them not run.

## Review and releases

A PR should explain the changed agent behavior, why it matters, validation performed, and remaining limits. Add an entry to CHANGELOG.md and update VERSION plus the README version for a release. Tag only the intended verified commit. Do not claim superiority without comparable evaluation results.
