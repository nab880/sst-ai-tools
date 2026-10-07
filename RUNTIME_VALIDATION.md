# SST runtime validation on devel

Run date: 2026-10-06T19:42:37.073294-07:00. The selected native invocations produced **173 passes, 6 skips, and 0 test failures/errors**. Two category skips were subsequently rerun and passed, leaving four unresolved skipped checks. The standalone behavioral checks produced **4 passes and one failed Carcosa registration assertion**. This is focused validation, not an exhaustive nightly certification.

## Sources and build

- sst-core devel: `09bc3927b1fc23e65f3aa0795739cad36f315d5a`; tracks canonical `upstream/devel` because the original core remote has no devel branch.
- sst-elements devel: `47b99537882df309fa2bdb2eb60c9a1e16efb5e5`; tracks `origin/devel`.
- sst-ai-tools: uncommitted `devel` branch. The reference knowledge-catalog repository remains on main with no devel ref.
- Isolated source copies, build directories, and installation: `.runtime/devel/`. Original tracked SST files were not changed; existing untracked notes were preserved.
- Apple Clang 21, Python 3.14.6, OpenMPI, C++17, `-O1 -g0`. Configure uses the already installed macOS 26.5 SDK because the default macOS 27 SDK failed the linker probe.
- Core and all 32 enabled elements compiled/installed. Balar was excluded for missing CUDA/GPGPU-Sim; Osseous for unavailable external RTL/C-model runtime artifacts.
- MPI transport: `OMPI_MCA_btl=self,tcp`; multi-rank checks use `OMPI_MCA_btl_tcp_if_include=lo0`. The default shared-memory backend emitted warnings that contaminated reference comparisons in an earlier diagnostic run. Its results are not included here.

The following build manifest, scripts, and raw logs are ignored local artifacts and are absent from a fresh checkout. The retained machine-readable results and core reassessment archive remain available. Build commands, source hashes, and stage results: build manifest (`.runtime/devel/build-state.json`). Build/install output is in `.runtime/devel/logs/`. [Machine-readable results](runtime-validation.json) contain exact commands, counts, paths, and fixture hashes.

## Native regressions

| Invocation | Passed | Skipped | Failures/errors | Evidence |
|---|---:|---:|---:|---|
| core-serial-tcp | 133 | 1 | 0 | log (`.runtime/devel/logs/core-serial-tcp.log`) |
| core-links-threads | 1 | 0 | 0 | log (`.runtime/devel/logs/core-links-threads.log`) |
| core-links-mpi | 1 | 0 | 0 | log (`.runtime/devel/logs/core-links-mpi.log`) |
| element-00-merlin | 2 | 0 | 0 | log (`.runtime/devel/logs/element-00-merlin.log`) |
| element-01-memHierarchy | 1 | 0 | 0 | log (`.runtime/devel/logs/element-01-memHierarchy.log`) |
| element-02-memHierarchy | 2 | 0 | 0 | log (`.runtime/devel/logs/element-02-memHierarchy.log`) |
| element-03-mercury | 2 | 0 | 0 | log (`.runtime/devel/logs/element-03-mercury.log`) |
| element-04-ember | 1 | 0 | 0 | log (`.runtime/devel/logs/element-04-ember.log`) |
| element-05-kingsley | 1 | 0 | 0 | log (`.runtime/devel/logs/element-05-kingsley.log`) |
| element-06-miranda | 1 | 1 | 0 | log (`.runtime/devel/logs/element-06-miranda.log`) |
| element-07-cassini | 3 | 0 | 0 | log (`.runtime/devel/logs/element-07-cassini.log`) |
| element-08-cacheTracer | 1 | 0 | 0 | log (`.runtime/devel/logs/element-08-cacheTracer.log`) |
| element-09-gensa | 1 | 0 | 0 | log (`.runtime/devel/logs/element-09-gensa.log`) |
| element-10-llyr | 0 | 1 | 0 | log (`.runtime/devel/logs/element-10-llyr.log`) |
| element-11-mask-mpi | 4 | 0 | 0 | log (`.runtime/devel/logs/element-11-mask-mpi.log`) |
| element-12-messier | 0 | 1 | 0 | log (`.runtime/devel/logs/element-12-messier.log`) |
| element-13-samba | 1 | 0 | 0 | log (`.runtime/devel/logs/element-13-samba.log`) |
| element-14-shogun | 1 | 0 | 0 | log (`.runtime/devel/logs/element-14-shogun.log`) |
| element-15-simpleElementExample | 3 | 0 | 0 | log (`.runtime/devel/logs/element-15-simpleElementExample.log`) |
| element-16-simpleSimulation | 2 | 0 | 0 | log (`.runtime/devel/logs/element-16-simpleSimulation.log`) |
| element-17-vaultsim | 1 | 0 | 0 | log (`.runtime/devel/logs/element-17-vaultsim.log`) |
| element-19-rdmaNic | 0 | 1 | 0 | log (`.runtime/devel/logs/element-19-rdmaNic.log`) |
| element-20-prospero | 1 | 0 | 0 | log (`.runtime/devel/logs/element-20-prospero.log`) |
| element-21-ariel | 0 | 1 | 0 | log (`.runtime/devel/logs/element-21-ariel.log`) |
| element-22-zodiac | 1 | 0 | 0 | log (`.runtime/devel/logs/element-22-zodiac.log`) |
| golem-ideal | 4 | 0 | 0 | log (`.runtime/devel/logs/golem-ideal.log`) |
| merlin-threads | 1 | 0 | 0 | log (`.runtime/devel/logs/merlin-threads.log`) |
| merlin-mpi | 1 | 0 | 0 | log (`.runtime/devel/logs/merlin-mpi.log`) |
| vanadis-hello-world | 1 | 0 | 0 | log (`.runtime/devel/logs/vanadis-hello-world.log`) |
| nightly-targeted | 2 | 0 | 0 | log (`.runtime/devel/logs/nightly-targeted.log`) |

