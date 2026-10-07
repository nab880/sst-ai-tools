---
{
  "type": "SST Guide",
  "title": "Merlin topology and routing extensions",
  "description": "Implement topology changes without recreating router and link machinery.",
  "tags": [
    "merlin",
    "extension"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:58.528406+00:00"
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
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/topology/singlerouter.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/topology/singlerouter.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "77034f6d8ddb8e428540e4087fa24835dc9b5ffa08431b2a86de4ba51d3b42b2"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/topology/singlerouter.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/topology/singlerouter.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "e7f73c2ac607a70205e605ad539d72e11cbdedc41c4f9c23f3ff2498ddeda77d"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "b853c0d246415fbcb2cbc8cf3b30bcd1f5b2cc1303b3b9917fb3d75ac4a5118e"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/hr_router/hr_router.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/hr_router/hr_router.cc",
      "x-sha256": "1a2f345bb5af6cedbba6c90036025799f62e16053c5028828a5d715f8b7cedfd",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---

# Merlin topology and routing extensions

`Topology` lives in `router.h`; the registered subcomponent API takes three integers: number of ports, router ID, and number of virtual networks. `topology/singlerouter.h` and `.cc` form the smallest concrete example; use a multi-router example for inter-router routing.

Inspect `route_packet`, `process_input`, `getPortState`, and `getVCsPerVN`, plus `routeUntimedData`, `process_UntimedData_input`, and endpoint ID mapping. Implement both modern untimed methods explicitly following concrete topologies. In this revision the base `process_UntimedData_input` calls itself recursively, and `hr_router` invokes it during untimed initialization, so a topology that does not override it recurses at runtime; inheriting it is unsafe even though the adjacent code is presented as legacy compatibility. The single-router implementation (`merlin.singlerouter`) returns a new `internal_router_event`, handles untimed broadcast separately from unicast routing, maps `getEndpointID(port)` to `port`, and reports every port as `R2N`; the base `Topology` exposes one ELI parameter, `network_name`.

Keep port mapping, packet next-port selection, VC assignment, and VN-to-VC counts consistent. Routing changes must respect buffer/credit availability where applicable and justify progress/deadlock behavior for the chosen topology. Adaptive routing requires inspecting queue/credit hooks and a related adaptive implementation.

Update ELI registration, `merlin/Makefile.am`, and Python topology construction when needed. Preserve topology-specific event metadata in cloning and serialization. Review the endpoint request ownership contract in [core contracts](../../core/contracts.md), then follow [validation](validation.md).
