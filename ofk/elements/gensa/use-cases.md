---
{
  "type": "SST Element Profile",
  "title": "gensa main use cases",
  "description": "Spiking processor with memory and network interfaces.",
  "tags": [
    "gensa",
    "Neuromorphic accelerator"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:24.664242+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/gensa/README",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/gensa/README",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "964d1c0ab06b12dafc7651310d173af3d53b2782a609724dc06e4267e0b431b2"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/gensa/gensa.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/gensa/gensa.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "c3507e1dc5bc8389e9f51cf3a6e8ef2741a524f67611bbb989aa663862980a67"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/gensa/tests/testsuite_default_gensa.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/gensa/tests/testsuite_default_gensa.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "6bf6f7978a60405141edd34efdb074a9adedc3029b493a06ae958e87ee428dda"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/gensa/gensa.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/gensa/gensa.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "992a158447412eb3dbeb9cedc4b2e8d05e78591416479f15963b934286cb8d84"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/gensa/tests/test_gensa_1.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/gensa/tests/test_gensa_1.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "f43f6ed17243908b96be57164ea1dfb50be6bbde67055f35bd75c8b045f56fab"
    }
  ],
  "x-element": "gensa",
  "x-role": "Neuromorphic accelerator",
  "x-coverage": "use-case-profile"
}
---

# gensa: main use cases

Role: **Neuromorphic accelerator**. Spiking processor with memory and network interfaces.

## Use it for

- Explore spike propagation and leaky-integrate-and-fire behavior using the supported neural context.
- Study event aggregation and memory interaction for a finite spiking workload.

## Boundaries and prerequisites

The `gensa.core` constructor requires a `networkIF` SimpleNetwork subcomponent set explicitly; memory comes from the `memory` slot or, when that is empty, an anonymous `memHierarchy.standardInterface` on the `mem_link` port. The supplied single-core case still connects the network interface to a Merlin router, and termination depends on it: the component ends the simulation only when its self-addressed sync event returns through `networkIF`. Supply a readable neuron/synapse `modelPath` (an unreadable file only prints `Failed to open file` and runs with zero neurons) and finite `steps`; `maxRequestDepth` is read but undocumented. Inspect the supported numeric behavior rather than treating README TODOs as implemented features.

## Common companions

[memHierarchy](../memHierarchy/use-cases.md), [merlin](../merlin/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/gensa/`. Read these selectively and verify ELI names against current source.

- `README`
- `gensa.h`

## Validation starting point

Use a tiny known neural case to verify firing/output events and deterministic completion, then run the Gensa suite.

Native runner suites:

- `tests/testsuite_default_gensa.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/test_gensa_1.py`

`tests/test.py` predates the `networkIF` requirement and uses obsolete parameters; it cannot construct the component unmodified.

Use `python3 tools/sst_tools.py plan-tests --target gensa` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
