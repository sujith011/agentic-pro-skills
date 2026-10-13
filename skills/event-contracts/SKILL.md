---
name: event-contracts
description: "Design or change durable event producers and consumers with compatible schemas, delivery semantics, and replay behavior."
---

# Event Contracts

## Process
1. State why asynchronous delivery is needed and identify the authoritative state. Event delivery does not require converting the whole application to event sourcing.
2. Define event ID, type/version, occurrence time, producer, correlation, entity identifier, and minimal payload. Separate a past fact from a command that may fail.
3. Specify the actual broker guarantee, ordering scope, retention, and acknowledgement behavior. Consumers must handle duplicates; global ordering is rarely free.
4. Coordinate database changes with publication through an outbox or another justified atomic boundary. Track publication retries and consumer progress.
5. Decide compatibility rules for added/removed fields and mixed consumer versions. Exercise duplicate, delayed, out-of-order, malformed, and replayed events.
6. Define replay scope and side effects before replay. A projection rebuild and sending external notifications need different treatment.

## Example
An order-paid event updates a read model by event ID. Rebuilding that model reprocesses facts without reissuing payment or sending the original receipt again.

## Stop conditions
An acknowledged message does not prove the business side effect committed. Do not promise exactly-once effects from a broker label alone or replay against production without authorization.

## Evidence
- Versioned sample payload and compatibility cases.
- Atomicity and deduplication boundary.
- Recovery/replay procedure with observed failure checks.

## Reference
Workflow independently written after reviewing [event-sourcing-architect](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/event-sourcing-architect/SKILL.md).
