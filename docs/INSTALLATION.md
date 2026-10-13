# Installation

Requires Python 3.10+ and a local checkout. Commands below work in PowerShell and POSIX shells; use python3 or py -3 when needed.

## Destination paths

| Agent | User scope | Project scope |
|-------|------------|---------------|
| Claude Code | ~/.claude/skills/NAME/SKILL.md | PROJECT/.claude/skills/NAME/SKILL.md |
| Codex | ~/.agents/skills/NAME/SKILL.md | PROJECT/.agents/skills/NAME/SKILL.md |

On Windows, ~ means your profile directory, normally C:\Users\YOUR_NAME. The installer uses the platform's home-directory resolution. Project scope requires an explicit project root so it does not accidentally install into this collection's checkout.

Sources checked for this release: [Claude Code](https://code.claude.com/docs/en/skills) and [Codex](https://learn.chatgpt.com/docs/build-skills).

## Selected skills

From the collection checkout, preview installation:

```sh
python scripts/install_skills.py --agent codex --skills root-cause-debug five-axis-gate
```

Repeat with --apply to perform the copies. Skills are self-contained. The router locates siblings only when available; it does not require installing every skill.

## Project installation

Replace the sample path with your actual project path, retaining quotes around spaces:

```sh
python scripts/install_skills.py --agent claude --scope project --project-root "/path/to/project" --skills root-cause-debug --apply
```

PowerShell example:

```powershell
python scripts/install_skills.py --agent codex --scope project --project-root "D:\My Project" --skills root-cause-debug --apply
```

Omit --apply to preview first.

## All skills

Version 0.2.0 contains 56 skills. See [recommended selections](SKILL-SELECTION.md) for domain-focused installations.

```sh
python scripts/install_skills.py --agent codex --skills all
python scripts/install_skills.py --agent codex --skills all --apply
```

Choose the agent flag matching your environment. Installing all skills makes them available; it should not cause every workflow to run on every request.

## Existing installations and updates

The installer preflights all selected destinations before copying. Identical folders are skipped. If any selected folder differs, the installation stops without overwriting it or starting other copies. Compare and back up your local customizations, then intentionally move the conflicting folder aside before retrying.

Filesystem errors during copying can still leave a partial new folder; inspect the printed destination before retrying. There is no automated deletion or replacement mode. Symlink resources are rejected.

Reload or start a fresh agent session if your agent has not discovered new skills. Verify discovery by explicitly invoking /root-cause-debug in Claude Code or $root-cause-debug in Codex. Managed policies may restrict loading; this installer does not change those policies.
