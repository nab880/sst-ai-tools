---
name: sst-refresh-knowledge
description: Review and update SST OKF documents after their source files change.
---

# sst-refresh-knowledge

This skill belongs to the sst-ai-tools repository. Resolve the real path of this skill directory first, then use `../..` as the repository root; this also works when the skill directory is symlinked into an agent's skill directory. Keep this repository intact when installing; sibling OFK documents and tools are required. Resolve SST source roots from the user or the sibling workspace, not the shell's current directory.

Read [the task guide](../../ofk/architecture.md). Run check with explicit workspace roots. For each changed source, read the diff and affected concepts, reconcile claims and routing, then update source hashes with record-source only after review. Keep status draft and omit verified until actual independent verification occurs. Never treat a new hash as proof of semantic correctness. Update `generated.at` for meaningful content edits. Review commit-pinned external sources separately because the local checker does not establish their freshness. Validate links and frontmatter afterward.

Use `python3 <tools-root>/tools/sst_tools.py --help` for deterministic helpers. Load only task-relevant knowledge. Documents are drafts; inspect current source for implementation details. Do not update, pull, install dependencies, or publish merely because the task uses this skill; follow the user's requested scope.
