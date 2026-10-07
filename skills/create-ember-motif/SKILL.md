---
name: create-ember-motif
description: Implement, build, run, and validate a new Ember communication motif from a specified communication pattern.
---

# create-ember-motif

This skill belongs to the sst-ai-tools repository. Resolve the real path of this skill directory first, then use `../..` as the repository root; this also works when the skill directory is symlinked into an agent's skill directory. Keep this repository intact when installing; sibling OFK documents and tools are required. Resolve SST source roots from the user or the sibling workspace, not the shell's current directory.

Read [the motif recipe](../../ofk/elements/ember/new-motif.md). Before writing code, check the [motif catalog](../../ofk/elements/ember/motifs.md) for an existing motif that already produces the requested pattern, and pin down the communication schedule: participating ranks, message sizes, counts, collectives, compute between phases, and the completion condition.

Copy the closest shipped motif, implement `generate` as a resumable state machine that enqueues `enQ_*` operations and returns true only when the schedule is finished, read parameters as `arg.<name>` with ELI documentation, register the motif and its sources in the Ember `Makefile.am`, rename the copied header guard, and rebuild the element (on macOS keep `SDKROOT` set to the SDK the install was configured with, or the relink fails). Run it from `ember/test` through `emberLoad.py` with `--cmdLine` entries bracketed by `Init` and `Fini`, then verify the schedule from the motif's own output, natural completion, and a neighboring motif regression; add a sweep or nightly entry when the user wants a regression. Report assumptions such as compute times and buffer semantics.

Use `python3 <tools-root>/tools/sst_tools.py --help` for deterministic helpers. Load only task-relevant knowledge. Documents are drafts; inspect current source for implementation details. Do not update, pull, install dependencies, or publish merely because the task uses this skill; follow the user's requested scope.
