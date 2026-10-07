---
{
  "type": "SST Guide",
  "title": "Checkpoint and restart",
  "description": "Produce SST checkpoints, restart from them, and make element state serializable.",
  "tags": [
    "checkpoint",
    "serialization"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/claude",
    "at": "2026-10-07T09:15:55.720397+00:00"
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
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/main.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/main.cc",
      "x-sha256": "03d2c1991a0dc059d44c03f1cf57cacecf34256b9a4c03a0ae977844ef27ec85",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/simulation.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/simulation.cc",
      "x-sha256": "789d9ae3803d4d242177415d1c0395014a16c400b375060083c79fa8cb713c9c",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/checkpointAction.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/checkpointAction.cc",
      "x-sha256": "6d09aecbb804194cd8a1b650744f71b17b7ef99b35f6b52c92a85dd0d94140e4",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/checkpointAction.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/checkpointAction.h",
      "x-sha256": "624824caa774039ce1ddda4fdeda545b1aab43cf6fc994ca1c6107d8c7c58a9f",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/baseComponent.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/baseComponent.cc",
      "x-sha256": "d8f7f86195d776d14d1190734a3e183f4b5aa01fb05373f27fb8bd1875534ed8",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/sync/syncManager.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/sync/syncManager.cc",
      "x-sha256": "45111731e7ca2a836fa8b5d49d73735a60ce70f7753e29f8664a811949253e76",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/serialization/serializable_base.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/serialization/serializable_base.h",
      "x-sha256": "ec26b35ce5ae30816baec1d3c51ee6e7866a6abbb17baa7f60a542509bac44bc",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/serialization/serialize.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/serialization/serialize.h",
      "x-sha256": "aeaa812ef8ee8f583e6dc3cbbc2e70f74734e111f8b3c6baee10d3a792b0884a",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/serialization/impl/serialize_unique_ptr.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/serialization/impl/serialize_unique_ptr.h",
      "x-sha256": "d34b926951cf0c3f462f26e99a32b857676a7859e912b9c0dd8506529da5b504",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statbase.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statbase.h",
      "x-sha256": "8e55ead677b51259dc9b5533f01670ce436eb2190f8709b8a80809c81e997892",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s11",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statengine.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statengine.cc",
      "x-sha256": "c0431f21a8a69e0c59b67937771fb4e32024a93160b683bb662c1bb060a5d659",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s12",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/testElements/coreTest_Checkpoint.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/testElements/coreTest_Checkpoint.cc",
      "x-sha256": "0d1eed164926eed13a9da2357685e3016d420ba4777124db16f5c108fd71bc22",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s13",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/testsuite_default_Checkpoint.py",
      "x-repository": "sst-core",
      "x-path": "tests/testsuite_default_Checkpoint.py",
      "x-sha256": "579a15e261e02bc64f6794532e430db1c5a0b6dd9fed82ab39402274a0fe831a",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s14",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/test_Checkpoint.py",
      "x-repository": "sst-core",
      "x-path": "tests/test_Checkpoint.py",
      "x-sha256": "73f3fe7f9ee10d0a88c0c5e9177e84b43a66b56caace6023cc71dec065985756",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s15",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/testsuite_default_DebugConsole_Checkpoint.py",
      "x-repository": "sst-core",
      "x-path": "tests/testsuite_default_DebugConsole_Checkpoint.py",
      "x-sha256": "302b143c748fa244464d22fe9fdecbde6eebe9837765baa8613b62a2e85889c9",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s16",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleElementExample/tests/testsuite_default_simpleComponents.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleElementExample/tests/testsuite_default_simpleComponents.py",
      "x-sha256": "872897afca6774363391413ac8eee236eede5632fd45b6b431c20691ba69dccd",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s17",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/router.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/router.h",
      "x-sha256": "22c1ae45060949c0017f12bdf93b38f435d82b9e1b15c9d6bfebddbb8d20575e",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s18",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/vanadis.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/vanadis.cc",
      "x-sha256": "a471600239c61a5ac4796fdf496ad74ecf2779fbed1ef14e8fca8580d5d7b1c7",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s19",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/os/vnodeoshandler.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/os/vnodeoshandler.cc",
      "x-sha256": "12dea0747422a465edfba8da64d4f069b9a9a83a9679415ee8449d6959ba9c22",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s20",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/tests/basic_vanadis.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/tests/basic_vanadis.py",
      "x-sha256": "3a9574055711fca2ec2190c90edcd156b9b4321bfc079ed425528957c8cef674",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---
# Checkpoint and restart

Checkpointing is marked experimental in this revision. It writes the serialized simulation state at simulated or wall-clock intervals and restarts by passing the checkpoint manifest in place of the Python configuration.

## Produce checkpoints

| Option | Effect |
|---|---|
| `--checkpoint-sim-period=PERIOD` | Checkpoint every PERIOD of simulated time (units required; `--checkpoint-period` is the older spelling). |
| `--checkpoint-wall-period=PERIOD` | Checkpoint every PERIOD of wall time (`H:M:S`, `M:S`, `S`, `Hh`, `Mm`, `Ss`). |
| `--sigusr1=sst.rt.checkpoint`, `--sigalrm="sst.rt.checkpoint(interval=2h)"` | Checkpoint on a signal or timer. |
| `--checkpoint-enable` | Only needed to allow the interactive console to trigger checkpoints. |
| `--checkpoint-prefix=PREFIX` | Directory and file prefix, default `checkpoint`, no `/` allowed; SST creates a unique directory with that name under `--output-directory` at startup and, when not parallel-loading, writes `<prefix>_config_graph.bin` there for repartitioned restarts. |
| `--checkpoint-name-format=FORMAT` | `<directory>/<file>` format with `%p` prefix, `%n` checkpoint index, `%t` simulated cycles; default `%p_%n_%t/%p_%n_%t`. Formats without `%n` or `%t` overwrite earlier checkpoints. |

Each checkpoint creates a subdirectory containing the manifest `<name>.sstcpt`, a `<name>_globals.bin` written by rank 0 thread 0, and one `<name>_<rank>_<thread>.bin` blob per rank and thread; the prefix help shows `checkpoint/checkpoint_1_1000/checkpoint_1_1000.sstcpt` for two ranks. The index starts at 1 (`checkpoint_id` in `checkpointAction.cc`) even though the name-format help says 0. Multi-rank runs can only checkpoint when ranks share links: with no cross-rank links the core installs `EmptyRankSync` and prints `EmptyRankSync: Checkpoint and interactive debug disabled`. In parallel runs a signal- or console-triggered checkpoint waits for the next synchronization point; serial runs take it immediately.

## Restart

Run `sst <dir>/<name>.sstcpt`; the `.sstcpt` extension is detected and `--load-checkpoint` is unused. Options annotated `R` in `sst -h` (`--stop-at`, `--timing-info`, heartbeat periods, `--timeVortex`, `--sigusr*`, library paths) are carried into the restart and may be overridden on the new command line; options annotated `X` (`--model-options`, `--timebase`, `--parallel-load`, configuration/graph output, `--run-mode`) are ignored. `simulation.cc` supports four restart layouts: the same ranks and threads as the checkpoint, a serial restart of a parallel checkpoint, a remap to the same number of partitions with a different rank/thread split, and a full repartition, which needs the saved configuration graph; direct inter-thread links are disabled on restart.

## What is saved

The core serializes each component's info and state, its clock handlers with their periods (re-registered on restart), links, subcomponents, and statistics (each statistic records its ELI type, name, sub-ID, and rate/start/stop factors, and the statistics engine re-registers it), plus the global state and pending events. An element must make this complete for its own members:

- Put `ImplementSerializable(Namespace::Class)` in every component, subcomponent, event, and helper class that must survive, and `NotSerializable(Class)` where support is intentionally absent.
- Override `serialize_order(serializer& ser)`, call the base class first, then `SST_SER(member)` for every member that defines state: links, handlers, time converters, output objects, RNGs, containers, and nested serializable objects. `coreTest_Checkpoint.cc` serializes its links, self link, clock handler and converter, counters, strings, output, and three RNGs in this way; Merlin's router serializes `requestNotifyOnEvent` and `vcs_with_data` after `SST::Component::serialize_order`.
- Pointers to polymorphic objects serialize through their registered serializable type. On the recorded revisions, serializing a polymorphic object through `std::unique_ptr<Base>` loses its dynamic type and leaves bytes unread ([core contracts](../core/contracts.md)); use raw or registered-pointer serialization for such members until that is fixed.
- A member that cannot be serialized (an open file, a host pointer) must be reconstructed in `serialize_order` on unpack rather than stored.

## Element support in this checkout

Files containing serializable classes per element (counts of files matching `Implement(Virtual)?Serializable`, so abstract bases are included): Vanadis 49, Merlin 45, memHierarchy 34, Carcosa 20, Miranda 15, simpleElementExample 12, cramSim 10, and one to three each for Cassini, Iris, Mercury, MMU, Shogun, Firefly, Kingsley, Messier, Opal, Ariel, Ember, Golem, Mask-MPI, Osseous, rdmaNic, Samba, simpleSimulation, Thornhill, and VaultSim. A serializable event class does not make its owning component restartable; only a component whose whole state is serialized is. No element test suite runs a checkpoint case in this checkout: simpleElementExample's `test_basic_checkpoint` is commented out, and the `checkpoint`/`checkpointDir` parameters in Vanadis configurations drive that element's own process-checkpoint syscall path (`vanadis.cc`, `os/vnodeoshandler.cc`), not core checkpoints.

The core's `testsuite_default_Checkpoint.py` is the reference: 43 cases over a `coreTestCheckpoint` ring, twelve `sc_*` subcomponent-nesting models, Clocks, SharedObject, Module, the statistics component, and MessageMesh; each case's two integer arguments select which checkpoint index the restart and the restart-of-restart start from, ranks and threads come from the runner, and the `_n2one`, `_remap`, `_restart_smaller`, and `_start_serial` variants exercise the other restart layouts. `testsuite_default_DebugConsole_Checkpoint.py` covers console-triggered checkpoints.

## Validate a checkpointed model

- Run the model to completion, then run it with a checkpoint period and restart from a middle checkpoint; outputs and final statistics must match the uninterrupted run.
- Choose a checkpoint at a known simulated time and confirm the directory name's `%t` matches it.
- Restart with the same layout, serially, remapped, or repartitioned, and keep the `_config_graph.bin` file for the last of these.
- Diff `--output-json` from the original run against the restart's configuration graph, and keep `R`-annotated options identical unless the test is about changing them.
- Add a checkpoint case to the element suite when adding serialization to an element, modeled on the core suite.

See [run-time options](run-options.md) for option spellings and [parallel execution](parallel.md) for the synchronization requirements that checkpointing inherits.
