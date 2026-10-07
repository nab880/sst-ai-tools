---
{
  "type": "SST Guide",
  "title": "Select a CPU abstraction",
  "description": "Choose instruction execution, dynamic tracing, trace replay, or synthetic traffic.",
  "tags": [
    "selection",
    "cpu-selection"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:00:43.438667+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/vanadis.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/vanadis.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "3a9ad3cdaa2503ded0096c1fd324890b4d708129a8261e18e14a8c0be7b8bef0"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ariel/arielcpu.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ariel/arielcpu.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "d63203c13553fc18e7daec83e8cf7c23a1982add98bb82a54a1e8e5ef2dd7744"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ariel/arielfrontend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ariel/arielfrontend.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "8111fe359a6dc8b809946d82f43a0e5c0ae45b5e72ebc449c3af578ef1bfb86c"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ariel/configure.m4",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ariel/configure.m4",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "93b208c6a84935e32bcaf310af5878d782eba154f30321389b9c9dd4643a1f1d"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/prospero/proscpu.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/prospero/proscpu.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "bc83e82e0ff241d492b9ff6ab108b90f1741f6001b2d249ffb2f80c41407e864"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/prospero/prosreader.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/prospero/prosreader.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "babbfdf98ef303e3c4aae55141001804fc890f3c215a02c0539f5effc41db7e0"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/miranda/mirandaCPU.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/miranda/mirandaCPU.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "6083b72ffdfdbe41ac58a6c0516b7ea0ca5ab36fe1f1e1abf81276bba3b0ab76"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/miranda/mirandaGenerator.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/miranda/mirandaGenerator.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "8eab30538ffe7660359674c5cb7c35342094812d1f9e83f50a2df2bd0457470e"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ariel/tests/testsuite_default_Ariel.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ariel/tests/testsuite_default_Ariel.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "625d309de584d0fb24539a2b45c1d86c03a81f8c3119c41e01221de3e133d2c3"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/prospero/proscpu.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/prospero/proscpu.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "65ad7a82d8c5e48c35760541af6506b43c2f76126773187584dd3fd2b908bf3b"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mmu/simpleMMU.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mmu/simpleMMU.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "de8aa318f54b2571b0760579d16d1b96f2acbf491ea2266db3bd008535a0b2e8"
    },
    {
      "id": "s11",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/samba/page_table_walker.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/samba/page_table_walker.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "5de607597b25a84c6c088fd50731a31bf76ad479dea0a2860a924304da06a42d"
    },
    {
      "id": "s12",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/opal/opal.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/opal/opal.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "64400cda6c2c49dd82ca5c2d09e5b9996f31892b2d9e99ba4cf02b4c8ec94afd"
    },
    {
      "id": "s13",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ariel/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ariel/Makefile.am",
      "x-sha256": "6232fe0cb6f8bcc8d9348c92a909152997354adc155b3a8d04a918377ee09c38",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---

# Choose the abstraction before the element

| Required behavior | Candidate and source evidence | Selection limit |
|---|---|---|
| Binary instruction execution with decoder/pipeline/OS interfaces | [Vanadis](../elements/vanadis/overview.md) | Check supported ISA/ABI, syscalls, and modeled pipeline mechanisms; do not claim arbitrary processor fidelity |
| Host application execution with instrumented memory traffic | [Ariel](../elements/ariel/use-cases.md), `ariel/arielcpu.h`, `arielfrontend.h` | Choose Pin (its frontend exists only in Pin-configured builds) or the EPA instrumentation route and host-compatible tools; request issue limits do not supply a detailed target-ISA pipeline |
| Replay existing memory-access traces | [Prospero](../elements/prospero/use-cases.md), `prospero/proscpu.h`, `prosreader.h` | Access traces omit application values; the current replay writes zero-filled payloads and cannot capture unrecorded execution feedback |
| Synthetic memory access patterns | Miranda, `miranda/mirandaCPU.h`, `mirandaGenerator.h` | Generates requests rather than executing arbitrary application instructions |
| A small memory-interface correctness workload | memHierarchy standardCPU, [example guide](../elements/memHierarchy/overview.md) | Test generator, not a calibrated production CPU model |
| CUDA/GPU coupling | [Balar](../elements/balar/overview.md) plus the chosen CPU path | Explicitly select trace-driven or Vanadis-driven mode and required artifacts |
| CPU/memory faults | [Carcosa](../elements/carcosa/overview.md) | Verify placement, fault semantics, and baseline oracle |

Use [Ariel](../elements/ariel/use-cases.md), [Prospero](../elements/prospero/use-cases.md), and [Miranda](../elements/miranda/use-cases.md) profiles for their main use cases; they do not yet have detailed extension guides. Read the named headers and one local test/configuration only when a user's requirements select that path. Ariel's configure checks include Pin support, shared memory, and ptrace-related setup. Its suite can automatically instrument through PEBIL, but the EPAX preparation branch is unimplemented; inspect the selected route before treating tool detection as readiness.

# Compose and calibrate

Select [memHierarchy](../elements/memHierarchy/overview.md) separately for cache/memory effects. Add an interconnect only if connectivity/contended transport matters to the question. For translation, [mmu](../elements/mmu/use-cases.md) uses the Vanadis OS/mapping contract, while [Samba](../elements/samba/use-cases.md) models a TLB/page-walk path with different consumer interfaces. [Opal](../elements/opal/use-cases.md) supplies physical-page allocation, but its current hint and unmap handlers do not implement the broader behavior described by its README. Specify what timing includes: execution, cache hits/misses, memory response, synchronization, or frontend costs. Keep cores and hardware threads separate from SST simulation ranks/threads.

Use an ISA-compatible deterministic program for execution, a short known trace for replay, or a finite checked request sequence for generators. Establish expected outputs/counts before a large workload. Detailed instruction effects require appropriate execution semantics; bandwidth-focused studies may need only controlled traffic. Missing binaries, trace artifacts, toolchains, or unsupported syscalls are concrete selection constraints, not reasons to silently change the user's objective.

Next: selected source/element overview, [model construction](models.md), and [testing](../development/testing.md).
