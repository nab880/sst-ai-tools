# Core review reassessment — October 6, 2026

**All eleven historical findings reproduce on the tested devel revisions. No finding is closed.** The focused probes completed without timeouts; the intentional clock-growth trigger exited with SIGSEGV (-11). Other processes exited normally while producing incorrect values/configuration. This is successful defect reproduction, not a passing correctness result.

- Core: `09bc3927b1fc23e65f3aa0795739cad36f315d5a`.
- Elements: `47b99537882df309fa2bdb2eb60c9a1e16efb5e5`.
- Platform: macOS ARM64, Apple Clang/C++17, Python 3.14, existing MPI-enabled devel installation; loopback TCP transport avoids the unrelated OpenMPI shared-memory warning.
- All affected implementation files were checked against the runtime build snapshot; [provenance](provenance.json) includes source and runtime-binary hashes.
- No production SST source changes, dependency installations, repairs, commits, or remote operations were made for this reassessment.

## Findings

| ID | Feature | Current result |
|---|---|---|
| F01 | Clock activation during a callback | Reproduced |
| F02 | Shared/scoped parameters | Reproduced |
| F03 | Discrete distributions | Reproduced |
| F04 | Polymorphic unique_ptr serialization | Reproduced |
| F05 | StandardMem locked-write responses | Reproduced |
| F06 | Subcomponent statistic configuration | Reproduced |
| F07 | Batched histogram samples | Reproduced |
| F08 | Histogram origin | Reproduced |
| F09 | Floating-point histogram range | Reproduced |
| F10 | Floating-point accumulator maximum | Reproduced |
| F11 | Accumulator variance API | Reproduced |

Focused observations:

- **F01:** one-handler control promises cycle 2 but calls the reactivated handler during cycle 1. Activating sixteen dormant handlers reproduces SIGSEGV; the stack includes Clock::execute. This does not establish a crash in every cache/NIC workload or cover grouped-clock mutation.
- **F02:** direct local backend.clock is 2GHz; scoped extraction returns the shared 1GHz default.
- **F03:** deterministic draws 0.1/0.5/0.99 yield 1/2/2 instead of 0/1/1. The actual installed TrafficGen HotSpot case emits destinations [4,4,4] for target 3 in range [0,4). This observes outgoing requests; it is not a router/network-completion test.
- **F04:** unique_ptr<Event> loses the derived type and consumes 40/44 bytes; unique_ptr<Request> loses the actual ExtendedRequest type and consumes 55/90 bytes. Raw-pointer controls preserve dynamic types and consume 52/52 and 98/98 bytes. Alias ownership, abstract pointees, following sentinel fields, and whole-application checkpoints remain additional coverage. No direct unique_ptr<Request>/unique_ptr<internal_router_event> ownership site was found in current Merlin sources; this is an infrastructure defect, not proof that a shipping checkpoint path hits it.
- **F05:** WriteUnlock::makeResponse changes both request and response virtual addresses from expected 0x8000 to zero. This confirms metadata corruption; it does not prove an incorrect physical write or CPU result.
- **F06:** exported receiver statistic parameters remain {rate: 10ns} after the second enable tries to add HistogramStatistic and binwidth=2. The once-enabled control has the same original parameters. New settings are lost.
- **F07:** 100 batched samples produce collection count 100 and bin population 100, but NumItemsBinned=1.
- **F08:** samples 5 and 14 are counted as two binned items, but displayed bins [5,14]/[15,24] both contain zero. Actual installed basicStatistics similarly collects/bins four integer samples with Sum=639 but displays ten empty bins under a non-aligned minimum.
- **F09:** floating sample 1.5 in the intended range [0,2) is rejected above maximum: collected=1, binned=0, above-max=1. Actual basicStatistics rejects all four floating samples in its configured [0,1) histogram.
- **F10:** the raw double accumulator maximum for [-3,-1] is 2.2250738585072014e-308 instead of -1. Reset and zero-only variants were not rerun; the constructor/reset source still uses numeric_limits::min(). Text output rounds the wrong maximum to zero.
- **F11:** the variance getter returns 4 for [-3,-1]; population variance is 1 and sample variance is 2. The desired convention still needs documentation. Raw Sum/SumSQ/Count output can be postprocessed correctly; no getVariance/getStandardDeviation caller was found in current element sources.

The broader runtime checks in [RUNTIME_VALIDATION.md](../../../RUNTIME_VALIDATION.md) passing did not cover these contracts. These focused reproductions explain why that campaign could pass while these defects remain.

## Evidence and rerun

- [Assessment JSON](evidence/assessment.json): observed/expected values per finding and raw controls.
- [Command/run records](evidence/results.json): exact compiler/runtime commands, exits, timings and probe hashes.
- [Basic probe output](evidence/basic.out), [clock control](evidence/clock_one.out), [clock crash stderr](evidence/clock.err).
- [HotSpot output](evidence/hotspot.out), [integer element histogram](evidence/element_stats_integer.out), [floating element histogram](evidence/element_stats_floating.out).
- [Once-enabled statistic JSON](evidence/substats_once.json) and [twice-enabled statistic JSON](evidence/substats_twice.json).
- [Runner](run_reassessment.py), [classifier](summarize_reassessment.py), and retained sources in probes/.

From the sst-ai-tools root:

```sh
.venv/bin/python reviews/core/2026-10-06/run_reassessment.py \
  --prefix "$PWD/.runtime/devel/install" --workspace "$PWD/.." \
  --output "$PWD/.runtime/reassessment-2026-10-06" \
  --sdk /Library/Developer/CommandLineTools/SDKs/MacOSX26.5.sdk
.venv/bin/python reviews/core/2026-10-06/summarize_reassessment.py \
  --input "$PWD/.runtime/reassessment-2026-10-06" \
  --archive "$PWD/reviews/core/2026-10-06/evidence"
```

Use a matching build for the intended source revision. The SDK setting above is this host's working setting; omit/adapt it on other hosts. The crash trigger is deliberate. The classifier reports reproduced defects separately from raw-pointer controls; it does not call a changed result fixed without investigation. Preserve evidence before rerunning because result paths are replaced.

The original [September 25 reports](../2026-09-25/index.md) are unchanged. Their [finding tracker](../2026-09-25/findings.json) now points to this assessment. Suggested repair order remains clock dispatch, scoped precedence/discrete sampling, StandardMem/stat ownership, then statistic and serialization contracts with focused regression tests. No fixes were attempted.

## Artifact verification

The final probe compile with -Wall/-Wextra emitted no diagnostics. Python runner/classifier formatting and lint checks passed, as did repository link validation and 14 tooling tests. clang-format was not available, so a C++ formatting check could not be run. The C++ probe follows the retained reproducer rather than a production source refactor.