The initial Vanadis selector selected zero tests; the discovered generated method name was used for the passing retry. The zero-selection attempt is retained in the machine-readable record and is not counted as a pass.

Unresolved skips:

- Core interactive sst-info: curses library unavailable. Closed on October 7, 2026 (gap-closure section below).
- Ariel Pin case: Pin unavailable; build/load success does not validate frontend execution. Opal's supplied application example also depends on the Ariel/frontend path and was not executed. Intel Pin has no Apple Silicon build, so this cannot close on this host.
- rdmaNic native case: suite requires a musl compiler that is unavailable. Its library compiled, but that application regression did not execute. Closed on October 7, 2026 with a Zig-backed musl cross compiler (gap-closure section below).
- Llyr: native test is unconditionally disabled by upstream (`Not testing llyr right now`). No disabled decorator was bypassed. Run directly on October 7, 2026, it matches its reference (gap-closure section below).

Miranda random generation and Messier GUPS passed when run with the nightly category. This was a targeted rerun, not a full nightly sweep. Golem tests covered ideal float/int arrays with one and multiple arrays; optional CrossSim behavior was not tested.

Prospero and Zodiac native cases used authentic public SST test fixtures. A validation-local standard-library downloader implements the specific download invocation the suites require because system wget is absent; it verifies TLS and caches the archives under `.runtime/devel/fixtures/`. No global wget installation or production dependency was added.

## Standalone behavioral checks

| Model | Result | Evidence |
|---|---|---|
| prospero | Pass | stdout (`.runtime/devel/logs/smoke-prospero.out`) |
| serrano | Pass | stdout (`.runtime/devel/logs/smoke-serrano.out`) |
| cramSim | Pass | stdout (`.runtime/devel/logs/smoke-cramSim.out`) |
| carcosa | Failed assertion | stdout (`.runtime/devel/logs/smoke-carcosa.out`) |
| ember-firefly | Pass | stdout (`.runtime/devel/logs/smoke-ember-firefly.out`) |

Acceptance checks:

- Prospero: a four-entry local trace produced two reads, two writes, 16 bytes read, 16 bytes written, and natural completion.
- Serrano: the supplied sum graph produced the exact sequence 100, 102, ..., 298 and completed.
- cramSim: a local adaptation of the synthetic generator reached 200 completed transactions without its original simulation-time cutoff. This checks the completion threshold, not drainage of every outstanding request or all device timing constraints.
- Ember/Firefly: two-node ping-pong reported ten iterations and 64-byte messages and completed. It checks scheduling/transport execution, not payload-data fidelity or every collective.
- Carcosa: the supplied manager-logic configuration completed, and each injector reported resolving its intended registry, but the stronger assertion that each manager consumed its registration failed.

