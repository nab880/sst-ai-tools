---
{
  "type": "SST Element Profile",
  "title": "samba main use cases",
  "description": "TLB hierarchy and page-walk modeling.",
  "tags": [
    "samba",
    "Address translation"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:00:41.511766+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/samba/README",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/samba/README",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "7f32291eb88cfe0b61e18a86fc7b6128fd2f70ef90f15831a73a84c59826f3a0"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/samba/samba.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/samba/samba.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "032c3943a912235c440851fc1b02a5122bde02592eb479ab400716df9d506d7d"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/samba/page_table_walker.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/samba/page_table_walker.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "766328a87760c5ef86fdd7ad2125f89d0d60d91bde5fbe92d38d5d21cf503590"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/samba/tests/testsuite_default_Samba.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/samba/tests/testsuite_default_Samba.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "37107ec36867bc0d72cd4002ed2020d65150efb2f901e7844659bd9ecdf7f27f"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/samba/samba.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/samba/samba.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "66724124df7f2de097cfbdb8d3e62d70667ec02b6ae031966f0b62374d8168c2"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/samba/page_table_walker.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/samba/page_table_walker.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "5de607597b25a84c6c088fd50731a31bf76ad479dea0a2860a924304da06a42d"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/samba/tlb_hierarchy.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/samba/tlb_hierarchy.cc",
      "x-sha256": "7f573542257506aa9c97fa20bf49949b82001a22ec281439f30ecde7513c64e8",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/samba/tests/gupsgen_mmu_opal.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/samba/tests/gupsgen_mmu_opal.py",
      "x-sha256": "3039566cd819b59a5ce09d7a54e68eac05588df6b79afe4a08dbb098dc905a3c",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "samba",
  "x-role": "Address translation",
  "x-coverage": "use-case-profile"
}
---

# samba: main use cases

Role: **Address translation**. TLB hierarchy and page-walk modeling.

## Use it for

- Explore TLB sizes/page sizes, hits/misses, and modeled translation cost.
- Integrate modeled page faults and physical-page allocation with the compatible memory-management path; verify any required shootdown behavior separately.

## Boundaries and prerequisites

Registration uses `Samba` capitalization. With fault emulation disabled, the walker generates dummy/random addresses for modeled page-table traffic. With `emulate_faults=1`, it uses page-allocation bookkeeping and the configured fault handler (default `Opal.PageFaultHandler`) to form walk addresses. That does not establish execution of an OS page-table implementation; check the selected path and Opal's current limitations. Shootdown dispatch in `TLBhierarchy::tick` is commented out. `self_connected=1` bypasses memory with a fixed `page_walk_latency`; otherwise walk traffic is plain `GetS` MemEvents.

## Common companions

[opal](../opal/use-cases.md), [ariel](../ariel/use-cases.md), [memHierarchy](../memHierarchy/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/samba/`. Read these selectively and verify ELI names against current source.

- `README`
- `samba.h`
- `page_table_walker.h`

## Validation starting point

Check known translation/hit-miss cases and page-walk traffic, then run compatible Samba regressions. The only `emulate_faults=1`/Opal example, `tests/gupsgen_mmu_opal.py`, is not in the native suite.

Native runner suites:

- `tests/testsuite_default_Samba.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/gupsgen_mmu.py`
- `tests/gupsgen_mmu_4KB.py`

Use `python3 tools/sst_tools.py plan-tests --target samba` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
