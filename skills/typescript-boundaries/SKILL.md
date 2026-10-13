---
name: typescript-boundaries
description: "Strengthen TypeScript input and module boundaries with runtime validation, explicit domain states, and verified build/runtime resolution."
---

# TypeScript Boundaries

## Process
1. Identify untrusted values entering through HTTP, storage, environment, messaging, and third-party APIs. Static interfaces disappear at runtime.
2. Accept unknown at external boundaries, validate using the project's schema/tool conventions, and narrow into domain types. Reject or deliberately handle extra fields.
3. Represent mutually exclusive states with discriminated unions and test exhaustive handling. Use units or branded identifiers where mixing values would cause a concrete defect.
4. Keep public types small and stable. Avoid broad any, unchecked assertions, or disabling type checks to silence a real mismatch.
5. Inspect the actual compiler configuration, package exports, module mode, and build runner. A TypeScript path alias does not automatically configure Node or the bundler.
6. Run type checking and the relevant emitted-code/runtime path. Verify malformed data and real package imports; compilation alone cannot establish either.

## Example
An API returns an amount as an arbitrary string. Validate finite numeric syntax and the domain's range/units before calculation instead of casting the JSON to an Invoice interface.

## Stop conditions
Do not introduce elaborate generic types for a simple local invariant. Resolve version-specific behavior from the installed compiler and official documentation.

## Evidence
- Boundary schema and invalid-input cases.
- Type-check result and relevant runtime check.
- Public compatibility and any remaining assertions.

## Reference
Workflow independently written after reviewing [typescript-expert](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/typescript-expert/SKILL.md).
