---
{
  "type": "SST Guide",
  "title": "Mercury application and node selection",
  "description": "Route Mercury work through its hg registration and node/OS/NIC layers.",
  "tags": [
    "mercury",
    "overview"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:05:35.363803+00:00"
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
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/operating_system.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/operating_system.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "b27abb003658c52b4a2417296352b7a49737afff5a887051dfa12d78807269e9"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/nic.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/nic.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "330ac29185f7e2881f6ca801eb6df52afa6fd858568e803da9e6106707a7ff91"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/compute_library/node_cl.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "35b4e39ba9e5ebdb6c8a80f19efa880c433e1407fa0a74e029fb7c8e41e48f74",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/compute_library/node_cl.h"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/compute_library/operating_system_cl.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "f01ef1d6bfbfa7d78ceb4031a5b6bfc34795904ac175f50db114e3acc854f734",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/compute_library/operating_system_cl.h"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/common/mercury.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/common/mercury.cc",
      "x-sha256": "e6a315019e6a3c59007e492106a81c4c350b240a822fec84abe25997599776df",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/operating_system/process/app.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/operating_system/process/app.cc",
      "x-sha256": "0f7b51e1ec5cd87d2ebd7abc58494ee55935e4c31aa20b9727abbc9fe77d41e0",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---

# Mercury application and node selection

Mercury supplies node, operating-system, NIC, and compute-library machinery for application modeling. Source directories use `mercury`, but ELI component names use `hg`: `hg.Node`, `hg.OperatingSystem`, and `hg.nic`. Do not invent `mercury.Node` from the directory name.

For the HGCC/Mask-MPI/MV2 examples that load `computelibrary:ComputeLibrary`, select the compute-capable pair **`hg.NodeCL` and `hg.OperatingSystemCL`**. Their definitions live under `components/compute_library/`; the plain Node/OperatingSystem pair is used by simpler OS models. Adding frequency or memory parameters to a plain node does not install the compute model.

`pymercury.py` provides `HgJob`, `HgNode`, `HgOS`, and `HgNIC` assembly integrated with Merlin; the Python module registers as `hg` (`import sst.hg`). `HgNode`/`HgOS` take their ELI names from the `name` parameter supplied by platform parameter sets, which is how `hg.NodeCL`/`hg.OperatingSystemCL` are selected, while `HgNIC` hard-codes `hg.nic`. `app1.libraries` entries of the form `lib:Name` instantiate ELI `lib.Name` keyed by `Name`, which is why fixed lookup keys such as `ComputeLibrary` and `libfabric` work. Start with `components/node.h`, `operating_system.h`, and `nic.h`; `operating_system/` contains runtime machinery and `libraries/compute/` supplies compute modeling. Application/API integrations may live in related elements, so trace the chosen workload's loader and dependencies.

Use [Ember](../ember/overview.md) for motif-driven workload schedules and [Merlin](../merlin/overview.md) for topology/routing behavior. Use the devel APIs and the actual communication consumer to determine supported collective behavior.

Next: [extension points](extension-points.md), [validation](validation.md).

For compiled C/C++ applications and MPI-implementation studies, read [SST-HGCC and MV2](hgcc-mv2.md). Mercury supplies the runtime; HGCC supplies compilation/rewriting, and the selected MPI path supplies communication semantics.
