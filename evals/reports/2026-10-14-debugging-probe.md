# Debugging fixture probe — 14 October 2026

This is a scripted reference repair performed during maintenance. It is not a blind agent evaluation or evidence that the revised skills improve model performance. The task author had read the fixture, skills, and grading requirements before writing the regression tests and repair.

## Setup

- Base repository commit: `598d0caf21727d4ef2232b0abc67eafb349172e8`.
- Fixture: a fresh isolated copy of `evals/fixtures/job-delivery`.
- Runtime: Python 3.13 on Windows; synchronous caller-owned in-memory ledger.
- Skills inspected: `root-cause-debug` and `proof-first-testing`.
- Execution: a maintenance script copied the fixture, wrote explicit regression checks, ran subprocesses, introduced/restored an import error, and applied a reference repair.
- Skill discovery, fresh agent sessions, without-skill conditions, and repeated model trials: not run.

## Observations

| Step | Actual result | What it establishes |
|------|---------------|---------------------|
| Existing baseline | One test passed; exit 0 | The new-job happy path works; retry behavior is not covered. |
| Two identical calls | `credits: 2`; exit 0 | The repeated-credit defect is independently reproducible. A successful command exit alone does not indicate correct behavior. |
| Added regression checks | Five tests ran, two assertion failures; exit 1 | Duplicate and conflicting retries are defective; distinct jobs and input validation passed. |
| Incorrect `from job import run_job` import | `ModuleNotFoundError`; exit 1 | A collection/setup failure, not the duplicate-credit regression. |
| Restored baseline import | One test passed; exit 0 | Setup is repaired; it says nothing new about retries. |
| Reference repair and same regressions | Five tests passed; exit 0 | The tested in-memory retry and input behaviors work in this copy. |
| Original two-call reproduction | `credits: 1`; exit 0 | The original trigger is fixed in this copy. |

The regression assertions were left intact during the repair. The defective repository fixture remains unchanged so future evaluations start from the same baseline.

## Reproduce the reference check

Copy the fixture to a fresh directory outside the repository. First run `python -m unittest discover -v` and the two-call reproduction from the [walkthrough](../../examples/duplicate-job.md).

Copy the contents of [the recorded regression tests](debugging-regression-tests.txt) into `test_regression.py` in that isolated directory. Run `python -m unittest discover -v` before any repair; observe the two assertion failures.

The reference repair adds this check after input validation and before appending a new credit:

```python
for existing in ledger:
    if existing['job_id'] == job_id:
        if existing['amount_cents'] != amount_cents:
            raise ValueError('job ID reused with a different amount')
        return existing
```

Rerun the same tests and original reproduction. To separately verify the setup-error distinction, temporarily change the baseline test import from `jobs` to `job`, run `python -m unittest test_jobs -v`, then restore it and rerun. Do not count that import error as the behavior-specific red result.

Actual command output and exit statuses are preserved in [the execution record](debugging-probe-results.json). Local workspace paths in tracebacks are replaced with `FIXTURE`.

## Limits and next evaluation

This reference repair is specific to the in-memory fixture. It does not establish concurrency safety, persistence, crash recovery, or provider idempotency. It is not production job-processing code.

Use the [evaluation protocol](../README.md) to test the revised workflows in fresh agent sessions, with grading checks withheld and failures retained. The new cases are `green-test-misses-trigger` and `setup-error-is-not-red`. No pass rate or performance improvement can be inferred from this scripted probe.
