---
{
  "type": "SST Element Profile",
  "title": "miranda main use cases",
  "description": "Address-generation and memory-access patterns.",
  "tags": [
    "miranda",
    "Synthetic workload"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:00:43.183656+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/miranda/mirandaCPU.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/miranda/mirandaCPU.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "6083b72ffdfdbe41ac58a6c0516b7ea0ca5ab36fe1f1e1abf81276bba3b0ab76"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/miranda/mirandaGenerator.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/miranda/mirandaGenerator.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "8eab30538ffe7660359674c5cb7c35342094812d1f9e83f50a2df2bd0457470e"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/miranda/tests/testsuite_default_miranda.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/miranda/tests/testsuite_default_miranda.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "4fd1d57f8de8e09a74a293302172efeca4c4c255b2ff06a56481e66caab288f4"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/miranda/mirandaCPU.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/miranda/mirandaCPU.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "49d490f909f7b439dc2a9989fa5d5091fc9d88aaf2c3286ead35c1743b45d457"
    }
  ],
  "x-element": "miranda",
  "x-role": "Synthetic workload",
  "x-coverage": "use-case-profile"
}
---

# miranda: main use cases

Role: **Synthetic workload**. Address-generation and memory-access patterns.

## Use it for

- Generate stream, random, stencil, or other supported synthetic memory traffic.
- Isolate memory bandwidth/latency effects with a controlled finite request sequence.

## Boundaries and prerequisites

`miranda.BaseCPU` executes request generators rather than application instructions. Supported access dependencies, reorder lookups, and outstanding limits constrain traffic behavior. The ELI documents `maxmemreqpending`, but the implementation reads only `maxloadmemreqpending`, `maxstorememreqpending`, and `maxcustommemreqpending`. Generators come from the `generator` slot or parameter, both of which register the CPU as primary, or from the `src` port, which does not. Normal generated writes carry zero-filled payloads; use it for access-pattern/timing experiments and provide a separate data oracle for value-sensitive studies.

## Common companions

[memHierarchy](../memHierarchy/use-cases.md), [cassini](../cassini/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/miranda/`. Read these selectively and verify ELI names against current source.

- `mirandaCPU.h`
- `mirandaGenerator.h`

## Validation starting point

Check generated addresses/counts and completions, then compare statistics under a fixed seed/pattern.

Native runner suites:

- `tests/testsuite_default_miranda.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/copybench.py`
- `tests/goblin_singlestream1-trace-map.py`

Use `python3 tools/sst_tools.py plan-tests --target miranda` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
