---
{
  "type": "SST Extension Guide",
  "title": "Iris collective algorithms and registration",
  "description": "Catalog the SUMI collective factories, configuration keys, and external-library extension path.",
  "tags": [
    "iris",
    "collectives",
    "extension"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:05:36.994867+00:00"
  },
  "sources": [
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/sumi/collective_registry.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/sumi/collective_registry.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "4781412e1c76ccf4bc33c4203f8709f55d25c5021ed6993694e2495e86a93747",
      "id": "s0"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/sumi/collective_registry.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/sumi/collective_registry.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "cdbc93c3ea160e7ff22b346bfa03502d138191b47a5089581fdc783186dfab81",
      "id": "s1"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/sumi/collective_registry_builtins.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/sumi/collective_registry_builtins.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "fcf81c278effa5fe64c1910e9a138fc5b08428077677f8e0556a843e5dd590e1",
      "id": "s2"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/sumi/sim_transport.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/sumi/sim_transport.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "cb48a9e1b5fb5189c59651f6f9cf4ca9bcc95eba87a2176eb5802399b37a4ff7",
      "id": "s3"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "ce83626e0d2a4b4c6a6ad281f668e09c7f087830be7765debda4a0e8f587080f",
      "id": "s4"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/tests/testsuite_default_mask_mpi.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/tests/testsuite_default_mask_mpi.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "af6b39371d27444f88cdd333ad70edc88de537f3361b5fe785b7d5f18f970c2e",
      "id": "s5"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/pymercury.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "28b879fca429a047cfac23554d31aef4c02b6f1271831d8cb06b14c54e24e718",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/pymercury.py"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/tests/test_hierarchical_allreduce.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "2dc854e28e461fe5a72c377a058e0bb655aa00c2d0bd6a7605512da4b225a000",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/tests/test_hierarchical_allreduce.py"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/mpi_api.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/mpi_api.cc",
      "x-sha256": "06d3ae33a82aeb9226a61b6e48f031d44110e6bf7ed4186a0cf586512bef4092",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---

# Iris collective algorithms and registration

## Registered algorithms in the selected devel source

These are SUMI collective implementations, not OFI providers or physical fabrics:

| Operation | Registered names | Default without an override |
|---|---|---|
| Allgather | `iris.bruck`, `iris.ring` | `iris.bruck` |
| Allreduce | `iris.recdouble`, `iris.ring` | `iris.recdouble` for flat/intra/inter stages |
| Alltoall | `iris.bruck`, `iris.direct` | `iris.bruck` |
| Reduce | `iris.recdouble` | `iris.recdouble` |
| Broadcast | `iris.btree` | `iris.btree` |
| Scan | `iris.btree` | `iris.btree` |
| Gather | `iris.btree` | `iris.btree` |
| Scatter | `iris.btree` | `iris.btree` |

Names are scoped by operation: `iris.ring` for Allgather and Allreduce resolves different classes. The current scalar-count registry does not support variable-count operations. Reduce-scatter deliberately has no selectable registry key in this source because its existing halving implementation is an abort stub; `gatherv`/`scatterv` abort unconditionally, and `allgatherv`/`alltoallv` use fixed Bruck/Direct classes. Reduce, broadcast, scan, gather, and scatter defaults construct the built-in class directly without consulting the registry; only the allgather/alltoall/allreduce defaults resolve through it. Do not infer support from an enum or class name alone.

## Selection and hierarchy

`sim_transport.cc` accepts `collective.allgather`, `collective.allreduce`, `collective.alltoall`, `collective.reduce`, `collective.bcast`, `collective.scan`, `collective.gather`, and `collective.scatter`. Nonempty parameter values take precedence over their `SUMI_*_ALG` environment defaults. The table gives the defaults in this revision. In an `HgOS` or operating-system platform configuration, prefix these keys with `app1.`: for example, `ep.os.addParam("app1.collective.allreduce", "iris.ring")`. The older `app1.allgather` and `app1.alltoall` keys are rejected with migration errors.

Hierarchical Allreduce separately accepts `collective.allreduce.hierarchy` and `collective.allreduce.intra`, `.inter`, and `.broadcast`, with corresponding intra/inter/broadcast algorithm environment defaults. Intra/inter use Allreduce algorithms; broadcast uses a Broadcast algorithm. Valid hierarchy values are `auto` (default), `hierarchical`, and `flat`. `auto` uses hierarchy when an SMP communicator exists; `hierarchical` falls back to the flat path whenever the communicator has no SMP sub-communicator; a stderr warning is printed at most once per transport, from communicator rank 0. `flat` rejects nonempty stage overrides, including those inherited from the environment. With hierarchy, intra defaults to `recdouble`; inter inherits the general Allreduce selector before falling back to `recdouble`; broadcast inherits the general Broadcast selector before falling back to `btree`.

The application must enable and establish SMP grouping (see `app1.smp_optimize` and the hierarchical test configuration). A topology choice alone does not create it. `smp_optimize` populates SMP neighbors in `SimTransport::init`, but the SMP sub-communicator itself is created by Mask-MPI, so a non-Mask-MPI consumer must create its own. Allgather and Alltoall also have balanced-SMP paths: Allgather applies its selector to intra/inter Allgathers; Alltoall applies its selector to the inter-node Alltoall, with fixed gather/broadcast stages.

The library-qualified form is `library.algorithm`; bare names use Iris. For example, selecting `iris.ring` for Allreduce resolves ELI name `iris.allreduce.ring`. Unknown `collective.*` keys fail during engine configuration. Algorithm names are resolved when the operation/stage executes; a single-rank shortcut or an unexercised stage can avoid that check. Use multiple virtual ranks and actually invoke the selected operation when testing invalid names or algorithm selection.

## Add a collective implementation

- Inspect `Collective`, a same-operation algorithm, `CollectiveFactoryArgs`, and its actors/messages/completion path. Preserve communicator/rank mapping, tags, reduction operation, source/destination buffer semantics, completion queue, and in-place/repeated invocation behavior as required by that operation.
- Add the implementation/header to `iris/Makefile.am` and register the factory with the matching constructor arguments.
- In the Iris library use `SUMI_REGISTER_COLLECTIVE`; for an external ELI library use `SUMI_REGISTER_COLLECTIVE_LIBRARY`. A supported scalar-count operation uses its existing selector. A new operation/selector also needs dispatch and parameter-validation support; adding a class alone is insufficient.

Illustrative external registration shape, once `MyAllreduce` implements the appropriate constructor and collective contract:

```cpp
SUMI_REGISTER_COLLECTIVE_LIBRARY(allreduce, "myalg", "custom", MyAllreduce,
    a.engine, a.dst, a.src, a.nelems, a.type_size, a.tag, a.fxn, a.cq_id, a.comm)
```

That registry shape creates an ELI entry for the Allreduce operation; request it using `myalg.custom`, with the library built and discoverable. This snippet is a registration illustration, not a complete compilable algorithm. Inspect the macro and adjacent built-ins for the exact API in the selected revision.

Validate numerical results at different rank/count sizes, message-size transitions, in-place buffers, repeated calls, invalid selectors, and relevant SMP/hierarchy cases. The existing Mask-MPI registry/hierarchical tests are useful consumer checks. For a new algorithm, compare result semantics against a known baseline before interpreting timing.

## Relation to MV2

Changing the SUMI collective registry changes consumers that invoke that registry. It does not automatically replace MVAPICH2's own collective scheduling. For an MV2 experiment, establish whether the operation executes in MPI-library code or through an explicitly delegated lower-layer collective before selecting the extension point. OFI provider changes concern transport/API behavior and are described in [fabrics](fabrics.md).
