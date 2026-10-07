---
{
  "type": "SST Guide",
  "title": "Extend Vanadis execution",
  "description": "Preserve ISA semantics and pipeline bookkeeping at the chosen boundary.",
  "tags": [
    "vanadis",
    "extension-points"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T01:55:08.144181+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/decoder/vriscv64decoder.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/decoder/vriscv64decoder.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "85f229024316b9a21102ecadce8ee61cf6e49873ca29b2cf3ba6a16fe55e5eb9"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/inst/vinst.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/inst/vinst.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "6ae75ed033b44b1c210e0c886f7669d19f1e9efe09ce7d0bd62174e21e29d31f"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/vanadis.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/vanadis.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "3a9ad3cdaa2503ded0096c1fd324890b4d708129a8261e18e14a8c0be7b8bef0"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "b23c13384245118d3d377c24c2cfebdc67044a385066228079627e2bd7e94a25"
    }
  ]
}
---

# Extend Vanadis execution

Decode new encodings in the matching ISA decoder and implement instruction semantics in an adjacent `inst/` pattern. Keep instruction width, signedness, register classes, immediate extension, branch behavior, and fault handling consistent with that ISA. Inspect ISA tables and cloning/execution methods instead of copying an unrelated opcode.

Pipeline changes belong in the CPU/functional-unit path; load/store behavior belongs in the LSQ and its memory interface. Trace architectural versus physical registers, readiness, dependencies, and retirement before changing scheduling. An application error may originate in OS syscall handling or binary/loader setup rather than instruction timing.

For a new feature provide a small target-ISA program with an observable result, plus neighboring tests. Match binary ABI/ISA with the configured decoder and OS handler. Build integration follows `Makefile.am`; consider checkpoint state only where the actual affected path supports it. Follow [validation](validation.md).
