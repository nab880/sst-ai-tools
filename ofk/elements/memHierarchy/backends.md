---
{
  "type": "SST Guide",
  "title": "Memory timing backends",
  "description": "Catalog of memHierarchy memory backends, their convertors, parameters, and tests.",
  "tags": [
    "memHierarchy",
    "memory",
    "backend"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/claude",
    "at": "2026-10-07T09:15:47.833246+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/memBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/memBackend.h",
      "x-sha256": "5460dadfccd92f7cea436d1fe6d1f70f13bd24470fcf9b0a360dc6e825b9d944",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/memBackendConvertor.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/memBackendConvertor.cc",
      "x-sha256": "db3a7d3ccca91b72f601ae7fa4382c6c51a5ec768cb90953debb5265e4f9e221",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/simpleMemBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/simpleMemBackend.h",
      "x-sha256": "bcaf188f435c1d3daeadab9cb5aaf2bae17da9420f1b622a122298bf03fbd9f9",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/simpleMemBackend.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/simpleMemBackend.cc",
      "x-sha256": "7a67e616695c0bdb79dc25bbd5f77e092f6c1699cdfe27c50a94b8d4b4e0be1f",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/simpleDRAMBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/simpleDRAMBackend.h",
      "x-sha256": "4f8457b60c8a30495b986db5b1fa8d7b7deeeaec03066db2f8b9da935e1c2fea",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/timingDRAMBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/timingDRAMBackend.h",
      "x-sha256": "36ee9b81e0602fe840db62eb04d9bdb79bfd337f07fee62c6d4d66140faf6b3a",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/timingAddrMapper.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/timingAddrMapper.h",
      "x-sha256": "3c34f25c8f5228eb88e2b0c254c973602092276a3af5a9ab5f58d67ed2c3fd73",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/timingPagePolicy.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/timingPagePolicy.h",
      "x-sha256": "53bb87fbf580c52cdc13067b579b9eabb0da3504f935f2218e7fd44e77946573",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/timingTransaction.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/timingTransaction.h",
      "x-sha256": "e052883b9282a8c297855dc434a2351a033809fde4ad1ded1bdbaa9437e56d89",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/delayBuffer.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/delayBuffer.h",
      "x-sha256": "e329895bb2d3cd8d6e4cc027d35c0f40c92d1bc7cb93ee898a1520f698a56815",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/requestReorderSimple.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/requestReorderSimple.h",
      "x-sha256": "48819c1e4df153f8bab4fad062c90f3bf3b6e77a708ef4d2c5c255dfa8ab2d1d",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s11",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/requestReorderByRow.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/requestReorderByRow.h",
      "x-sha256": "44ba08b30e741f7cb878338381c33f462be075b6fda3650dd454ff6aa1cf56d6",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s12",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/cramSimBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/cramSimBackend.h",
      "x-sha256": "9b7675aff508bdf7af3709ddd1941540083e9ed37ca184643d55ea25e32cdf5a",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s13",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/MessierBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/MessierBackend.h",
      "x-sha256": "5158510b117453b81fc449d4cc4a958785bad28fc90c989d94eebc45c286fdd6",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s14",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/vaultSimBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/vaultSimBackend.h",
      "x-sha256": "60c9d0f9361794314fd92b073f93cf7b739e000e6308dcca0cacf065015ffc95",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s15",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/vaultSimBackend.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/vaultSimBackend.cc",
      "x-sha256": "6727581e316a8102460ec9784093bf4d4a01761a19e06098218436051786bd7b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s16",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/goblinHMCBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/goblinHMCBackend.h",
      "x-sha256": "af1fef73987f2e3f9d6f14cccb633b38e6b31b70da5f3a1ec62744724bd2f9f7",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s17",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/ramulatorBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/ramulatorBackend.h",
      "x-sha256": "e9f1fde7a92f05d52fa6ef2d784ebe7082d0f5995d14607406a7787d4c940a22",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s18",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/ramulator2Backend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/ramulator2Backend.h",
      "x-sha256": "46c0f8bd658e7ec5587a2996164a1256b5fb8bb40b15dac9006652f9239e8397",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s19",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/backing.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/backing.h",
      "x-sha256": "72f8322a08ae505ef25bb596738c6d1b3564b644bb218ee653b9b399f8f5e862",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s20",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memoryController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memoryController.h",
      "x-sha256": "252967f0759b504d26596bb3f77f8cb091464c78fbe24400d7362d500f4ed3a3",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s21",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memoryController.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memoryController.cc",
      "x-sha256": "3229cea5bf28f6d1ee083169a947215b0dbc704710ed7803436ce1a28e32ff29",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s22",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/scratchpad.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/scratchpad.h",
      "x-sha256": "f7a159ec732875fe045940a8b9bc7e07093c5925c60cb4d1dbcc68d25837588b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s23",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/Makefile.am",
      "x-sha256": "0aa84e22bf953e62466fc78d9451001d5138756f70645f5da8276ac27982f3ea",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s24",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/configure.m4",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/configure.m4",
      "x-sha256": "0041644bcc9a489c2c803a214300b597e81af751b1f513ff08d09ba6fd848dcd",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s25",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHA.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHA.py",
      "x-sha256": "94ebfdff60f7fb4f055dc1e5f5711de9ddf7f3ea01675167a3bfa233d562d786",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s26",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memory.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memory.py",
      "x-sha256": "46c5b8e38c83811cde200b6fcad13bbc36ae9a6e00e0aeb5583bd8f4ff0801f1",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s27",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/scratchpad.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/scratchpad.cc",
      "x-sha256": "d52d28611302b7a67740df1960511b0e40d05d32fc9e595bfafc4ff99a2bca35",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s28",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/simpleMemScratchBackendConvertor.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/simpleMemScratchBackendConvertor.h",
      "x-sha256": "66e69b59b2c9930a942d560c432876925ab94660807157b2dc306369869d5d1a",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s29",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/scratchBackendConvertor.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/scratchBackendConvertor.h",
      "x-sha256": "4aca19f7182eee5bf73a27638efb64841792b441f643a38ea059097fc725a1ac",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---
# Memory timing backends

A `MemController` delegates timing to a backend subcomponent in its `backend` slot; the controller keeps data in its backing store, so the backend only answers "when does this request complete". Detailed DRAM timing theory is out of scope here; this guide catalogs what exists, what each backend's knobs are, and how to tell them apart.

## The backend contract

`membackend/memBackend.h` defines three APIs. `SimpleMemBackend::issueRequest(id, addr, isWrite, numBytes)` returns false to make the convertor retry later and completes with `handleMemResponse(id)`. `FlagMemBackend` adds request and response flags. `ExtMemBackend` also receives custom data and must override `issueCustomRequest`, which the base fatals on. Each backend names its convertor through `getBackendConvertorType()` (`memHierarchy.simpleMemBackendConvertor`, `flagMemBackendConvertor`, `extMemBackendConvertor`; scratchpads use `simpleMemScratchBackendConvertor`, the only registered `ScratchBackendConvertor`, which must be set in the Scratchpad's `backendConvertor` slot because the parameter default names an unregistered spelling). The convertor splits controller requests to the backend's `request_width` (default 64) and caps issue at `max_requests_per_cycle` (default -1, unlimited; `simpleMem` overrides it to 1). Every backend requires `mem_size`.

## Backends registered in this checkout

| Backend | Models | Key parameters (defaults) | Build/dependency |
|---|---|---|---|
| `memHierarchy.simpleMem` | Constant latency, unclocked | `access_time` (100ns) | built in |
| `memHierarchy.simpleDRAM` | Banks with open/closed rows and three timing constants | `cycle_time` (4ns), `tCAS`/`tRCD`/`tRP` (9), `banks` (8), `bank_interleave_granularity` (64B), `row_size` (8KiB), `row_policy` (closed) | built in |
| `memHierarchy.timingDRAM` | Channels, ranks, banks with transaction queues and page policies | `id` (required), `channels` (1), `channel.numRanks` (1), `channel.transaction_Q_size` (32), `channel.rank.numBanks` (8), `channel.rank.bank.CL`/`CL_WR`/`RCD`/`TRP` (11), `channel.rank.bank.dataCycles` (4), `printconfig` (true) | built in |
| `memHierarchy.DelayBuffer` | Adds a fixed delay in front of another backend | `request_delay` (0ns), `backend` slot (simpleMem) | built in |
| `memHierarchy.reorderSimple` | Reorders a window of requests before a wrapped backend | `max_issue_per_cycle` (-1), `search_window_size` (-1), `backend` slot (simpleDRAM) | built in |
| `memHierarchy.reorderByRow` | Reorders to favor open rows | `banks` (8), `row_size` (8KiB), `reorder_limit` (1), `backend` slot (simpleDRAM) | built in |
| `memHierarchy.cramsim` | Bridges to the cramSim element over `cramsim_link` | `access_time` (100ns link latency), `max_outstanding_requests` (256) | built in; the cramSim element supplies timing |
| `memHierarchy.Messier` | Bridges to the Messier NVM element over `nvm_link` | `access_time` (1ns link latency) | built in; see the Messier profile |
| `memHierarchy.vaultsim` | Bridges to VaultSim over `cube_link`; a `FlagMemBackend` that refuses new requests above 255 outstanding | `access_time` (100ns) | built in; see the VaultSim profile |
| `memHierarchy.goblinHMC` | GOBLIN HMC-Sim stacked memory | external | compiled only with `USE_GOBLIN_HMCSIM`; absent from the recorded install |
| `memHierarchy.ramulator`, `memHierarchy.ramulator2` | Ramulator DRAM simulators (`tests/ramulator-ddr3.cfg`, `tests/ramulator2-ddr4.cfg`, `membackend/ramulator2/Instructions.md`) | external configuration file | compiled only with `HAVE_RAMULATOR`/`HAVE_RAMULATOR2`; absent from the recorded install |

The recorded devel install's `sstsimulator.conf` has empty `LIBDIR` entries for `GOBLIN_HMCSIM`, `RAMULATOR`, and `RAMULATOR2`, and `sst-info memHierarchy` lists none of those backends, so the memHA cases that need them skip.

## timingDRAM structure

`timingDRAM` is the most configurable built-in model. Its `addrMapper` module (`memHierarchy.simpleAddrMapper` default, `roundRobinAddrMapper`, `sandyBridgeAddrMapper`) maps addresses to channel/rank/bank; each bank fills a `transactionQ` slot (`memHierarchy.fifoTransactionQ` default, or `reorderTransactionQ` with `windowCycles` (10)) and a `pagePolicy` slot (`memHierarchy.simplePagePolicy` with `close` (true), or `timeoutPagePolicy` with `timeoutCycles` (5)). The four memHA `BackendTimingDRAM_*` cases exercise these combinations (reorder queue with round-robin mapping and open pages, reorder queue with simple mapping and closed pages, reorder queue with Sandy Bridge mapping and the timeout policy, FIFO queue with round-robin mapping and closed pages) and are the reference configurations to copy; they and `BackendGoblinHMC` are categorized `nightly`, so a default-category run skips them.

## Backing store and data

The controller, not the backend, owns data. `backing` selects `mmap` (default), `malloc` (with `backing_size_unit` granularity, default 1MiB, and `backing_init_zero`), or `none`, which disables data entirely. `backing_in_file` preloads contents, `backing_out_file` writes them at the end, and `backing_out_screen` prints them; `memory_file` is deprecated. The `testsuite_default_memHierarchy_memory.py` cases (`backing_0_mmap_out` through `backing_5_init`) cover the `mmap` and `malloc` modes and init-time writes; `none` has no case there. A data-correctness oracle therefore requires a backing store other than `none`, and `backing_out_file` is the simplest way to capture final memory contents.

## Where each backend is tested

memHA covers `BackendChaining`, `BackendDelayBuffer`, `BackendReorderRow`, `BackendReorderSimple`, `BackendSimpleDRAM_1/2`, `BackendTimingDRAM_1..4`, `BackendVaultSim`, and the conditional `BackendGoblinHMC`, `CustomCmdGoblin_1..3`, `BackendRamulator_1/2`, and `BackendRamulator2` (the last also skips on macOS). cramSim and Messier are validated through their own element suites. Start from the matching memHA configuration under `tests/` when adopting a backend; see [validation](validation.md).

Next: [systems](systems.md) for composing controllers with caches and networks, [extension points](extension-points.md) for writing a backend.
