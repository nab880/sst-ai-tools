---
{
  "type": "SST Guide",
  "title": "Ember motif catalog",
  "description": "Registered Ember motifs by family with selection syntax and defining parameters.",
  "tags": [
    "ember",
    "workload"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/claude",
    "at": "2026-10-07T09:15:53.915823+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/pyember.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/pyember.py",
      "x-sha256": "725b81f9f1e38e54c7a0ea2ee36fcb6eb87340507bd35922cc7598e51225bf78",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/test/emberLoad.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/test/emberLoad.py",
      "x-sha256": "162a44de6f921e5fddc13f0a103d2eb53e2045a42ae41e061630cdfe1ad5a79d",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/test/loadInfo.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/test/loadInfo.py",
      "x-sha256": "80f250752524052af4ffc263a405c227f977187a430da7b7cd3cc5007cbdc760",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/tests/testsuite_default_ember_sweep.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/tests/testsuite_default_ember_sweep.py",
      "x-sha256": "685ab6d46c649d043a5bc80609fd703b2d72aa08a14909b1fe7e3ad0d29f1e98",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/mpi/motifs/emberpingpong.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/mpi/motifs/emberpingpong.h",
      "x-sha256": "6c232b0ee2553cac9465b9770a3de4e7cfba23c66e84d72877c5df028feda166",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/mpi/motifs/emberhalo3d.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/mpi/motifs/emberhalo3d.h",
      "x-sha256": "50ca55e642dd8f7f5d81cc0d664e0f0f4de579a80535d36ff9eed4af1be9351c",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/test/basicDetailedModel.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/test/basicDetailedModel.py",
      "x-sha256": "79d29391e9e49ee2eb0085785ea1ae916dd0f66a0480b09a56befb1356f9e42e",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/embergen.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/embergen.cc",
      "x-sha256": "85eb4a831d0702d53800dc468f08cce17f9dd7b007cec4e4315a87fd2f3d4438",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/mpi/motifs/ember3dcommdbl.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/mpi/motifs/ember3dcommdbl.cc",
      "x-sha256": "f6ac0500849d962b0a385cd57b5093b22d8eb82ec9a20366df53681613e51596",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---
# Ember motif catalog

The recorded devel install registers 128 `ember.<Name>Motif` subcomponents. This catalog groups them by family and names the parameters that define each workload; descriptions are the ELI text. Selection mechanics and the shared caveats come first because every family uses them.

## Selecting motifs

`test/emberLoad.py` accepts repeated `--cmdLine "<Motif> key=value ..."` options and appends each one to the workflow in order; `pyember.py`'s `addMotif` maps the first token to `ember.<Motif>Motif` (or `<lib>.<Motif>Motif` when a library prefix is given) and every `key=value` token to the ELI parameter `arg.<key>` of that motif, so `PingPong iterations=10 messageSize=64` sets `arg.iterations` and `arg.messageSize`. Node placement comes from the loader's own node list (`0-<N-1>` by default, or a load file's `nid_list`), not from the command string; the `-nidList=` prefixes that `emberLoad.py` builds for random placement and background traffic (`Init`, `TrafficGen mean=... stddev=... messageSize=... startDelay=...`, `Fini`) have no parser in `loadInfo.py` in this checkout, so treat those paths as unverified. Begin a workflow with `Init` and end it with `Fini`, as the sweep suite does (`--cmdLine="Init" --cmdLine="<motif> <args>" --cmdLine="Fini"` inside `--model-options`); `motif_count` and `motif<N>.name` are generated for you. Every motif also accepts `primary`, whose ELI default reads 0 but whose code default is true, so a motif holds the simulation open until it finishes unless set false, and `distribModule`, whose code default is `ember.ConstDistrib` (`GaussianDistrib` is also registered). ELI defaults can lag the code elsewhere too (CommDouble reads `arg.pex`, `arg.items_per_node`, and `arg.compute_at_step` with defaults 0, 64, and 2000 while its ELI lists 1, 100, and 1000), so confirm a default in the motif's `.cc` before relying on it.

Parameter spellings differ between motifs (`messageSize` versus `messagesize`, `iterations`, `count`, `nelems`); `sst-info ember.<Name>Motif` lists the exact names.

## MPI point-to-point and traffic patterns

| Motif | ELI description | Defining parameters (defaults) |
|---|---|---|
| `PingPong` | Performs a Ping-Pong Motif | `messageSize` (1024), `iterations` (1), `rank2` for the partner |
| `BiPingPong` | Performs a InOut Motif | `messageSize` (1024), `iterations` (1) |
| `AllPingPong` | Performs a All Ping Pong Motif | `iterations` (1024), `messageSize` (128) |
| `Ring` | Performs a Ring Motif | `messagesize` (1024), `iterations` (1) |
| `Sendrecv` | Performs a Sendrecv Motif | `rankmapper` only |
| `MsgRate` | Performs a message rate test | `msgSize` (0), `numMsgs` (128) |
| `Incast` | Performs a message incast Motif | `messageSize` (1024), `iterations` (1) |
| `NtoM` | Performs a N to M Motif | `messageSize` (1024), `iterations` (1) |
| `HotSpots` | Models network traffic with hot spots | `messageSize` (1), `mean` (1) |
| `Random` | Performs a random traffic pattern communication | `messagesize` (1), `iterations` (1) |
| `TrafficGen` | Models network traffic | `messageSize` (1), `mean` (1); `stddev`, `startDelay` in the loader |
| `Comm`, `CommDouble` | comm_split test; communication doubling pattern | `messagesize`/`iterations`; `pex`/`pey` |
| `Testany`, `Waitany` | Request completion tests | `rankmapper` only |
| `DetailedRing`, `DetailedStream` | Ring and Stream with the detailed compute model | `messagesize`/`iterations`; `stream_n` (1024), `n_per_call_copy` (1000); both need Thornhill detailed compute (see `test/basicDetailedModel.py`) |
| `SIRIUSTrace` | SIRIUS trace-based execution | `traceprefix` |
| `TestNetworkIO` | Network IO Test | `messageSize` (1024), `iterations` (1) |

## MPI collectives

| Motif | ELI description | Defining parameters (defaults) |
|---|---|---|
| `Barrier` | Performs a Barrier Motif | `iterations` (1024), `compute` (1) |
| `Bcast`, `Reduce` | float64 broadcast / SUM reduction from a user-specified root | `iterations` (1), `count` (1) |
| `Allreduce`, `Allgather`, `Alltoall` | float64 SUM operations | `iterations` (1), `compute` (1) |
| `Allgatherv`, `Alltoallv`, `Scatter`, `Scatterv` | variable-count and scatter variants | `iterations` (1), `count` (1) |

## Application and stencil motifs

| Motif | ELI description | Defining parameters (defaults) |
|---|---|---|
| `Halo2D`, `Halo2DNBR` | 2D halo exchange, blocking or non-blocking receives | `iterations` (10), `computenano` (10) |
| `Halo3D`, `Halo3D26`, `Halo3DSV` | 3D blocking exchange, 26-neighbor non-blocking, single-variable | `nx`, `ny`, `nz` (100) |
| `Sweep2D`, `Sweep3D` | sweep exchanges with multiple vertex orderings | `computetime` (1000), `iterations`; `pex`/`pey`, `nx/ny/nz` (50), `kba` (1) |
| `3DAMR` | Adaptive refinement step from MiniAMR | `nx` (8) and related dimensions |
| `FFT3D` | Models an FFT | `nx`, `ny` (8) |
| `NASLU` | NAS-LU communication from two opposite vertices | `computetime` (1000), `pex` |
| `LQCD` | CG portion of Lattice QCD (MILC) with Naik gathers | `nx`, `ny` (8) |
| `CMT1D`, `CMT2D`, `CMT3D`, `CMTCR` | nearest-neighbor exchange over 1D/2D/3D decompositions; Crystal Router all-to-all | `iterations` (1), `elementsize` (10) |
| `BFS`, `TriCount`, `Unstructured` | ComBLAS BFS; triangle counting; graph-driven unstructured communication | `sz` (14), `seed`; `vertices_filename`; `graphfile`, `p_size` (10000) |

## Control motifs

`Init` and `Fini` initialize and finalize communication and take no arguments; `Null` idles a node; `Stop` performs a barrier and then raises a fatal error (used by NetworkSim to end a run); `Test` is a smoke motif.

## SHMEM and FAM motifs

Seventy-six motifs model OpenSHMEM-style operations (68 SHMEM plus eight `ShmemFAM_*`), named by operation and data type: `ShmemPut`/`Get`/`Putv`/`Getv`/`GetNBI` with `Int`, `Long`, `Float`, and `Double` suffixes (`nelems`, `biDir`, `printResults`); `ShmemAdd`, `Fadd`, `Cswap`, and `Swap` atomics per type; `ShmemAtomicInc` and its `Hot`, `NS`, and `V2` variants (`computeTime` 50, or 0 for the V2 variants, `dataSize` (33554432)); `ShmemReduction` per type; `ShmemCollect32/64`, `Fcollect32/64`, `Alltoall32/64`, `Alltoalls32/64`, `Broadcast32/64`; `ShmemBarrier`, `BarrierAll`, `Wait`, `WaitUntil`, `Test`, `Ring`, `Ring2`. Eight `ShmemFAM_*` motifs (`Put`, `Get2`, `Gatherv`, `Scatterv`, `AtomicInc`, `Cswap` by type) target fabric-attached memory with `totalBytes` and loop counts. These need the SHMEM Hermes/Firefly stack rather than the MPI one; the `ESshmem` suite is the entry point.

## Which motif for which question

- Point-to-point latency: `PingPong` (two ranks) or `AllPingPong`; message-rate limits: `MsgRate`.
- Collective scaling: `Allreduce`, `Barrier`, `Allgather`, `Alltoall`, with `compute` to model work between operations.
- Stencil or application-shaped traffic: `Halo3D`/`Halo3D26`, `Sweep3D`, `FFT3D`, `LQCD`, `NASLU`, `CMT*`.
- Irregular or hotspot load: `Unstructured`, `BFS`, `HotSpots`, `Random`, `Incast`, `TrafficGen` as background.

Motif completion does not validate payloads; the sweep compares only the simulation-complete line, skips indices at or below 100 outside the nightly category, and takes `SST_TEST_ES_LIST=first-last` ([validation](validation.md)). Generator semantics and the completion contract are in [extension points](extension-points.md); the stack assembly is in [overview](overview.md).
