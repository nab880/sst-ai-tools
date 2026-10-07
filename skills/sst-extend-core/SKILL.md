---
name: sst-extend-core
description: Change SST framework internals or public APIs and assess element compatibility.
---

# sst-extend-core

This skill belongs to the sst-ai-tools repository. Resolve the real path of this skill directory first, then use `../..` as the repository root; this also works when the skill directory is symlinked into an agent's skill directory. Keep this repository intact when installing; sibling OFK documents and tools are required. Resolve SST source roots from the user or the sibling workspace, not the shell's current directory.

Read [the task guide](../../ofk/core/extending.md). Find symbol consumers in both source trees. Explain the framework boundary and compatibility implications. Implement the focused change and test the affected core path plus relevant element integration. Do not move element-specific behavior into core without a concrete framework need.

Use `python3 <tools-root>/tools/sst_tools.py --help` for deterministic helpers. Load only task-relevant knowledge. Documents are drafts; inspect current source for implementation details. Do not update, pull, install dependencies, or publish merely because the task uses this skill; follow the user's requested scope.
