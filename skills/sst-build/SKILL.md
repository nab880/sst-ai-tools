---
name: sst-build
description: Build or diagnose SST core/elements installations and runtime discovery.
---

# sst-build

This skill belongs to the sst-ai-tools repository. Resolve the real path of this skill directory first, then use `../..` as the repository root; this also works when the skill directory is symlinked into an agent's skill directory. Keep this repository intact when installing; sibling OFK documents and tools are required. Resolve SST source roots from the user or the sibling workspace, not the shell's current directory.

Read [the task guide](../../ofk/development/build.md). Inventory the workspace and existing installation with the inspect tool. Resolve the intended prefix and configuration, build core before elements when necessary, and verify runtime discovery. Report commands, loaded installation, and validation gaps. For a library outside sst-elements, follow [external elements](../../ofk/development/external-elements.md).

Use `python3 <tools-root>/tools/sst_tools.py --help` for deterministic helpers. Load only task-relevant knowledge. Documents are drafts; inspect current source for implementation details. Do not update, pull, install dependencies, or publish merely because the task uses this skill; follow the user's requested scope.
