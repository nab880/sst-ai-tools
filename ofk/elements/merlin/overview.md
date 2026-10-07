---
{
  "type": "SST Guide",
  "title": "Merlin model selection",
  "description": "Select Merlin interfaces and network extension boundaries.",
  "tags": [
    "merlin",
    "network"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:58.406073+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/router.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/router.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "22c1ae45060949c0017f12bdf93b38f435d82b9e1b15c9d6bfebddbb8d20575e"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/hr_router/hr_router.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/hr_router/hr_router.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "8c55c50ed76b626465df4a5c32410994f14522d733ce31356346639eb6509d0c"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/tests/testsuite_default_merlin.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/tests/testsuite_default_merlin.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "f2f31edb4736e799e7da720c3a0f629295948ed3d8db9108dfb12b103ced4577"
    }
  ]
}
---

# Merlin model selection

Merlin provides configurable network routing and link behavior. Start at `router.h` for `Router`, `Topology`, router events, and arbitration interfaces; `hr_router/hr_router.h` for the registered router; and core `interfaces/simpleNetwork.h` for the endpoint-facing contract.

| Desired change | Inspect first |
|---|---|
| Connectivity or route selection | `topology/` and `Topology` |
| Router datapath | `hr_router/` |
| Port buffering or flow control | `interfaces/portControl.h` and `.cc` |
| Endpoint network interface | `interfaces/linkControl.h` and `.cc` |
| Arbitration | `OutputArbitration`, `XbarArbitration`; crossbar arbiters `hr_router/xbar_arb_*.h` (default `merlin.xbar_arb_lru`), output arbiters `interfaces/output_arb_*.h`, and `arbitration/single_arb.h` |
| Destination/workload generation | `trafficgen/`, `target_generator/` |
| Python assembly | `pymerlin-base.py`, `topology/pymerlin-topo-*.py` |

This devel guide covers router, topology, link-control, and workload interfaces. Confirm any additional capability in the selected source revision before relying on it.

Next: [extension points](extension-points.md) for C++ work, [validation](validation.md) for test entry points, or [model construction](../../using-sst/models.md) for configuration.
