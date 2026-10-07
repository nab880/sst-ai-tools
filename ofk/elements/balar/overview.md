---
{
  "type": "SST Guide",
  "title": "Balar GPU integration selection",
  "description": "Choose trace-driven or Vanadis-driven CUDA execution before implementation.",
  "tags": [
    "balar",
    "overview"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:23.963994+00:00"
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
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/configure.m4",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/configure.m4",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "247373b2f64fd571995420d4ab66708fe01f92def16f0f2c72187abbb59c1fa7"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/balarMMIO.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/balarMMIO.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "14a52510134d8eeb0c90d1421f8683fafbf605d3073bc00b23319dda32d9f9b5"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/tests/libcudart/Makefile",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/tests/libcudart/Makefile",
      "x-sha256": "6c975d34dd48a14d77f26a15730698678a46e230f79af831b05d8193152d6b27",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---

# Balar GPU integration selection

Balar integrates GPGPU-Sim with SST. The local README describes two workflows: trace-driven CUDA API replay and direct execution with a Vanadis RISC-V CPU. These have different prerequisites; select the mode before building or editing.

The registered `balar.balarMMIO` component in `balarMMIO.h` uses a StandardMem `mmio_iface` slot. `dmaEngine.h` and `balar_packet.h` support data movement and command representation. Inspect `tests/testBalar-testcpu.py` for trace replay and `tests/testBalar-vanadis.py` for CPU integration.

`configure.m4` checks CUDA and GPGPU-Sim and leaves the element unbuilt without GPGPU-Sim, including `balar.dmaEngine` and `balar.BalarTestCPU`. Trace generation requires GPU tooling according to the README; direct execution uses a matching RISC-V/LLVM toolchain and the custom runtime `libcudart_vanadis` built from `tests/libcudart/` (which needs `LLVM_INSTALL_PATH` and `RISCV_TOOLCHAIN_INSTALL_PATH`) and linked by the example programs in `tests/vanadis_llvm_rv64/`. Listed tested versions are historical checkout documentation, not a verified current compatibility recommendation.

Read [Vanadis](../vanadis/overview.md) and [memHierarchy](../memHierarchy/overview.md) only for the selected integration. Next: [extension points](extension-points.md), [validation](validation.md).
