---
{
  "type": "SST Element Profile",
  "title": "hermes main use cases",
  "description": "Shared communication and service interfaces.",
  "tags": [
    "hermes",
    "API/support library"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:59.628285+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/hermes/hermes.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/hermes/hermes.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "189a0006b4544dc5b7e08cc24a3ce5f4039f61e6afa40a0d144b26df84f16900"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/hermes/msgapi.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/hermes/msgapi.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "741e878fe318bbc90bbef60a0e69a6ff1f0a987f00c44a2d1413c13d042a4fa0"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/hermes/shmemapi.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/hermes/shmemapi.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "0bc6afe689463e9abbeeee7a53b73386a2034d0435f67233509687ae472bf2a7"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/hermes/networkIOapi.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/hermes/networkIOapi.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "9fb80f0dacb6217f59de57321faa98f787b3d0279410672cc5446352c7a3eca7"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/hermes/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/hermes/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "54176746b9b61530e45e1a69ffa713e843a56d76673631e982efffd441b15aff"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/test/emberLoad.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/test/emberLoad.py",
      "x-sha256": "162a44de6f921e5fddc13f0a103d2eb53e2045a42ae41e061630cdfe1ad5a79d",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "hermes",
  "x-role": "API/support library",
  "x-coverage": "use-case-profile"
}
---

# hermes: main use cases

Role: **API/support library**. Shared communication and service interfaces.

## Use it for

- Implement or consume message-passing, SHMEM, and network-storage read/write APIs.
- Connect workload generators to compatible OS/protocol implementations without hard-coding their concrete classes.

## Boundaries and prerequisites

Hermes is primarily interface/support code, not a standalone router or workload. Unimplemented base methods are `assert(0)` (no-ops under `NDEBUG`), and `OS::getDetailedCompute()`/`getMemHeapLink()` return null by default, so consumers must null-check. The library registers only API types, so `sst-info hermes` reports nothing.

## Common companions

[ember](../ember/use-cases.md), [firefly](../firefly/use-cases.md), [thornhill](../thornhill/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/hermes/`. Read these selectively and verify ELI names against current source.

- `hermes.h`
- `msgapi.h`
- `shmemapi.h`
- `networkIOapi.h`

## Validation starting point

Validate the changed interface through Ember/Firefly consumers, including callbacks and completion behavior; no standalone Hermes suite exists here.

No runner suite lives under this element; Ember's suites exercise it through the Firefly implementations loaded by `test/emberLoad.py`. Run those when changing it, and report any remaining coverage gap explicitly.

Use `python3 tools/sst_tools.py plan-tests --target hermes` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
