# Try a skill: stop duplicate job credits

This practice task uses a deliberately defective Python fixture. You can reproduce the bug locally and ask your agent to repair it. It is an in-memory simulation, not a real queue, payment provider, or published agent comparison.

Requires Python 3.10+, this repository checkout, and Claude Code or Codex. Use `python3` or `py -3` if needed.

## 1. Copy a fresh workspace

Run from the repository root. Choose a new sibling directory; do not reuse a workspace that contains a previous repair.

PowerShell:

```powershell
Copy-Item -LiteralPath "evals/fixtures/job-delivery" -Destination "../agentic-job-demo" -Recurse
```

macOS/Linux:

```sh
cp -R evals/fixtures/job-delivery ../agentic-job-demo
```

Both shells:

```sh
cd ../agentic-job-demo
python -m unittest discover -v
```

The existing test passes because it checks only a new job. Passing that test does not establish correct retry behavior.

## 2. Observe the defect

```sh
python -c "from jobs import run_job; ledger = []; run_job('job-1', 500, ledger); run_job('job-1', 500, ledger); print(ledger); print('credits:', len(ledger))"
```

The unmodified fixture prints two credits with the same job ID. The desired behavior is one credit for an identical retry, and `ValueError` when an existing ID is reused with a different amount.

## 3. Install the relevant skills

Return to the collection checkout in a separate terminal. Preview, then install at user scope. Choose one agent:

Claude Code:

```sh
python scripts/install_skills.py --agent claude --skills background-jobs proof-first-testing
python scripts/install_skills.py --agent claude --skills background-jobs proof-first-testing --apply
```

Codex:

```sh
python scripts/install_skills.py --agent codex --skills background-jobs proof-first-testing
python scripts/install_skills.py --agent codex --skills background-jobs proof-first-testing --apply
```

If there is a collision or discovery problem, use the [installation troubleshooting guide](../docs/INSTALLATION.md#troubleshooting).

## 4. Give your agent the task

Open `agentic-job-demo` as your agent's task workspace. Start a fresh session and explicitly invoke `/background-jobs` in Claude Code or `$background-jobs` in Codex. Then send:

```text
Use background-jobs and proof-first-testing for this task.
Fix duplicate credits when run_job receives the same job ID twice.
Return the original credit for an identical retry; raise ValueError
if that ID is reused with a different amount. Preserve new-job behavior.
Add and run a failing regression before fixing the code, then rerun
the tests. Report your commands, actual results, and simulation limits.
Do not commit or push.
```

Inspect the session to confirm which skills loaded. The explicit invocation and named second skill do not establish discovery without session evidence.

## 5. Check the result

From the demo directory, rerun the tests and duplicate-credit command. Review the regression coverage for identical retries, conflicting amounts, distinct job IDs, and invalid inputs. The repeated-credit command should now print `credits: 1`.

Keep the transcript, before/after commands, and diff. If the agent skips the failing regression, edits outside the fixture, or cannot run the tests, record that limitation. Do not report a successful run merely because it proposed a plausible fix.

[Share a usage report](https://github.com/sujith011/agentic-pro-skills/issues/new?template=usage-report.yml) with your agent/model version and observed outcome. Remove secrets and personal data from any artifacts.

For an actual comparison, use fresh separate copies and sessions with and without the skills, repeat each condition at least three times, include failures, and follow the [evaluation protocol](../evals/README.md). This guided walkthrough exposes expected checks and is not a blind evaluation.
