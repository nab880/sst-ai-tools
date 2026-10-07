---
{
  "type": "SST Element Profile",
  "title": "serrano main use cases",
  "description": "Standalone coarse-grained iterator/add/output graphs.",
  "tags": [
    "serrano",
    "CGRA accelerator"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:25.072194+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/serrano/serrano.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/serrano/serrano.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "6110a8e58237d306dd03a0bbb67ed4c08cc60479558c09b495984cffecb42141"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/serrano/serstdunit.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/serrano/serstdunit.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "8f1185ff7ed42ca2e8151e76b6e43bbc3acf813efee326c72ad199131dc76448"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/serrano/seriterunit.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/serrano/seriterunit.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "3b7c3a211cb2900fa48a935ebe3c3ddd4a87d8ebe01cdf85ba11ce0d1f7fb9b8"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/serrano/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/serrano/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "9df889f06ad788e472ba0c2df644f6f0fb65edb2f9a8389d84c0fb20a08d9290"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/serrano/serrano.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/serrano/serrano.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "b653d96ee228c11e19af730ba5a1dba002e2bb1943042528f6044e171e22bc05"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/serrano/tests/test_serrano.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/serrano/tests/test_serrano.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "e050ba510b62c18525213a92128bea0a7bec8fe84bbdca84d7915e67fc83fcf9"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/serrano/tests/graphs/sum.graph",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/serrano/tests/graphs/sum.graph",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "ad1cb65af63aa37606825dee4765ce15ef5f1deac0fed8020a7a8a3dffe548a3"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/serrano/sercgunit.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/serrano/sercgunit.h",
      "x-sha256": "b831c5659db5f358e0c7fa282a8f2a0ad62ac71722aab81b9c59b630ad123b4f",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/serrano/serprintunit.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/serrano/serprintunit.h",
      "x-sha256": "5489264216e172df968546472f76090a590f3f4c7a1f2a6b141ce96bb9555a16",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "serrano",
  "x-role": "CGRA accelerator",
  "x-coverage": "use-case-profile"
}
---

# serrano: main use cases

Role: **CGRA accelerator**. Standalone coarse-grained iterator/add/output graphs.

## Use it for

- Construct a graph of supported coarse-grained functional units.
- Explore token/value flow through the implemented addition, iteration, and output units.

## Boundaries and prerequisites

The graph parser recognizes ITERATOR, ADD, SUB, and PRINTER, but `SerranoBasicUnit::configureFunction` only implements ADD; parsed SUB is not a working operation. The current component constructs only the first queued kernel and has no memory interface/ports. Use it for the implemented standalone graph behavior; additional kernels, operations, or memory coupling require code changes. The component is `serrano.Serrano` with an empty ELI parameter list although it reads `verbose`, `clock`, and `kernel0..N`; `msg_queues` is never populated, so termination is driven solely by iterator exhaustion.

## Common companions

The supplied graph runs standalone. No memHierarchy integration is implemented in this component.

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/serrano/`. Read these selectively and verify ELI names against current source.

- `serrano.h`
- `serstdunit.h`
- `seriterunit.h`

## Validation starting point

Check deterministic graph outputs, token progress, and termination. The supplied `tests/test_serrano.py` references `test/graphs/sum.graph`, while the checked file is `tests/graphs/sum.graph`; correct that input path in a copied configuration. The finite sum example should emit 100, 102, ..., 298 as `[cgra]: N` verbose lines, after a `Line[...]` echo of each graph line; no native runner suite exists here.

No native runner suites were found under `test/` or `tests/` in this snapshot. Validate standalone configurations or the consuming integration; report absent runtime coverage explicitly.

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/test_serrano.py`

Use `python3 tools/sst_tools.py plan-tests --target serrano` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
