# Share specific workflows

These are draft posts for the maintainer. They have not been posted. Check each community's current promotion rules and adapt the wording before publishing.

## Debugging workflow

> An AI-generated fix is easier to trust when you can reproduce the bug and inspect a regression check.
>
> Agentic Pro Skills includes a root-cause-debug workflow for recording expected versus actual behavior, testing a hypothesis, and verifying the smallest supported repair. The collection supports Claude Code and Codex.
>
> Try it on a reproducible bug and tell me what helped or added friction:
> https://github.com/sujith011/agentic-pro-skills/blob/main/skills/root-cause-debug/SKILL.md

## Regression testing

> How do you check that a coding agent's regression test actually catches the bug?
>
> I maintain a proof-first-testing workflow that asks for a failing check before the repair and evidence from the rerun. There is also a small duplicate-job fixture you can use to try the workflow.
>
> Walkthrough: https://github.com/sujith011/agentic-pro-skills/blob/main/examples/duplicate-job.md
>
> Comparative agent results haven't been published yet. I'm looking for actual usage reports, including failures.

## Pull request review

> Reviewing an AI-generated pull request needs concrete evidence for the changed behavior and its risks.
>
> Agentic Pro Skills includes a five-axis review workflow. Try it on a real change and report which checks were useful and which were unnecessary for the task.
>
> https://github.com/sujith011/agentic-pro-skills/blob/main/skills/five-axis-gate/SKILL.md

## Collection introduction

> Agentic Pro Skills is an MIT-licensed collection of 56 engineering workflows for Claude Code and Codex. Start with six core skills for understanding code, debugging, testing, review, browser checks, and security boundaries.
>
> The repository includes installation helpers and evaluation fixtures. Its CI checks structure and helper behavior; it does not establish live-agent effectiveness.
>
> https://github.com/sujith011/agentic-pro-skills

## Review what worked

After publishing, record the channel, date, post link, useful feedback, confirmed first uses, and installation problems. Public stars alone do not show whether users tried a skill. Feature real reports in the [showcase](SHOWCASE.md) with permission and evidence.

Use feedback to refine the workflow and onboarding before adding more skills. Do not post the same promotional message repeatedly, buy stars, or imply endorsement from tool vendors.
