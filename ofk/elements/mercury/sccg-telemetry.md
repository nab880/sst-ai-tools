---
{
  "type": "SST Guide",
  "title": "Static communication graphs and epoch telemetry for Mercury applications",
  "description": "Emit a compiler-side communication-compute graph with hg++ --emit-sccg, record per-epoch simulated time in Mercury, and run paired ideal/fabric Merlin experiments without exhausting host memory.",
  "tags": [
    "mercury",
    "sst-hgcc",
    "merlin",
    "telemetry",
    "machine-learning"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/claude",
    "at": "2026-11-03T11:00:00+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/da6456ef319bc45c7e7a6c66965546fda0a4b82c/src/sst/elements/mercury/common/skeleton.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/common/skeleton.h",
      "x-commit": "da6456ef319bc45c7e7a6c66965546fda0a4b82c",
      "x-sha256": "733d75ae12e2959c6233dcb9dcefba488fcd6de34343b2745bbeaf06b9c38f5e"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/da6456ef319bc45c7e7a6c66965546fda0a4b82c/src/sst/elements/mercury/common/skeleton.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/common/skeleton.cc",
      "x-commit": "da6456ef319bc45c7e7a6c66965546fda0a4b82c",
      "x-sha256": "fb92e395b78b6038890245caa2d36699b4f6210f3574d5dbf908deb2c77ced34"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/da6456ef319bc45c7e7a6c66965546fda0a4b82c/src/sst/elements/mercury/libraries/compute/memory_model.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/libraries/compute/memory_model.cc",
      "x-commit": "da6456ef319bc45c7e7a6c66965546fda0a4b82c",
      "x-sha256": "dfbed374c87f7fb5dc70f08d34af1c79c8c7691a24434f0131b4148bc89ae8ac"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/da6456ef319bc45c7e7a6c66965546fda0a4b82c/src/sst/elements/mercury/libraries/compute/instruction_processor.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/libraries/compute/instruction_processor.cc",
      "x-commit": "da6456ef319bc45c7e7a6c66965546fda0a4b82c",
      "x-sha256": "e6b35584ad3b08bdbe6b4a99780824575b7a2c439c5a8016d278085c8d422d36"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/da6456ef319bc45c7e7a6c66965546fda0a4b82c/src/sst/elements/mercury/operating_system/process/app.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/operating_system/process/app.cc",
      "x-commit": "da6456ef319bc45c7e7a6c66965546fda0a4b82c",
      "x-sha256": "0f7b51e1ec5cd87d2ebd7abc58494ee55935e4c31aa20b9727abbc9fe77d41e0"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/da6456ef319bc45c7e7a6c66965546fda0a4b82c/src/sst/elements/merlin/interfaces/linkControl.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/interfaces/linkControl.cc",
      "x-commit": "da6456ef319bc45c7e7a6c66965546fda0a4b82c",
      "x-sha256": "d61c8793dd5133afa155d7b84f49e02d1be71f1f9d18a29850cac2b5de4600ce"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-hgcc/blob/2a37f8c541f02344f7d540188e52efd1f080a6fc/clang/computeVisitor.cc",
      "x-commit": "2a37f8c541f02344f7d540188e52efd1f080a6fc",
      "x-review-scope": "External checkout inspected locally; the SCCG pass lives on a local branch (sccg-ml) of this checkout"
    }
  ]
}
---
# Static communication graphs and epoch telemetry for Mercury applications

This guide records a toolchain extension developed on 2026-11-02/03 in the
sibling workspace (`sst-hgcc` and `sst-elements` branch `sccg-ml`, harness in
`hg-netgnn/`). It turns a Mask-MPI skeleton into two artifacts: a **static
communication-compute graph** (SCCG) emitted by `ssthg_clang`, and **per-epoch
simulated timestamps** recorded by Mercury. Paired runs of the same skeleton on
an uncongested and a cycle-accurate Merlin fabric give training labels for a
surrogate that predicts fabric congestion from source. Everything below was
executed on the recorded devel checkouts; the upstream branches do not carry it.

## Compile: `hg++ --emit-sccg`

`hg++ --emit-sccg[=path] -c app.cc` implies `--skeletonize` and runs an extra
read-only AST pass after the skeleton pass. The pass sees `mask_mpi_*` calls
(the `MPI_*` macros expand before the AST exists), every loop as written, and
the `#pragma sst compute` regions the skeleton pass already replaced. It writes
`<app>.sccg.json` with:

- communication nodes (primitive, blocking/collective class, partner, count and
  datatype expressions, request handle key, enclosing loops and `if` guards),
  compute nodes (trip count, flops/intops/bytes per iteration from
  `ComputeVisitor`), and call-site nodes for user functions that communicate;
- edges `CFG_SEQUENTIAL` (lexical order within a function, not a control-flow
  graph), `LOOP_BACKEDGE`, `ASYNC_COMPLETION` (nonblocking request to the wait
  that names the same handle), `CALL`/`RETURN`;
- expressions printed in Python syntax over `P` (world size), `R` (rank),
  `ARGC`, `ARG<k>` (`atoi(argv[k])`, also through single-return helper
  functions) and loop variables, so a harness can evaluate partners, counts and
  trip counts per rank and per iteration.

