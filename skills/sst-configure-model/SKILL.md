---
name: sst-configure-model
description: Construct or debug Python system models using existing SST elements.
---

# sst-configure-model

This skill belongs to the sst-ai-tools repository. Resolve the real path of this skill directory first, then use `../..` as the repository root; this also works when the skill directory is symlinked into an agent's skill directory. Keep this repository intact when installing; sibling OFK documents and tools are required. Resolve SST source roots from the user or the sibling workspace, not the shell's current directory.

Read [the task guide](../../ofk/using-sst/models.md). Identify the required behavior and choose existing components. Load the chosen element's use-case profile, available detailed guides, and one matching source configuration. Verify parameters/ports/slots against ELI and implementation where they differ. Produce a finite minimal model and demonstrate the requested observable behavior. Use [statistics](../../ofk/using-sst/statistics.md) for outputs and [run-time options](../../ofk/using-sst/run-options.md) for flags.

Use `python3 <tools-root>/tools/sst_tools.py --help` for deterministic helpers. Load only task-relevant knowledge. Documents are drafts; inspect current source for implementation details. Do not update, pull, install dependencies, or publish merely because the task uses this skill; follow the user's requested scope.
