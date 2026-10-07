---
{
  "type": "SST Element Profile",
  "title": "carcosa main use cases",
  "description": "Inject faults and coordinate interception with CPU/memory models.",
  "tags": [
    "carcosa",
    "Fault injection"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:09:02.716742+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/injectors/faultInjectorBase.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/injectors/faultInjectorBase.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "35b6d6b2057f3dbc51f857c0d4178a895cd91aaa1463f27f8326d4e814bbb04c"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/components/hali.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/components/hali.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "55a75be9b3d3448851e24ad4dc1e68383be7eb94a826a7ef8a4781ccb690202a"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/tests/testcarcosaPingPong.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/tests/testcarcosaPingPong.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "b4e60dbd3723c7c3a06317ebbe663d5056747b7957e00bac1c30181c2f172906"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "a47fe08eeb343d10ea6284f542d586bf9b011f8d09bd50821f886a7a63e3db2e"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/injectors/faultInjectorMemH.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/injectors/faultInjectorMemH.h",
      "x-sha256": "4ed1efdef106273c9dbbc3aac37ce5df18d8713c6a88f30530c0e4d8d98f09a7",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/tests/testRandomFlip.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/tests/testRandomFlip.py",
      "x-sha256": "3c03256f4cfcb6712d6a14727ef9e4995da67d1a1e06d336faa5eb57921fa4ec",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "carcosa",
  "x-role": "Fault injection",
  "x-coverage": "detailed"
}
---

# carcosa: main use cases

Role: **Fault injection**. Inject faults and coordinate interception with CPU/memory models.

## Use it for

- Study reproducible flips, drops, stuck-at faults, or memory corruption.
- Coordinate Hali interception/MMIO behavior with Vanadis and memory components.

## Boundaries and prerequisites

Concrete port/event hooks determine supported fault placement. Injector ELI names are `carcosa.RandomFlipFaultInjector`, `RandomDropFaultInjector`, `DropFlipFaultInjector`, `StuckAtFaultInjector`, `CorruptMemFaultInjector`, and the lowercase `carcosa.faultInjectorMemH`; components include `Hali`, `SensorComponent`, `CarcosaCPU`, and `CarcosaMemCtrl`, with `FaultInjManager` as a subcomponent. Some standalone examples hard-code binary/ISA paths (`testRandomFlip.py`, `testRandomDrop.py`, and `testStuckAtBasic.py` point at `../../vanadis/tests/small/basic-math/sqrt-double/riscv64/sqrt-double`, so they must run from `carcosa/tests` with the Vanadis test binaries present); no native runner suites exist in this checkout. `sst-info carcosa` can fail to load the library standalone on macOS because it references memHierarchy's convertor type without linking it; a simulation that loads memHierarchy first runs normally. The recorded devel smoke failed the Hali manager-registration assertion despite simulation completion; use the [validation guide](validation.md) before relying on coordinated interception.

## Common companions

[vanadis](../vanadis/use-cases.md), [memHierarchy](../memHierarchy/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/carcosa/`. Read these selectively and verify ELI names against current source.

- `injectors/faultInjectorBase.h`
- `components/hali.h`
- `tests/testcarcosaPingPong.py`

## Validation starting point

Use a no-fault baseline and explicit data/event oracle, including overlapping faults where relevant.

No native runner suites were found under `test/` or `tests/` in this snapshot. Validate standalone configurations or the consuming integration; report absent runtime coverage explicitly.

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/testCorruptMemBasic.py`
- `tests/testCorruptMemDouble.py`

Use `python3 tools/sst_tools.py plan-tests --target carcosa` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). For implementation detail read [overview](overview.md), [extension points](extension-points.md), and [validation](validation.md) as needed.
