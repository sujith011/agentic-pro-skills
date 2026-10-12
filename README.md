<div align="center">

# Expert Engineering Skills

**20 expert-level engineering skills for Claude Code and other AI coding agents**

Tighter gates · Stronger verification · Higher signal

[![Skills](https://img.shields.io/badge/Skills-20-brightgreen?style=for-the-badge&logo=claude&logoColor=white)](https://github.com/sujith011/expert-engineering-skills)
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

## Skills

### Define
| Skill | Purpose |
|-------|---------|
| [`intent-extraction`](skills/intent-extraction/SKILL.md) | Extract true intent one question at a time until ~95% confidence |
| [`concept-sharpening`](skills/concept-sharpening/SKILL.md) | Turn a vague idea into concrete, evaluable proposals |
| [`prd-first`](skills/prd-first/SKILL.md) | Write a complete PRD before any code |
| [`quality-bar`](skills/quality-bar/SKILL.md) | Decide the quality bar once and enforce it everywhere |

### Plan
| Skill | Purpose |
|-------|---------|
| [`atomic-task-breakdown`](skills/atomic-task-breakdown/SKILL.md) | Decompose a spec into small, verifiable, ordered tasks |

### Build
| Skill | Purpose |
|-------|---------|
| [`vertical-slices`](skills/vertical-slices/SKILL.md) | Implement in thin vertical slices — code, test, verify, commit |
| [`curated-context`](skills/curated-context/SKILL.md) | Feed the agent the right information at the right time |
| [`understand-first`](skills/understand-first/SKILL.md) | Read and understand existing code before modifying it |
| [`contract-first`](skills/contract-first/SKILL.md) | Design clean APIs and interfaces before implementation |
| [`accessible-ui`](skills/accessible-ui/SKILL.md) | Build accessible, performant UI with clear component boundaries |

### Verify
| Skill | Purpose |
|-------|---------|
| [`proof-first-testing`](skills/proof-first-testing/SKILL.md) | Red-Green-Refactor. Tests are proof |
| [`root-cause-debug`](skills/root-cause-debug/SKILL.md) | Reproduce → localize → reduce → fix → guard |
| [`real-browser-check`](skills/real-browser-check/SKILL.md) | Verify UI behavior in a real browser |
| [`measure-first`](skills/measure-first/SKILL.md) | Measure before you optimize |

### Review
| Skill | Purpose |
|-------|---------|
| [`five-axis-gate`](skills/five-axis-gate/SKILL.md) | Five-axis review: correctness, readability, architecture, security, performance |
| [`clarity-refactor`](skills/clarity-refactor/SKILL.md) | Reduce complexity while preserving exact behavior |
| [`threat-surface`](skills/threat-surface/SKILL.md) | Harden inputs, auth, and secrets |

### Ship
| Skill | Purpose |
|-------|---------|
| [`atomic-commits`](skills/atomic-commits/SKILL.md) | Small, meaningful commits with clear messages |
| [`pre-ship-gate`](skills/pre-ship-gate/SKILL.md) | Pre-launch verification checklist |
| [`skill-router`](skills/skill-router/SKILL.md) | Route work to the correct skill and enforce shared rules |

---

## Quick Start

**Claude Code**
```bash
# Clone and point Claude Code at the skills folder
git clone https://github.com/sujith011/expert-engineering-skills.git
# Then copy or symlink skills/ into your Claude Code skills directory
```

**Any agent that supports SKILL.md**
```bash
git clone https://github.com/sujith011/expert-engineering-skills.git
# Reference individual skills/NAME/SKILL.md files
```

Each skill is self-contained. The agent loads it when the description matches the request.

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

## Why these skills

Most AI coding agents take the shortest path. They skip the spec, weaken tests, and ship without verification.

These skills encode the gates senior engineers actually use. They are opinionated, lean, and designed so the agent produces production-ready code with fewer correction rounds.

---

<div align="center">

**Built for engineers who want agents that follow senior practices.**

[Star this repo](https://github.com/sujith011/expert-engineering-skills) · [Open an issue](https://github.com/sujith011/expert-engineering-skills/issues) · [MIT License](LICENSE)

</div>
