# Repository discovery and community setup

These are owner configuration steps, separate from committed files. They do not take effect when this document is merged.

## About panel

Open the repository's main page and use the edit control beside **About**.

Suggested description:

> Engineering workflows for Claude Code and Codex: reproduce bugs, test fixes, review changes, and record verification evidence.

Add these relevant topics:

```text
agent-skills
ai-agents
claude-code
openai-codex
developer-tools
software-engineering
code-review
testing
debugging
prompt-engineering
```

For the website field, use the existing installation documentation until a dedicated site exists:

```text
https://github.com/sujith011/agentic-pro-skills/blob/main/docs/INSTALLATION.md
```

This is a documentation destination, not a separately deployed homepage. Save and check that the public About panel shows the intended topics, description, and link.

## Discussions

In repository **Settings → General → Features**, enable **Discussions**. Configure these categories from the Discussions tab:

| Category | Format | Purpose |
|----------|--------|---------|
| Showcase | Open-ended discussion | Real usage reports and demonstrations |
| Skill requests | Open-ended discussion | Task-specific gaps and proposals |
| Questions | Question and answer | Installation, discovery, and usage help |
| Evaluation results | Open-ended discussion | Reproducible agent comparisons, failures, and trade-offs |

Keep reproducible defects in Issues and changes in pull requests. Do not add a README link to Discussions until it is enabled and publicly accessible.

Suggested welcome text:

> Welcome to Agentic Pro Skills. Tell us what you tried, which skills loaded, and what happened. Failed and mixed results are welcome. Use Showcase for task reports, Questions for help, Skill requests for concrete workflow gaps, and Evaluation results for comparisons with reproducible evidence. Report actionable bugs through the issue forms. Remove secrets and private code from all artifacts.

Review the current GitHub UI and permissions before applying settings. A signed-in repository owner or an account with the required access must make these changes. No automation in this repository changes account authentication or permissions.
