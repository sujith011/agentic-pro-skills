---
name: system-design
description: "Compare service and storage boundaries for a new system or a significant architecture change using concrete workload and failure constraints."
---

# System Design

## Process
1. Identify the critical user journey, existing topology, expected traffic/data volume, consistency needs, and measurable latency or availability targets. Mark estimates as assumptions.
2. Model ownership and trust boundaries before deployment boundaries. Compare the simplest extension of the existing system with one justified alternative.
3. Trace a request through storage and external dependencies. Identify the bottleneck, failure propagation, timeout budget, and behavior when a dependency is unavailable.
4. Decide which operations require atomic consistency and which can tolerate delay. Describe recovery from partial success and duplicate delivery.
5. Record the selected design, rejected alternative, operational cost, and a measurement that would justify revisiting it. Implement the smallest observable slice.

## Example
For an invoice export, start with a bounded synchronous request. Move large exports to a durable worker when measured request duration exceeds the service budget; expose job status and an authorized download.

## Stop conditions
Architecture work does not authorize provisioning. Avoid a service split without a concrete ownership, capacity, or isolation benefit; a diagram alone cannot establish throughput.

## Evidence
- Workload assumptions and failure trace.
- Decision with tradeoffs and a revisit threshold.
- Slice checks and remaining capacity uncertainty.

## Reference
Workflow independently written after reviewing [backend-architect](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/backend-architect/SKILL.md).
