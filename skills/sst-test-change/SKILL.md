---
name: sst-test-change
description: Select and run SST regressions for a source change and investigate failures.
---

# sst-test-change

This skill belongs to the sst-ai-tools repository. Resolve the real path of this skill directory first, then use `../..` as the repository root; this also works when the skill directory is symlinked into an agent's skill directory. Keep this repository intact when installing; sibling OFK documents and tools are required. Resolve SST source roots from the user or the sibling workspace, not the shell's current directory.

Read [the task guide](../../ofk/development/testing.md). Map changed behavior to source suite files; use plan-tests to obtain a starting command, then narrow it. Verify installed runner help and runtime build identity. Investigate mismatches before altering reference outputs. Check exact generated test names and category filters; zero executed tests or an all-skipped selection provides no behavioral coverage. Report commands, executed counts, passes/failures/skips, and coverage gaps. For parallel or checkpointed runs, read [parallel execution](../../ofk/using-sst/parallel.md) and [checkpoint and restart](../../ofk/using-sst/checkpoint.md).

Use `python3 <tools-root>/tools/sst_tools.py --help` for deterministic helpers. Load only task-relevant knowledge. Documents are drafts; inspect current source for implementation details. Do not update, pull, install dependencies, or publish merely because the task uses this skill; follow the user's requested scope.
