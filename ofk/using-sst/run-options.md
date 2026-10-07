---
{
  "type": "SST Guide",
  "title": "Run-time options",
  "description": "Command-line and Python-settable SST run options on the recorded devel revision.",
  "tags": [
    "configuration",
    "runtime"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/claude",
    "at": "2026-10-07T09:16:00.405490+00:00"
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
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/config.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/config.h",
      "x-sha256": "558122861f5b4f6b87e3ef09c851f2bf21eb478b3b1cb89e5532839f0d112297",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/configBase.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/configBase.cc",
      "x-sha256": "cdd882997aa9f35dbc482bab06eb5719bbe3178c32c1c688378f0cfe3e2a8ced",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/configShared.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/configShared.cc",
      "x-sha256": "3b32a8efe56cd62003dfcaca0b4b47ec521f9f931e868dbd5e871ce434f23bd7",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/model/python/pymodel.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/model/python/pymodel.cc",
      "x-sha256": "50756980d9a002a223f75593ed329a245007d4decdc32f6de37c280c23c36e70",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/test_StatisticsComponent_basic.py",
      "x-repository": "sst-core",
      "x-path": "tests/test_StatisticsComponent_basic.py",
      "x-sha256": "f1e8cca6463f2380518fa497e96922b306b9f3d244f6f23c4365da75eb1e4532",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/test_Component_enableAllStats.py",
      "x-repository": "sst-core",
      "x-path": "tests/test_Component_enableAllStats.py",
      "x-sha256": "6f0cf2d12a8b072b3c449db28de68da8e58adf185e1a06d33dcb6c9f764098ee",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    }
  ]
}
---
# Run-time options

The option list below comes from `sst -h` on the recorded devel install (sst-core `09bc3927`); `config.cc` defines each option. `sst --help` by itself reports that `--help` requires an argument, so use `sst -h`/`--usage` for the summary and `sst --help=<option>` for extended help. Annotations in the summary mean: `S` the option can be set from the Python configuration, `R` it is carried into a restart from a checkpoint, `X` it is ignored on a restart, `H` extended help exists. Command-line values override values set in the configuration.

From Python, `sst.setProgramOption("stop-at", "25us")` and `sst.setProgramOptions({...})` set `S`-annotated options using the long option names, and `sst.getProgramOptions()` returns the current values. The core tests use `stop-at` and `partitioner` this way; setting a non-`S` option from Python is fatal, bare element names such as `roundrobin` get an `sst.` prefix, and `sst.setThreadCount(n)` sets the thread count directly. `sst.getMPIRankCount()`, `sst.getMyMPIRank()`, and `sst.getThreadCount()` expose the parallel layout to the script.

## Basic options

| Option | Meaning |
|---|---|
| `-v`, `--verbose[=level]` (S) | Core runtime verbosity; without a value, each use increments it. |
| `-n`, `--num-threads=NUM` (S) | Threads per rank. Ranks come from the MPI launcher. |
| `--sdl-file=FILE` | The configuration file, normally given as the positional argument; a checkpoint manifest (`*.sstcpt`) is accepted here. |
| `--model-options=STR` (X) | Arguments passed to the Python script; anything after a final `--` on the command line is appended to them. |
| `--stop-at=TIME` (S, R) | Simulated time at which the run ends. |
| `--exit-after=TIME` (S) | Wall-clock limit, formats `H:M:S`, `M:S`, `S`, `Hh`, `Mm`, `Ss`. |
| `--partitioner=lib.name` (S) | Partitioner selection; see [parallel execution](parallel.md). |
| `--timing-info[=LEVEL]` (S, R) | Host-side timing report; level 1 prints total runtime, 2 or more adds detail, 0 disables, and no value means 2. `--print-timing-info` is the deprecated spelling. |
| `--heartbeat-sim-period=PERIOD`, `--heartbeat-wall-period=PERIOD` (S, R) | Progress reports in simulated or wall time; `--heartbeat-period` is the older simulated-time spelling. |
| `--output-directory=DIR` (S) | Directory for every SST output file, including statistics files. |
| `--output-prefix-core=STR` (S, R, X) | Prefix for core `Output` messages. |

## Configuration and graph output

| Option | Meaning |
|---|---|
| `--output-config=FILE` (S, X) | Write the final configuration as Python. |
| `--output-json=FILE` (S, X) | Write the configuration graph as JSON. |
| `--parallel-output[=BOOL]` (S, X) | Write configuration output per rank; requires one of the two options above; also emits partition information. |
| `--output-dot=FILE`, `--dot-verbosity=INT` (S, X) | GraphViz output of the graph. |
| `--output-partition[=FILE]` (S) | Partition assignment; without a file name it is added to the JSON/Python output. |

