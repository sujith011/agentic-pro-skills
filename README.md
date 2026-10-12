<div align="center">

# Expert Engineering Skills

**32 expert-level engineering skills for Claude Code and other AI coding agents**

Tighter gates · Stronger verification · Higher signal than other collections

[![Skills](https://img.shields.io/badge/Skills-32-brightgreen?style=for-the-badge&logo=claude&logoColor=white)](https://github.com/sujith011/expert-engineering-skills)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-D97757?style=for-the-badge&logo=claude&logoColor=white)](https://claude.ai/code)
[![Stars](https://img.shields.io/github/stars/sujith011/expert-engineering-skills?style=for-the-badge&color=yellow)](https://github.com/sujith011/expert-engineering-skills/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/sujith011/expert-engineering-skills?style=for-the-badge)](https://github.com/sujith011/expert-engineering-skills/commits)

</div>

---

## Lifecycle

<div align="center">

[![Define](https://img.shields.io/badge/1._DEFINE-intent_%26_spec-blue?style=for-the-badge)](#define)
→
[![Plan](https://img.shields.io/badge/2._PLAN-atomic_tasks-green?style=for-the-badge)](#plan)
→
[![Build](https://img.shields.io/badge/3._BUILD-vertical_slices-orange?style=for-the-badge)](#build)
→
[![Verify](https://img.shields.io/badge/4._VERIFY-tests_%26_proof-purple?style=for-the-badge)](#verify)
→
[![Review](https://img.shields.io/badge/5._REVIEW-five_axis_gate-red?style=for-the-badge)](#review)
→
[![Ship](https://img.shields.io/badge/6._SHIP-pre_ship_gate-brightgreen?style=for-the-badge)](#ship)

</div>

---

## Why these are different

| Other collections | This collection |
|-------------------|-----------------|
| Often skip or soften gates | Hard gates with explicit verification |
| Generic advice | Opinionated process + anti-rationalization tables |
| Tests as optional | Proof-first testing with seam rules and anti-patterns |
| Review as optional polish | Five-axis gate with evidence required |
| Large, process-owning frameworks | Lean, composable skills you can use individually |

Inspired by the best practices in the ecosystem (including Matt Pocock’s skills), but tightened further: every skill has numbered steps, explicit rejection criteria, and a verification checklist that must pass before the work is considered done.

---

## Skills

### Define
| Skill | Purpose |
|-------|---------|
| [`intent-extraction`](skills/intent-extraction/SKILL.md) | Extract true intent one question at a time until ~95% confidence |
| [`concept-sharpening`](skills/concept-sharpening/SKILL.md) | Turn a vague idea into concrete, evaluable proposals |
| [`prd-first`](skills/prd-first/SKILL.md) | Write a complete, testable PRD before any code |
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
| [`load-proof`](skills/load-proof/SKILL.md) | Prove performance under load before declaring ready |
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
| [`skill-router`](skills/skill-router/SKILL.md) | Route work to the correct skill and enforce shared rules |

---

## Quick Start

**Claude Code**
```bash
git clone https://github.com/sujith011/expert-engineering-skills.git
# Copy or symlink skills/ into your Claude Code skills directory
```

**Any agent that supports SKILL.md**
```bash
git clone https://github.com/sujith011/expert-engineering-skills.git
# Reference individual skills/NAME/SKILL.md files
```

Each skill is self-contained and activates when its description matches the request.

---

## Design Principles

| Principle | Rule |
|-----------|------|
| **Spec before code** | No implementation until the PRD is approved |
| **Tests are proof** | Failing test first. No production code without it |
| **One slice at a time** | Finish a vertical slice completely before starting the next |
| **Measure before optimize** | Baseline first. Change only what the data shows |
| **Verify before ship** | Checklist gate. No silent exceptions |
| **Clarity over cleverness** | Simpler code that a new engineer can understand faster |

---

<div align="center">

**Built for engineers who want agents that follow senior practices.**

[Star this repo](https://github.com/sujith011/expert-engineering-skills) · [Open an issue](https://github.com/sujith011/expert-engineering-skills/issues) · [MIT License](LICENSE)

</div>
