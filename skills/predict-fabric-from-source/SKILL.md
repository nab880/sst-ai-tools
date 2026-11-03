---
name: predict-fabric-from-source
description: Build SCCG-instrumented Mercury skeletons with hg++ --emit-sccg, run paired uncongested and cycle-accurate Merlin sweeps with epoch telemetry, and assemble the dataset for a congestion surrogate.
---

# predict-fabric-from-source

This skill belongs to the sst-ai-tools repository. Resolve the real path of this skill directory first, then use `../..` as the repository root; this also works when the skill directory is symlinked into an agent's skill directory. Keep this repository intact when installing; sibling OFK documents and tools are required. Resolve SST source roots from the user or the sibling workspace, not the shell's current directory.

Read [the SCCG and telemetry guide](../../ofk/elements/mercury/sccg-telemetry.md), then [skeleton applications](../../ofk/elements/mercury/skeleton-apps.md) and [HGCC installation](../../ofk/development/hgcc-install.md). The pass and hooks live on local `sccg-ml` branches of `sst-hgcc` and `sst-elements`; confirm `hg++ --help` lists `--emit-sccg` and `nm libhg.so` shows `ssthg_ml_epoch_begin` before relying on them, and build them from those branches otherwise.

Establish the question first: which motifs or applications, rank counts, message-size regimes and Merlin topologies, and whether modeled compute volume is part of the study (it drives memory; see the guide). Write or select skeletons with `#pragma sst compute` on the loops to model, null payload buffers, and argument conventions the harness can evaluate symbolically (`atoi(argv[k])`, world size and rank from `MPI_Comm_size/rank`).

Compile every variant with `hg++ --emit-sccg`, parse each sidecar as JSON, and check that every MPI call has `hooks: true`, that partner and count expressions are `resolved`, and that nonblocking requests have `ASYNC_COMPLETION` edges to their waits. Run one configuration in both network modes before any sweep and verify the epoch files join one-to-one on (rank, node_id, seq), that compute rows carry the modeled flop counts, and that the fabric makespan is not shorter than the uncongested one. Then sweep with bounded parallelism (two niced, RSS-capped simulators on a 16 GB host), ordered cheap-first and resumable, compacting each run's statistics to router stall totals and NIC latency quantiles as it finishes.

The reference harness is `hg-netgnn/` in the sibling workspace (`hgnet.build`, `hgnet.run`, `hgnet.sweep`, `hgnet.dataset`, `hgnet.train`). Report the simulator revision, platform parameters (`flow_mtu`, eager threshold, link bandwidth and buffers), failed or killed runs, and the split used for any accuracy claim; a random split over one rank count is a smoke test, not the leave-one-motif-out or scale-extrapolation result.