## Advanced options

| Option | Meaning |
|---|---|
| `--timebase=TIMEBASE` (H, S, R, X) | Base time step, default `1ps`. |
| `--parallel-load[=MODE]` (X) | Parallel configuration loading for multi-rank jobs: `NONE`, `SINGLE` (same file on every rank), `MULTI` (default; one file per rank). |
| `--timeVortex=MODULE` (S, R) | TimeVortex implementation, `lib.timevortex`. |
| `--interthread-links[=BOOL]` (S) | Experimental direct inter-thread links. |
| `--cache-align-mempools[=BOOL]` (S, R, X) | Experimental cache-aligned memory pools. |
| `--debug-file=FILE` (S, X) | Destination for debug output. |
| `--lib-path=LIBPATH` (R), `--add-lib-path=LIBPATH` (R) | Replace or extend the element library search path; see [external element libraries](../development/external-elements.md). |
| `--enable-python-coverage` (H, X) | Activate Python coverage in the configuration interpreter (`SST_CONFIG_PYTHON_COVERAGE` also enables it). |

## Profiling and debugging

`--enable-profiling=POINTS` (H, S) takes a semicolon-separated list of `name:lib.type(params)[point]` entries; the points are `clock` (registered clock handlers), `event` (link event handlers), and `sync` (the SyncManager, parallel runs only), and the core registers tools such as `sst.profile.handler.event.count`, `sst.profile.handler.event.time.high_resolution`, `sst.profile.handler.clock.time.steady`, and `sst.profile.component.codesegment.count`. `--profiling-output=FILE` (S) sends profiling and timing data to stdout and/or a `.txt` or `.json` file. The API is marked not final.

| Option | Meaning |
|---|---|
| `--run-mode=MODE` (S, X) | `init`, `run`, or `both` (default). |
| `--interactive-start[=TIME]`, `--interactive-console=ACTION` (S) | Experimental interactive debugger; the default console is `sst.interactive.debugger`. |
| `--replay-file=FILE` | Replay an interactive session. |
| `--output-undeleted-events=FILE` (S) | Report events never deleted, to `STDOUT`, `STDERR`, or a file. |
| `--force-rank-seq-startup` (X) | Run startup phases one rank at a time. |
| `--print-env`, `--no-env-config`, `--disable-signal-handlers` | Environment and signal-handler controls. |
| `--sigusr1=MODULE`, `--sigusr2=MODULE` (H, S, R), `--sigalrm=ACTION(interval=TIME);...` (H, S, R) | Real-time actions: `sst.rt.exit.clean`, `sst.rt.exit.emergency`, `sst.rt.status.core` (default for SIGUSR1), `sst.rt.status.all` (default for SIGUSR2), `sst.rt.checkpoint`, `sst.rt.heartbeat`, and `sst.rt.interactive` (SIGUSR1/2 only). |

## Checkpointing (experimental)

`--checkpoint-sim-period=PERIOD` and `--checkpoint-wall-period=PERIOD` (S) trigger checkpoints; `--checkpoint-enable` only allows the interactive console to trigger one; `--checkpoint-prefix=PREFIX` (H, S) defaults to `checkpoint`; `--checkpoint-name-format=FORMAT` (H, S) defaults to `%p_%n_%t/%p_%n_%t` with `%p` prefix, `%n` checkpoint index, `%t` simulated cycles; `--load-checkpoint` is unused because a `*.sstcpt` positional argument is detected automatically. Procedure and limits are in [checkpoint and restart](checkpoint.md).

## Common invocations

```sh
sst model.py                                   # serial
sst --stop-at=10us --output-json=graph.json model.py
sst --model-options="--topo=torus --shape=4x4" model.py
sst model.py -- --topo=torus --shape=4x4       # same, appended after --
sst -n 4 model.py                              # one rank, four threads
mpirun -n 2 sst -n 2 model.py                  # two ranks, two threads each
sst --add-lib-path=/path/to/libdir model.py    # an out-of-tree element library
sst --checkpoint-sim-period=1ms --checkpoint-prefix=cp model.py
sst cp/cp_1_1000000/cp_1_1000000.sstcpt        # restart from a checkpoint manifest
sst --enable-profiling="ev:sst.profile.handler.event.time.high_resolution(level=component)[event]" model.py
sst --sigalrm="sst.rt.checkpoint(interval=2h);sst.rt.heartbeat(interval=30m)" model.py
```

The core's own tests set `stop-at` and `partitioner` from Python and pass `--model-options` for task selection; `-h` on the installed binary is authoritative for any other revision.
