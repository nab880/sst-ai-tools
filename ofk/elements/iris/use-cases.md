---
{
  "type": "SST Element Profile",
  "title": "iris main use cases",
  "description": "SUMI collective/transport and PMI/libfabric support.",
  "tags": [
    "iris",
    "Communication support library"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:05:36.122843+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "ce83626e0d2a4b4c6a6ad281f668e09c7f087830be7765debda4a0e8f587080f"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/sumi/sim_transport.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/sumi/sim_transport.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "68777bfa01d8a5d32a8c278b08016695a27488ddeaebb2280a5fa2a194657463"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/sumi/transport.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/sumi/transport.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "b2be97dfeb3eb5fa1f0c91540fbbb22a1eeb7b8e52daabf0265a33d808c8785a"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/sumi/allreduce.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/sumi/allreduce.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "902c5df4fcdac8b0e0bf0808740c05ed451b63c6e32fff071b25460fdf248836"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/sumi/sim_transport.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/sumi/sim_transport.cc",
      "x-sha256": "cb48a9e1b5fb5189c59651f6f9cf4ca9bcc95eba87a2176eb5802399b37a4ff7",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/sumi/collective_registry.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/sumi/collective_registry.cc",
      "x-sha256": "cdbc93c3ea160e7ff22b346bfa03502d138191b47a5089581fdc783186dfab81",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "iris",
  "x-role": "Communication support library",
  "x-coverage": "use-case-profile"
}
---

# iris: main use cases

Role: **Communication support library**. SUMI collective/transport and PMI/libfabric support.

## Use it for

- Study or extend SUMI collective/transport behavior in the Mercury-related stack.
- Inspect application communication support and PMI/libfabric integration boundaries.

## Boundaries and prerequisites

This directory supplies libraries and interfaces rather than a drop-in topology component: its build products are the `ext` libraries `libsumi`, `libpmi`, and `libfabric` under `lib/sst-elements-library/ext`, not an ELI element library, so `sst-info` lists no `iris` entries. ELI names are `macro.libfabric` for the fabric transport, `macro.null`/`macro.pattern` for QoS analyses, and `iris.<op>.<alg>` for collectives; `Transport::get()` resolves the application library named `sumi`. Determine the exact consumer and supported API implementation.

## Common companions

[mercury](../mercury/use-cases.md), [mask-mpi](../mask-mpi/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/iris/`. Read these selectively and verify ELI names against current source.

- `Makefile.am`
- `sumi/sim_transport.h`
- `sumi/transport.h`
- `sumi/allreduce.h`

## Validation starting point

Exercise the relevant Mercury/Mask-MPI integration and verify collective results, progress, and rank mapping; no standalone Iris suite exists here.

No native runner suites were found under `test/` or `tests/` in this snapshot. Validate standalone configurations or the consuming integration; report absent runtime coverage explicitly.

Use `python3 tools/sst_tools.py plan-tests --target iris` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.

The adapted MV2 route uses Iris libfabric/PMI beneath Mercury-hosted application execution; see [Mercury, SST-HGCC, and MV2](../mercury/hgcc-mv2.md). The provider name in the checked source is `sstmac`.

## Fabric and collective extension paths

Use [the fabric/provider guide](fabrics.md) to identify the existing `sstmac` provider and implement a new provider contract. Use [the collective guide](collectives.md) for built-in algorithms and registration. Provider identity, runtime transport, physical network topology, and collective policy are distinct decisions.
