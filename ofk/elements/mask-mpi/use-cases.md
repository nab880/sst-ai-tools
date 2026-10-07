---
{
  "type": "SST Element Profile",
  "title": "mask-mpi main use cases",
  "description": "MPI API modeling over the Mercury-related runtime.",
  "tags": [
    "mask-mpi",
    "Application API/runtime"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:05:35.841268+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/mask_mpi.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/mask_mpi.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "c0f11f1fbd7a9a38fcbc635316345cb04da1af9c0133ff78d4cf7b2b37d7a64f"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/mpi_api.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/mpi_api.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "29c40fb8f01b7e064917ba0bb0b3bf02ee3e33b8b55204cb3a259d141503c0ff"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/tests/testsuite_default_mask_mpi.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/tests/testsuite_default_mask_mpi.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "af6b39371d27444f88cdd333ad70edc88de537f3361b5fe785b7d5f18f970c2e"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/Makefile.am",
      "x-sha256": "44ee4746144aacd370a551efb702f49ca3ee08787075cf1227a13f5054277a39",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/tests/test_sendrecv.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/tests/test_sendrecv.py",
      "x-sha256": "6bf30c326aa0adf6477492ba41a3a40b353d6e27bfba2aab852d95a0ac898c5f",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/mpi_api.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/mpi_api.cc",
      "x-sha256": "06d3ae33a82aeb9226a61b6e48f031d44110e6bf7ed4186a0cf586512bef4092",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "mask-mpi",
  "x-role": "Application API/runtime",
  "x-coverage": "use-case-profile"
}
---

# mask-mpi: main use cases

Role: **Application API/runtime**. MPI API modeling over the Mercury-related runtime.

## Use it for

- Run supported MPI application/skeleton communication through a modeled runtime.
- Explore send/receive, collective, rank/VN mapping, and supported collective algorithm selection.

## Boundaries and prerequisites

The API is `mask_mpi.MpiApi`, a `SimTransport` library loaded through `app1.libraries` (`computelibrary:ComputeLibrary`, `mask_mpi:MpiApi`) with `app1.dependencies: [sumi]`; it builds as `libmask_mpi.so` under `lib/sst-elements-library/ext` together with per-test application libraries, none of which `sst-info` lists. Supported MPI calls and semantics must be checked individually; the API name does not imply complete MPI standard coverage. Keep simulated ranks separate from host MPI ranks, and note that SMP communicators exist only when MpiApi runs with `smp_optimize`. Collective selectors use the `app1.collective.*` namespace through `HgOS`; see the [Iris algorithm/default/hierarchy guide](../iris/collectives.md). The native suite includes selector errors, ring/direct alternatives, and hierarchical cases; its sparse-communicator case skips with multiple host SST ranks.

## Common companions

[mercury](../mercury/use-cases.md), [iris](../iris/use-cases.md), [merlin](../merlin/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/mask-mpi/`. Read these selectively and verify ELI names against current source.

- `mask_mpi.h`
- `mpi_api.h`
- `tests/testsuite_default_mask_mpi.py`

## Validation starting point

Check application-level send/receive and collective results, progress, and the supported collective/rank-mapping cases. Parameter-error cases use the `ALG`/`ALG_PARAM` environment variables, and every run sets the working directory to `tests/` because the platform file is loaded by module name.

Native runner suites:

- `tests/testsuite_default_mask_mpi.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/test_sendrecv.py`
- `tests/test_allgather.py`
- `tests/test_hierarchical_allreduce.py`

`tests/platform_file_mask_mpi_test.py` is an imported platform-definition helper, not a standalone workload.

Use `python3 tools/sst_tools.py plan-tests --target mask-mpi` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
