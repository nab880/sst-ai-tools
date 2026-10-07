---
{
  "type": "SST Guide",
  "title": "Validate Carcosa fault behavior",
  "description": "Run standalone configurations with explicit prerequisites and fault oracles.",
  "tags": [
    "carcosa",
    "validation"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T19:00:10.073567+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/tests/testcarcosaPingPong.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/tests/testcarcosaPingPong.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "b4e60dbd3723c7c3a06317ebbe663d5056747b7957e00bac1c30181c2f172906"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/tests/testStuckAtBasic.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/tests/testStuckAtBasic.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "64143ab10c914d9b122b02e02381fdbeb87ab28ac00096fea879cf5afa7320d7"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/tests/testRandomFlip.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/tests/testRandomFlip.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "3c03256f4cfcb6712d6a14727ef9e4995da67d1a1e06d336faa5eb57921fa4ec"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/components/hali.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/components/hali.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "320ed19c8efd5b31221ac1a6a9736b37f76053786af6e1204ee53fdf2411dd92"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/components/faultInjManager.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/components/faultInjManager.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "bde034f3fc2c91bde53843c2f9ce824ffabfc62147dd9d83332aa203a02ba931"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/injectors/faultInjectorMemH.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/injectors/faultInjectorMemH.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "79bd3d7fd6ef353f79c39349d34c755f8d203b9c0ab07a3f02f9a5963e2603d4"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/portModule.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/portModule.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "284ef4c28362ccc7fbe274cb2efd36ee52e5e127e618d5c46f045e97301054d2"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/injectors/faultInjectorBase.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/injectors/faultInjectorBase.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "cd712be8b217f479bc318ace9d92a28b6b1a5cf5c605f2a577048e47ec362b6b"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/faultlogic/stuckAtFault.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/faultlogic/stuckAtFault.cc",
      "x-sha256": "f9f468959d00adc5fa15be37a9e03412dd0a89af18982760a4d810e22f640694",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/faultlogic/corruptMemFault.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/faultlogic/corruptMemFault.cc",
      "x-sha256": "5d11d699047d31f7d6b41a4a956c8b77ce2cf3f9542a8600338163e748696e3b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---

# Validate Carcosa fault behavior

There are no native `testsuite_*.py` files in this checkout's `tests/`. The planner must report standalone configurations instead of presenting an empty runner discovery as successful coverage.

Examples include `testRandomFlip.py`, `testRandomDrop.py`, `testStuckAtBasic.py`, overlap/multiple stuck-at cases, and corruption cases. Inspect binary paths, ISA overrides, fault parameters, and working-directory assumptions before execution. Use a nonzero explicit seed and a no-fault baseline, then verify the intended bit/address/event effect and unaffected behavior. In `FaultInjectorBase`, zero skips the explicit RNG seed call. Simulation completion alone does not prove a fault occurred correctly.

On October 7, 2026 all seven shipped configurations ran on the recorded devel install with the default RISC-V `sqrt-double` binary. The corruption, drop, flip, and overlap cases complete at 10.5924 ms with program output identical to Vanadis's gold; the two stuck-at cases abort during construction with `bitset string ctor has invalid argument` because `StuckAtFault::convertString` extracts each mask with `>>`, so the shipped `"4D88, 3, 11110000, 00001111"` leaves a trailing comma on the mask token, while separators written as ` , ` run. None of these configurations can change that program's result: they target `0x4D88` and its lowest section starts at `0x10120`, so identical output is expected and only completion is being checked. The injectors register no statistics and their debug prints compile out without `__SST_DEBUG_OUTPUT__`, so an injection oracle needs an address the program actually touches.

`testcarcosaPingPong.py` documents cross-compiling `pingpong.c` with the local `hyades.h` include and running two Vanadis cores. Program output goes to per-process `stdout-100`/`stdout-101` and corresponding stderr files. Check roles, iteration counts, and coordination as well as simulator output.

For overlap faults test combined semantics; for dropped events test expected recovery or intentionally bounded failure. Build an executable assertion around a selected configuration or add a runner suite if that is part of the requested change. See [test planning](../../development/testing.md).


## Registration ordering on devel

The local runtime check found injector RegisterPM messages arriving after Hali setup, without the expected manager-consumption records. Assert both injector resolution and manager consumption; successful simulator completion is insufficient. `PortModule` has no `init` lifecycle callback, so `FaultInjectorMemH::init(unsigned)` is not a core-invoked override. Its first eligible event can resolve registries and enqueue registration after `Hali::setup` has already drained manager messages. `FaultInjectorMemH` pushes RegisterPM only from `executeFaults`, which runs only when `doInjection()` fires under `injection_probability` (default 0.5), so registration timing is nondeterministic without a seed and never happens at probability 0. `Hali` calls `processMessagesFromPMs()` only when a `faultInjManager` subcomponent is loaded, and the manager records `managedPMIds_` silently unless `debugManagerLogic` is set, so the consumption record requires that flag. See repository-root `RUNTIME_VALIDATION.md` for the failed assertion when that evidence is installed; fault-data correctness remains a separate oracle.
