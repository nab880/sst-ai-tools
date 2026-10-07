---
{
  "type": "SST Element Profile",
  "title": "llyr main use cases",
  "description": "Configurable graph-based dataflow execution.",
  "tags": [
    "llyr",
    "Dataflow accelerator"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T19:00:09.846200+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/llyr/llyr.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/llyr/llyr.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "6b605f85af3b1938c5a80015e0bd2a6ac720d6125413df8da503dc9a6d39437f"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/llyr/mappers/llyrMapper.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/llyr/mappers/llyrMapper.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "01c8191839a6cda029b2cdce15b91867aba274cef2c362c9a577aa4700577bb6"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/llyr/tests/simple_test.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/llyr/tests/simple_test.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "dbe5f1d2a4f3f388628023abf4f58b13c67957471b512c4f6aba58b72f3b5407"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/llyr/tests/testsuite_default_llyr.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/llyr/tests/testsuite_default_llyr.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "c5ce762f79678934376a10d540af511f097da75301188ce4e55cd97db0c7032a"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/llyr/llyr.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/llyr/llyr.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "92f195b043761b7d6bc7769c92dcb8594cc9aca17225b2fda137149da306087c"
    }
  ],
  "x-element": "llyr",
  "x-role": "Dataflow accelerator",
  "x-coverage": "use-case-profile"
}
---

# llyr: main use cases

Role: **Dataflow accelerator**. Configurable graph-based dataflow execution.

## Use it for

- Map an application graph onto a specified hardware connectivity graph.
- Explore processing-element mapping, functional behavior, and load/store interaction.

## Boundaries and prerequisites

Provide the application graph, hardware graph, and any memory-initialization file required by the case. The supplied example selects `llyr.mapper.simple`; an external mapping tool is conditional on mapper choice. The implementation loads the StandardMem interface from the `iface` slot used in `tests/simple_test.py`, although the header documents a `memory` slot; if `iface` is empty, the fallback requests `memHierarchy.memInterface`, which is not registered, so set the slot explicitly. The documented `complex_latency` parameter is read as `complex_latency_`, so the documented name is ignored. `simple_test.py` inputs are working-directory relative, and the component writes `llyr_mapped.dot` there. Follow the implementation and example.

## Common companions

[memHierarchy](../memHierarchy/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/llyr/`. Read these selectively and verify ELI names against current source.

- `llyr.h`
- `mappers/llyrMapper.h`
- `tests/simple_test.py`

## Validation starting point

Check graph outputs, mapping validity, token progress, and memory results using a standalone case. The native suite has an unconditional `skipIf(True, ...)`, so selecting it provides no execution coverage until that upstream test is enabled or an independent oracle is run. Run directly on the recorded devel install on October 7, 2026, `sst simple_test.py` exits 0 at 120 ns and its statistics match `refFiles/test_llyr_simple_test.out` apart from blank lines, so the disabled case is a working regression at that revision.

Native runner suites:

- `tests/testsuite_default_llyr.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/simple_test.py`

Use `python3 tools/sst_tools.py plan-tests --target llyr` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
