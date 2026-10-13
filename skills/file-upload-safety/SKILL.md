---
name: file-upload-safety
description: "Implement uploads and downloads with authorized object ownership, bounded resource use, content inspection, and safe serving behavior."
---

# File Upload Safety

## Process
1. Define allowed content, maximum byte/decompressed size, quota, retention, and who can create/read/delete each object.
2. Generate storage identifiers on the server. Treat the original filename as display metadata; never join it into a storage path or let the client choose another owner's key.
3. Enforce limits at the edge and processing boundary. Stream within bounds, inspect actual content, and handle partial uploads. File extension, declared MIME type, and magic bytes alone do not prove safety.
4. If using signed uploads, constrain object key, lifetime, method, and supported size/type conditions. Confirm the uploaded object's actual size/content before marking it usable.
5. Quarantine or process untrusted content according to product risk. Serve active content with deliberate content headers and isolation; require authorization for download-link issuance and private cache handling.
6. Test oversized, mismatched, malformed, unauthorized, interrupted, and abandoned uploads. Clean temporary objects without deleting unrelated data.

## Example
A claimed PNG contains HTML. The application rejects or quarantines it before attachment visibility; changing the object ID cannot access another tenant's upload.

## Stop conditions
Do not fetch arbitrary supplied URLs as an upload shortcut without reviewing the network boundary. Do not promise that one signature check detects malware.

## Evidence
- Ownership and signed-URL constraints.
- Resource/content/denial probes.
- Storage lifecycle and serving policy.

## Reference
Workflow independently written after reviewing [file-uploads](https://github.com/sickn33/agentic-awesome-skills/blob/cb30121a2dfd007531bd2fbefb56f68de927da6a/skills/file-uploads/SKILL.md).
