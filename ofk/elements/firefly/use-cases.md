---
{
  "type": "SST Element Profile",
  "title": "firefly main use cases",
  "description": "Communication protocol and NIC behavior for workload integration.",
  "tags": [
    "firefly",
    "Protocol/NIC/runtime"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:59.224327+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/firefly/nic.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/firefly/nic.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "f596e734fd650e7e78bec27ed65ca753c60dc568d4fb7c1d47ea6fa95faa6afc"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/firefly/hadesMP.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/firefly/hadesMP.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "640bd26f68e979972e91f5162f6a408511cdab1fb3324ec47409b6d41fbd89e5"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/firefly/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/firefly/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "40a34de05f54fb12fd5deceb7555c9c6a8337412239e4cfadcacd362e807ae90"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/firefly/hades.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/firefly/hades.cc",
      "x-sha256": "ff4b26bf9875fe0210f60223f226227fe22ca9e539a4b8afe976440f215b10cd",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/test/EmberEP.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/test/EmberEP.py",
      "x-sha256": "2e602eaeacd4180e8cd45f0fec8ea124fc1baeda899aaf834b509bab1587732b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/test/defaultParams.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/test/defaultParams.py",
      "x-sha256": "c53f3ee57a878accf9f00e3e2e3f9df772fe8ac05d9ddac1b95de6e828392f5a",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "firefly",
  "x-role": "Protocol/NIC/runtime",
  "x-coverage": "use-case-profile"
}
---

# firefly: main use cases

Role: **Protocol/NIC/runtime**. Communication protocol and NIC behavior for workload integration.

## Use it for

- Model message-passing/SHMEM operations behind Hermes interfaces.
- Study host/protocol/NIC overhead, DMA/memory interaction, and network integration independently of topology.

## Boundaries and prerequisites

ELI names are `firefly.nic` and `firefly.hadesMP` (implementing `SST::Hermes::MP::Interface`). A common stack uses Ember and Merlin, but inspect the actual configuration; Thornhill hooks load only when `detailedCompute.name`/`memoryHeapLink.name` are set. Protocol timing is not interchangeable with link/router timing.

## Common companions

[ember](../ember/use-cases.md), [hermes](../hermes/use-cases.md), [merlin](../merlin/use-cases.md), [thornhill](../thornhill/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/firefly/`. Read these selectively and verify ELI names against current source.

- `nic.h`
- `hadesMP.h`
- `Makefile.am`

## Validation starting point

Check matching and completion, request ownership, host cost attribution, and a neighboring Firefly/Ember integration case.

No runner suite lives under this element; its runtime coverage comes from Ember's suites, whose `test/emberLoad.py`, `EmberEP.py`, and `defaultParams.py` instantiate `firefly.nic`, `firefly.hades`, and `firefly.hadesMP`/`hadesSHMEM`/`hadesMisc`. Run those when changing it, and report any remaining coverage gap explicitly.

Use `python3 tools/sst_tools.py plan-tests --target firefly` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
