---
{
  "type": "SST Element Profile",
  "title": "balar main use cases",
  "description": "CUDA/GPGPU-Sim integration through MMIO and DMA.",
  "tags": [
    "balar",
    "Accelerator"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:23.699539+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/README.md",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/README.md",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "d19c3ce940a38c0ca14ddf9312f0871a16fb003696f9d36bc595e2df125cb1c5"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/balarMMIO.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/balarMMIO.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "14a52510134d8eeb0c90d1421f8683fafbf605d3073bc00b23319dda32d9f9b5"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/dmaEngine.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/dmaEngine.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "35b117910eae73bb6a53318e67545d079b5f193a51a49d607e1ef994b4f75ffd"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/tests/testsuite_default_balar.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/tests/testsuite_default_balar.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "201f9b7be2e61c1049f8c81af568a82400bb23c03fc16f42b82a50d705499e92"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/tests/testBalar-testcpu.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/tests/testBalar-testcpu.py",
      "x-sha256": "68fea274cfacc2d8190d5e849bac7ac41c74add9f3d1f3576458db7897c5ad94",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/tests/testBalar-vanadis.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/tests/testBalar-vanadis.py",
      "x-sha256": "aa9f57252df7e82dabace5eb64b78fc359be779f47ebea0030968822e9e24c2c",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/configure.m4",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/configure.m4",
      "x-sha256": "247373b2f64fd571995420d4ab66708fe01f92def16f0f2c72187abbb59c1fa7",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "balar",
  "x-role": "Accelerator",
  "x-coverage": "detailed"
}
---

# balar: main use cases

Role: **Accelerator**. CUDA/GPGPU-Sim integration through MMIO and DMA.

## Use it for

- Study CUDA kernel execution and host/device data movement with an SST memory system.
- Compare trace-driven replay with Vanadis-driven application integration when the required artifacts exist.

## Boundaries and prerequisites

CUDA/GPGPU-Sim and mode-specific toolchains/traces are prerequisites; without GPGPU-Sim, `configure.m4` disables the whole element, so `sst-info balar` is empty in such builds. Trace generation uses a CUDA GPU and the tracer; existing traces can then be replayed. Direct execution uses the supplied Vanadis RISC-V/toolchain integration. The native suite currently exposes a Vanadis/Clang vector-add case; several other cases are commented out. A disabled or skipped test is not execution evidence.

## Common companions

[vanadis](../vanadis/use-cases.md), [memHierarchy](../memHierarchy/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/balar/`. Read these selectively and verify ELI names against current source.

- `README.md`
- `balarMMIO.h`
- `dmaEngine.h`

## Validation starting point

Check vector/kernel numerical results, transfer sizes, command completion, and selected Balar regressions.

Native runner suites:

- `tests/testsuite_default_balar.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/testBalar-testcpu.py` (trace replay)
- `tests/testBalar-vanadis.py` (Vanadis-driven)

`balarBlock.py`, `memory.py`, `vanadisBlock.py`, and `vanadisOS.py` are helper builder modules imported by those configurations, not runnable models.

Use `python3 tools/sst_tools.py plan-tests --target balar` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). For implementation detail read [overview](overview.md), [extension points](extension-points.md), and [validation](validation.md) as needed.
