---
{
  "type": "SST Element Profile",
  "title": "mercury main use cases",
  "description": "Node, OS, NIC, and modeled compute machinery.",
  "tags": [
    "mercury",
    "Application runtime"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T09:42:17.624014+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/pymercury.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/pymercury.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "28b879fca429a047cfac23554d31aef4c02b6f1271831d8cb06b14c54e24e718"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/node.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/node.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "dd59fadf352b84ff4f7fc4cff86000017fdb3d3231859dadb9dcc1eab8a7a3a1"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/nic.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/nic.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "330ac29185f7e2881f6ca801eb6df52afa6fd858568e803da9e6106707a7ff91"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/operating_system.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/operating_system.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "b27abb003658c52b4a2417296352b7a49737afff5a887051dfa12d78807269e9"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/tests/testsuite_default_hg.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/tests/testsuite_default_hg.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "2a20990c96f2da713333b4b30fdea279ae2561e134d75cb0ba47260e853d35a7"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/compute_library/node_cl.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "35b4e39ba9e5ebdb6c8a80f19efa880c433e1407fa0a74e029fb7c8e41e48f74",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/compute_library/node_cl.h"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/compute_library/operating_system_cl.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "f01ef1d6bfbfa7d78ceb4031a5b6bfc34795904ac175f50db114e3acc854f734",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/compute_library/operating_system_cl.h"
    }
  ],
  "x-element": "mercury",
  "x-role": "Application runtime",
  "x-coverage": "detailed"
}
---

# mercury: main use cases

Role: **Application runtime**. Node, OS, NIC, and modeled compute machinery.

## Use it for

- Construct application/runtime nodes connected to a network.
- Explore compute/memory/communication cost and modeled application communication.

## Boundaries and prerequisites

Components register under hg, not mercury. Workloads using `computelibrary:ComputeLibrary` need the `hg.NodeCL` / `hg.OperatingSystemCL` pair. `HgJob` node/core allocation sets virtual ranks; OS compute-core parameters serve a separate purpose. OS/context switching and some tests are architecture or host-rank/thread specific; check the current transport and OS APIs before extending them.

## Common companions

[iris](../iris/use-cases.md), [mask-mpi](../mask-mpi/use-cases.md), [merlin](../merlin/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/mercury/`. Read these selectively and verify ELI names against current source.

- `pymercury.py`
- `components/node.h`
- `components/nic.h`
- `components/operating_system.h`

## Validation starting point

Check application completion, wakeup/progress, VN/rank mapping, and relevant hg/runtime tests with their skip conditions.

Native runner suites:

- `tests/testsuite_default_hg.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/ostest-nano.py`
- `tests/ostest.py`

Use `python3 tools/sst_tools.py plan-tests --target mercury` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). For implementation detail read [overview](overview.md), [extension points](extension-points.md), and [validation](validation.md) as needed.

## Compiled application and MPI implementation use cases

Use SST-HGCC to turn compatible C/C++ sources into registered Mercury application libraries, or build a skeleton in tree as an `ext` library ([skeleton applications](skeleton-apps.md)). Choose the supported Mask-MPI path for modeled MPI behavior, or the adapted MVAPICH2/MV2 integration when implementation-specific collective/protocol behavior matters. See [the HGCC/MV2 guide](hgcc-mv2.md) for prerequisites, rank semantics, and validation boundaries.
