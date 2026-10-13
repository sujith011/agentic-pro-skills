---
name: mobile-runtime-check
description: "Verify a changed mobile journey on identified devices or emulators, including permissions, lifecycle, offline behavior, and platform-specific limits."
---

# Mobile Runtime Check

## Process
1. Identify the changed journey, platforms, SDK/runtime versions, and native dependencies. Record the test device, OS, build variant, and whether it is a physical device or emulator.
2. Build and run targeted unit/static checks. Then exercise the actual interaction on a connected runtime with accessible logs.
3. Test first launch, denied/granted permissions, cancellation, background/foreground, process recreation, and offline/reconnection when relevant. Include duplicate taps and interrupted submissions.
4. Check navigation/deep links and pending state after restart. Offline writes need explicit conflict, ordering, retry, and cancellation semantics.
5. For camera, location, Bluetooth, notifications, or background services, verify the physical/platform conditions that an emulator cannot establish. A JavaScript-only preview may omit native behavior.
6. Report each platform and lifecycle case separately. Preserve privacy when collecting screenshots and logs.

## Example
A location-sharing screen stops sharing when cancelled. Reopen the app after a process restart and verify the cancelled session is not revived by stale storage or delayed worker events.

## Stop conditions
An offline/unauthorized device connection means runtime checks remain unverified. Do not describe a successful build as successful camera, permission, or background execution.

## Evidence
- Device/build/OS identity.
- Journey and lifecycle observations with logs.
- Physical-device gaps and platform-specific failures.

## Reference
Workflow independently written after reviewing [react-native-architecture](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/react-native-architecture/SKILL.md).
