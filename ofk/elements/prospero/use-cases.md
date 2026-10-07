---
{
  "type": "SST Element Profile",
  "title": "prospero main use cases",
  "description": "Memory-trace replay with supported reader formats.",
  "tags": [
    "prospero",
    "Trace workload"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:00:42.825111+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/prospero/proscpu.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/prospero/proscpu.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "bc83e82e0ff241d492b9ff6ab108b90f1741f6001b2d249ffb2f80c41407e864"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/prospero/prosreader.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/prospero/prosreader.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "babbfdf98ef303e3c4aae55141001804fc890f3c215a02c0539f5effc41db7e0"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/prospero/prostextreader.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/prospero/prostextreader.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "0891c35b965e7045bef5c52b403b3f69d1635a8f41d2df4ee68a3d6c4704a3fc"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/prospero/tests/testsuite_default_prospero.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/prospero/tests/testsuite_default_prospero.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "c07a94e804db7007d45e52aeb2e3e5f47aff867c91288ac2d1e3320a74226b97"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/prospero/prostextreader.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/prospero/prostextreader.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "0fb50a820e9b11cb2f4bf28d007377a5d128f532962da7795fdbc0f88e48b1c5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/prospero/proscpu.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/prospero/proscpu.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "65ad7a82d8c5e48c35760541af6506b43c2f76126773187584dd3fd2b908bf3b"
    }
  ],
  "x-element": "prospero",
  "x-role": "Trace workload",
  "x-coverage": "use-case-profile"
}
---

# prospero: main use cases

Role: **Trace workload**. Memory-trace replay with supported reader formats.

## Use it for

- Replay captured memory-access sequences through a cache/memory system.
- Compare memory configurations while holding a supported trace fixed.

## Boundaries and prerequisites

The CPU is `prospero.prosperoCPU`; readers are `prospero.ProsperoTextTraceReader` (default), `ProsperoBinaryTraceReader`, and `ProsperoCompressedBinaryTraceReader`, the last requiring zlib support. The text reader parses `cycle <op> decimal_address byte_length`, where `R`/`r` is a read and any other character becomes a write. Requests longer than `cache_line_size` are clamped before issue, and addresses pass through the Prospero memory manager's page translation. Recorded cycles gate issue, while issue/outstanding limits and memory responses can delay it. Replayed writes carry zero-filled data, so traces preserve access behavior rather than application values or unrecorded execution feedback.

## Common companions

[memHierarchy](../memHierarchy/use-cases.md), [cacheTracer](../cacheTracer/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/prospero/`. Read these selectively and verify ELI names against current source.

- `proscpu.h`
- `prosreader.h`
- `prostextreader.h`

## Validation starting point

Verify a short known trace produces the expected requests/completions, then run the relevant Prospero suite. The suite downloads its trace archive from SST-downloads during setup, so it needs network access or a cached copy; Pin variants also need `sst-prospero-trace`.

Native runner suites:

- `tests/testsuite_default_prospero.py`

Use `python3 tools/sst_tools.py plan-tests --target prospero` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
