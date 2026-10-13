---
name: container-delivery
description: "Build and verify a deployable container with a bounded build context, runtime dependencies, graceful shutdown, and controlled secrets."
---

# Container Delivery

## Process
1. Inspect the existing Docker context, target architecture, runtime command, ports, filesystem needs, and deployment environment. Verify the selected daemon/context before running.
2. Keep credentials, local data, and irrelevant files out of the build context. Use supported build secret mechanisms; deleting a secret in a later layer does not remove it from earlier layers.
3. Separate build dependencies from the runtime artifact where useful. Use compatible, supported base images and reproducible dependency installs; account for native libraries and architecture.
4. Run as an appropriate non-root identity, set ownership deliberately, and write only to intended locations. Ensure the entrypoint receives shutdown signals and closes work within the deployment deadline.
5. Build and run the resulting image in isolation. Check the real request path, startup dependencies, health behavior, restart, and termination.
6. Record image identity, size, startup time, and relevant scan results. Assess findings in context without claiming that a scan establishes security.

## Example
The image builds, but its healthcheck uses an executable absent from the runtime stage. Run the image and exercise the healthcheck rather than accepting build success.

## Stop conditions
Do not switch to another Docker context or prune shared images/volumes to repair a local build. An image build does not prove production readiness.

## Evidence
- Build/context and image identity.
- Runtime health and shutdown observations.
- Secret/runtime-dependency review and deployment limits.

## Reference
Workflow independently written after reviewing [docker-expert](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/docker-expert/SKILL.md).
