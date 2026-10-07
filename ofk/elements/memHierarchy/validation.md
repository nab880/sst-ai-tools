---
{
  "type": "SST Guide",
  "title": "Validate memory behavior",
  "description": "Select memory, coherence, and configuration tests by changed semantics.",
  "tags": [
    "memHierarchy",
    "testing"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T09:15:52.717359+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-1core-nocache.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-1core-nocache.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "e5084ba0f62d2b51da267186efb3f4fa2be18d7da16ae783f15d012e64bf368b"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-1core-1level.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-1core-1level.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "4c3faf5b97b155c781e41f14c948a3e4b2eea3acecd183f75b5d2363c6552c55"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memory.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memory.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "46c5b8e38c83811cde200b6fcad13bbc36ae9a6e00e0aeb5583bd8f4ff0801f1"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_coherence.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_coherence.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "a4910161dc9d05be091809338f6e9d32c60e70ba01bd979d790611a4ddedff88"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/interfaces/stdMem.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/interfaces/stdMem.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "0774a9fdbd647d6ed9375f3c6a686fac54e9d998aac2100a41fd45f7712bc8c4"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHA.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHA.py",
      "x-sha256": "94ebfdff60f7fb4f055dc1e5f5711de9ddf7f3ea01675167a3bfa233d562d786",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHSieve.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHSieve.py",
      "x-sha256": "bf317fe5831a30a8d74dfd126b1fa17b2d21cfebc1e03717e269ee89a32a7cca",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_sdl.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_sdl.py",
      "x-sha256": "cd917fd983ba7d3a90ea8df826b5decd5b9cd956d71d661a5954d6cc10c0c3cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_openMP_memHierarchy_dirnoncacheable.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_openMP_memHierarchy_dirnoncacheable.py",
      "x-sha256": "ce617b8f4a890daa53962a002e19704684d51ed658bcf112ac900948217855f9",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_openMP_memHierarchy_diropenMP.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_openMP_memHierarchy_diropenMP.py",
      "x-sha256": "5de9c785291e6446fde4090237ff73eb42855d8c46e15e135605c71c175dfc57",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_openMP_memHierarchy_noncacheable.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_openMP_memHierarchy_noncacheable.py",
      "x-sha256": "1901d61a7a6894cf54a19f45800419cbee0f350204fc367e2cca0be9ef8138c1",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s11",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_openMP_memHierarchy_openMP.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_openMP_memHierarchy_openMP.py",
      "x-sha256": "e41fed457581c82521eb83990b8d3265369e71c68c439022df3a0cd879c440ac",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s12",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_sweep_memHierarchy_dir3LevelSweep.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_sweep_memHierarchy_dir3LevelSweep.py",
      "x-sha256": "31459d972c4b390da954d1ef491e5afcf492d4bd7c72315aa4ff30edcfa2c9da",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s13",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_sweep_memHierarchy_dirSweep.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_sweep_memHierarchy_dirSweep.py",
      "x-sha256": "d5b92f0a11effdd6d8ed4ea7b99e3f856efa1b5afc47e06eadf20c9a4399a5a7",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s14",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_sweep_memHierarchy_dirSweepB.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_sweep_memHierarchy_dirSweepB.py",
      "x-sha256": "53f2e4a43209758b3c1f17fe0b2aa2ada4d158484e47f9e7e271a5f1ea294f0f",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s15",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_sweep_memHierarchy_dirSweepI.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_sweep_memHierarchy_dirSweepI.py",
      "x-sha256": "a0936f193d8144639550124d465a5a330ac788d90bab3e460a03e829701e4121",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s16",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_sweep_memHierarchy_openMP.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_sweep_memHierarchy_openMP.py",
      "x-sha256": "94a30475a049f8bae8bc757b1e10fc74681bd746467ddaa3fda9e8df27e1008c",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s17",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_weekly_memHierarchy_examples.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_weekly_memHierarchy_examples.py",
      "x-sha256": "1a9b0bc272e85a74570816e0b03c85cbc2a05798136299a95e65fe638f544385",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s18",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-1core-3level.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-1core-3level.py",
      "x-sha256": "a9ff38b99fcf2e3bc32d227eca5d9a510f6a76c63b2b40c23d82658ec9aab568",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s19",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-4core-shared-llc.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-4core-shared-llc.py",
      "x-sha256": "eb92baeff33ece28f48196924cdf7518c0d49e29da26203fd7a1a65c75ebaff2",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s20",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-4core-shared-distributed-llc.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-4core-shared-distributed-llc.py",
      "x-sha256": "741eff91755a032a9f4f81e78969053be70c51b32cb1129355a44c7c61a92c0e",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s21",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memoryController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memoryController.h",
      "x-sha256": "252967f0759b504d26596bb3f77f8cb091464c78fbe24400d7362d500f4ed3a3",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s22",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/testcpu/standardCPU.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/testcpu/standardCPU.h",
      "x-sha256": "f5ccb0ce81c5ec8b0191e3352d4ef75190290960194d8ec7fe37046556d9e99b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s23",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/cacheController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/cacheController.h",
      "x-sha256": "441c5e2f7f2a7a43121573eca67bec3eba3fd30d4dd3b44363227f4c10027006",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s24",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cacheTracer/cacheTracer.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cacheTracer/cacheTracer.h",
      "x-sha256": "1c67a3f6a82a5ba5006bbcb514f37465eff27820e6c9a97563b6bfdae023e3e4",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---
# Validate memory behavior

Use `examples/example-1core-nocache.py` for controller/backend isolation and `example-1core-1level.py` for a small cached model. The latter uses a finite seeded workload, enables statistics, and shows units and address ranges. The weekly examples suite runs all five examples with a completion check only.

## Suites

| Suite | Scope and prerequisites |
|---|---|
| `tests/testsuite_default_memHierarchy_memory.py` | Backing-store modes: `backing_0_mmap_out` through `backing_5_init`. |
| `tests/testsuite_default_memHierarchy_coherence.py` | Single-core (cases 0-6), two-core (0-11), and four-core (0-3) MESI cases plus `none` (0-4). |
| `tests/testsuite_default_memHierarchy_memHA.py` | 43 feature cases: backends (`BackendChaining`, `DelayBuffer`, `ReorderRow`, `ReorderSimple`, `SimpleDRAM_1/2`, `TimingDRAM_1..4`, `VaultSim`, conditional `GoblinHMC`, `Ramulator_1/2`, `Ramulator2`), cache features (`DistributedCaches`, `Flushes`, `Flushes_2`, `HashXor`, `Noninclusive_1/2`, `PrefetchParams`, `ThroughputThrottling`, `CoherenceDomains`, `RangeCheck`, `MemoryCache`), custom commands (`CustomCmdGoblin_1..3`), Kingsley transport, scratchpads (`ScratchCache_1..4`, `ScratchDirect`, `ScratchNetwork`), and StandardMem (`StdMem`, `StdMem_flush`, `StdMem_nic`, `StdMem_noninclusive`, `StdMem_mmio`, `StdMem_mmio2`, `StdMem_mmio3`). External-backend cases skip when `sstsimulator.conf` has no `LIBDIR` for them; `Ramulator2` also skips on macOS; `BackendTimingDRAM_1..4` and `BackendGoblinHMC` are nightly-only. The memHA oracle is a reference diff of statistics with tolerances on `outstanding_requests`, `total_cycles`, and `MSHR_occupancy`. |
| `tests/testsuite_default_memHierarchy_sdl.py` | Fourteen `sdl*` configuration regressions; its filters drop the rank/thread warning, DRAMSim2 banner lines, memory-region notices, and alignment notes before comparing. |
| `tests/testsuite_default_memHierarchy_memHSieve.py` | Ariel Sieve profiling; requires Pin (compiled, valid version, loaded). |
| `tests/testsuite_openMP_memHierarchy_{openMP,diropenMP,noncacheable,dirnoncacheable}.py` | OpenMP binaries under Ariel; skip without `INTEL_PIN_DIR`. |
| `tests/testsuite_sweep_memHierarchy_{dirSweep,dirSweepB,dirSweepI,dir3LevelSweep,openMP}.py` | Parameterized matrices that skip without Pin; `SST_SWEEP_dirsweep_LIST`, `SST_SWEEP_dirsweepB_LIST`, `SST_SWEEP_dirsweepI_LIST`, `SST_SWEEP_dir3levelsweep_LIST`, and `SST_SWEEP_openMP_LIST` take `first-last` ranges and `SST_SWEEP_OPENMP` picks the application. |
| `tests/testsuite_weekly_memHierarchy_examples.py` | The five examples; completion and no `FATAL` only. |

Choose by the affected behavior rather than running only the memory suite for every change. Use [test planning](../../development/testing.md) with target `memHierarchy`; the planner lists all fifteen suite files.

## Oracles beyond "it completed"

For timing changes check completions, request counts, latency expectations, and preserved data behavior. For coherence changes include conflicting accesses and a meaningful data-correctness oracle; cache hit/miss statistics alone are insufficient. Cover address boundaries, writes/writebacks, and outstanding requests as applicable. Useful instruments:

- `backing_out_file` or `backing_out_screen` on the controller dumps final memory contents; `backing_in_file` preloads a known image; `backing=none` removes data entirely, so leave it unset for correctness checks.
- `standardCPU` `test_init` writes initial values, and its frequency parameters (`write_freq`, `flush_freq`, `llsc_freq`, `custom_freq`) select which command classes a run exercises; `verbose` prints each operation.
- `debug`, `debug_level` (0-10), and `debug_addr` on caches, directories, controllers, and NICs trace one address through the hierarchy; they require a core configured with `--enable-debug`.
- `cacheTracer` sits between an interface and a cache to count events and histogram latencies without changing the model.
- Statistics such as `TotalEventsReceived` and `MSHR_occupancy` are declared in `cacheController.h`; enable them per [statistics](../../using-sst/statistics.md) and validate the counters on a tiny workload first.

For locked-write metadata checks, account for the reproduced `StandardMem::WriteUnlock::makeResponse` defect: it zeroes `vAddr` in both the request and response. See [core contracts](../../core/contracts.md) and validate virtual-address propagation separately from physical-memory data correctness. Backend-only timing tests do not cover this interface path; the memHA suite's `test_memHA_StdMem*` cases drive StandardMem through reference-output comparison rather than a virtual-address assertion.

Parallel runs change output ordering and add per-rank statistics files; compare sorted outputs ([parallel execution](../../using-sst/parallel.md)). Components with serializable events do not thereby support checkpoints; see [checkpoint and restart](../../using-sst/checkpoint.md).
