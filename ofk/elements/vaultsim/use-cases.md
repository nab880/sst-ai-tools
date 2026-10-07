---
{
  "type": "SST Element Profile",
  "title": "vaultsim main use cases",
  "description": "Fixed-delay memory vaults and logic-layer organization.",
  "tags": [
    "vaultsim",
    "Stacked-memory model"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T03:56:03.858919+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vaultsim/vaultsim.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vaultsim/vaultsim.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "bf25f922d92cc998a2f458a69b19464e41750480aaefdfb506f49350c2167f12"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vaultsim/logicLayer.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vaultsim/logicLayer.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "2ebcb5c001b89bd4a3a32ac88ffce3663de55030d952c6a00191b25a20cac80e"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vaultsim/cpu.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vaultsim/cpu.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "26158404c4493c162e62482ee45ec1b3b545050e3e744e7be5464c69bac73e09"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vaultsim/tests/testsuite_default_VaultSim.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vaultsim/tests/testsuite_default_VaultSim.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "71c28c0f4056b92f47a2ad4eb650c52e949f27705c73ae630df201ff92b79e28"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vaultsim/vaultsim.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vaultsim/vaultsim.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "a2192ae71f90414396f9d07fb604b454f798b1587a87a3600fb9a5c33a20d51e"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/vaultSimBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/vaultSimBackend.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "60c9d0f9361794314fd92b073f93cf7b739e000e6308dcca0cacf065015ffc95"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/vaultSimBackend.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/vaultSimBackend.cc",
      "x-sha256": "6727581e316a8102460ec9784093bf4d4a01761a19e06098218436051786bd7b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vaultsim/tests/sdl1.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vaultsim/tests/sdl1.py",
      "x-sha256": "eeaccc6b84653821833c8b3d3893aaf28e805c10080662282569a1f5e533b88b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHA.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHA.py",
      "x-sha256": "94ebfdff60f7fb4f055dc1e5f5711de9ddf7f3ea01675167a3bfa233d562d786",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "vaultsim",
  "x-role": "Stacked-memory model",
  "x-coverage": "use-case-profile"
}
---

# vaultsim: main use cases

Role: **Stacked-memory model**. Fixed-delay memory vaults and logic-layer organization.

## Use it for

- Explore a stacked-memory system with vault and logic-layer components.
- Study request distribution and bandwidth under supported vault/cube organization.

## Boundaries and prerequisites

The supplied CPU is a simple traffic source. The vault implementation returns custom `MemReqEvent`/`MemRespEvent` transactions after a configured fixed `delay` (default 40 ns), polled on its clock; it is not a bank-command DRAM model. `delay` is read by the implementation but absent from the ELI parameter list, so `sst-info` does not show it, and although the `bus` port text says `MemEvent`, the clock handler fatals on anything except `MemReqEvent`. A memHierarchy consumer needs the `memHierarchy.vaultsim` backend, a `FlagMemBackend` that refuses new requests above 255 outstanding, and its `cube_link` adapter. Data backing and detailed memory timing must be supplied/checked in the surrounding model.

## Common companions

[memHierarchy](../memHierarchy/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/vaultsim/`. Read these selectively and verify ELI names against current source.

- `vaultsim.h`
- `logicLayer.h`
- `cpu.h`

## Validation starting point

Check known address/vault routing, completion counts and bandwidth boundaries, then select the VaultSim suite. It runs only `sdl1` and `sdl2`; `sdl1.py` writes `TestOutput.csv` into the working directory, and `pimExper.py` belongs to no suite and needs Ariel, Merlin, and MemNIC. memHierarchy's memHA suite exercises the backend path in `test_memHA_BackendVaultSim`.

Native runner suites:

- `tests/testsuite_default_VaultSim.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/pimExper.py`
- `tests/sdl1.py`

Use `python3 tools/sst_tools.py plan-tests --target vaultsim` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
