---
{
  "type": "SST Guide",
  "title": "Validate Mercury runtime and transport",
  "description": "Respect serial-only and architecture-specific runtime cases.",
  "tags": [
    "mercury",
    "validation"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:05:35.714557+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/tests/testsuite_default_hg.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/tests/testsuite_default_hg.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "2a20990c96f2da713333b4b30fdea279ae2561e134d75cb0ba47260e853d35a7"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/configure.m4",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/configure.m4",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "6886f336f7a15aa06e3a8475f34f672b158b91c71a71083a4a72082d3d6739c2"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/Makefile.am",
      "x-sha256": "76ac810ac435e0b2232aa8b78005c23ad678e9b5d2c5e0a397a937c621b26aaa",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---

# Validate Mercury runtime and transport

The devel runner suite is `tests/testsuite_default_hg.py`, despite the source directory being `mercury`. Prefer `plan-tests --target mercury` with explicit paths over an assumed `*mercury*` filename wildcard.

`ostest.py` and `ostest-nano.py` exercise OS behavior. Their suite cases skip when SST ranks or threads exceed one. Inspect `configure.m4` and the runtime context-switching implementation for host-architecture support: only the fcontext backend is compiled (pth/ucontext are commented out), with assembly for x86_64 and arm64 on ELF/Mach-O, and there is no separate fcontext regression suite in this devel snapshot. The hg suite logs a non-empty stderr without failing; its pass criterion is the sorted reference diff.

For runtime changes check wakeup/progress, application output, and natural completion. For transport changes check request identity, logical/physical mapping, injection/completion, and the supported communication interface. Use relevant Iris/Mask-MPI integrations for collective algorithm changes.

Use [test planning](../../development/testing.md), preserving installation identity and respecting the selected test's rank/thread restrictions.

For HGCC/MV2 applications, add compiler/rewriter, registration, per-rank state, MPI-result, and provider-binding checks from [the integration guide](hgcc-mv2.md). Passing OS or Mask-MPI regressions alone does not establish MV2 correctness.
