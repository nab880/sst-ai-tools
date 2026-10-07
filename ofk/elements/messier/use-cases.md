---
{
  "type": "SST Element Profile",
  "title": "messier main use cases",
  "description": "Nonvolatile memory controller, banks, and ranks.",
  "tags": [
    "messier",
    "Memory technology"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T03:56:03.545058+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/messier/README",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/messier/README",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "b28b9110d1eaab23cf7c4bf5e03816df3194d1d769456ea38eaf3a75e946b42b"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/messier/messier.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/messier/messier.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "414d650de5d92721444d413d860b59af507b1ce0b283103146bd9bfa9ba246c6"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/messier/tests/testsuite_default_Messier.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/messier/tests/testsuite_default_Messier.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "28335a860f865b34df45bce73feb6c3ea08293841e8257d77e1775851a4977ad"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/MessierBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/MessierBackend.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "5158510b117453b81fc449d4cc4a958785bad28fc90c989d94eebc45c286fdd6"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/messier/nvm_dimm.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/messier/nvm_dimm.cc",
      "x-sha256": "b62dd3df82a54690a23f4d2dc187e42348b97b90628c91d095a8ca82650474ec",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/messier/nvm_params.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/messier/nvm_params.h",
      "x-sha256": "44d7ed580c3923e9db7c5f18a424148556963fb4d0813fe9db80e7e9dfc61712",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/messier/tests/gupsgen.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/messier/tests/gupsgen.py",
      "x-sha256": "0ce68099650fa33ab1dfc67e6640de05d36075319e992c788396b6c127c6d78f",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "messier",
  "x-role": "Memory technology",
  "x-coverage": "use-case-profile"
}
---

# messier: main use cases

Role: **Memory technology**. Nonvolatile memory controller, banks, and ranks.

## Use it for

- Explore the modeled NVM device/controller organization and parameters.
- Compare workload latency/throughput under supported bank/rank configurations.

## Boundaries and prerequisites

Source registration uses `Messier` capitalization: the component is `Messier.Messier`, and the native configurations instantiate it as plain `Messier`, which SST resolves to that library/element pair. Connect a memHierarchy controller through its `memHierarchy.Messier` backend and `nvm_link` to the NVM component; keep adapter link latency separate from the modeled bank/controller timing. There is no endurance/wear model, but the controller enforces a power budget that throttles concurrent reads and writes through `max_current_weight`, `read_weight`, and `write_weight`; it reports no energy.

## Common companions

[memHierarchy](../memHierarchy/use-cases.md), [miranda](../miranda/use-cases.md), [cassini](../cassini/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/messier/`. Read these selectively and verify ELI names against current source.

- `README`
- `messier.h`

## Validation starting point

Check finite request completion, address/bank behavior, and selected Messier regressions with the intended controller configuration. Three of the five native cases (`gupsgen`, `gupsgen_2RANKS`, `stencil3dbench_messier`) are categorized `nightly` and skip under the default category; `gupsgen_fastNVM` and `streambench_messier` run by default. The configuration candidates below are nightly cases that also depend on `miranda.BaseCPU` generators and `cassini.StridePrefetcher`; no memHA case covers this backend.

Native runner suites:

- `tests/testsuite_default_Messier.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/gupsgen.py`
- `tests/gupsgen_2RANKS.py`

Use `python3 tools/sst_tools.py plan-tests --target messier` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
