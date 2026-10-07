---
{
  "type": "SST Element Profile",
  "title": "zodiac main use cases",
  "description": "SIRIUS MPI trace replay for network simulation.",
  "tags": [
    "zodiac",
    "Trace workload"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:26.226808+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/zodiac/zsirius.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/zodiac/zsirius.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "c6c942fc18bf519afe4937aaa6019a4c469bc4421f84541d415cbcede301d121"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/zodiac/test/testsuite_default_SiriusZodiacTrace.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/zodiac/test/testsuite_default_SiriusZodiacTrace.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "12aaa1175630ae35d81b3bcf60eb997eab0ebd65ffd0e32c473ac3c7aa3c05d5"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/zodiac/test/allreduce/allreduce.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/zodiac/test/allreduce/allreduce.py",
      "x-sha256": "fe234a40b8534c3a8820d7b53dd04b8b20a689d985aaedcb61923324fb5fe852",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/zodiac/configure.m4",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/zodiac/configure.m4",
      "x-sha256": "e6de02f99f9fdd38efb7923a9047e120f147740699d9e1aa3a1d80b6929b59bc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "zodiac",
  "x-role": "Trace workload",
  "x-coverage": "use-case-profile"
}
---

# zodiac: main use cases

Role: **Trace workload**. SIRIUS MPI trace replay for network simulation.

## Use it for

- Replay supported MPI communication traces through a network-model stack.
- Compare network configurations with a fixed recorded communication workload.

## Boundaries and prerequisites

Trace inputs and reader semantics constrain supported behavior and feedback. `zodiac.ZodiacSiriusTraceReader` supports the implemented trace events (including send/receive, wait, barrier, and allreduce), rather than every MPI call. Its native suite lives under `test/` and downloads a trace fixture from SST-downloads; preserve its working-directory and host-rank requirements.

## Common companions

[ember](../ember/use-cases.md), [firefly](../firefly/use-cases.md), [merlin](../merlin/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/zodiac/`. Read these selectively and verify ELI names against current source.

- `zsirius.h`
- `test/testsuite_default_SiriusZodiacTrace.py`

## Validation starting point

Verify trace communication/completion and required input artifacts; preserve the suite working directory and host-rank restrictions. The suite's oracle greps only the `Total.Allreduce.Count`/`Total.Allreduce.Bytes` lines against `sirius/tests/refFiles/`; its configuration uses `firefly.hades` with `firefly.VirtNic` and working-directory-relative `npe-N/allred-N.stf` traces, the tarball is downloaded in each `setUp`, and the 128-rank case is nightly-only. OTF and DUMPI readers are build-conditional; only SIRIUS is unconditional.

Native runner suites:

- `test/testsuite_default_SiriusZodiacTrace.py`

Use `python3 tools/sst_tools.py plan-tests --target zodiac` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
