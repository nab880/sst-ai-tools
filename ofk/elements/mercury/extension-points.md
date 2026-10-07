---
{
  "type": "SST Guide",
  "title": "Extend Mercury nodes and services",
  "description": "Separate modeled compute, application runtime, and NIC transport behavior.",
  "tags": [
    "mercury",
    "extension-points"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:05:34.815955+00:00"
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
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/nic.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/nic.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "330ac29185f7e2881f6ca801eb6df52afa6fd858568e803da9e6106707a7ff91"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/operating_system_api.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/operating_system_api.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "099f623599e41512f19b25be00b5538977d1aa05b5ce4fb9db493853e55419da"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/nic_api.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/nic_api.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "96549197fca5b4e099411d0b21430a932610379520d196b8ee4e1e67f1a3a967"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "76ac810ac435e0b2232aa8b78005c23ad678e9b5d2c5e0a397a937c621b26aaa"
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
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/compute_library/node_cl.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/compute_library/node_cl.cc",
      "x-sha256": "6c890ed581699e200177ecb3a9b758bea1c422f0def489ca00bf79277adf2dac",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/sumi/sim_transport.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/sumi/sim_transport.cc",
      "x-sha256": "cb48a9e1b5fb5189c59651f6f9cf4ca9bcc95eba87a2176eb5802399b37a4ff7",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/libraries/compute/compute_scheduler.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/libraries/compute/compute_scheduler.cc",
      "x-sha256": "448451c42550a05c6638676f8d0774f0a9e7bb16cf3fb4d8acd6108b09453c2e",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/operating_system_impl.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/operating_system_impl.cc",
      "x-sha256": "e457c5886a49dd4c327d7d679de4a69c7bb7d4a72a2bdaaf6703bb29718131e6",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---

# Extend Mercury nodes and runtime

| Behavior | Inspect first |
|---|---|
| Node construction and rank mapping | `components/node.h`, `node_base.h`, `pymercury.py` |
| Application lifecycle and blocking | `components/operating_system_api.h`, `operating_system_impl.h`, `operating_system/` |
| NIC communication and injection | `components/nic.h`, `nic_api.h` |
| Modeled compute/memory costs | `components/compute_library/node_cl.h`, `operating_system_cl.h`, and `libraries/compute/` |
| Communication collectives | The selected Iris/Mask-MPI consumer and transport |

Keep application-visible logical ranks separate from physical endpoint IDs. `HgJob.build` derives the logical ID from the allocation map and installs node, OS, NIC, and a network-interface slot. Inspect current API and VN handling at the actual caller/transport before changing communication behavior.

Use `hg.NodeCL` with `hg.OperatingSystemCL` when the application loads `computelibrary:ComputeLibrary`; keep this pairing when extending compute or memory behavior. `HgJob(job_id, numNodes, numCores=1, nicsPerNode=1)` sizes the Merlin job as `numNodes * nicsPerNode` endpoints; `HgJob.build` then passes `nranks = numNodes * numCores` and `npernode = numCores` to each node, and the OS launches `npernode` application instances per node. The separate OS `ncores` parameter configures compute resources; it does not set that job rank count, and `NodeCL`'s constructor shadows its own `ncores_`/`nsockets_` members with locals, so its accessors return uninitialized values while the compute scheduler reads `ncores` itself. All transport delays route through the application's `ComputeLibrary`: `SimTransport` resolves it by name and uses it without a null check for `post_*_delay`, `pinRdma`, and memcpy costs, so an application that omits `computelibrary:ComputeLibrary` has no valid compute hook for those costs.

Runtime context switching is host-architecture sensitive. Preserve blocking/wakeup ownership and pending operations when changing OS/NIC paths. Update `Makefile.am` for new sources and check related-element callers before API edits. Follow [validation](validation.md).