## Carcosa finding

The trace shows all four Hali setup messages before any injector sends RegisterPM. No expected manager consumption messages appear afterward. In the selected source, `Hali::setup()` calls `processMessagesFromPMs()`; the injector can send registration lazily on its first timed event. Its `init(unsigned)` method is not an override of a lifecycle hook in the current core PortModule API. This supports an ordering explanation for the failed assertion; it is not proof of every resulting fault behavior.

Source entry points: `sst-elements/src/sst/elements/carcosa/components/hali.cc`, `components/faultInjManager.cc`, `injectors/faultInjectorMemH.cc`, and `sst-core/src/sst/core/portModule.h`. SST code was not patched. Follow-up should add a registration-consumption regression and resolve the lifecycle/late-registration contract. Fault data correctness, fault overlap, and checkpoint/restart remain separate checks.

## Reproduce and extend

Use the isolated installation for exploratory runs:

```sh
export PATH="$PWD/.runtime/devel/install/bin:$PATH"
export OMPI_MCA_btl=self,tcp
export OMPI_MCA_btl_tcp_if_include=lo0
unset OMPI_MCA_btl_tcp_if_exclude
.venv/bin/python .runtime/devel/validate_runtime.py core
.venv/bin/python .runtime/devel/validate_runtime.py elements
.venv/bin/python .runtime/devel/validate_runtime.py parallel-core
.venv/bin/python .runtime/devel/validate_runtime.py parallel-network
.venv/bin/python .runtime/devel/validate_runtime.py golem
.venv/bin/python .runtime/devel/validate_runtime.py supplement
.venv/bin/python .runtime/devel/direct_smokes.py
```

Run from sst-ai-tools. These generated validation scripts and logs are local ignored artifacts, not installed agent skills. Reproduction requires local MPI/shared-memory/socket permissions. Execution replaces corresponding result directories; retain the existing machine-readable report before rerunning. For fresh source revisions create fresh snapshots/builds rather than reusing this installation blindly.

Support libraries Hermes/Thornhill were exercised through Ember/Firefly and Iris through Mask-MPI. MMU integration was exercised by Vanadis. This does not independently certify every API. Wider rank/thread matrices, all hardware policies, external runtimes, disabled tests, and paired AI token-efficiency measurements remain outside this run.

## SST-HGCC and MV2 scope

The [Mercury application/toolchain guide](ofk/elements/mercury/hgcc-mv2.md) now documents SST-HGCC and the adapted MVAPICH2 (MV2) path. The October 6 campaign did **not** compile or execute those applications; the gap-closure section at the end of this file records the October 7, 2026 run that did. Mercury OS, Mask-MPI, Iris, and Merlin passes are prerequisite/integration evidence for their own tested paths, not an MV2 validation result.

Before claiming MV2 validation, verify a compatible HGCC/MV2 build, prepared `libmpi_nopmi.a`, simulated PMI and the Iris `sstmac` provider, registered application/library names, per-rank state isolation, and numerical results. The inspected eight-rank Allreduce fixture expects SUM=36 on every rank; running it remains additional work.

### Main use cases and Mercury correlation

| Layer/path | Main use case | Relationship to Mercury | Evidence in this campaign |
|---|---|---|---|
| SST-HGCC (`hgcc` / `hg++`) | Compile and rewrite C/C++ applications into loadable workloads; handle entry points, per-rank globals/TLS, and selected modeled compute/runtime calls | Produces the application library that Mercury registers, loads, and schedules | Toolchain/app path documented from source; not executed here |
| HGCC + Mask-MPI | Study supported modeled MPI calls and collective policies without embedding an external MPI implementation | Uses Mercury application/runtime facilities and Iris communication support | Related Mask-MPI runtime cases passed; HGCC compilation itself was not tested |
| HGCC + adapted MVAPICH2 (MV2) | Study MPI implementation-specific algorithms, thresholds, protocol progress, and correctness | Loads adapted MPI-library code with the application; Iris libfabric/PMI connects it to Mercury and the selected network | Source integration inspected; MV2 execution remains unvalidated |

