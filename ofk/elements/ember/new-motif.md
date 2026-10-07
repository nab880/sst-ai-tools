---
{
  "type": "SST Guide",
  "title": "Create an Ember motif",
  "description": "Implement, register, build, run, and validate a new communication motif.",
  "tags": [
    "ember",
    "extension",
    "workload"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/claude",
    "at": "2026-10-07T16:47:41.444168+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/embergen.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/embergen.h",
      "x-sha256": "9b0abe7315a71633cbfb893d587197c23ecf8fb2b090e39bd856d55c5cc7b67b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/embergen.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/embergen.cc",
      "x-sha256": "85eb4a831d0702d53800dc468f08cce17f9dd7b007cec4e4315a87fd2f3d4438",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/emberengine.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/emberengine.cc",
      "x-sha256": "757bef71e798f27a2d51211987f02972631fec7757dbe730118f4467c5625648",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/mpi/embermpigen.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/mpi/embermpigen.h",
      "x-sha256": "3dce203c8fbada9f8ec23eee0aa1a649ec4e4e4f8a5f7f6bd0db73dd8ec11319",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/libs/emberMpiLib.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/libs/emberMpiLib.h",
      "x-sha256": "e14d60e4739d1a73aac50974803a4fe656471d4dae45f1bc8c24198f51221e86",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/libs/emberMpiLib.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/libs/emberMpiLib.cc",
      "x-sha256": "8699c1c1620b2f92134efc83bc0720c2dfe32731f6ef59f238ae9c202070d320",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/mpi/motifs/emberpingpong.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/mpi/motifs/emberpingpong.h",
      "x-sha256": "6c232b0ee2553cac9465b9770a3de4e7cfba23c66e84d72877c5df028feda166",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/mpi/motifs/emberpingpong.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/mpi/motifs/emberpingpong.cc",
      "x-sha256": "d943c49d96bd769b3d4888d8aab87fa4aa25e9426ba752d57b872b3800f6aabc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/shmem/emberShmemGen.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/shmem/emberShmemGen.h",
      "x-sha256": "668db347becd4641505e73da0188a640d550a4cfb64f380dc45827ceecf07b00",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/Makefile.am",
      "x-sha256": "16c80b881b2c8639639423157e53be1f2802a3e8120671d8702d1324a0074ec8",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/pyember.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/pyember.py",
      "x-sha256": "725b81f9f1e38e54c7a0ea2ee36fcb6eb87340507bd35922cc7598e51225bf78",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s11",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/test/emberLoad.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/test/emberLoad.py",
      "x-sha256": "162a44de6f921e5fddc13f0a103d2eb53e2045a42ae41e061630cdfe1ad5a79d",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s12",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/tests/testsuite_default_ember_sweep.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/tests/testsuite_default_ember_sweep.py",
      "x-sha256": "685ab6d46c649d043a5bc80609fd703b2d72aa08a14909b1fe7e3ad0d29f1e98",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s13",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/tests/testsuite_default_ember_nightly.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/tests/testsuite_default_ember_nightly.py",
      "x-sha256": "a930d0737c0bdbe5e4bedd0e81c531c4e669415c3e44d0fec342ee7b376dddb9",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s14",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/hermes/msgapi.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/hermes/msgapi.h",
      "x-sha256": "741e878fe318bbc90bbef60a0e69a6ff1f0a987f00c44a2d1413c13d042a4fa0",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s15",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/mpi/motifs/emberhalo3d.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/mpi/motifs/emberhalo3d.h",
      "x-sha256": "50ca55e642dd8f7f5d81cc0d664e0f0f4de579a80535d36ff9eed4af1be9351c",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s16",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/mpi/motifs/emberhalo3d.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/mpi/motifs/emberhalo3d.cc",
      "x-sha256": "e2f24c081ec060ea548e6e326b5183cbe58fa3ae010a53bccc0090213c762484",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---
# Create an Ember motif

A motif is an `EmberGenerator` subcomponent that the engine calls repeatedly; each call enqueues the next batch of communication or compute events and returns true when the schedule is complete. MPI-style motifs derive from `EmberMessagePassingGenerator` (`mpi/embermpigen.h`); SHMEM motifs derive from `EmberShmemGenerator` (`shmem/emberShmemGen.h`). Check the [motif catalog](motifs.md) first: 128 motifs already exist, and a parameter may cover the requested pattern.

## Files and registration

Copy `mpi/motifs/emberpingpong.h` and `.cc` to `mpi/motifs/ember<name>.h/.cc`, rename the class, and register it:

```cpp
class EmberMyPatternGenerator : public EmberMessagePassingGenerator {
public:
    SST_ELI_REGISTER_SUBCOMPONENT(EmberMyPatternGenerator, "ember", "MyPatternMotif",
        SST_ELI_ELEMENT_VERSION(1,0,0), "Sends to both neighbors, then reduces",
        SST::Ember::EmberGenerator)
    SST_ELI_DOCUMENT_PARAMS(
        { "arg.iterations",  "Number of exchange rounds", "1" },
        { "arg.messageSize", "Bytes per message",        "1024" })
    EmberMyPatternGenerator(SST::ComponentId_t id, Params& params);
    bool generate(std::queue<EmberEvent*>& evQ) override;
private:
    uint32_t m_iterations, m_messageSize, m_loopIndex;
    void* m_sendBuf; void* m_recvBuf;
    MessageRequest m_req[2];
};
```

The ELI name must end in `Motif` because `pyember.py` appends that suffix to the command-line token (`MyPattern` selects `ember.MyPatternMotif`). Python passes every `key=value` on the command line as `arg.<key>`, so read parameters with that prefix, as in `params.find<uint32_t>("arg.iterations", 1)`. The constructor passes the motif's display name to the base: `EmberMessagePassingGenerator(id, params, "MyPattern")`. The `time-*` statistics that shipped motifs declare are not registered on this revision (the registration in `libs/emberMpiLib.cc` is compiled out), so that block is optional. Add both files to `libember_la_SOURCES` in `Makefile.am`, rerun the elements build, and install.

## The generate contract

`generate` runs again after the queued events execute, so keep state in members and treat the method as a resumable state machine:

```cpp
bool EmberMyPatternGenerator::generate(std::queue<EmberEvent*>& evQ) {
    if (m_loopIndex == m_iterations) {
        if (rank() == 0) output("MyPattern: %u rounds of %u bytes on %d ranks\n",
                                m_iterations, m_messageSize, size());
        return true;                                  // finished; queued events still run
    }
    int left = (rank() + size() - 1) % size(), right = (rank() + 1) % size();
    enQ_isend(evQ, m_sendBuf, m_messageSize, CHAR, right, 0xBEEF, GroupWorld, &m_req[0]);
    enQ_irecv(evQ, m_recvBuf, m_messageSize, CHAR, left,  0xBEEF, GroupWorld, &m_req[1]);
    enQ_waitall(evQ, 2, m_req, NULL);
    enQ_compute(evQ, 1000);                           // 1000 ns of modeled compute
    enQ_allreduce(evQ, m_sendBuf, m_recvBuf, 1, DOUBLE, SUM, GroupWorld);
    ++m_loopIndex;
    return false;
}
```

Rules from `emberengine.cc` and `embergen.h`: returning true ends the motif after the queued events drain; a false return with an empty queue also ends it, so never return false with nothing queued to "wait"; the base `generate` and `completed` are `assert(0)`, so override `generate(std::queue<EmberEvent*>&)` (the three-argument form is unused) and `completed` if you need end-of-motif work; `primary` defaults to true in code, so the engine holds the simulation open until the motif finishes; nonparticipating ranks should return true on their first call, as PingPong does for ranks other than 0 and `arg.rank2`. Buffers come from `memAlloc(bytes)` and must stay valid until the matching wait completes.

## Operations

The `enQ_*` names are macros onto `libs/emberMpiLib.h`, all taking the event queue first:

| Call | Signature after the queue |
|---|---|
| `enQ_init`, `enQ_fini`, `enQ_barrier` | none; `barrier(comm)` |
| `enQ_rank`, `enQ_size`, `enQ_getTime` | `(comm, uint32_t*)`, `(comm, uint32_t*)`, `(uint64_t*)` |
| `enQ_send`, `enQ_recv` | `(buf, count, PayloadDataType, rank, tag, comm)`; `recv` adds `MessageResponse*` |
| `enQ_isend`, `enQ_irecv`, `enQ_wait`, `enQ_waitall`, `enQ_waitany`, `enQ_test`, `enQ_testany`, `enQ_cancel` | nonblocking forms with `MessageRequest*`; `waitall(count, req[], resp[])` |
| `enQ_sendrecv` | combined send and receive |
| `enQ_allreduce`, `enQ_reduce` | `(sendbuf, recvbuf, count, type, op, comm)`; `reduce` adds `root` before `comm` |
| `enQ_bcast`, `enQ_scatter`, `enQ_scatterv`, `enQ_allgather`, `enQ_allgatherv`, `enQ_alltoall`, `enQ_alltoallv` | collectives with `root` where applicable |
| `enQ_commSplit`, `enQ_commCreate`, `enQ_commDestroy` | communicator management; `GroupWorld` is the default communicator |
| `enQ_compute` | `(uint64_t nanoseconds)` or `(std::function<uint64_t()>)`; `enQ_detailedCompute` needs the Thornhill detailed model |
| `enQ_memAlloc`, `enQ_makeProgress` | heap allocation through a memory-heap link; progress polling |

Payload types are the Hermes `PayloadDataType` values (`CHAR`, `INT`, `LONG`, `DOUBLE`, `FLOAT`, the fixed-width integer types, `COMPLEX`); reduction operations are `SUM`, `MIN`, `MAX`, `NOP`, or `op_create(fn, commute)`; `AnyTag` and `AnySrc` are wildcards.

## Run and validate

From `ember/test`, the loader selects motifs by name:

```sh
sst --model-options="--topo=torus --shape=2 --cmdLine=\"Init\" --cmdLine=\"MyPattern iterations=4 messageSize=64\" --cmdLine=\"Fini\"" emberLoad.py
```

`--topo` and `--shape` follow the sweep suite's values (`torus` with `2` or `4x4x4`, `fattree` with `9,9:9,9:18`, `dragonfly` with `8:8:4:8`); `--cmdLine` entries run in order, so bracket the motif with `Init` and `Fini`. Verify the schedule from the motif's own `output` lines (rank count, rounds, bytes), natural completion (`Simulation is complete`), and the absence of hangs, which usually mean mismatched sends and receives rather than a network fault. For a regression, add a `test = {'motif': 'MyPattern', 'args': [...]}` entry to the sweep matrix in `tests/testsuite_default_ember_sweep.py` or a case in `testsuite_default_ember_nightly.py`, with a reference line; payload values are never checked by those suites ([validation](validation.md)). Separate modeled compute from host time, test zero-size messages and nonparticipating ranks where the pattern allows them, and do not promise checkpoint support without serializing motif state ([extension points](extension-points.md)).

## Executed check on the recorded devel install

This recipe was exercised on the isolated devel build (sst-elements `47b99537`, macOS ARM64) by cloning the shipped Halo3D motif: `mpi/motifs/emberhalo3d.{h,cc}` were copied to `emberhalo3dtest.{h,cc}`, the class became `EmberHalo3DTestGenerator`, the ELI name `Halo3DTestMotif`, the base-constructor name `"Halo3DTest"`, and the header guard was renamed (a copied guard would otherwise collide); both files were added after `emberhalo3d.cc` in `libember_la_SOURCES`. `make -C <build>/src/sst/elements/ember install` regenerated the Makefile through automake and compiled the new object, but the link step failed until `SDKROOT` was set to the SDK the install had been configured with (`MacOSX26.5.sdk`); with the default macOS 27 SDK the linker reports `tapi error: malformed file ... unknown architecture`. Replaying the recorded build environment fixed it, and `sst-info ember.Halo3DTestMotif` then listed the motif. Running

```sh
cd <isolated src>/sst-elements/src/sst/elements/ember/test
sst --model-options="--topo=torus --shape=2x2x2 --cmdLine=\"Init\" --cmdLine=\"Halo3DTest nx=16 ny=16 nz=16 iterations=2\" --cmdLine=\"Fini\"" emberLoad.py
```

produced output identical to the shipped `Halo3D` motif under the same arguments (decomposition `2x2x2`, compute time 10649 ns, two iterations, `Simulation is complete, simulated time: 60.61 us`) apart from the motif name, in about half a second. Gaps the exercise exposed: the guide originally omitted the header-guard rename and the SDK environment, and `emberLoad.py` must be run from `ember/test` because it imports its sibling modules by name. Evidence is under the repository's ignored `.runtime/guide-exercise-2026-10-07/` directory.
