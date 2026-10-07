---
{
  "type": "SST Element Profile",
  "title": "thornhill main use cases",
  "description": "Detailed compute callbacks and memory-heap integration.",
  "tags": [
    "thornhill",
    "Compute/support library"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:59.907078+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/thornhill/detailedCompute.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/thornhill/detailedCompute.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "f4ff54e77127fbf8938d34b36611f7704566533c6144dbaefe19e6652f3d4a67"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/thornhill/singleThread.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/thornhill/singleThread.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "8be04c8b51016809c928c3078fe3e2c57a366fbe6cd204929ca5ffc6e2e88aa4"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/thornhill/memoryHeap.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/thornhill/memoryHeap.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "00c609391b5034c707c143e2f2dc720ff4d8fd76a07e66d17f01d15bea2eb39a"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/thornhill/memoryHeapLink.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/thornhill/memoryHeapLink.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "8660feeba62935204b62be5356a5977679bd450da89ee776dbd9aa567ab4e44e"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/thornhill/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/thornhill/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "a4c20fc1f61db6086f71fea9b94f882335538afee5d7190c2cacf8d037282158"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/thornhill/singleThread.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/thornhill/singleThread.cc",
      "x-sha256": "3a3b184b824dec98f51fc7268966e348bfc0282008d0733d303ed149406418a2",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/test/EmberEP.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/test/EmberEP.py",
      "x-sha256": "2e602eaeacd4180e8cd45f0fec8ea124fc1baeda899aaf834b509bab1587732b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/test/defaultParams.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/test/defaultParams.py",
      "x-sha256": "c53f3ee57a878accf9f00e3e2e3f9df772fe8ac05d9ddac1b95de6e828392f5a",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "thornhill",
  "x-role": "Compute/support library",
  "x-coverage": "use-case-profile"
}
---

# thornhill: main use cases

Role: **Compute/support library**. Detailed compute callbacks and memory-heap integration.

## Use it for

- Connect workload/runtime compute requests to a supported detailed compute model.
- Use memory-heap allocation/link helpers in compatible consumer stacks.

## Boundaries and prerequisites

This is support infrastructure used by other elements, not a general CPU architecture. Inspect callback and completion contracts and the exact consumer connection. `thornhill.SingleThread` asserts that its `detailed0` port is connected and exchanges Miranda request/response events, so its peer must consume Miranda events; `thornhill.MemoryHeapLink` asserts its `memoryHeap` port, and `MemoryHeap` ports are `detailed%d`.

## Common companions

[ember](../ember/use-cases.md), [firefly](../firefly/use-cases.md), [hermes](../hermes/use-cases.md), [miranda](../miranda/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/thornhill/`. Read these selectively and verify ELI names against current source.

- `detailedCompute.h`
- `singleThread.h`
- `memoryHeap.h`
- `memoryHeapLink.h`

## Validation starting point

Validate start/completion callbacks and heap behavior through the actual consumer; no standalone Thornhill suite exists here.

No runner suite lives under this element; Ember's suites load `thornhill.SingleThread`/`MemoryHeapLink`/`MemoryHeap` through `test/EmberEP.py` and `defaultParams.py`. Run those when changing it, and report any remaining coverage gap explicitly.

Use `python3 tools/sst_tools.py plan-tests --target thornhill` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
