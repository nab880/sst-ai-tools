---
{
  "type": "SST Element Profile",
  "title": "cacheTracer main use cases",
  "description": "Observe memory events, address distributions, and boundary latency.",
  "tags": [
    "cacheTracer",
    "Observation"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T03:56:05.079575+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cacheTracer/README",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cacheTracer/README",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "4da45f93779ea67a41b06b89707ff106016eaae346e04dda5a20b046beb095f4"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cacheTracer/cacheTracer.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cacheTracer/cacheTracer.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "1c67a3f6a82a5ba5006bbcb514f37465eff27820e6c9a97563b6bfdae023e3e4"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cacheTracer/tests/testsuite_default_cacheTracer.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cacheTracer/tests/testsuite_default_cacheTracer.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "09180e0e821f76c772fd844d0b997667ce25bea4779a87a6d3d7c2a0231c4de6"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cacheTracer/cacheTracer.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cacheTracer/cacheTracer.cc",
      "x-sha256": "6ffde0b56a209a8aca480c90b12a30debcad52a39796a38c0af2aca919edc2b0",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "cacheTracer",
  "x-role": "Observation",
  "x-coverage": "use-case-profile"
}
---

# cacheTracer: main use cases

Role: **Observation**. Observe memory events, address distributions, and boundary latency.

## Use it for

- Generate a trace between a CPU-side component and memHierarchy.
- Count events and build address/access-latency histograms at an explicitly chosen observation boundary.

## Boundaries and prerequisites

The component is `cacheTracer.cacheTracer`. The `northBus` and `southBus` links carry memHierarchy `MemEvent` traffic; any other event type is a fatal error. Place the tracer on that side of a CPU's memory interface; it does not consume arbitrary CPU events or raw StandardMem requests. The README assumes a request travels northBus to southBus and its response reverses direction with a matching ID; latency is recorded in whole nanoseconds only for responses whose response-to ID matches a northBus request. Report this observation boundary when interpreting access latency.

## Common companions

[memHierarchy](../memHierarchy/use-cases.md), [ariel](../ariel/use-cases.md), [miranda](../miranda/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/cacheTracer/`. Read these selectively and verify ELI names against current source.

- `README`
- `cacheTracer.h`

## Validation starting point

Compare observed requests/responses and known addresses with a finite workload; check latency definitions against the connection point. `test_cacheTracer_2` writes its trace and statistics files into the working directory and skips with more than one rank.

Native runner suites:

- `tests/testsuite_default_cacheTracer.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/test_cacheTracer_1.py`
- `tests/test_cacheTracer_2.py`

Use `python3 tools/sst_tools.py plan-tests --target cacheTracer` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
