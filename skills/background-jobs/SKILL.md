---
name: background-jobs
description: "Implement durable asynchronous work with confirmed enqueue, bounded retries, idempotent effects, and recoverable worker failure."
---

# Background Jobs

## Process
1. Define acceptance, completion, cancellation, and failure states. Report accepted work only after durable enqueue or durable intent is confirmed.
2. Use small versioned payloads with identifiers and trusted context. Recheck current authorization when job semantics require it; queued work may outlive a session or permission.
3. Coordinate originating database writes and enqueue through an outbox or equivalent durable boundary. Document what happens if either half fails.
4. Assume redelivery and crashes between effect and acknowledgement. Use an atomic local effect/deduplication transaction or a downstream idempotency key; marking a job complete before an external call is insufficient.
5. Classify transient, permanent, and unknown outcomes. Bound attempts, deadlines, backoff/jitter, concurrency, and downstream load. Retain failed-job information for inspection and controlled retry.
6. Test duplicate delivery, worker termination, dependency timeout after success, and shutdown. Monitor oldest pending age as well as counts.

## Example
A receipt worker crashes after the email provider accepts a send. Redelivery uses the same provider idempotency key or reconciles the unknown result before sending again.

## Stop conditions
A queue library's deduplication option does not guarantee exactly-once external effects. Do not retry all failed jobs in a live queue without knowing their effect and scope.

## Evidence
- Durable acceptance and effect boundaries.
- Failure/recovery tests.
- Retry policy, pending-age metric, and remaining provider limitations.

## Reference
Workflow independently written after reviewing [bullmq-specialist](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/bullmq-specialist/SKILL.md).
