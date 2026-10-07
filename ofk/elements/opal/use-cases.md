---
{
  "type": "SST Element Profile",
  "title": "opal main use cases",
  "description": "Physical-memory allocation for shared/disaggregated systems.",
  "tags": [
    "opal",
    "Memory allocation manager"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:00:41.973935+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/opal/README",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/opal/README",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "8f72d22d6a03f2b31877ad1962f2ad90e9b9684c65cfadff211b9cd214f6cbc0"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/opal/opal.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/opal/opal.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "17a30df94b32a4acadaa761a3b27e99a4fe3c49305b616a6ec09bb928593662a"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/opal/page_fault_handler.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/opal/page_fault_handler.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "d4c1b0aa4ef9d190385663b21f147f9cc19215beca9c5f49d2192a8a6176f2c9"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/opal/arielmemmgr_opal.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/opal/arielmemmgr_opal.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "bbae25f0a46d2be717f658e0dacf4c25b42b60e328b410ba8e767690b9dc9072"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/opal/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/opal/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "ba6730d4e5925ff6110ba38e2ba3f0588a2a6956fc666572dd7d0dbef5edd065"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/opal/opal.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/opal/opal.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "64400cda6c2c49dd82ca5c2d09e5b9996f31892b2d9e99ba4cf02b4c8ec94afd"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/opal/arielmemmgr_opal.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/opal/arielmemmgr_opal.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "049fe0f91944d01802b2160696d032210f101c7a27ae499a92b3b34e78fa801c"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/opal/tests/basic_1node_1smp.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/opal/tests/basic_1node_1smp.py",
      "x-sha256": "1e9f738684a2112d64ad0b01276ce04896544a1767f3105387447d1e22a3a09f",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "opal",
  "x-role": "Memory allocation manager",
  "x-coverage": "use-case-profile"
}
---

# opal: main use cases

Role: **Memory allocation manager**. Physical-memory allocation for shared/disaggregated systems.

## Use it for

- Explore allocation across configured memory capacity/types and nodes.
- Serve physical-page allocation requests from the compatible Samba page-fault path.

## Boundaries and prerequisites

Source registration uses `Opal` capitalization. The README describes broader intended behavior than the current implementation: `Opal::tick` services only REQUEST (page-allocation) events; HINT, MMAP, and UNMAP are logged to stderr and dropped, the `processHint` call is commented out, and the Ariel adapter's `freeMMAP` is empty. Nothing in sst-elements constructs MMAP/UNMAP events (the Ariel adapter sends HINT for both malloc and mmap), and `processRequest` fatals on multi-page requests. Do not select this snapshot for working hint-driven placement, unmap reclamation, or a complete shootdown/migration workflow without implementing and validating that path. Allocation policy and DRAM timing remain separate.

## Common companions

[samba](../samba/use-cases.md), [ariel](../ariel/use-cases.md), [memHierarchy](../memHierarchy/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/opal/`. Read these selectively and verify ELI names against current source.

- `README`
- `opal.h`
- `page_fault_handler.h`
- `arielmemmgr_opal.h`

## Validation starting point

Check physical-page placement/capacity, allocation responses, and consumer mapping updates. If a study requires reclamation, hints, or shootdowns, add a focused behavioral oracle before claiming that support; no standalone Opal runner suite exists here. Both configuration candidates need Ariel with Pin and a compiled `tests/app/opal_test`, and their reference files are used by no suite.

No native runner suites were found under `test/` or `tests/` in this snapshot. Validate standalone configurations or the consuming integration; report absent runtime coverage explicitly.

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/basic_1node_1smp.py`
- `tests/basic_2node_1smp.py`

Use `python3 tools/sst_tools.py plan-tests --target opal` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
