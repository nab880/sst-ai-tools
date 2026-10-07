---
{
  "type": "SST Element Profile",
  "title": "ember main use cases",
  "description": "Communication/computation motifs for network studies.",
  "tags": [
    "ember",
    "Workload"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T08:57:15.696064+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/emberengine.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/emberengine.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "0c179653219c018afa5a97d0f74cc01021ee53ccef95618459a1feba4ad9413d"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/embergen.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/embergen.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "9b0abe7315a71633cbfb893d587197c23ecf8fb2b090e39bd856d55c5cc7b67b"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/mpi/motifs/emberpingpong.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/mpi/motifs/emberpingpong.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "6c232b0ee2553cac9465b9770a3de4e7cfba23c66e84d72877c5df028feda166"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/tests/testsuite_default_ember_ESshmem.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/tests/testsuite_default_ember_ESshmem.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "c0783d0b0b3f2d393abc509168667bfa0553bb520ed91af563582bc9117743bc"
    }
  ],
  "x-element": "ember",
  "x-role": "Workload",
  "x-coverage": "detailed"
}
---

# ember: main use cases

Role: **Workload**. Communication/computation motifs for network studies.

## Use it for

- Generate repeatable MPI-style point-to-point or collective schedules.
- Study workload placement, compute delay, communication overlap, or supported SHMEM motifs.

## Boundaries and prerequisites

Ember supplies workload behavior; transport/protocol and router/topology behavior are separate choices. Nonblocking request/buffer lifetimes matter.

## Common companions

[firefly](../firefly/use-cases.md), [hermes](../hermes/use-cases.md), [merlin](../merlin/use-cases.md), [thornhill](../thornhill/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/ember/`. Read these selectively and verify ELI names against current source.

- `emberengine.h`
- `embergen.h`
- `mpi/motifs/emberpingpong.h`

## Validation starting point

Verify participant/iteration counts, message matching, collective order, and natural completion before using latency statistics.

Native runner suites:

- `tests/testsuite_default_ember_ESshmem.py`
- `tests/testsuite_default_ember_nightly.py`
- `tests/testsuite_default_ember_otf2.py`
- `tests/testsuite_default_ember_qos.py`

Additional suites exist; use the planner to discover them.

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `test/EmberEP.py`
- `test/basicDetailedModel.py`

Use `python3 tools/sst_tools.py plan-tests --target ember` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). For implementation detail read [overview](overview.md), the [motif catalog](motifs.md), [extension points](extension-points.md), and [validation](validation.md) as needed.
