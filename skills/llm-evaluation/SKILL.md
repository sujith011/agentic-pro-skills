---
name: llm-evaluation
description: "Evaluate a model, prompt, retrieval, or agent-tool change against a fixed baseline with task-specific scoring, held-out cases, and failure evidence."
---

# LLM Evaluation

## Process
1. State the intended improvement and unacceptable regressions. Choose observable task metrics, hard failures, cost, and latency before inspecting candidate results.
2. Build representative synthetic or authorized examples, including ambiguity, missing evidence, adversarial content, and tool failure. Separate development cases from held-out evaluation.
3. Record model/provider version, prompt, tools, parameters, dataset revision, and environment. Use comparable setups and repeat stochastic runs; preserve failures and blocked cases.
4. Prefer deterministic grading for checkable outputs. For human/model judges, define the rubric, calibrate on reviewed examples, randomize pair order where useful, and inspect disagreement.
5. Compare per-case and per-category outcomes, not only aggregate scores. A formatting improvement cannot compensate for an unauthorized action or data leak.
6. Report sample counts, variation, cost, latency, and uncertainty. Re-run after material model, prompt, tool, or retrieval changes.

## Example
A new extraction prompt improves valid JSON rate but invents missing invoice amounts. Grade schema validity and grounded field accuracy separately, with invented required data treated as a hard failure.

## Stop conditions
Do not tune on held-out answers or discard inconvenient runs. Similarity metrics and a judge's preference alone cannot establish factual correctness or production safety.

## Evidence
- Versioned cases, rubric, and baseline.
- Raw sanitized outcomes with grading pointers.
- Regression breakdown, cost, and limits.

## Reference
Workflow independently written after reviewing [llm-evaluation](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/llm-evaluation/SKILL.md).
