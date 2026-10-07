---
{
  "type": "SST Guide",
  "title": "Carcosa fault-injection selection",
  "description": "Distinguish port interception, fault logic, and Hali coordination.",
  "tags": [
    "carcosa",
    "overview"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:08:23.881342+00:00"
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
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/faultlogic/faultBase.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/faultlogic/faultBase.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "538bfd752ece60714b310e120997b7c01c90daca780841273434f238ba3019e6"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/components/hali.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/components/hali.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "55a75be9b3d3448851e24ad4dc1e68383be7eb94a826a7ef8a4781ccb690202a"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/tests/testRandomFlip.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/tests/testRandomFlip.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "3c03256f4cfcb6712d6a14727ef9e4995da67d1a1e06d336faa5eb57921fa4ec"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/tests/testcarcosaPingPong.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/tests/testcarcosaPingPong.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "b4e60dbd3723c7c3a06317ebbe663d5056747b7957e00bac1c30181c2f172906"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/injectors/faultInjectorMemH.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/injectors/faultInjectorMemH.h",
      "x-sha256": "4ed1efdef106273c9dbbc3aac37ce5df18d8713c6a88f30530c0e4d8d98f09a7",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---

# Carcosa fault-injection selection

Carcosa provides fault-injection machinery and coordinating components. `injectors/faultInjectorBase.h` derives from `SST::PortModule`; `faultlogic/faultBase.h` contains fault behavior. Concrete injectors cover flips, drops, stuck-at faults, and memory corruption; the memHierarchy-typed injector registers with a lowercase name, `carcosa.faultInjectorMemH`, unlike the others. `components/hali.h` provides interception/coordination, with a fault manager API and agents.

`tests/testRandomFlip.py` attaches `carcosa.RandomFlipFaultInjector` using `addPortModule` on a memory-controller port. These configurations commonly combine [Vanadis](../vanadis/overview.md) and [memHierarchy](../memHierarchy/overview.md); fault placement must match the intended event and data path.

This checkout has standalone configurations rather than `testsuite_*.py` suites. Some examples hard-code executable paths or overwrite ISA settings; inspect and adapt them before running. Use `testcarcosaPingPong.py` for documented two-core Hali/MMIO coordination setup.

Next: [extension points](extension-points.md), [validation](validation.md).
