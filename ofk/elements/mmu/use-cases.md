---
{
  "type": "SST Element Profile",
  "title": "mmu main use cases",
  "description": "MMU/TLB components for execution-model integration.",
  "tags": [
    "mmu",
    "Address translation"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:00:41.152831+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mmu/simpleMMU.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mmu/simpleMMU.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "8c0073771068f27c5dec3607cdb07a6e52cb55a22e2454ab964e61f1a0e8039a"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mmu/simpleTLB.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mmu/simpleTLB.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "08fdeaa3553855c3bc0324f86dc9a8aa3b4e3056b106f8d5ab36a6ffd657730f"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mmu/tlb.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mmu/tlb.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "228dc14c679ae3be88e0d1836a5efe13f4e071dc8103551b62acc28cb5b2d8a7"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mmu/tlbWrapper.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mmu/tlbWrapper.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "a048f6c41f966e85c36e514766081bf2f19a0f4fbe5ab7dac8a97d81cfd07aa7"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mmu/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mmu/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "26200e235328c2ac76c74b2f9f5883a3e3fe74bc0586f8c3a04a90895ab3f277"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mmu/simpleMMU.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mmu/simpleMMU.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "de8aa318f54b2571b0760579d16d1b96f2acbf491ea2266db3bd008535a0b2e8"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mmu/simpleTLB.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mmu/simpleTLB.cc",
      "x-sha256": "18d83d70eb31dc61e25ab1b83c7074bfe81a55680dd247a280fe3bf3a2c19a35",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mmu/tlbWrapper.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mmu/tlbWrapper.cc",
      "x-sha256": "e485820d8cf7eb260bb3d18cac928c524a8b5517b9e4d7b48892c51997a355e0",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "mmu",
  "x-role": "Address translation",
  "x-coverage": "use-case-profile"
}
---

# mmu: main use cases

Role: **Address translation**. MMU/TLB components for execution-model integration.

## Use it for

- Attach supported virtual-to-physical translation and TLB behavior to a CPU/OS path.
- Compare a simple translation configuration with a pass-through baseline where appropriate.

## Boundaries and prerequisites

The SimpleMMU path works with OS-managed mappings and permission callbacks; it does not issue a hardware page-table walk through memory. Select Samba only when its different page-walk/consumer contracts fit the model. Inspect the selected TLB wrapper and translation latency; pass-through translation returns the original address. `mmu.simpleMMU` fatals on a multi-page `map` with a PPN list; `mmu.tlb_wrapper` uses `highlink`/`lowlink` ports with deprecated `cpu_if`/`cache_if` fallbacks; `mmu.simpleTLB` fails translations outside its `min_virt_addr`/`max_virt_addr` window (defaults 4096 and 0x80000000).

## Common companions

[vanadis](../vanadis/use-cases.md), [memHierarchy](../memHierarchy/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/mmu/`. Read these selectively and verify ELI names against current source.

- `simpleMMU.h`
- `simpleTLB.h`
- `tlb.h`
- `tlbWrapper.h`

## Validation starting point

Use known virtual/physical mappings and permissions where supported, and validate through a Vanadis integration; no standalone mmu suite exists here.

No native runner suites were found under `test/` or `tests/` in this snapshot. Validate standalone configurations or the consuming integration; report absent runtime coverage explicitly.

Use `python3 tools/sst_tools.py plan-tests --target mmu` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
