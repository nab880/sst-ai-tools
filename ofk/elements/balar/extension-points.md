---
{
  "type": "SST Guide",
  "title": "Extend Balar command and memory integration",
  "description": "Trace CUDA commands through MMIO, DMA, and GPU completion.",
  "tags": [
    "balar",
    "extension-points"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:24.219316+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/balarMMIO.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/balarMMIO.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "14a52510134d8eeb0c90d1421f8683fafbf605d3073bc00b23319dda32d9f9b5"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/balar_packet.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/balar_packet.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "f7709e99788d7b3f67e038fda77d9ba8143beda5f13d0c3406a23b152c2df772"
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
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "8fcb45517d8bec1aefb22c4e3000886e3a0bdf5a7e5bfce1c93614e33708a5cb"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/balar/testcpu/balarTestCPU.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/balar/testcpu/balarTestCPU.h",
      "x-sha256": "d6c3da0c0ac0b83ab35f6a559a1f858f8d1efa2a6913f7f6b42c1f4742150506",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---

# Extend Balar command and memory integration

| Behavior | Inspect first |
|---|---|
| MMIO command handling and callbacks | `balarMMIO.h`, `balarMMIO.cc` |
| Command representation | `balar_packet.h`, `cuda_runtime_api.h` |
| Host/device transfer | `dmaEngine.h`, `dmaEngine.cc` |
| Trace ingestion | `balar.BalarTestCPU` in `testcpu/` (`trace_file`, `cuda_executable`) and `tests/testBalar-testcpu.py` |
| CPU-issued CUDA calls | `tests/vanadis_llvm_rv64`, `tests/libcudart/`, `tests/testBalar-vanadis.py` |

For a new CUDA operation, trace command encoding, pointer/address translation, payload movement, GPGPU-Sim invocation, and completion back to the requester. Check which layers already implement the operation; adding only a dispatch case is insufficient when data or synchronization semantics change.

Preserve stream/event ordering, request ownership, and memory-transfer completion. Distinguish modeled CPU/GPU memory from host simulator pointers. Follow registration/build conventions in `Makefile.am`. Do not install or upgrade external dependencies without authorization; record prerequisites and validate in a compatible environment. Follow [validation](validation.md).
