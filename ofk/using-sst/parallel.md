---
{
  "type": "SST Guide",
  "title": "Parallel execution and partitioning",
  "description": "Run SST across MPI ranks and threads, choose a partitioner, and validate parallel results.",
  "tags": [
    "parallel",
    "partitioning"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/claude",
    "at": "2026-10-07T09:15:54.320633+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/config.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/config.cc",
      "x-sha256": "0b3e06f2092a2202f316c504a7486279e01f0503a68a1c3a7cddaa810c9e3f82",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/simulation.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/simulation.cc",
      "x-sha256": "789d9ae3803d4d242177415d1c0395014a16c400b375060083c79fa8cb713c9c",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/sync/syncManager.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/sync/syncManager.cc",
      "x-sha256": "45111731e7ca2a836fa8b5d49d73735a60ce70f7753e29f8664a811949253e76",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/sstpart.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/sstpart.h",
      "x-sha256": "9932ae88f239bf8df0a8397e2bbf13033e20fb3f0d69df35aace5b242d480dad",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/impl/partitioners/linpart.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/impl/partitioners/linpart.h",
      "x-sha256": "588090d604a92b3097477a7cae4aed4254eafcf414d28a7f9fb2f1f976526cfa",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/impl/partitioners/rrobin.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/impl/partitioners/rrobin.h",
      "x-sha256": "6a54f6113c30de365d56ee1b8c6d7f9fa23ab62df00a633d2453a72c64f05ee6",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/impl/partitioners/selfpart.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/impl/partitioners/selfpart.h",
      "x-sha256": "90a192432fad150d60996d84f582d6200ac9a65a8be4759a02bb99afbeb886df",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/impl/partitioners/simplepart.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/impl/partitioners/simplepart.h",
      "x-sha256": "32673b68bf0c5372dd7dc282582187f159a1104de2fbb2996f4d95f244f44ae4",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/impl/partitioners/singlepart.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/impl/partitioners/singlepart.h",
      "x-sha256": "729c2930c4d7f08bdb45cd357b5a2c3ab79fd500c0a7fe319bf328cbe838c774",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/model/python/pymodel_comp.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/model/python/pymodel_comp.cc",
      "x-sha256": "d1ca70c38da5f2ab2a22d202d816499ae622de07dfb134ad1868a18724e7f58c",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/model/python/pymodel.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/model/python/pymodel.cc",
      "x-sha256": "50756980d9a002a223f75593ed329a245007d4decdc32f6de37c280c23c36e70",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s11",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/testingframework/sst_unittest.py",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/testingframework/sst_unittest.py",
      "x-sha256": "644fec8123672c16293dae9a9f55a4e62a5a26321942ae0345ed0af5b7b60d33",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s12",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/testsuite_default_partitioner.py",
      "x-repository": "sst-core",
      "x-path": "tests/testsuite_default_partitioner.py",
      "x-sha256": "a247e3dbc8aea3cbc30dd9e676cad776da8e222975d8fef72f969f59f4dae47a",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s13",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/test_StatisticsComponent_basic.py",
      "x-repository": "sst-core",
      "x-path": "tests/test_StatisticsComponent_basic.py",
      "x-sha256": "f1e8cca6463f2380518fa497e96922b306b9f3d244f6f23c4365da75eb1e4532",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s14",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/config.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/config.h",
      "x-sha256": "558122861f5b4f6b87e3ef09c851f2bf21eb478b3b1cb89e5532839f0d112297",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s15",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/main.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/main.cc",
      "x-sha256": "03d2c1991a0dc059d44c03f1cf57cacecf34256b9a4c03a0ae977844ef27ec85",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    }
  ]
}
---
# Parallel execution and partitioning

SST runs one process per MPI rank and `-n`/`--num-threads` threads per rank. Every component is assigned to one rank and thread; links between partitions are the only interaction, and their latency bounds how far partitions may drift apart. Ranks come from the launcher: `mpirun -n 2 sst -n 2 model.py` runs two ranks of two threads.

## Partitioners

`--partitioner=lib.name` (or `sst.setProgramOptions({"partitioner": "roundrobin"})` in the configuration) selects how components are placed; the default is `sst.linear`:

