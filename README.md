# Agentic Pro Skills

Professional engineering workflows for AI coding agents.

**56 engineering skills** for Claude Code, Codex, and agents that support SKILL.md.

Version: **0.2.0** · [Release notes](CHANGELOG.md) · [MIT License](LICENSE)

Practical workflows for defining, building, reviewing, and releasing software. Each skill includes decision criteria, a concrete example, stop conditions, and evidence to collect.

## What this collection provides

- Test-first behavior changes with the same sequence across testing and vertical slices.
- Scope and verification scaled to actual risk.
- Existing user authorization carried forward without repeated routine approval stops.
- Specific checks for tenant authorization, retry side effects, migration recovery, accessibility, and runtime behavior.
- Self-contained skills that can be installed individually.

Skills guide an agent; Markdown does not enforce a runtime gate. The included CI validates repository structure and helper behavior. It does not prove agents follow every instruction or that this collection outperforms another one. Behavioral evaluation cases are provided, but no comparative results have been published.

## Start small

Start with understand-first, proof-first-testing, root-cause-debug, five-axis-gate, real-browser-check, and threat-surface. They apply only when relevant. Add planning, capacity, migration, and release workflows when the task calls for them; every task does not need the entire lifecycle.

Examples:
- Label correction: focused edit and visual check.
- Cross-tenant data leak: inspect ownership boundaries, add a failing abuse test, fix, and verify denial.
- Destructive migration: compatibility, data integrity, rehearsed recovery, and target authorization.
- Read-only review: inspect and report; do not edit, commit, or publish.

## Skills

The 24 additions in v0.2.0 cover implementation and operational boundaries beyond the original lifecycle workflows. Browse [recommended selections](docs/SKILL-SELECTION.md) and [reference provenance](docs/SOURCES.md).

### Define
| Skill | Purpose |
|-------|---------|
| [`intent-extraction`](skills/intent-extraction/SKILL.md) | Extract true intent one question at a time when material decisions are unresolved |
| [`concept-sharpening`](skills/concept-sharpening/SKILL.md) | Turn a vague idea into concrete, evaluable proposals |
| [`prd-first`](skills/prd-first/SKILL.md) | Define testable scope, scaled to the change |
| [`quality-bar`](skills/quality-bar/SKILL.md) | Decide the quality bar once and enforce it everywhere |
| [`docs-before-code`](skills/docs-before-code/SKILL.md) | Write the user-facing documentation before or alongside the implementation |

### Plan
| Skill | Purpose |
|-------|---------|
| [`atomic-task-breakdown`](skills/atomic-task-breakdown/SKILL.md) | Decompose a spec into small, verifiable, ordered tasks |
| [`adr-record`](skills/adr-record/SKILL.md) | Record significant architecture decisions |

### Build
| Skill | Purpose |
|-------|---------|
| [`vertical-slices`](skills/vertical-slices/SKILL.md) | Implement in thin vertical slices — one behavior, one commit |
| [`curated-context`](skills/curated-context/SKILL.md) | Feed the agent the right information at the right time |
| [`understand-first`](skills/understand-first/SKILL.md) | Read and understand existing code before modifying it |
| [`contract-first`](skills/contract-first/SKILL.md) | Design clean APIs and interfaces before implementation |
| [`accessible-ui`](skills/accessible-ui/SKILL.md) | Build accessible, performant UI with clear component boundaries |
| [`flag-discipline`](skills/flag-discipline/SKILL.md) | Use feature flags for risky or incomplete changes |
| [`error-boundaries`](skills/error-boundaries/SKILL.md) | Define clear error handling and failure modes |
| [`version-contracts`](skills/version-contracts/SKILL.md) | Treat public interfaces as versioned contracts |

### Verify
| Skill | Purpose |
|-------|---------|
| [`proof-first-testing`](skills/proof-first-testing/SKILL.md) | Red-Green-Refactor with seam rules and anti-patterns |
| [`root-cause-debug`](skills/root-cause-debug/SKILL.md) | Reproduce → localize → reduce → fix → guard |
| [`real-browser-check`](skills/real-browser-check/SKILL.md) | Verify UI behavior in a real browser |
| [`measure-first`](skills/measure-first/SKILL.md) | Measure before you optimize |
| [`load-proof`](skills/load-proof/SKILL.md) | Measure capacity and concurrency when risk warrants it |
| [`a11y-gate`](skills/a11y-gate/SKILL.md) | Verify accessibility before merge |
| [`dep-audit`](skills/dep-audit/SKILL.md) | Audit dependencies for known vulnerabilities and necessity |

