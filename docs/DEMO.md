# Record a short workflow demo

A useful demo shows the task, what the agent actually did, and verification evidence. This guide is a recording plan; no agent recording is included yet.

## Prepare

1. Use a fresh isolated copy from the [duplicate-job walkthrough](../examples/duplicate-job.md).
2. Record the collection commit, Python version, and agent/model version.
3. Preview and install `root-cause-debug` and `proof-first-testing` for your chosen agent. Run from the collection checkout:

```sh
python scripts/install_skills.py --agent claude --skills root-cause-debug proof-first-testing
python scripts/install_skills.py --agent claude --skills root-cause-debug proof-first-testing --apply
```

For Codex, replace `--agent claude` with `--agent codex`. Start a fresh session in the copied fixture workspace. Confirm discovery rather than assuming it from the copied files.

4. Invoke `/root-cause-debug` in Claude Code or `$root-cause-debug` in Codex and give the task below. Keep the fixture's defective baseline intact until the agent works on it.

```text
Use root-cause-debug and proof-first-testing.
Fix duplicate credits when run_job receives the same job ID twice.
Return the original credit for an identical retry; raise ValueError
if that ID is reused with a different amount. Preserve new-job behavior.
Add and observe a failing regression before fixing the code, then rerun
the tests. Report actual commands/results and simulation limits.
Do not commit or push.
```

## 30–45 second edit

| Segment | Show |
|---------|------|
| 0–7 seconds | Actual installer command and printed destinations |
| 7–14 seconds | Skill invocation, loading evidence, and the task |
| 14–25 seconds | The duplicate-credit reproduction and failing regression from the real session |
| 25–36 seconds | The resulting diff and successful regression run, if the agent achieves it |
| 36–45 seconds | Evidence report: commands, outcome, and in-memory simulation limits |

If a run fails or cannot execute a check, show and explain it. Editing out idle time is fine; recreating terminal output or presenting a manually written fix as agent output is not. Preserve the complete transcript and explain any cuts.

## Publish checklist

- Use readable terminal text and captions; avoid flashing effects.
- Remove private paths, credentials, and personal data.
- Export a GIF for the README or a video with a stable public link.
- Store the recording in `assets/` only when its size is reasonable; otherwise link to the public video.
- Accompany it with a [showcase report](SHOWCASE.md) containing the commit IDs, commands, diff, and limits.
- Run `python scripts/validate.py` after adding a local recording link.

This fixture does not test a durable queue, concurrent database transactions, or a payment provider. Do not label its repair as proof of exactly-once external effects. For comparative results, use the separate [evaluation protocol](../evals/README.md).