It also wraps statement-level MPI calls as
`{ ssthg_ml_epoch_begin(id); ssthg_ml_epoch_msg(id, partner, count, datatype);
MPI_X(...); ssthg_ml_epoch_end(id); }` and modeled compute regions as
`begin / ssthg_ml_epoch_compute(id, flops, intops, bytes) /
sst_hg_compute_detailed / end`. Calls nested in larger expressions are listed
with `hooks: false`. Node ids are stable between the sidecar and the hooks but
not globally source-ordered (compute regions are numbered first).

Because `hg++` hands `ssthg_clang` a preprocessed file, "main file" tests must
use the presumed (line-marker) file name; `isWrittenInMainFile` matches every
header.

## Runtime: Mercury hooks

`common/skeleton.h` declares, with C linkage, `sst_hg_compute_detailed` and
`sst_hg_compute_detailed_nthr` (the compute pragma emits these; upstream
defines neither, so a skeletonized compute loop fails to resolve at load time)
and the four `ssthg_ml_epoch_*` hooks. The hooks are no-ops unless
`SSTHG_ML_EPOCH_FILE` names a CSV in the simulator's environment; the Python
driver sets it with `os.environ` since the application runs in-process. Each
completed epoch writes
`rank,node_id,seq,start_ns,end_ns,partner,count,datatype,flops,intops,bytes`,
keyed by the calling `Hg::Thread` and timestamped with `Thread::now()`, so
suspension inside a blocking call is included. `seq` counts completions per
(rank, node) so two runs of the same configuration join one-to-one.

The compute hook reaches `ComputeLibrary` through a new virtual
`ComputeAPI::computeDetailed`: `libhg` may not reference the ext library's
RTTI, and application libraries are keyed by the name after the colon in
`app1.libraries` (`ComputeLibrary`, `MpiApi`), as `App::getLibrary` shows.

## Driver facts that cost time to learn

- `app1.argv` must not repeat the application name; Mercury inserts `argv[0]`.
- `sst` passes script arguments only through `--model-options`.
- Enable statistics after `System.build()`; type-based enabling before the
  components exist records nothing. `merlin.linkcontrol` statistics reach the
  interface nested inside `ReorderLinkControl`. `packet_latency` is in
  nanoseconds (`getCurrentSimTimeNano()`), so histogram `binwidth` is in ns.
- Mercury has no analytical network model. An "uncongested" baseline is a
  Merlin configuration with 10 TB/s links, 1 ns latency and 16 MB buffers; it
  still charges Mask-MPI protocol costs, which is what makes the residual
  isolate fabric contention.
- Unallocated topology hosts become `EmptyJob` endpoints, so shapes need not
  equal the rank count. `topoDragonFly.setShape` has a parameter-name bug;
  set the attributes directly.

## Memory: the `flow_mtu` request chunk and an event leak

A modeled compute region (`#pragma sst compute`) is executed by
`InstructionProcessor::compute`: instruction time from flops and intops, then
`MemoryModel::accessFlow(bytes, ...)` splits `mem_sequential` bytes into
`bytes / flow_mtu` sequential requests across the node's memory channels
(`node.flow_mtu`, 512 B in the shipped platform files). Each request costs
two `ExecutionEvent`s, and a probe counting constructions against destructions
showed every one of them still allocated at exit (556,767 after two timesteps
of a 16-rank 3D stencil, 2,781,663 after ten): memory grows by roughly 240 B
per request for the life of the process. A 4-million-element region at 512 B
chunks is 200,000 requests per rank per iteration, so compute-heavy skeletons
reach 4-6 GB within seconds in any network mode, and six parallel simulators
exhausted a 17 GB workstation twice.

Mitigations used, in order of fidelity:

1. Keep modeled compute regions proportional to the message size (a 64-row
   slab per rank rather than an N x N tile) unless the volume term is the
   point of the experiment.
2. Raise `node.flow_mtu`. Timing is unchanged when a region fits in one chunk
   and within 0.1% for very large regions, but mid-size regions lose channel
   pipelining: a 786 KB region took 1.14 ms at 64 KB chunks and 1.79 ms at
   4 MB. 64 KB is a reasonable default; do not go to multi-megabyte chunks
   for small-compute studies.
3. Cap and watch the host: nice the `sst` processes, poll RSS and kill above a
   budget, and start new runs only when the machine has headroom
   (`hg-netgnn/hgnet/run.py`). Never run more parallel simulators than the
   RAM divided by the largest expected RSS.

The leak itself (events sent through `HgBase::sendExecutionEvent` on the
component self link, whose handler does call `delete`) was not resolved; see
the sibling workspace's `SCCG-PLAN.md` for the probe and current status.

## Validate

Compile a one-function fixture with `hg++ --emit-sccg` and check the sidecar
with FileCheck (`sst-hgcc/tests/lit-tests/sccg/emit-sccg.cc`; `llvm::json`
writes keys alphabetically, so use `CHECK-DAG`). Run one skeleton in both
network modes and confirm the epoch files have the same row count, join
one-to-one on (rank, node_id, seq), that compute rows carry the modeled flop
counts, point-to-point rows carry partner and byte counts, and that the fabric
run's makespan is never shorter than the uncongested one. The 2026-11-02
exercise did this for nine motifs in blocking and nonblocking variants on
torus, fat tree and dragonfly at 16 ranks (1:1 joins, fabric slower in every
case), and timed a 256-rank 1 MB butterfly at about 150 s wall and 1.8 GB.