For MV2, application ranks belong to the simulated workload; host MPI ranks partition SST execution. The inspected eight-rank Allreduce fixture uses `HgJob(0, 8)` with a single-router topology. It links through prepared MV2 libraries and Iris's `sstmac` provider. Every virtual rank checks SUM=36; a successful simulator exit by itself is insufficient.

For a first HGCC/MV2 validation campaign, run a small HGCC application, a rank/TLS-isolation case, MV2 send/receive, then the numerical Allreduce case. Confirm loaded library/provider identities and completion before comparing simulated timing. Preserve computation required for the correctness oracle when selecting skeletonization settings. These are proposed additional checks, not results of the completed campaign.

## Installation recipes and Iris fabric scope

Follow [SST-HGCC installation](ofk/development/hgcc-install.md) and [adapted MV2 installation](ofk/development/mv2-install.md) for the additional toolchain campaign. The [Iris fabric guide](ofk/elements/iris/fabrics.md) documents the built `sstmac` provider, its `macro:libfabric` Mercury binding, and the steps to create a new simulated provider. The [collective registry guide](ofk/elements/iris/collectives.md) separately lists operation-scoped algorithms and extension macros. Generic dispatcher names do not establish additional built hardware providers; these guides do not add runtime results to this report.

## MV2 Linux/macOS and timing evidence boundaries

The [platform guide](ofk/elements/mercury/mv2-platforms.md) adds Linux ELF and macOS Mach-O build/link/runtime details. Both have inspected source paths; the October 6 campaign did not establish end-to-end MV2 support on either platform, and the October 7 pass established it on macOS ARM64 with the provider patch recorded below. The [timing guide](ofk/elements/mercury/mv2-timing.md) traces MPI_Wtime backend selection, HGCC clock replacements, Mercury delayed wakeups, Iris post-send/RDMA hooks, and network/compute costs.

Source findings requiring verification before MV2 timing claims:

- The support object defines a no-op hgcc_usleep; Mercury has a separate simulated-time implementation. Verify actual symbol binding.
- MPI timer objects need a simulated clock backend/replacement; the supplied build recipes alone do not establish one.
- poll_delay is stored but no consumer was found in the reviewed devel source.
- Mask-MPI rendezvous calls pinRdma; the reviewed OFI MR-registration handlers do not. Mask-MPI thresholds do not automatically tune embedded MV2.

These are source observations and proposed acceptance checks, not additional timing measurements or new runtime passes.

## Earlier core correctness review

The [September 25 review and follow-up](reviews/core/2026-09-25/index.md) are now retained for tracking. They cover different revisions and eleven focused findings. The passes in this runtime campaign do not establish those findings' current fix status; the archive tracker now links to the focused October 6 reassessment.

## Focused core finding reassessment

The [October 6 reassessment](reviews/core/2026-10-06/index.md) reproduced all eleven historical core findings on the same devel revisions recorded above. The intentional clock-growth case crashed, and the other targeted contracts produced incorrect values/configuration. Raw polymorphic-pointer controls passed. Actual TrafficGen and basicStatistics follow-ups reproduced the hotspot and histogram defects. These outcomes are recorded separately from the 173 passing broad native checks; those checks did not close the findings. No source fixes were applied.

## Guide exercise — October 7, 2026

To test the motif and skeleton workflow guides, the isolated devel build (same revisions as above) was extended in place: a copy of the Halo3D motif registered as `ember.Halo3DTestMotif`, a copy of the `halo3d-26` Mask-MPI skeleton registered as `halo3dtest`, and the upstream SST-HGCC checkout (`2a37f8c541f02344f7d540188e52efd1f080a6fc`) configured and installed against the devel install in `.runtime/devel/install-hgcc`. Results, each with exit code 0:

| Check | Result |
|---|---|
| Shipped `Halo3D` motif, torus 2x2x2, `nx=ny=nz=16`, two iterations | completes at 60.61 us |
| Cloned `Halo3DTest` motif, same arguments | identical output apart from the name |
| Shipped `test_halo3d26.py` (eight ranks) | matches `refFiles/test_halo3d26.out`, 1.1873 ms |
| Cloned `halo3dtest` skeleton and driver | `halo3d-test executed successfully`, 1.1873 ms |
| `hg++`-built `mercury_hello` example, two ranks | `Hello from rank 0/1`, 1.32435 us |
| `hg++`-built Halo3D skeleton (`halo3dhg`) | `halo3d-hg executed successfully`, 1.1873 ms |

