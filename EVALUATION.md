# Evaluate the pilot

The comparison measures correctness first, then total tokens, exploration, and elapsed time. No paired agent evaluation outcome has been claimed yet, and independent-session token totals are not exposed here. An isolated SST devel installation now exists under `.runtime/devel/install`; its tested scope and gaps are recorded in [RUNTIME_VALIDATION.md](RUNTIME_VALIDATION.md). It is local setup, not a portable prerequisite or an installation to share across extension runs.

## Prepared smoke test

The first baseline/pilot pair is prepared in `../sst-ai-evaluation-smoke/`. It predates the move to devel and subsequent knowledge additions; keep it frozen and prepare a new experiment for the current corpus. Read each experiment's `experiment.json` for randomized run order. Each run has identical tracked SST working-tree contents, a TASK.txt, and common AGENTS.md instructions. Only the pilot receives the frozen knowledge/skills/tools and an instruction to use them. Original untracked files and Git metadata are excluded. Source commits and content hashes are recorded outside the run directories; `inspect` reporting no Git commit inside a run is expected.

Open one fresh agent session per run with that run directory as the workspace. Send this same message in each session:

> Read AGENTS.md and complete TASK.txt. Work only inside this workspace. Report validation evidence and any limitations.

Use the same model, reasoning effort, tool permissions, and budget. Disable unrelated/global SST skills for both arms. Do not reuse conversation context. Keep each session confined to its run directory; the preparation tool does not configure an OS sandbox, so establish workspace isolation in your agent environment. An agent must not inspect sibling runs, frozen snapshots, or evaluation rubrics.

Before timed runs, install/build SST with the same configuration in each isolated environment. Use distinct prefixes for each run, especially extension tasks; never let one run load another run's libraries. Keep setup outside the measured task, record setup commands, and verify runtime identity. If no installation is available, runs can measure exploration but cannot earn a correctness pass. Do not compare such runs with runtime-enabled ones.

## Tasks and scoring

Agent prompts live in `evaluation/prompts/`; evaluator-only rubrics live in `evaluation/rubrics/`. Eight tasks cover existing-model configuration, Merlin routing extension, memory-backend timing extension, Ember workloads, Mercury runtime, Vanadis program execution, Carcosa injection, and Balar vector execution. The new element tasks deliberately expose prerequisite and integration gaps; missing binaries/toolchains must score blocked rather than pass. Prompts specify desired behavior without implementation paths. Rubrics score observable behavior rather than an exact patch.

After a run, independently review its deliverable and execute the rubric checks against that run's installation. New experiments freeze the scoring rubric at `evaluator/rubric.json`, outside the agent workspaces, and record SHA-256 hashes for it, the task, and the pilot files in `experiment.json`. Use that frozen rubric instead of a subsequently edited repository copy. Older experiments without a rubric snapshot need an explicitly recorded rubric version before scoring. Save command outputs outside the agent workspace. Score pass only with evidence for every criterion; use fail for demonstrated incorrect behavior and blocked for missing prerequisites or a demonstrated source capability gap under the task's constraints. Preserve failed attempts and interventions in the results.

Some tasks deliberately test whether the agent recognizes implementation limits. For example, TrafficGen ends on injection completion and does not expose the per-packet arrival/identity oracle required by `network-config`; `merlin.test_nic` sends to all peers, including itself, rather than only the next neighbor. A bounded destination distribution alone does not resolve these constraints. Carcosa has a reproduced manager-registration ordering issue, but the direct `StuckAtFaultInjector` path can bypass Hali; that manager finding alone does not justify blocking `carcosa-fault`. Inspect the selected path, artifacts, and oracle. A source-backed limitation report can be a useful result, but it does not earn a model-correctness pass. Do not interpret token savings from these blocked pairs as savings on a successful model construction task.

For the configuration task, explicitly inspect the packet-count/destination oracle: an SST process exiting successfully alone is not sufficient. For code tasks, verify both targeted behavior and a neighboring regression. Do not disclose the rubric or the other arm's implementation to an agent before it finishes.

## Record measurements

Fill `results.csv` in the prepared experiment directory. Blank means unknown; do not enter zero for unavailable usage.

- `input_tokens`: total input usage for the entire fresh session, including instructions, knowledge loading, tool results, and cached input.
- `cached_input_tokens`: subset of input, when reported. Do not add it to input again.
- `output_tokens`: total output usage for the session. Record whether the provider includes reasoning tokens in notes.
- `usage_source`: exported session report or trace path. If only per-request usage exists, sum every request; do not use only the final request's usage.
- `elapsed_seconds`: wall time from task submission through final validation/report, excluding prebuilt environment setup.
- `source_files_read`: distinct source files whose contents the agent inspected; count search-result snippets too. Use null/blank if the trace cannot support an accurate count.
- `exploratory_calls`: tool calls made to discover or understand code, excluding edits, builds, and validation. Use the same classification in both arms.
- `human_interventions`: corrections or assistance after the task begins.
- `evidence`: evaluator output/trace location. Keep raw traces private; inspect for secrets before sharing.

A character count or estimated token count is not measured session usage. If your agent does not report usage, still score correctness and exploration and leave token fields blank.

Summarize:

```sh
python3 tools/evaluate.py summarize --results ../sst-ai-evaluation-smoke/results.csv
```

The summary reports all verdicts, unpaired run IDs, and paired token totals. Invalid arms/verdicts, duplicate runs or pairs, negative/non-numeric usage, and cached input exceeding total input are rejected. Interpret saved tokens as an efficiency improvement only when both runs pass; report failures separately. Cached usage can affect latency and price even when total token counts match.

## Repeat the comparison

Run at least three pairs per task with fresh sessions. Alternate/randomize arm order to reduce order effects; keep all other settings fixed.

```sh
python3 tools/evaluate.py prepare --workspace .. --output ../sst-ai-evaluation-network --task network-extension --repeats 3
python3 tools/evaluate.py prepare --workspace .. --output ../sst-ai-evaluation-memory --task memory-extension --repeats 3
```

Preparation copies tracked working-tree contents once, then copies that frozen snapshot into each arm. It does not change source repositories or install dependencies. Existing output directories are rejected. Each pair can consume hundreds of MB; remove completed generated experiments manually after retaining results and patches.

## Freshness and selective-loading checks

The helper tests already exercise changed-source detection, missing sources, and broken links. To check agent behavior, use a disposable pilot run: change a referenced source file, run the knowledge check, and ask the agent to reconcile the affected guide before using it. Keep this separate from the primary paired trials. Check the trace to determine whether it inspected current source rather than only refreshing the hash.

For selective loading, inspect configuration-run traces for irrelevant core-extension/memory guidance. Report files loaded and their contribution to total usage; do not claim savings merely because fewer source files were read.

Additional task choices: `ember-workload`, `mercury-runtime`, `vanadis-program`, `carcosa-fault`, and `balar-vector`. Select one with `prepare --task <name>`. Existing prepared experiments remain frozen; prepare a new experiment to evaluate expanded knowledge.
