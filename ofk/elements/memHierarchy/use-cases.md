---
{
  "type": "SST Element Profile",
  "title": "memHierarchy main use cases",
  "description": "Caches, coherence, controllers, and memory interfaces.",
  "tags": [
    "memHierarchy",
    "Cache/memory system"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T08:57:15.378178+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/cacheController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/cacheController.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "441c5e2f7f2a7a43121573eca67bec3eba3fd30d4dd3b44363227f4c10027006"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memoryController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memoryController.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "252967f0759b504d26596bb3f77f8cb091464c78fbe24400d7362d500f4ed3a3"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-1core-1level.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-1core-1level.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "4c3faf5b97b155c781e41f14c948a3e4b2eea3acecd183f75b5d2363c6552c55"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_coherence.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_coherence.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "a4910161dc9d05be091809338f6e9d32c60e70ba01bd979d790611a4ddedff88"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_weekly_memHierarchy_examples.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_weekly_memHierarchy_examples.py",
      "x-sha256": "1a9b0bc272e85a74570816e0b03c85cbc2a05798136299a95e65fe638f544385",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHA.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHA.py",
      "x-sha256": "94ebfdff60f7fb4f055dc1e5f5711de9ddf7f3ea01675167a3bfa233d562d786",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHSieve.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHSieve.py",
      "x-sha256": "bf317fe5831a30a8d74dfd126b1fa17b2d21cfebc1e03717e269ee89a32a7cca",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "memHierarchy",
  "x-role": "Cache/memory system",
  "x-coverage": "detailed"
}
---

# memHierarchy: main use cases

Role: **Cache/memory system**. Caches, coherence, controllers, and memory interfaces.

## Use it for

- Assemble cache hierarchies and compare documented replacement/prefetch/coherence behavior.
- Connect CPU/request sources to memory controllers/backends and distributed memory networks.

## Boundaries and prerequisites

Cache, coherence, transport, and backend timing are distinct layers. Backend choice and workload fidelity constrain conclusions about real hardware.

## Common companions

[vanadis](../vanadis/use-cases.md), [miranda](../miranda/use-cases.md), [cassini](../cassini/use-cases.md), [merlin](../merlin/use-cases.md), [kingsley](../kingsley/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/memHierarchy/`. Read these selectively and verify ELI names against current source.

- `cacheController.h`
- `memoryController.h`
- `examples/example-1core-1level.py`

## Validation starting point

Check data correctness, completions, coherence/conflicting accesses where relevant, and targeted cache/controller/backing-store regressions.

Native runner suites:

- `tests/testsuite_default_memHierarchy_coherence.py`
- `tests/testsuite_default_memHierarchy_memHA.py`
- `tests/testsuite_default_memHierarchy_memHSieve.py`
- `tests/testsuite_default_memHierarchy_memory.py`

Fifteen suites exist (five `default_*`, four `openMP_*`, five `sweep_*`, one `weekly_*`); use the planner to discover them. `testsuite_weekly_memHierarchy_examples.py` runs every `examples/*.py` with only a completion/no-FATAL check; `memHSieve` skips without Pin, and `memHA` skips cases whose GOBLIN_HMCSIM/Ramulator backends are absent.

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `examples/example-1core-1level.py`
- `examples/example-1core-3level.py`

Use `python3 tools/sst_tools.py plan-tests --target memHierarchy` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). For implementation detail read [overview](overview.md), [backends](backends.md), [systems](systems.md), [extension points](extension-points.md), and [validation](validation.md) as needed.
