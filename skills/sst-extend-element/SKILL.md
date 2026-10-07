---
name: sst-extend-element
description: Add simulated behavior to an SST element, including network, workload, CPU, fault-injection, and GPU integrations.
---

# sst-extend-element

This skill belongs to the sst-ai-tools repository. Resolve the real path of this skill directory first, then use `../..` as the repository root; this also works when the skill directory is symlinked into an agent's skill directory. Keep this repository intact when installing; sibling OFK documents and tools are required. Resolve SST source roots from the user or the sibling workspace, not the shell's current directory.

Read [the task guide](../../ofk/development/extending-elements.md). Separate configuration from implementation. Load the selected element's use-case profile and available extension guide, then the exact base class and nearest implementation. Profile-only elements require this targeted source inspection before choosing an extension point. Define correctness criteria before editing. Complete build integration and targeted behavioral validation; report assumptions and unsupported cases. A library outside sst-elements follows [external elements](../../ofk/development/external-elements.md).

Use `python3 <tools-root>/tools/sst_tools.py --help` for deterministic helpers. Load only task-relevant knowledge. Documents are drafts; inspect current source for implementation details. Do not update, pull, install dependencies, or publish merely because the task uses this skill; follow the user's requested scope.
