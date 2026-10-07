---
{
  "type": "SST Element Profile",
  "title": "cramSim main use cases",
  "description": "Detailed memory transaction and command modeling.",
  "tags": [
    "cramSim",
    "Memory device/controller"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T03:56:04.244922+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cramSim/README",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cramSim/README",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "a685a153bd33b3c802f47e5563a41b054c6d2becff0811847d5a257fd7127405"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cramSim/c_Controller.hpp",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cramSim/c_Controller.hpp",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "efc1d6a0fabe84aed8b771ce35ece126bf6791622af04a77f0da6bb7fa693474"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cramSim/c_DeviceDriver.hpp",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cramSim/c_DeviceDriver.hpp",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "036c5b4ae259614967ede8a6e181193790a6bbffd54f755b6ae48dcf25175739"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cramSim/c_AddressHasher.hpp",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cramSim/c_AddressHasher.hpp",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "2d284728af582f9af8d612d1237ad1f31320baf049e2e5454ce2e035fa24d39a"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cramSim/tests/testsuite_default_cramSim.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cramSim/tests/testsuite_default_cramSim.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "4a13f91e5a2dfb9ed4ef932150f70b5d347de912041be0b193e38e20fc421b4e"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/cramSimBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/cramSimBackend.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "9b7675aff508bdf7af3709ddd1941540083e9ed37ca184643d55ea25e32cdf5a"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cramSim/tests/ariel_cramsim.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cramSim/tests/ariel_cramsim.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "2870b0024d7217c6fddb93ea11b940a9d563472dcf4369b8eb9c2074253074ea"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cramSim/c_MemhBridge.hpp",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cramSim/c_MemhBridge.hpp",
      "x-sha256": "2ac1b0b443d5008533102cfa1b1d2b064381671706fa716c162865007b9bdd29",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/cramSimBackend.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/cramSimBackend.cc",
      "x-sha256": "2b02ab950bbfd781c3e3e1a2a74add0212660d9b3f3439b11114b228be07e478",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "cramSim",
  "x-role": "Memory device/controller",
  "x-coverage": "use-case-profile"
}
---

# cramSim: main use cases

Role: **Memory device/controller**. Detailed memory transaction and command modeling.

## Use it for

- Explore address mapping, transaction/command scheduling, and DRAM device timing.
- Compare synthetic or trace-driven memory traffic through controller/device configurations.

## Boundaries and prerequisites

The README includes historical standalone build instructions; use the current SST build system. Device/configuration choice governs supported timing detail. For a memHierarchy consumer, use its `memHierarchy.cramsim` backend and the bridge/controller wiring in `tests/ariel_cramsim.py`: MemController, `memHierarchy.cramsim` (`cramsim_link`, with `cube_link` accepted as a fallback port name), `cramSim.c_MemhBridge` (`cpuLink`/`memLink`), then `c_Controller` (`txngenLink`); the controller does not directly accept StandardMem requests. That example also fills a `DeviceController` slot with `cramSim.c_DeviceController`, which the controller does not declare and no registration provides (the declared slot is `DeviceDriver`), and it needs a `./stream` binary with Ariel/Pin.

## Common companions

[memHierarchy](../memHierarchy/use-cases.md), [miranda](../miranda/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/cramSim/`. Read these selectively and verify ELI names against current source.

- `README`
- `c_Controller.hpp`
- `c_DeviceDriver.hpp`
- `c_AddressHasher.hpp`

## Validation starting point

Check transaction completions, legal command timing, address mapping, and the selected cramSim configuration/regression. Every native case passes on a `Simulation is complete` message whenever its reference diff fails, and the suite's own comment says that diff always fails; the suite also downloads VeriMem traces from SST-downloads in `setUpClass` and skips when offline. So also check the requested completion count and whether outstanding work was drained.

Native runner suites:

- `tests/testsuite_default_cramSim.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/ariel_cramsim.py`
- `tests/test_multilanes_4lane.py`

Use `python3 tools/sst_tools.py plan-tests --target cramSim` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
