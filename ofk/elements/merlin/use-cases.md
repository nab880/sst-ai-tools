---
{
  "type": "SST Element Profile",
  "title": "merlin main use cases",
  "description": "Configurable routers, topologies, link control, and traffic.",
  "tags": [
    "merlin",
    "Interconnect"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:57.911751+00:00"
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
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/interfaces/linkControl.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/interfaces/linkControl.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "703b8da5b59cc3bcea8197ff03270ce84bbc6cef7ed3900e7eb9667cd9057479"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/tests/testsuite_default_merlin.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/tests/testsuite_default_merlin.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "f2f31edb4736e799e7da720c3a0f629295948ed3d8db9108dfb12b103ced4577"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/trafficgen/trafficgen.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/trafficgen/trafficgen.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "1283e25f9963bd88c232618759deed3e61917142fcbe58c14795fe883b89baff"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/trafficgen/trafficgen.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/trafficgen/trafficgen.cc",
      "x-sha256": "d0b2d8edf1317317afc7a868f4da10403b8a5d61e69141e3914b8ae09ae6fff6",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "merlin",
  "x-role": "Interconnect",
  "x-coverage": "detailed"
}
---

# merlin: main use cases

Role: **Interconnect**. Configurable routers, topologies, link control, and traffic.

## Use it for

- Build node-to-node networks and explore topology/routing choices.
- Study buffering, arbitration, backpressure, endpoint interfaces, and compatible endpoint integration.

## Boundaries and prerequisites

A topology name does not establish protocol fidelity or deadlock freedom. Separate endpoint/workload behavior from routing and router timing. `merlin.trafficgen` supplies finite synthetic traffic without Ember or an application runtime. Its HotSpot pattern inherits the [reproduced discrete-distribution defect](validation.md); validate generated destination bounds before using it for measurements. `PacketDest.Seed` has no effect on the HotSpot or Normal generators: their `seed` replaces the RNG without rebinding the distribution, which keeps seeding from wall-clock time; only Uniform reseeds. The ELI descriptions of `RangeMin`/`RangeMax` are swapped, and the documented `Seed` default `11` is actually `1010101`.

## Common companions

[ember](../ember/use-cases.md), [firefly](../firefly/use-cases.md), [mercury](../mercury/use-cases.md), [memHierarchy](../memHierarchy/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/merlin/`. Read these selectively and verify ELI names against current source.

- `router.h`
- `hr_router/hr_router.h`
- `interfaces/linkControl.h`

## Validation starting point

Check timed/untimed delivery, counts, mapping, finite completion, and stressed routing/credit behavior as appropriate. Anytopo test construction needs NetworkX; PolarFly/PolarStar construction needs SymPy. The native SlimFly Anytopo case is unconditionally skipped for inconsistent results.

Native runner suites:

- `tests/testsuite_default_merlin.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/anytopo_complete_4_test.py`
- `tests/anytopo_cubical_test.py`

Use `python3 tools/sst_tools.py plan-tests --target merlin` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). For implementation detail read [overview](overview.md), [extension points](extension-points.md), and [validation](validation.md) as needed.
