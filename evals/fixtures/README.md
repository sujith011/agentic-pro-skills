# Evaluation fixtures

These deliberately incomplete examples belong only in isolated evaluation workspaces. They are not production code. Copy one folder outside this repository before a run and provide the agent its scenario prompt without grader criteria.

| Fixture | Scenario | Baseline coverage |
|---------|----------|-------------------|
| tenant-store | tenant-isolation | An allowed read; unauthorized reads remain defective |
| job-delivery | duplicate-job-delivery | A new credit; repeated job IDs still duplicate credits |
| model-output | semantic-model-output | Valid output; unauthorized customers and nonpositive amounts still pass |

Run the baseline from a copied fixture directory:

```sh
python -m unittest discover -v
```

Each fixture's baseline is expected to pass and intentionally misses the defect. It does not establish the requested behavior. The job fixture is a synchronous in-memory ledger; it cannot establish durable queue delivery, concurrent transactions, crash recovery, or exactly-once provider effects. The output fixture has no live model or payment provider.

Use [scenarios.json](../scenarios.json) and the [evaluation protocol](../README.md). Keep grading criteria outside the agent's task workspace. Preserve actual before/after command evidence; do not claim a failing regression ran before a fix unless it did.

Other cases require the isolated setup described in their scenario. Prepare those environments separately and report unavailable cases as not run.
