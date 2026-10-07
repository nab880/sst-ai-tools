---
{
  "type": "SST Element Profile",
  "title": "cassini main use cases",
  "description": "Prefetching and cache-access instrumentation.",
  "tags": [
    "cassini",
    "Cache policy/observation"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T03:56:04.689771+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cassini/nbprefetch.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cassini/nbprefetch.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "b22e3bffe73a0a3e37aa7bbf77297d4953f3e53d2afdbb4250fa29ee6cb0d992"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cassini/strideprefetch.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cassini/strideprefetch.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "35287704a10d73a6ee229f46431925ce3f64a49589279b8b6477012ffc3b4063"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cassini/addrHistogrammer.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cassini/addrHistogrammer.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "e9486b19b41567b9cd1db0e365d5cee63007823167562dc1bac0cd8110b6790d"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cassini/cacheLineTrack.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cassini/cacheLineTrack.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "25b7fec8105b92000eaca607f9b143eeeda0c040b1ef4b228c7e8680f779e859"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cassini/tests/testsuite_default_cassini_prefetch.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cassini/tests/testsuite_default_cassini_prefetch.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "2c775f3dbdbe000bbe4eab0d712d7d2ed9ad18117620e32b4405a34aee250dec"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/cacheController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/cacheController.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "441c5e2f7f2a7a43121573eca67bec3eba3fd30d4dd3b44363227f4c10027006"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/cacheFactory.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/cacheFactory.cc",
      "x-sha256": "10a083ac03e618572c485e284bd53c84cb277c4aec72436c347295111c08ab29",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cassini/tests/streamcpu-nbp.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cassini/tests/streamcpu-nbp.py",
      "x-sha256": "40e3f0edc6032d2febe95d4e4097daab82d530f2601788a914b94d0aeb3d6ad8",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/cassini/palaprefetch.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/cassini/palaprefetch.h",
      "x-sha256": "6b1ae31554ae341edc06d6181ab438fe32c7efbe80ecf7c1d1de2d6d8294a0f8",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "cassini",
  "x-role": "Cache policy/observation",
  "x-coverage": "use-case-profile"
}
---

# cassini: main use cases

Role: **Cache policy/observation**. Prefetching and cache-access instrumentation.

## Use it for

- Compare next-block or stride prefetch behavior on a controlled access sequence.
- Observe address distributions and cache-line usage before eviction.

## Boundaries and prerequisites

Attach the chosen CacheListener through the memHierarchy cache's `prefetcher` slot when it must issue requests, or the `listener` slot for observation. The listener slot cannot send prefetches. The shipped configurations instead set the legacy `prefetcher` parameter, which the cache factory loads anonymously with the same callback. `cassini.PalaPrefetcher` is registered alongside the next-block and stride prefetchers. Match `cache_line_size` and distinguish speculative traffic from demand accesses.

## Common companions

[memHierarchy](../memHierarchy/use-cases.md), [miranda](../miranda/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/cassini/`. Read these selectively and verify ELI names against current source.

- `nbprefetch.h`
- `strideprefetch.h`
- `addrHistogrammer.h`
- `cacheLineTrack.h`

## Validation starting point

Check generated prefetch addresses, demand-data correctness, and traffic/hit-rate changes under a fixed workload. All three suite cases skip when SST threads exceed 3; the stride case runs `tests/streamcpu-sp.py`.

Native runner suites:

- `tests/testsuite_default_cassini_prefetch.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/streamcpu-nbp.py`
- `tests/streamcpu-nopf.py`

Use `python3 tools/sst_tools.py plan-tests --target cassini` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
