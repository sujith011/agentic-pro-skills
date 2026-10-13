# Skill selection

Install only the workflows relevant to the work. The six core defaults remain unchanged; domain skills supplement them when a concrete boundary or failure needs attention. Individual skills have no required sibling files.

## Recommended selections

| Task | Domain skills | Add when needed |
|------|---------------|-----------------|
| Backend feature | api-implementation, authorization-design, database-modeling | system-design for a significant boundary decision; python-service-design for Python |
| Asynchronous work | background-jobs, event-contracts | cache-correctness when cached results participate |
| File attachments | file-upload-safety, authorization-design | e2e-journeys for upload-to-download verification |
| Interactive frontend | frontend-state, typescript-boundaries | react-performance for a measured bottleneck |
| Mobile journey | mobile-runtime-check | frontend-state for state/lifecycle coordination |
| Integration verification | e2e-journeys, test-data-isolation | proof-first-testing for reproducible behavior changes |
| Delivery | ci-pipeline, container-delivery | infrastructure-review when infrastructure changes |
| Dependency change | dependency-upgrade | dep-audit for vulnerability/necessity assessment |
| AI feature | llm-evaluation, structured-output | rag-quality for retrieval; mcp-tool-design for tools |

Names identify capabilities, not mandatory stages. Use the existing library/framework rather than adding one because a skill mentions a pattern.

## Install a selection

From the repository root, preview a backend selection:

```sh
python scripts/install_skills.py --agent codex --skills api-implementation authorization-design database-modeling
```

Repeat with --apply after inspecting the destinations. Substitute --agent claude for Claude Code. See [installation](INSTALLATION.md) for project scope and existing-folder collision handling.

## Verification claims

A type check, unit test, build, browser journey, physical-device run, and live-provider integration each establish different evidence. Each workflow identifies the boundary it can verify. Report unavailable checks explicitly.

See the [router](../skills/skill-router/SKILL.md) for lifecycle selection and the [catalog](../README.md#skills) for all 56 skills.
