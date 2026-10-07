---
{
  "type": "SST Element Profile",
  "title": "kingsley main use cases",
  "description": "Two-dimensional mesh on-chip network.",
  "tags": [
    "kingsley",
    "Interconnect"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:58.728691+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/kingsley/noc_mesh.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/kingsley/noc_mesh.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "a874bf5674b5a1b7779f75a56d33131125d45f60eb7b214c12e781ef71858c86"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/kingsley/linkControl.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/kingsley/linkControl.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "97bee7c44aba41ef7247b0f8cee37829eb0b462c4bd5a14a12afaa66e6bc57ee"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/kingsley/tests/testsuite_default_kingsley.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/kingsley/tests/testsuite_default_kingsley.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "5472b7ad97eee492dcdd555b801b6be9f781856405b1efff41606728f1211870"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/kingsley/noc_mesh.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/kingsley/noc_mesh.cc",
      "x-sha256": "04dc1f25e375ead847a55ae67e8c23464c0ced851ecab212f84abdbcc7c8cc69",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/kingsley/tests/noc_mesh_32_test.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/kingsley/tests/noc_mesh_32_test.py",
      "x-sha256": "ef97ba7859f59d84e4eb79746085902c0575560232c7ee385c1bb7ebf68d9c62",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "kingsley",
  "x-role": "Interconnect",
  "x-coverage": "use-case-profile"
}
---

# kingsley: main use cases

Role: **Interconnect**. Two-dimensional mesh on-chip network.

## Use it for

- Connect memory/processor endpoints through a directional 2-D mesh.
- Explore mesh bandwidth, buffering, dimension-order routing, and endpoint-priority behavior exposed by its parameters.

## Boundaries and prerequisites

Use `kingsley.noc_mesh` with `kingsley.linkcontrol` implementing SimpleNetwork. Wire north/south/east/west ports and `localN` endpoint ports consistently; mesh dimensions and router coordinates are discovered in `init()` from link connectivity rather than parameters. Edge routers' outward ports can carry endpoints, and the sparse ID map numbers that halo as an extra ring, so the shipped test sizes `num_peers` as endpoints per router times routers plus `2x + 2y`. Choose X-first or Y-first routing with `route_y_first`, verify sparse versus dense endpoint IDs (`use_dense_map`) against the workload, and note that `port_priority_equal` (default false) otherwise prioritizes endpoint ports.

## Common companions

[memHierarchy](../memHierarchy/use-cases.md), [vanadis](../vanadis/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/kingsley/`. Read these selectively and verify ELI names against current source.

- `noc_mesh.h`
- `linkControl.h`

## Validation starting point

Check endpoint delivery/counts and route behavior for a small mesh, including contention when studying throughput. The lone suite method is spelled `test_kingsly_noc_mesh_32`.

Native runner suites:

- `tests/testsuite_default_kingsley.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/noc_mesh_32_test.py`

Use `python3 tools/sst_tools.py plan-tests --target kingsley` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