Relinking in this build required `SDKROOT=/Library/Developer/CommandLineTools/SDKs/MacOSX26.5.sdk`, as the original campaign's configure did; HGCC's configure required `sst-config` on `PATH`. Logs, outputs, and the derived sources are under the ignored `.runtime/guide-exercise-2026-10-07/` directory; the derived sources also remain in the isolated `.runtime/devel/src/sst-elements` copy and its install. MV2 was built and run later the same day; see the next section.

## Gap closure — October 7, 2026

Every testing gap recorded above was retried on the same isolated devel build. Three changes to that build were required and now distinguish it from the October 6 install: core was reconfigured with `--with-ncurses=/opt/homebrew/opt/ncurses` and reinstalled, elements were rebuilt with numpy visible to `sst-config --PYTHON` and reinstalled (adding Golem's CrossSim arrays), and the Iris `sstmac` libfabric provider carries a local patch in the isolated source copy (`.runtime/gap-closure-2026-10-07/mv2/iris-sumi-provider.patch`). The tracked `sst-core`, `sst-elements`, `sst-hgcc`, and `mv2-test` checkouts are untouched. HGCC was additionally installed into the SST prefix with `--with-std=17`, and MVAPICH2 (`mv2-test` `0bd13efd`) was built there with `build_mac.sh` in 22 minutes.

| Gap | Outcome | Evidence |
|---|---|---|
| Interactive `sst-info` (curses) | Native `testsuite_default_sstinfo.py` passes both cases after the ncurses reconfigure; the interactive case also requires `TERM` to be set | `.runtime/gap-closure-2026-10-07/sstinfo/` |
| rdmaNic native suite (musl) | Gate satisfied by Zig 0.15.1 wrappers; `msg` case runs with functional output matching the gold and node 1 reporting `validate complete`, failing only the toolchain-specific statistics diff; IMB-MPI1 passes through the native suite with `-m pr nightly` and matches all six gold files | `.runtime/gap-closure-2026-10-07/rdmaNic/` |
| Llyr disabled test | `simple_test.py` run directly exits 0 and matches `refFiles/test_llyr_simple_test.out` apart from blank lines | `.runtime/gap-closure-2026-10-07/llyr/` |
| Carcosa standalone configurations | Five of seven complete with application output identical to the no-fault gold; the two stuck-at cases abort on a mask-parser defect (`", "` separators leave a trailing comma on the mask token) and run with whitespace-separated masks; the targeted address lies below the program's lowest section, so no configuration can affect the result | `.runtime/gap-closure-2026-10-07/carcosa/` |
| Golem CrossSim | Four CrossSim cases execute with per-process output identical to `golem.stdout.gold`; their SST statistics golds do not match because busy-wait counts depend on the CrossSim 3.2.1 / numpy 2.5.3 environment; the four ideal-array cases pass | `.runtime/gap-closure-2026-10-07/golem/` |
| HGCC + adapted MVAPICH2 | Unpatched: every runner stalls at 2^64 ps with no application output because the Iris provider never completes a receive. Patched: shipped send/receive passes (4.85879 us), all nine eight-rank collectives pass with `SUM=36` on reduce and allreduce (21.8 to 24.5 us), a staged probe passes zero-byte, ordered, nonblocking, `Sendrecv`, barrier, and finalize stages; twelve MPI entry points had to be added to HGCC's wrapper table because unwrapped symbols bind to the host Open MPI | `.runtime/gap-closure-2026-10-07/mv2/` |
| Ariel Pin, Osseous, Balar | Not closable on this host: Intel Pin has no Apple Silicon build, Osseous drives its testbench through Ariel/Pin, and no CUDA toolkit exists for ARM64 macOS (`nvcc` absent), which `configure.m4` requires before GPGPU-Sim | — |

Findings for upstream: the five Iris provider defects (receive context dropped, posted-send payload never copied, double free after `matchRecv`, sliced acknowledgement clone, `fi_cancel` unimplemented), the HGCC wrapper-table gap, the Carcosa stuck-at mask parser, the rdmaNic suite's stale `mipsel-linux-musl-gcc` gate, and `HgOS` rejecting `app1.env.*` keys that `App::getenv` would consume. These are observations at the recorded revisions; no tracked source was changed.
