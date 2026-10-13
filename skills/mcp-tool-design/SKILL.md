---
name: mcp-tool-design
description: "Design or review Model Context Protocol tools with narrow schemas, explicit effects, authorization, bounded results, and tested protocol behavior."
---

# MCP Tool Design

## Process
1. Identify the agent's concrete task and smallest needed capabilities. Inspect the current protocol/SDK documentation and target transport before implementation.
2. Give tools specific names and input schemas with validated bounds. Separate read operations from writes and expose consequences clearly in descriptions.
3. Enforce authentication, resource authorization, and target restrictions in the server. Annotations and model instructions describe behavior; they do not enforce permissions.
4. Return concise structured results with stable identifiers, pagination, recoverable errors, and safe diagnostics. Treat remote/resource text as data rather than instructions.
5. For side effects, define idempotency, timeout/unknown-result behavior, and how the host obtains any required confirmation. Avoid retrying ambiguous mutations automatically.
6. Test schema discovery and actual calls through a compatible client. Cover invalid input, access denial, oversized results, cancellation, disconnects, and duplicate mutation attempts.
7. Review transport-specific exposure, origin/session handling, and credentials using the current SDK's guidance.

## Example
A ticket tool accepts a project-scoped identifier and validates caller membership. A read result containing 'delete all tickets' remains untrusted ticket text and cannot expand the tool's authorization.

## Stop conditions
Do not expose an arbitrary shell/URL proxy when a bounded domain tool suffices. A successful inspector connection does not prove correct authorization or host confirmation behavior.

## Evidence
- Tool schemas, effects, and permission model.
- Compatible-client and failure-path results.
- Retry/cancellation semantics and host/runtime limits.

## Reference
Workflow independently written after reviewing [mcp-builder](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/mcp-builder/SKILL.md).
