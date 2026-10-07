---
{
  "type": "SST Guide",
  "title": "Extend Carcosa injection",
  "description": "Keep fault policy distinct from placement and event interception.",
  "tags": [
    "carcosa",
    "extension-points"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:08:24.151960+00:00"
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
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/components/faultInjManagerAPI.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/components/faultInjManagerAPI.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "e3020341b5cebcf9180f87c3011f47d6e847bdb0bcf9e048d769ab38f43b91c2"
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
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/portModule.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/portModule.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "284ef4c28362ccc7fbe274cb2efd36ee52e5e127e618d5c46f045e97301054d2"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/injectors/faultInjectorBase.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/injectors/faultInjectorBase.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "cd712be8b217f479bc318ace9d92a28b6b1a5cf5c605f2a577048e47ec362b6b"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/faultlogic/randomDropFault.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/faultlogic/randomDropFault.cc",
      "x-sha256": "928ce9f9e330a0a87ca40f98bd7eebeeb9dc81aa4faf04f0e9489d523b56cb94",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/injectors/faultInjectorMemH.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/injectors/faultInjectorMemH.cc",
      "x-sha256": "79bd3d7fd6ef353f79c39349d34c755f8d203b9c0ab07a3f02f9a5963e2603d4",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/link.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/link.cc",
      "x-sha256": "61a922da0a6e798432b7f6ba15c41c3003278e3018f3cde1359005610fbfb0f8",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/ssthandler.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/ssthandler.h",
      "x-sha256": "0f07886ab2b441083231118d548239535806371c57c85d5dea3658a6ecc84788",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    }
  ]
}
---

# Extend Carcosa injection

Choose `faultlogic/` for a new fault transformation and `injectors/` for placement/filtering/interception behavior. Start from the closest concrete injector, then inspect `FaultInjectorBase` and `FaultBase`. Derived injector constructors must call `setValidInstallation` with supported send/receive installation modes, as documented in the base.

The current parser accepts only `install_direction="Send"` or `"Receive"`; the ELI text also advertises `"Both"`, but that value becomes `Invalid` and fails. `SEND_RECEIVE_VALID` means either direction may be selected, not simultaneous installation. Check implementation when selecting modes.

Trace `eventSent`, `interceptHandler`, event replacement, cancellation, and ownership end to end. Core requires canceled events to be deleted; on the receive path also null the pointer. Carcosa's `cancelDelivery()` sets only the cancel flag, so the fault transformation must perform disposal. A replacement event must copy delivery information before the original is deleted. Two hazards exist in the current code: `RandomDropFault::faultLogic` deletes the event without nulling the reference, so on a Send installation core, which skips queuing only when the pointer is null, inserts a freed event, and on Receive the pointer is left dangling after cancellation; and `cancel_` is bound only inside `interceptHandler`, so calling `cancelDelivery()` from a Send-path fault dereferences an unset pointer, while `SST_SER(cancel_)` checkpoints a pointer to a stack variable. `FaultInjectorMemH` selects faults by `faultType` (`stuckAt`, `randomFlip`, `randomDrop`, `corruptMemRegion`; `custom` fatals), accepts the legacy `installDirection` key, and defaults `injection_probability` to 0.5. Keep random seeds, injection windows, address/bit selection, and repeat/overlap semantics reproducible.

Hali coordination and fault manager behavior live in `components/`; inspect `FaultInjManagerAPI` before changing highlink/lowlink transformations. Preserve relevant serialization state and update `Makefile.am` for new implementations. Validate with both an unaffected baseline and a targeted fault oracle; follow [validation](validation.md).
