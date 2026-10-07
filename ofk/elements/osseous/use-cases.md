---
{
  "type": "SST Element Profile",
  "title": "osseous main use cases",
  "description": "External RTL-model component integration.",
  "tags": [
    "osseous",
    "RTL integration/template"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T19:00:11.373167+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/osseous/README.md",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/osseous/README.md",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "21c44cb13597619bc23641bf2e6b2f6bd80ed18b2623441028caaeed75368dd3"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/osseous/rtlcomponent.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/osseous/rtlcomponent.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "09ef7383e400e635835fc97f0e09c24ef737248f38f62cd1427d43896f419eb6"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/osseous/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/osseous/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "2a2c58455b4dcd983d2fb6d8ecc9223c4f7ce42c81c258b5ae6183090ee5284c"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/osseous/tests/runstream.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/osseous/tests/runstream.py",
      "x-sha256": "916f71de0f6ed8e54e4258da628273408b44c0f9679b969804612396a8853fd5",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/osseous/rtlcomponent.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/osseous/rtlcomponent.cc",
      "x-sha256": "967bf484c0049475e78a84b276a7a7bb42493af7e411f3c453ed829d46c41324",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/osseous/rtlmemmgr_simple.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/osseous/rtlmemmgr_simple.h",
      "x-sha256": "a1a51915e20e8d825059c70f2ee1ad3e1f5ff9068b77345ee90f437124a533e6",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "osseous",
  "x-role": "RTL integration/template",
  "x-coverage": "use-case-profile"
}
---

# osseous: main use cases

Role: **RTL integration/template**. External RTL-model component integration.

## Use it for

- Adapt the generic RTL template to a generated dynamically loadable component.
- Exercise the supplied vector shift-register integration and CPU-side interaction.

## Boundaries and prerequisites

The README describes an ERAS/template flow and a concrete generated example. The checked header registers `rtlcomponent.Rtlmodel`, so the directory name `osseous` is not its ELI component name. Required C-model/generated artifacts and the demonstrated Ariel/Pin frontend must be available (the constructor asserts its Ariel link); adapt that interface explicitly for another consumer. The library builds as `librtlcomponent`, so `sst-info osseous` finds nothing, and `ExecFreq` and `maxCycles` must be supplied because the constructor fatals when either is absent despite documented defaults.

## Common companions

[ariel](../ariel/use-cases.md), [memHierarchy](../memHierarchy/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/osseous/`. Read these selectively and verify ELI names against current source.

- `README.md`
- `rtlcomponent.h`

## Validation starting point

Compare known RTL/example outputs and interface transactions with the source testbench; no native runner suite exists here. `runstream.py` drives the testbench through `ariel.ariel`, so it needs a Pin-capable host, which an ARM64 macOS machine is not, and `tests/Makefile` uses GNU `-Wl,-rpath=` syntax; neither ran in the October 7, 2026 pass.

No native runner suites were found under `test/` or `tests/` in this snapshot. Validate standalone configurations or the consuming integration; report absent runtime coverage explicitly.

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/runstream.py`

As checked in, `runstream.py` requests `rtlaximodel.MemoryManagerSimple`, which is not registered; the manager is `rtl.MemoryManagerSimple` (also the constructor default), so fix that line or drop the `setSubComponent` call.

Use `python3 tools/sst_tools.py plan-tests --target osseous` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
