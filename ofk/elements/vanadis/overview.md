---
{
  "type": "SST Guide",
  "title": "Vanadis CPU and application selection",
  "description": "Choose instruction execution, pipeline, OS, or memory boundaries.",
  "tags": [
    "vanadis",
    "overview"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:00:40.708116+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/vanadis.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/vanadis.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "3a9ad3cdaa2503ded0096c1fd324890b4d708129a8261e18e14a8c0be7b8bef0"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/decoder/vdecoder.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/decoder/vdecoder.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "7aaea70caa9ea3524b4e22cfa909444316fd9c9bf57927f7127bd868825423c8"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/tests/testsuite_default_vanadis.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/tests/testsuite_default_vanadis.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "7d6bbd8ef2d5ccae675c4a7329af8bbe2c65d4dacd0c2aa24792757d4901a5d9"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/tests/basic_vanadis.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/tests/basic_vanadis.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "3a9574055711fca2ec2190c90edcd156b9b4321bfc079ed425528957c8cef674"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/Makefile.am",
      "x-sha256": "b23c13384245118d3d377c24c2cfebdc67044a385066228079627e2bd7e94a25",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---

# Vanadis CPU and application selection

Vanadis models processor execution of binaries with decoder, instruction, pipeline, load/store, and OS interfaces. The checked test matrix exercises MIPS little-endian and RISC-V64 binaries; choose an ISA-compatible executable and configuration together.

| Need | Entry point |
|---|---|
| CPU parameters/pipeline | `vanadis.h`, `vanadis.cc` |
| Decode an instruction | `decoder/vdecoder.h`, `vmipsdecoder.h`, `vriscv64decoder.h` |
| Instruction semantics | `inst/vinst.h` and one adjacent opcode class |
| Load/store ordering | `lsq/` |
| OS/system calls | `os/` |
| Model assembly | `tests/basic_vanadis.py`, `examples/vanadis_L1_L2_L3.py` |

Use [memHierarchy](../memHierarchy/overview.md) for cache/memory behavior, [Carcosa](../carcosa/overview.md) for fault injection, and [Balar](../balar/overview.md) for CUDA/GPU integration. Check ELI names and aliases in the actual headers/configuration rather than inferring them from class names. The CPU registers as `vanadis.core` with the legacy alias `dbg_VanadisCPU`; the Makefile also builds `libvanadisdbg` from the same sources with `-DVANADIS_BUILD_DEBUG`, registering the same components under the `vanadisdbg` library, which `basic_vanadis.py` selects with `--library` or `VANADIS_LIBRARY`.

Next: [extension points](extension-points.md), [validation](validation.md).
