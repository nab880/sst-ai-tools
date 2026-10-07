---
{
  "type": "SST Guide",
  "title": "Validate Balar execution",
  "description": "Account for external toolchains, expensive cases, and disabled tests.",
  "tags": [
    "balar",
    "validation"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T19:00:11.687319+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/tests/testsuite_default_balar.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/tests/testsuite_default_balar.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "201f9b7be2e61c1049f8c81af568a82400bb23c03fc16f42b82a50d705499e92"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/tests/testBalar_testsuite_util.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/tests/testBalar_testsuite_util.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "907d61f023d12cc76f0fdff1caa2609836414044fb83b2a231658e1d9bb41d99"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/README.md",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/README.md",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "d19c3ce940a38c0ca14ddf9312f0871a16fb003696f9d36bc595e2df125cb1c5"
    }
  ]
}
---

# Validate Balar execution

Read `tests/testsuite_default_balar.py` and `testBalar_testsuite_util.py` before running. The checked suite has an active Vanadis/LLVM vector-add case with a 30-minute timeout; several other cases are commented out. Suite discovery or disabled cases do not establish coverage. `configure.m4` disables the element without CUDA and GPGPU-Sim, and no CUDA toolkit exists for ARM64 macOS, so Balar stayed unbuilt in the October 7, 2026 pass; closing it needs an x86-64 Linux host with the toolkit. As checked in, module setup lists `tests/vectorAdd`, but that directory is now `tests/balar_trace`, so `os.listdir` raises before any compile step and the active case cannot run unmodified.

The active helper checks that the statistics file exists and that its line count differs from the reference by at most 15. It does not compare vector values. Add or inspect an explicit numerical application assertion before calling this a data-correctness test. Setup compiles the custom runtime and examples; if `GPUAPPS_ROOT` is supplied it also builds Rodinia and fetches data, even when selecting the basic vector-add case.

For trace mode record trace files, data payloads, CUDA executable/PTX information, and GPU configuration. For direct execution record the RISC-V executable, custom runtime/toolchain, `VANADIS_EXE`, `VANADIS_ISA`, and `BALAR_CUDA_EXE_PATH` as required by the selected example; the suite's clang template instead passes binaries through `--vanadis-binary`/`--cuda-binary` model options and sets only `VANADIS_ISA`. Use a small deterministic vector operation with numerical output checks and completion checks, not only simulator exit status.

Compare kernel/API behavior and transferred bytes; include synchronization and data-movement cases for changed operations. Identify missing CUDA, GPGPU-Sim, GPU trace tooling, binaries, or toolchains as blockers. Avoid automatically triggering an expensive compile or application collection sweep just to inspect tests.

Use [test planning](../../development/testing.md) with target `balar`; perform prerequisite checks and narrow the case first.
