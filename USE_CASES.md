# Common SST model use cases

The [element selector](ofk/elements/index.md) contains all 34 profiles. Choose the abstraction needed to answer the question, then pair a workload with its hardware and supporting interfaces.

| Question | Starting combination | What to check |
|---|---|---|
| How does topology/routing affect message latency or congestion? | Merlin plus its traffic generator, Ember/Firefly, or Mercury with the selected MPI stack | Workload schedule, endpoint/protocol costs, routes, offered load, buffering and completion |
| How does an on-chip mesh compare with a crossbar? | Kingsley or Shogun plus compatible endpoints and memHierarchy | Same workload, routes and contention; Kingsley models flits, while Shogun uses fixed round-robin and messages per cycle |
| What limits memory bandwidth under controlled traffic? | Miranda plus memHierarchy; optional Cassini | Known request patterns/counts, outstanding limits, memory timing and prefetch versus demand traffic |
| How do cache changes affect a real binary? | Vanadis or a compatible Ariel frontend plus memHierarchy | ISA/ABI or frontend prerequisites, application outputs, cache misses/stalls and modeled CPU fidelity |
| How does a recorded memory workload respond to a memory change? | Prospero plus memHierarchy; optional cacheTracer | Trace format, known request sequence and completion; current Prospero writes zero-filled payloads |
| How do TLB/page allocation policies affect requests? | Compatible mmu or Samba path; Opal for supported allocation integration | Translation API, mappings/page sizes and walk assumptions; Opal hint/unmap handlers are incomplete |
| How do DRAM/NVM/stacked-memory configurations compare? | memHierarchy's built-in `simpleDRAM`/`timingDRAM` backends first; cramSim, Messier, or VaultSim through their memHierarchy bridges; Ramulator/GOBLIN only when built | Equal workloads and address mapping; the [backend catalog](ofk/elements/memHierarchy/backends.md) lists knobs and tests; cramSim has command timing, Messier models NVM organization, VaultSim uses fixed-delay vault responses |
| How do several cores share caches, or a directory over a network? | memHierarchy Bus or MemNIC with DirectoryController; the two 4-core examples | Transport choice, address interleaving, cache type, and coherence protocol; see [memory systems](ofk/elements/memHierarchy/systems.md) |
| How do fault patterns affect application or memory correctness? | Carcosa plus Vanadis/memHierarchy | Injection hook, address/bit/timing, reproducible seed, no-fault baseline, recovery and data oracle |
| What are CPU/GPU command and transfer bottlenecks? | Balar plus selected trace or Vanadis mode and memory system | CUDA/GPGPU-Sim artifacts, MMIO/DMA ordering, numerical results, transfer counts and completion |
| What do in-memory matrix-vector arrays gain or lose? | Golem plus Vanadis/RoCC; optional CrossSim | Matrix outputs, precision/nonidealities, array timing and selected Python environment |
| How do dataflow or CGRA graph mappings behave? | Llyr for mapped graphs with memory; Serrano for the implemented standalone iterator/add/output graph | Llyr's native suite is disabled; Serrano SUB and general memory coupling require implementation |
| How does a spiking neural workload progress? | Gensa plus compatible StandardMem memory and a required SimpleNetwork interface (example uses Merlin) | Network/neuron context, firing events, supported numeric semantics and finite workload |
| How does RDMA-style NIC behavior interact with host memory? | rdmaNic plus compatible memory and network components | Supported command semantics, DMA/MMIO wiring, remote data, ordering and completion |
| How can external RTL join a model? | Osseous/generated component and its demonstrated consumer | Generated C-model artifacts, signal/transaction interface, example outputs and time coordination |
| How can recorded communication be replayed? | Zodiac and its supported SIRIUS/communication stack | Trace availability, supported calls, working directory, completion and trace-limited feedback |
| How should a new component use SST APIs? | simpleElementExample; simpleSimulation for decomposition examples | Registration, ownership, lifecycle, statistics, termination and matching example references |

Hermes, Iris, and Thornhill supply APIs/runtime/compute support; validate them through actual consumers rather than inventing standalone hardware roles. Likewise, choose memory endpoints and translation interfaces by their contracts, not by element names alone.

Read the linked profiles for implementation limits, dependencies, and known failures. These are starting combinations, not drop-in compatibility guarantees. Inspect the selected source configuration and current ELI/interface definitions before constructing a model. Use [build-network-model](skills/build-network-model/SKILL.md) or [build-cpu-model](skills/build-cpu-model/SKILL.md) to clarify priorities, choose elements, build the configuration, and validate the mechanism under study.

## Cross-cutting workflows

| Need | Guide |
|---|---|
| Enable, output, and validate statistics | [Statistics](ofk/using-sst/statistics.md); implementation in [statistics API](ofk/core/statistics-api.md) |
| Command-line and Python-settable options | [Run-time options](ofk/using-sst/run-options.md) |
| Ranks, threads, partitioners, synchronization | [Parallel execution](ofk/using-sst/parallel.md) |
| Checkpoint and restart, element serialization | [Checkpoint and restart](ofk/using-sst/checkpoint.md) |
| Element library outside sst-elements | [External elements](ofk/development/external-elements.md) |
| Which Ember motif models which pattern | [Ember motif catalog](ofk/elements/ember/motifs.md) |
| Write a new Ember motif | [Create an Ember motif](ofk/elements/ember/new-motif.md) with the `create-ember-motif` skill |
| Run application code on Mercury | [Mercury skeleton applications](ofk/elements/mercury/skeleton-apps.md) with the `create-mercury-skeleton` skill |

## Mercury application toolchains

For C/C++ application studies, SST-HGCC compiles/rewrites loadable Mercury workloads. Use Mask-MPI for its supported modeled MPI behavior; use an adapted MVAPICH2 stack when implementation-specific collective/protocol behavior is the target. The latter connects through Iris libfabric/PMI to Mercury and the selected network. See [the HGCC/MV2 use-case guide](ofk/elements/mercury/hgcc-mv2.md); both routes ran on the recorded devel install on October 7, 2026, the MV2 route only with the Iris provider patch that guide records. Neither route is a substitute for a detailed CPU pipeline model.