### Review
| Skill | Purpose |
|-------|---------|
| [`five-axis-gate`](skills/five-axis-gate/SKILL.md) | Five-axis review with evidence required on every axis |
| [`clarity-refactor`](skills/clarity-refactor/SKILL.md) | Reduce complexity while preserving exact behavior |
| [`threat-surface`](skills/threat-surface/SKILL.md) | Harden inputs, auth, and secrets |
| [`safe-refactor`](skills/safe-refactor/SKILL.md) | Refactor only with a safety net of tests and small steps |

### Ship
| Skill | Purpose |
|-------|---------|
| [`atomic-commits`](skills/atomic-commits/SKILL.md) | Small, meaningful commits with clear messages |
| [`pre-ship-gate`](skills/pre-ship-gate/SKILL.md) | Pre-launch verification checklist |
| [`observe-first`](skills/observe-first/SKILL.md) | Add logging, metrics, and tracing before the feature is done |
| [`migration-gate`](skills/migration-gate/SKILL.md) | Plan and gate any data or schema migration |
| [`incident-playbook`](skills/incident-playbook/SKILL.md) | Write the incident response steps before the feature ships |
| [`skill-router`](skills/skill-router/SKILL.md) | Select the smallest relevant workflow |


### Backend and data
| Skill | Purpose |
|-------|---------|
| [`system-design`](skills/system-design/SKILL.md) | Compare service and storage boundaries for a new system or a significant architecture change using concrete workload and failure constraints. |
| [`api-implementation`](skills/api-implementation/SKILL.md) | Implement an HTTP endpoint from an agreed contract, including authorization, pagination, concurrency, and safe retry behavior. |
| [`event-contracts`](skills/event-contracts/SKILL.md) | Design or change durable event producers and consumers with compatible schemas, delivery semantics, and replay behavior. |
| [`authorization-design`](skills/authorization-design/SKILL.md) | Design and verify server-side access rules for roles, tenants, resource ownership, and sensitive actions. |
| [`database-modeling`](skills/database-modeling/SKILL.md) | Design relational entities, constraints, and transaction boundaries for new persisted behavior while preserving existing data semantics. |
| [`query-optimization`](skills/query-optimization/SKILL.md) | Diagnose a slow database query using workload evidence and execution plans, then verify a bounded change without altering result semantics. |
| [`cache-correctness`](skills/cache-correctness/SKILL.md) | Add or repair caching with explicit key scope, staleness bounds, invalidation races, and safe failure behavior. |
| [`background-jobs`](skills/background-jobs/SKILL.md) | Implement durable asynchronous work with confirmed enqueue, bounded retries, idempotent effects, and recoverable worker failure. |
| [`file-upload-safety`](skills/file-upload-safety/SKILL.md) | Implement uploads and downloads with authorized object ownership, bounded resource use, content inspection, and safe serving behavior. |
| [`python-service-design`](skills/python-service-design/SKILL.md) | Implement or review Python HTTP service boundaries, request-scoped resources, async execution, and durable work using the installed framework. |

### Frontend and mobile
| Skill | Purpose |
|-------|---------|
| [`frontend-state`](skills/frontend-state/SKILL.md) | Design or fix client, URL, and server state ownership, including request races, optimistic updates, and session changes. |
| [`react-performance`](skills/react-performance/SKILL.md) | Investigate measured React or Next.js interaction and loading bottlenecks while preserving rendering, accessibility, and data isolation. |
| [`typescript-boundaries`](skills/typescript-boundaries/SKILL.md) | Strengthen TypeScript input and module boundaries with runtime validation, explicit domain states, and verified build/runtime resolution. |
| [`mobile-runtime-check`](skills/mobile-runtime-check/SKILL.md) | Verify a changed mobile journey on identified devices or emulators, including permissions, lifecycle, offline behavior, and platform-specific limits. |

