---
{
  "type": "SST Element Profile",
  "title": "simpleSimulation main use cases",
  "description": "Monolithic and distributed car-wash models.",
  "tags": [
    "simpleSimulation",
    "Teaching/simulation example"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T03:23:59.906455+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleSimulation/README",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleSimulation/README",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "95c3bc70460a590719cc79501145b291e85e7e32e8d56499708c9bcb78b6555d"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleSimulation/simpleCarWash/simpleCarWash.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleSimulation/simpleCarWash/simpleCarWash.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "1833ef27eee5c28f9cf08c74df9e8d36c394f8127385841e0a1a71cd7cec0a73"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleSimulation/distCarWash/distCarWash.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleSimulation/distCarWash/distCarWash.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "504124430df6db156bad4dc2bdceb1728e7a82806e8d4127ca22895c87ca7bad"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleSimulation/tests/testsuite_default_simpleSimulation.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleSimulation/tests/testsuite_default_simpleSimulation.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "eed95907e1a73403b857ae97bfbcf9ead3f6f330b142ac77c6bd4a8ca3968584"
    }
  ],
  "x-element": "simpleSimulation",
  "x-role": "Teaching/simulation example",
  "x-coverage": "use-case-profile"
}
---

# simpleSimulation: main use cases

Role: **Teaching/simulation example**. Monolithic and distributed car-wash models.

## Use it for

- Learn discrete-event/queue simulation with the single-component car-wash model.
- Compare the distributed customer-generator/car-wash decomposition and parallel execution concepts.

## Boundaries and prerequisites

These are learning models of a car wash, not CPU/network hardware models.

## Common companions

[simpleElementExample](../simpleElementExample/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/simpleSimulation/`. Read these selectively and verify ELI names against current source.

- `README`
- `simpleCarWash/simpleCarWash.h`
- `distCarWash/distCarWash.h`

## Validation starting point

Check arrival/service counts, deterministic example output where applicable, and the simpleSimulation suite. The single-component case skips when host ranks times threads exceeds one; the two-component distributed case skips when that product exceeds two.

Native runner suites:

- `tests/testsuite_default_simpleSimulation.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/test_distCarWash.py`
- `tests/test_simpleCarWash.py`

Use `python3 tools/sst_tools.py plan-tests --target simpleSimulation` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
