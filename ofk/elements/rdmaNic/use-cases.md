---
{
  "type": "SST Element Profile",
  "title": "rdmaNic main use cases",
  "description": "RDMA-style host, memory, and network integration.",
  "tags": [
    "rdmaNic",
    "NIC/offload"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T19:00:09.589157+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/rdmaNic/rdmaNic.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/rdmaNic/rdmaNic.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "6dc108e0973c0592c53f1b09b48761d471ce6d0aa7f2f7d2d1492ad2e3e731bf"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/rdmaNic/rdmaNicHostInterface.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/rdmaNic/rdmaNicHostInterface.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "097ad0ab28748d4d70fb2db0a6276a312ac7cf35635fdf04b5bddd9414a1858f"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/rdmaNic/rdmaNicCmds.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/rdmaNic/rdmaNicCmds.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "1a12b69cd3b8b9a2388d0f04220f4f88ec1052f71401cd4381d8e8e1ddcac7d8"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/rdmaNic/tests/testsuite_default_rdmaNic.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/rdmaNic/tests/testsuite_default_rdmaNic.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "d9172913952b1bf622ed8e66e7d628c16bf5b1019dbf6903e60d713b7b72b236"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/rdmaNic/rdmaNic.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/rdmaNic/rdmaNic.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "df3ac9b628d55d8be50eec3deb73592d2c67e26af0cf458c8f6fdd677f61d677"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/rdmaNic/tests/runVanadis.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/rdmaNic/tests/runVanadis.py",
      "x-sha256": "7d1c4903d4da524815f2f93e88340315419d3fa184f6e8b958daafcb68206f95",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "rdmaNic",
  "x-role": "NIC/offload",
  "x-coverage": "use-case-profile"
}
---

# rdmaNic: main use cases

Role: **NIC/offload**. RDMA-style host, memory, and network integration.

## Use it for

- Study supported host commands, DMA, remote-memory access, and NIC queues.
- Explore send/receive, registered-region read/write, completion queues, and the implemented barrier path.

## Boundaries and prerequisites

`rdmaNic.nic` uses StandardMem interfaces for MMIO/DMA and SimpleNetwork for network transport. Its host-command enum has no atomic operation; the `cyclePerIncOp`/`addrIncOp` statistics do not establish an atomic API. The `mmio`, `dma`, and `rtrLink` names are loaded as user subcomponent slots although documented only as ports; the example fills them with `memHierarchy.standardInterface`. Supported commands and ordering must be checked against the host API before assuming external RDMA-standard coverage.

## Common companions

[memHierarchy](../memHierarchy/use-cases.md), [merlin](../merlin/use-cases.md), [vanadis](../vanadis/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/rdmaNic/`. Read these selectively and verify ELI names against current source.

- `rdmaNic.h`
- `rdmaNicHostInterface.h`
- `rdmaNicCmds.h`

## Validation starting point

Check local/remote data, completion and ordering, memory effects, and the targeted rdmaNic regression. The suite requires musl tooling and serial host execution; its availability check invokes `mipsel-linux-musl-gcc` even though the current test matrix uses RISC-V applications. Inspect that gate and the application Makefiles when diagnosing a skip. The IMB-MPI1 matrix entry is nightly-only and `app/mpi` has no Makefile, so setup builds only `app/rdma`. On October 7, 2026 both cases ran on the recorded devel install: wrapper scripts named `mipsel-linux-musl-gcc`, `riscv64-linux-musl-gcc`, and `riscv64-linux-musl-ar` that call `zig cc -target riscv64-linux-musl` (and `mipsel-linux-musleabihf`) from a self-contained Zig 0.15.1 download satisfy the gate, and `app/rdma` builds static RVC double-float ELFs. The `msg` case completes at 120.147 us with node 1 reporting `validate complete` and per-node output matching the gold except for one link-layout address, but its statistics differ from `msg.out.gold`, which came from the upstream GCC 10.2.1 musl binary, so the native case fails on that exact diff. The IMB-MPI1 case uses the shipped binary and passes through the native suite with `-m pr nightly` (both categories are required; `-m nightly` alone skips it), matching all six gold files at 9.93425 ms.

Native runner suites:

- `tests/testsuite_default_rdmaNic.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/runVanadis.py` (driven by `RDMANIC_EXE`, `RDMANIC_NUMNODES`, and `RDMANIC_NETWORK_SHAPE`)

`node.py`, `memory.py`, `rdmaNic.py`, `vanadisBlock.py`, and `vanadisOS.py` are builder modules it imports, not runnable models.

Use `python3 tools/sst_tools.py plan-tests --target rdmaNic` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
