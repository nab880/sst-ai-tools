---
{
  "type": "SST Extension Guide",
  "title": "Iris fabrics and provider extensions",
  "description": "Identify the installed simulated provider, its Mercury transport binding, and the contracts for adding a provider.",
  "tags": [
    "iris",
    "fabric",
    "provider",
    "extension"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T18:59:43.522632+00:00"
  },
  "sources": [
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/libfabric/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/libfabric/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "dbc09cca8a9f0d32618a12cb1d425e102f81be15a347d2e8e19186ba9a69f018",
      "id": "s0"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/libfabric/src/fabric.c",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/libfabric/src/fabric.c",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "59eca17a01a2e1851c5839684b32043158495e9abe1f539aab7c75105291575a",
      "id": "s1"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/libfabric/include/ofi_prov.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/libfabric/include/ofi_prov.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "d1f47512a80da142829449e4ad05ebccbc29eae1e88c8f3870dfd0b198b3d04e",
      "id": "s2"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/libfabric/libfabric_config.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/libfabric/libfabric_config.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "8647804d0787e7d025dbb824f6b9689a2c7a1bdd0f8de135cfe345daab147e2f",
      "id": "s3"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/libfabric/prov/sumi/src/sumi_fabric.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/libfabric/prov/sumi/src/sumi_fabric.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "ea1bf3196e45ff6d66233d760e07ff5cb237e346ef955cb7de2ce227c78b5353",
      "id": "s4"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/libfabric/prov/sumi/src/sumi_ep.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/libfabric/prov/sumi/src/sumi_ep.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "0c393adab9ac0cb076ebc0a31cbf176c3e676e1f28ed98c3ef2856bd2490438a",
      "id": "s5"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/libfabric/prov/sumi/src/sumi_prov.cpp",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/libfabric/prov/sumi/src/sumi_prov.cpp",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "ba8eb987a1ff211ab2dfc865fd598430c56239c5677aafcedb1093234e3fa579",
      "id": "s6"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/libfabric/prov/sumi/include/sumi_fabric.hpp",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/libfabric/prov/sumi/include/sumi_fabric.hpp",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "dd08da0cf5791e03b7c3a8e9ceaa4b5e08ab7d4a072c29f56d325d651f5445e8",
      "id": "s7"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/libfabric/prov/sumi/src/sumi_mr.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "086c6ef7a26b7b5119c44336040e7e63887dbf92bb86a169aadce90b738640fa",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/libfabric/prov/sumi/src/sumi_mr.cc"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/libfabric/prov/sumi/src/sumi_cq.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "6a5c57b0fab87fd643473158299e4f02c6cf8930e0409bf104fcc6b0bb87cae7",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/libfabric/prov/sumi/src/sumi_cq.cc"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/iris/libfabric/prov/sumi/include/sumi_prov.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "b7fabf9d457c8ef605eda88b2403c12abf858f792b9e0ffcbfc4d47b2c2c8cea",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/iris/libfabric/prov/sumi/include/sumi_prov.h"
    },
    {
      "id": "s11",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/hardware/network/network_message.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/hardware/network/network_message.cc",
      "x-sha256": "5c14b4d488ec754ae7df26164e51c08c69bc74bb40722c091d780615d8beae2d",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---

# Iris fabrics and provider extensions

## What "fabric" means here

Keep four choices separate: the libfabric **provider**, its fabric/domain/endpoint objects, the Mercury runtime transport behind them, and the physical network topology modeled by Merlin. SUMI collective algorithms are another layer, covered in [the collective registry guide](collectives.md).

## Fabrics/providers present in this checkout

| Name/layer | What exists | Selection/use |
|---|---|---|
| `sstmac` OFI provider | The simulated provider built from `libfabric/prov/sumi/` | Select with `FI_PROVIDER=sstmac` for the inspected MV2 route |
| `sstmac` fabric and domain names | Names assigned by provider discovery and its fabric/domain construction | Returned by provider information; not separate hardware fabrics |
| `macro:libfabric` Mercury runtime library | `FabricTransport` derived from Iris `SimTransport`, registered in `sumi_fabric.hpp` | The MV2 driver's `app1.libraries` includes this library |
| SUMI transport/collective stack | Messaging and collective machinery beneath Iris consumers | Select its algorithms separately; see [collectives](collectives.md) |
| `prov/hook` and `prov/util` directories | Provider wrapper/infrastructure code | Not additional simulated network topologies or proof of another hardware provider |

The checked Makefile compiles the SUMI provider and shared libfabric/hook/util code. Generic dispatcher entries for verbs, TCP, sockets, PSM, GNI, EFA, shared memory, and others are inherited libfabric machinery; conditional macros can resolve them to NULL. Their names in `src/fabric.c` do **not** establish an installed working provider in this SST build. A newly supplied dynamic provider also requires compatible code/build/runtime bindings, not merely an environment variable.

The fabric name does not choose torus versus dragonfly or change modeled link bandwidth. Those belong to the selected Merlin topology and Mercury/NIC configuration.

## Existing API implementation map

Paths are relative to `sst-elements/src/sst/elements/iris/libfabric/`:

| Responsibility | Source entry point |
|---|---|
| Provider discovery, attributes, version/name and fabric operations | `prov/sumi/src/sumi_fabric.cc` |
| FabricTransport runtime registration | `prov/sumi/include/sumi_fabric.hpp` |
| Resolve current Mercury thread's runtime library | `prov/sumi/src/sumi_prov.cpp` |
| Domain, address vector, endpoint and connection management | `sumi_dom.cc`, `sumi_av.cc`, `sumi_ep.cc`, `sumi_cm.cc` in provider src |
| Completion/event queues and counters | `sumi_cq.cc`, `sumi_eq.cc`, `sumi_cntr.cc` |
| Memory registration, scalable endpoints, wait/poll | `sumi_mr.cc`, `sumi_sep.cc`, `sumi_wait.cc`, `sumi_poll.cc` |
| Provider registration/dispatch | `src/fabric.c`, `include/ofi_prov.h` |
| Sources, headers, includes and installed library | `Makefile.am` |

`fi_ops_msg`, `fi_ops_tagged`, `fi_ops_rma`, and `fi_ops_atomic` tables are present, but some concrete handlers return `-FI_ENOSYS`. Audit the individual operations, caps and modes the application needs; a populated operation table does not certify full support. For a new implementation, provider discovery should advertise only implemented behavior. The current provider has concrete gaps that must be accounted for:

- `FI_ATOMICS` is advertised, but the regular endpoint atomic execution handlers return `-FI_ENOSYS`; their validity-query handlers return success without establishing execution support.
- Untagged `sendmsg`/`recvmsg` and tagged `tsendmsg` return `-FI_ENOSYS`. The send/receive vector handlers accept only one IOV. `trecvmsg` uses only the first IOV after checking that at least one exists, so do not infer scatter/gather support.
- `sumi_mr_reg`, `sumi_mr_regv`, and `sumi_mr_regattr` allocate metadata and return success without assigning the caller's `*mr` result. A success return alone is not a usable registered-memory handle; validate or repair this path before relying on registration.
- Untagged `fi_inject`/`fi_injectdata`, RMA `readmsg`/`writemsg`/`inject_write`/`inject_writedata`, and `fi_mr_bind` return `-FI_ENOSYS`; only tagged `tinject`/`tinjectdata` are implemented, so `SUMI_FI_INJECT_SIZE` matters only on the tagged path. `fi_cq_readerr` always returns `-FI_EINVAL` and `fi_cq_signal` aborts. Discovery advertises `iov_limit = 1`, consistent with the single-IOV handlers.

These are observations from the pinned source, not newly reproduced runtime failures.

The provider accessor gets the current simulated Mercury thread, retrieves its library using the fixed runtime key `libfabric`, and initializes it as needed. Preserve that contract if reusing the accessor; changing an ELI name alone is not enough to substitute another runtime library.

## Provider controls with active consumers

`SUMI_CQ_NONBLOCK_YIELD_NS` defaults to **1 ns** and controls a simulated timeout when a nonblocking completion-queue read finds no next completion. Zero disables it. This is separate from the unused `SimTransport` `poll_delay` member. `SUMI_FI_INJECT_SIZE` controls the advertised inject size (default **64 bytes**, positive overrides capped at **16384 bytes**); it does not itself add latency. Both settings are cached on first use in the host process. See [MV2 timing](../mercury/mv2-timing.md) for the MV2 call sites and progress implications.

## Choose the smallest extension boundary

| Desired change | Extend |
|---|---|
| New router/connectivity/routing behavior | Merlin topology/router; retain provider when its API still fits |
| New host/NIC/progress cost behavior | Mercury/Iris transport or NIC at the causal boundary |
| New collective algorithm | SUMI [collective registration](collectives.md) or MV2's own algorithm, depending on which executes |
| New OFI operation/capability or provider semantics | Existing provider handler, or a new provider if a separate identity/API contract is required |
| A different real host libfabric backend | An explicit compatible integration; host transport performance is not automatically simulated network fidelity |

## Create a new simulated OFI provider

1. Define a concrete API contract: endpoint type, required message/tagged/RMA/atomic operations, caps/modes, addressing, ordering, completion semantics, memory registration, and progress/error behavior. Decide which unsupported calls return an appropriate error.
2. Use the smallest matching pieces of `prov/sumi` as references. Create an owning provider directory such as `prov/newsim`, provider metadata with a unique name, fabric/domain constructors, and only the operation handlers promised by discovery. Preserve resource ownership and buffer/completion lifetimes.
3. Choose how operations reach simulated state. Reuse a compatible `FabricTransport`/Mercury library or register a new runtime implementation with the appropriate ELI API. If changing the runtime key, update accessors/callers explicitly; preserve virtual-rank context, blocking/wakeup, request identity, and simulated timing.
4. Add source/header/include/build entries to the Iris libfabric Makefile. For static integration, declare a distinct provider initializer in `ofi_prov.h` and register it in `src/fabric.c`; avoid colliding with the existing provider's `fi_prov_ini` entry. For dynamic integration, follow the dispatcher's actual plugin entry/version/loading contract and link compatibility. Do not assume upstream libfabric's current build machinery is identical to this bundled snapshot.
5. Configure the application to request the new provider name, keeping app-library dependencies and the selected network consistent. Confirm `fi_getinfo` resolves the intended name, endpoint/caps/modes and fabric/domain attributes before sending traffic.
6. Add behavioral tests for the implemented operations, matching/ordering, completion queues, backpressure/progress, errors, cleanup, and multiple virtual ranks. Verify unsupported combinations fail clearly. Compare an unchanged-provider baseline and include an actual Mercury/MV2 integration case when that is the consumer.

A new provider needs code and validation, not a duplicate source directory plus renamed strings. For a network experiment requiring only topology/latency changes, build a new model configuration with the existing provider instead.

## Validation evidence and limits

The previous runtime campaign compiled Iris and exercised Mask-MPI consumers. It did not directly validate MV2 through this provider, enumerate all OFI capabilities, or implement/test a new provider. Use [MV2 installation](../../development/mv2-install.md) and the small numerical workload before making claims about that route. Log loaded library/provider identity and simulated timing boundaries separately from host runtime.

## Timing on the MV2 provider path

See [MV2 timing through Mercury/Iris](../mercury/mv2-timing.md) for active post-send/RDMA costs, the distinction between Mask-MPI pinning and OFI registration, and parsed-but-unconsumed settings. Changing provider parameters does not establish that a given application path invokes their cost hooks.

## Defects found at the recorded revision

Running MVAPICH2's OFI netmod over the `sstmac` provider on October 7, 2026 exposed five defects in `libfabric/prov/sumi/` at `47b99537`: `sstmaci_ep_recv` drops the caller's `context` and every completion reports the message's own context, which is the sender's request, so a consumer that routes completions by `op_context` never completes a receive; `RecvQueue::finishMatch` tests `localBuffer()` before copying, but posted sends carry their payload in the small-message buffer, so matched receives got no data; `matchRecv` frees the staged copy without clearing the pointer and `~NetworkMessage` frees it again; `cloneInjectionAck` slices `FabricMessage` to the base `Message`; and `fi_cancel` returns `-FI_ENOSYS`. Mask-MPI does not go through this provider, which is why earlier passes did not reach them. A local patch that fixes all five is recorded with the results in the [MV2 application guide](../mercury/hgcc-mv2.md); upstream does not carry it.
