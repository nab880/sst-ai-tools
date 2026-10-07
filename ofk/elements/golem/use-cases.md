---
{
  "type": "SST Element Profile",
  "title": "golem main use cases",
  "description": "Matrix-vector arrays and CPU coprocessor integration.",
  "tags": [
    "golem",
    "Processing using memory"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T19:00:10.610050+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/golem/README.md",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/golem/README.md",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "840bf526b504ecde29101467011a6680bc3f825e484532946fd4d37a35b201e3"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/golem/array/computeArray.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/golem/array/computeArray.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "e1d75a95c0f2658e9c5281d9e991b5083fa4d3afbc8f4eb272c3c4999d1376ba"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/golem/array/mvmFloatArray.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/golem/array/mvmFloatArray.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "ba5c3d79c8e590161c8d47ec69eabca193e76144a2dd572261e4d4c414ac1ea3"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/golem/tests/testsuite_default_golem.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/golem/tests/testsuite_default_golem.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "31e5e22c1d6359e23a064592a524d54b7ab2aa7d2b0a95ffd617d344734a77d6"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/golem/configure.m4",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/golem/configure.m4",
      "x-sha256": "ef6472c8bf8906d6d3e8a1500cf74cf65f4d7feba5d67a9782c78106424d39b5",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/golem/tests/basic_golem.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/golem/tests/basic_golem.py",
      "x-sha256": "93ec88a4d949eb1f5c098b7938c41d04cd1f206b11fdc1d75994b9b7bb7f3e62",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/config/sst_check_numpy.m4",
      "x-repository": "sst-elements",
      "x-path": "config/sst_check_numpy.m4",
      "x-sha256": "4cd69445b615e1a71f215253ca8e2b97d16818b03825bc94478eebf3b532b268",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "golem",
  "x-role": "Processing using memory",
  "x-coverage": "use-case-profile"
}
---

# golem: main use cases

Role: **Processing using memory**. Matrix-vector arrays and CPU coprocessor integration.

## Use it for

- Compare ideal integer/float matrix-vector computation arrays.
- Include analog nonidealities through optional CrossSim and connect arrays to Vanadis via RoCC.

## Boundaries and prerequisites

CrossSim cases need the appropriate Python environment; the README supports using the same Python interpreter as SST core. Ideal arrays are a separate path. The suite adds CrossSim cases only if both the Python package and CrossSim ELI components are found, so an all-pass ideal-array run does not establish CrossSim coverage. Array timing and numerical fidelity need explicit assumptions. On the recorded devel install the components appeared only after reconfiguring elements with numpy importable by `sst-config --PYTHON` (`config/sst_check_numpy.m4` runs that interpreter; `PYTHONPATH` pointing at a `pip install --target` directory holding numpy 2.5.3, scipy 1.18.1, and CrossSim 3.2.1 from GitHub satisfied it for Homebrew Python 3.14 on October 7, 2026). The four CrossSim cases then executed with per-process output identical to `golem.stdout.gold`, but their `sst.stdout.gold` comparisons fail because the busy-wait instruction counts depend on the CrossSim and numpy versions, so those golds are tied to the environment that produced them; the four ideal-array cases pass.

## Common companions

[vanadis](../vanadis/use-cases.md), [memHierarchy](../memHierarchy/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/golem/`. Read these selectively and verify ELI names against current source.

- `README.md`
- `array/computeArray.h`
- `array/mvmFloatArray.h`
- `tests/testsuite_default_golem.py`

## Validation starting point

Check known matrix-vector numerical outputs, single/multiple array cases, and which optional CrossSim implementations are actually registered. The suite skips when ranks or threads exceed one, runs prebuilt riscv64 ELFs under `tests/small/` with `MakeTests = False`, and drives `basic_golem.py` through `GOLEM_ROCC_TYPE`, `GOLEM_ARRAY_TYPE`, `GOLEM_NUM_ARRAYS`, `VANADIS_EXE`, and `VANADIS_ISA`. CrossSim array sources compile only when configure finds numpy, so an absent registration is a build-time outcome.

Native runner suites:

- `tests/testsuite_default_golem.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/basic_golem.py`

Use `python3 tools/sst_tools.py plan-tests --target golem` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
