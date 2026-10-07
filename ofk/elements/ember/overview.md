---
{
  "type": "SST Guide",
  "title": "Ember workload selection",
  "description": "Select communication motifs separately from network and transport models.",
  "tags": [
    "ember",
    "overview"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T01:55:08.144181+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/emberengine.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/emberengine.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "0c179653219c018afa5a97d0f74cc01021ee53ccef95618459a1feba4ad9413d"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/embergen.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/embergen.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "9b0abe7315a71633cbfb893d587197c23ecf8fb2b090e39bd856d55c5cc7b67b"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/mpi/embermpigen.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/mpi/embermpigen.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "3dce203c8fbada9f8ec23eee0aa1a649ec4e4e4f8a5f7f6bd0db73dd8ec11319"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/test/emberLoad.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/test/emberLoad.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "162a44de6f921e5fddc13f0a103d2eb53e2045a42ae41e061630cdfe1ad5a79d"
    }
  ]
}
---

# Ember workload selection

Ember generates communication/computation workloads as motifs executed by `EmberEngine`; it does not define network topology. Choose it for prescribed MPI-style or SHMEM communication patterns. Its common assembly uses Hermes/Firefly services over a Merlin network; inspect the chosen configuration rather than assuming every motif uses the same transport.

| Need | Entry point |
|---|---|
| Existing motif parameters | `mpi/motifs/emberpingpong.h` and adjacent motif ELI |
| Motif generation | `embergen.h`, `mpi/embermpigen.h` |
| Event scheduling/execution | `emberengine.h`, `emberevent.h` |
| Workload/network assembly | `test/emberLoad.py`, `pyember.py` |
| SHMEM behavior | `shmem/` |

Change a motif for a new communication schedule; change [Merlin](../merlin/overview.md) for network routing/datapath behavior. For application execution through Mercury, consult [Mercury](../mercury/overview.md). Start from the configuration used by a matching test rather than reconstructing the entire stack.

Next: [extension points](extension-points.md), [validation](validation.md).