### Quality and delivery
| Skill | Purpose |
|-------|---------|
| [`e2e-journeys`](skills/e2e-journeys/SKILL.md) | Test a complete user journey through a real application boundary using stable selectors, isolated state, and observable final outcomes. |
| [`test-data-isolation`](skills/test-data-isolation/SKILL.md) | Prepare integration or end-to-end test data with explicit environment safeguards, per-run ownership, parallel isolation, and bounded cleanup. |
| [`ci-pipeline`](skills/ci-pipeline/SKILL.md) | Create or repair repository CI with deterministic installs, meaningful failure propagation, safe trust boundaries, and verified required checks. |
| [`container-delivery`](skills/container-delivery/SKILL.md) | Build and verify a deployable container with a bounded build context, runtime dependencies, graceful shutdown, and controlled secrets. |
| [`infrastructure-review`](skills/infrastructure-review/SKILL.md) | Review Terraform or OpenTofu changes against the intended environment, state, plan, replacement risk, and authorized apply scope. |
| [`dependency-upgrade`](skills/dependency-upgrade/SKILL.md) | Upgrade a dependency or framework through verified compatibility, migration guidance, reproducible installs, and relevant runtime checks. |

### AI and tools
| Skill | Purpose |
|-------|---------|
| [`llm-evaluation`](skills/llm-evaluation/SKILL.md) | Evaluate a model, prompt, retrieval, or agent-tool change against a fixed baseline with task-specific scoring, held-out cases, and failure evidence. |
| [`rag-quality`](skills/rag-quality/SKILL.md) | Improve retrieval-augmented answers by evaluating ingestion, authorized retrieval, evidence support, freshness, and abstention separately. |
| [`structured-output`](skills/structured-output/SKILL.md) | Consume model-generated JSON or typed responses with schema validation, semantic checks, bounded repair, and independent authorization for actions. |
| [`mcp-tool-design`](skills/mcp-tool-design/SKILL.md) | Design or review Model Context Protocol tools with narrow schemas, explicit effects, authorization, bounded results, and tested protocol behavior. |

---

## Install

Requires Git and Python 3.10 or newer. On Windows, use PowerShell; on macOS/Linux, use your shell. Replace python with python3 or py -3 if that is your installed launcher.

Clone once:

```sh
git clone https://github.com/sujith011/agentic-pro-skills.git
cd agentic-pro-skills
```

The installer prints a dry run by default. Inspect the destinations, then repeat with --apply. It refuses differing existing content and skips identical installs; it never overwrites another skill.

### Claude Code

```sh
python scripts/install_skills.py --agent claude
python scripts/install_skills.py --agent claude --apply
```

### Codex

```sh
python scripts/install_skills.py --agent codex
python scripts/install_skills.py --agent codex --apply
```

These install six core workflows at the user scope. See [installation details](docs/INSTALLATION.md) for project scope, selected skills, all 56 skills, collisions, and platform paths.

Use /root-cause-debug in Claude Code or $root-cause-debug in Codex to invoke a skill explicitly. Automatic selection depends on the agent and its configuration; inspect the session to confirm which skill loaded.

## Validate and evaluate

Run from the repository root:

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
```

The validator checks the supported portable frontmatter, directory/name consistency, catalog count, release version, evaluation schema, and local inline Markdown links/heading anchors. It does not fetch external URLs or validate arbitrary YAML/Markdown syntax. GitHub Actions runs the validator and tests on Ubuntu and Windows with Python 3.10 and 3.13.

For live agent behavior, use the [evaluation protocol](evals/README.md) and isolated [fixtures](evals/fixtures/README.md). Record actual outcomes rather than assuming a green structural check establishes instruction-following.

## Contribute

Keep descriptions narrow, instructions scoped, and verification claims honest. Follow the [contribution guide](CONTRIBUTING.md). If adapting a published workflow, preserve its required attribution and license.

Official format and discovery references: [Claude Code skills](https://code.claude.com/docs/en/skills), [Codex skills](https://learn.chatgpt.com/docs/build-skills), and [Agent Skills specification](https://agentskills.io/specification).
