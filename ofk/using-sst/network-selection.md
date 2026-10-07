---
{
  "type": "SST Guide",
  "title": "Select a network model",
  "description": "Choose the network mechanism and workload abstraction from user priorities.",
  "tags": [
    "selection",
    "network-selection"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:05:00.227824+00:00"
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
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/kingsley/noc_mesh.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/kingsley/noc_mesh.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "a874bf5674b5a1b7779f75a56d33131125d45f60eb7b214c12e781ef71858c86"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/embergen.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/embergen.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "9b0abe7315a71633cbfb893d587197c23ecf8fb2b090e39bd856d55c5cc7b67b"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/node.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/node.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "dd59fadf352b84ff4f7fc4cff86000017fdb3d3231859dadb9dcc1eab8a7a3a1"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/shogun/shogun.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/shogun/shogun.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "20a57a404d2ae3e02b3f811a294474872f4d69a3c4c1533049a53a9f9cce5043"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/shogun/shogun_nic.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/shogun/shogun_nic.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "976737d8c990f6397fd1d644d4c8681da43699ee89cb831bb9bcddfffa27eb52"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/trafficgen/trafficgen.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/trafficgen/trafficgen.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "1283e25f9963bd88c232618759deed3e61917142fcbe58c14795fe883b89baff"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/firefly/hadesMP.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/firefly/hadesMP.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "640bd26f68e979972e91f5162f6a408511cdab1fb3324ec47409b6d41fbd89e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/firefly/nic.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/firefly/nic.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "f596e734fd650e7e78bec27ed65ca753c60dc568d4fb7c1d47ea6fa95faa6afc"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/zodiac/zsirius.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/zodiac/zsirius.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "c6c942fc18bf519afe4937aaa6019a4c469bc4421f84541d415cbcede301d121"
    }
  ]
}
---

# Choose the network and workload separately

| Required behavior | Candidate and source evidence | Selection limit |
|---|---|---|
| Router/topology/routing and link behavior | [Merlin](../elements/merlin/overview.md); `merlin/router.h` | Verify required topology, flow control, and routing in the chosen implementation |
| A 2-D on-chip mesh with directional ports | [Kingsley](../elements/kingsley/use-cases.md), `kingsley/noc_mesh.h` | Use its SimpleNetwork linkcontrol and verify endpoint IDs (including the edge-port halo ring) and X/Y routing order |
| A single arbitrated crossbar | [Shogun](../elements/shogun/use-cases.md), `shogun/shogun.cc` | Current arbitration is fixed round-robin and service is messages per cycle (negative ejection limits clamp to 256); this differs from byte/flit serialization |
| Controlled synthetic offered load | [Merlin trafficgen](../elements/merlin/use-cases.md), `merlin/trafficgen/trafficgen.h` | Check packet counts, destination bounds, and generator distributions; the reviewed HotSpot path has a known defect |
| Prescribed communication/computation motifs | [Ember](../elements/ember/overview.md) | Workload generation; pair it with transport and network models |
| Message-passing/SHMEM protocol and NIC overhead | [Firefly](../elements/firefly/use-cases.md) through [Hermes](../elements/hermes/use-cases.md) | Match the selected workload API and network interface; protocol costs and router costs are separate |
| Replay recorded MPI communication | [Zodiac](../elements/zodiac/use-cases.md) | Requires a supported SIRIUS trace and protocol stack; supported calls and recorded execution limit feedback |
| Application/runtime/node communication | [Mercury](../elements/mercury/overview.md) | Registered under hg; verify application integration and runtime prerequisites |
| Memory-system network traffic | [memHierarchy](../elements/memHierarchy/overview.md) | Endpoint/cache semantics and transport must match the chosen interconnect |
| Fault injection | [Carcosa](../elements/carcosa/overview.md) | Confirm the injection hook can represent the requested network fault; memory examples alone do not establish network support |

These are candidates, not an exhaustive ranking of SST networks. Search other elements when a hard requirement is unsupported. Choose the smallest abstraction that preserves the causal mechanisms needed for the requested result. A topology name alone does not establish router timing or protocol fidelity. For application MPI, choose [Mask-MPI or adapted MV2](../elements/mercury/hgcc-mv2.md) according to the implementation behavior being studied. Iris [fabric/provider selection](../elements/iris/fabrics.md) is a separate choice from physical topology.

# Turn priorities into checks

For latency, specify start/end boundaries, load, packet/message size, and whether endpoint/transport overhead is included. For congestion/fairness, preserve offered load, buffering/backpressure, arbitration, and observation window. For collective completion, distinguish application scheduling from network traffic and any in-network processing. For resilience, define failure/injection semantics and the expected recovery or bounded failure.

Use user measurements for calibration when available. Label provisional bandwidths, latencies, buffers, seeds, and traffic patterns as assumptions and expose them as parameters. Record omitted mechanisms and ensure the workload can actually exercise the effect under study. Reuse a nearby example only after checking its traffic and completion semantics.

Next: the chosen element overview, [model construction](models.md), and [testing](../development/testing.md).