| Partitioner | Behavior |
|---|---|
| `sst.linear` | Divides the component ID space into equal ranges; sequential IDs stay together. |
| `sst.roundrobin` | Places sequential IDs on different ranks. |
| `sst.simple` | Partitions across high-latency links while balancing component counts. |
| `sst.self` | Uses the placement already in the configuration: `comp.setRank(rank, thread)` and optional `comp.setWeight(w)` from Python. |
| `sst.single` | Everything on rank 0; selected automatically for serial runs. |

`--output-partition[=FILE]` writes the assignment, or adds it to `--output-json`/`--output-config` output when given without a file. `--parallel-output` writes configuration output per rank.

## What synchronizes

Only links cross partitions. During graph setup rank 0 (every rank under `--parallel-load`) computes the smallest latency of any link between ranks and an MPI all-reduce distributes it as `min_part`; each thread then computes the smallest latency of links to each other thread on its rank (`interThreadMinLatency`). Those minimums are the synchronization lookahead, so one short cross-partition link forces every partition to synchronize at that interval. A partition with no cross-rank links and no cross-thread links is marked independent and never synchronizes.

The sync objects are chosen from those minimums (`sync/syncManager.cc`): `RankSyncSerialSkip` when each rank has one thread, `RankSyncParallelSkip` otherwise, and `EmptyRankSync` when no link crosses ranks, in which case checkpointing and the interactive console are disabled with a warning. Threads with no inter-thread link dependency get `EmptyThreadSync`; otherwise they use `ThreadSyncSimpleSkip`, or `ThreadSyncDirectSkip` when `--interthread-links` is enabled; that experimental mode selects a `.ts` TimeVortex variant and is turned off automatically on checkpoint restart.

## Loading the configuration in parallel

By default only rank 0 runs the Python script and builds the whole graph; after partitioning, `splitGraph` sends each rank its subgraph over MPI. `--parallel-load[=MODE]` (multi-rank jobs only, and only for model types that support it) makes every rank run the script: `SINGLE` passes the same file to all ranks, `MULTI` (the default when the flag is given) expects one file per rank, `NONE` disables it. `sst.getMPIRankCount()`, `sst.getMyMPIRank()`, and `sst.getThreadCount()` let a script create only its own components, which is required for `MULTI`.

## What may differ from a serial run

The core's partitioner suite runs `test_MessageMesh.py` serially and under the requested ranks/threads with `sst.linear`, `sst.roundrobin`, and `sst.simple`, then compares sorted output: content must match, line order may not. Expect the same differences in models: statistics outputs become per-rank files with a `Rank` column ([statistics](statistics.md)), and interleaved console output changes order. A behavioral difference beyond ordering indicates shared static state, a component that assumes it sees every event, or a link latency that does not represent the modeled delay.

## Host requirements and the recorded campaign

Parallel ranks require a core built against MPI (`sstsimulator.conf` records `MPICXX`); threads need no extra dependency. The test runners build the command from `-r` and `-t`: more than one thread adds `-n T`, and more than one rank requires `mpirun` on the PATH. The recorded devel campaign ran `testsuite_default_Links.py` with ranks 1/threads 2 and ranks 2/threads 1, plus the Merlin thread and MPI cases, under `OMPI_MCA_btl=self,tcp` and `OMPI_MCA_btl_tcp_if_include=lo0` because OpenMPI's shared-memory transport printed warnings on this host (evidence: repository `RUNTIME_VALIDATION.md`).

Many element suites skip under parallelism: single-component examples skip when ranks times threads exceeds one, Vanadis and Golem skip above one rank or thread, Mercury OS tests skip above one, and Mask-MPI's sparse-communicator case skips with multiple ranks. Check the element profile before attributing a skip to a failure.

## Checklist for a parallel model

- Run the same configuration serially and in parallel; compare sorted outputs and per-rank statistics totals.
- Give every cross-partition link the full modeled latency; a tiny latency is a performance problem, not a correctness aid.
- Avoid static or global state in elements; partitions cannot see each other's memory.
- Record ranks, threads, the partitioner, and the MPI environment with results; `--output-partition` documents the placement.
- Use `--timing-info` to separate simulated time from host time when judging scaling.

See [run-time options](run-options.md) for the option list and [testing](../development/testing.md) for runner flags.
