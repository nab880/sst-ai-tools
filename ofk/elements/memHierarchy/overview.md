---
{
  "type": "SST Guide",
  "title": "memHierarchy model selection",
  "description": "Choose cache, controller, backend, and interface boundaries.",
  "tags": [
    "memHierarchy",
    "memory"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T09:13:57.893596+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-1core-1level.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-1core-1level.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "4c3faf5b97b155c781e41f14c948a3e4b2eea3acecd183f75b5d2363c6552c55"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/standardInterface.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/standardInterface.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "d463d514122fdde7b6ed8298817f48920de7d4e7bed6430274e47f277a12d449"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/cacheController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/cacheController.h",
      "x-sha256": "441c5e2f7f2a7a43121573eca67bec3eba3fd30d4dd3b44363227f4c10027006",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memoryController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memoryController.h",
      "x-sha256": "252967f0759b504d26596bb3f77f8cb091464c78fbe24400d7362d500f4ed3a3",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/directoryController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/directoryController.h",
      "x-sha256": "3c543eb0e1df469e950f028ab4d71a56e7f27ea9341d2396f74da730cef03b48",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/bus.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/bus.h",
      "x-sha256": "2ab6018116fcc4cbaa50fcc7531868d9f5a5fcb076cffdacf2aefe2806fc9933",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/testcpu/standardCPU.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/testcpu/standardCPU.h",
      "x-sha256": "f5ccb0ce81c5ec8b0191e3352d4ef75190290960194d8ec7fe37046556d9e99b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/testcpu/standardMMIO.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/testcpu/standardMMIO.h",
      "x-sha256": "def3c5167ce5a3de1b70a26c2f67bcf63fa7fd3bb8934a232b78af321c2b6e40",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/multithreadL1Shim.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/multithreadL1Shim.h",
      "x-sha256": "981f076d2464cef3ac560a6840a0bdb41e9283dbddc7c017dbfb4d325eed7bbe",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/scratchpad.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/scratchpad.h",
      "x-sha256": "f7a159ec732875fe045940a8b9bc7e07093c5925c60cb4d1dbcc68d25837588b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memLink.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memLink.h",
      "x-sha256": "14ea829abc33e33978f03d68b611681e895d3fce95aa8ffcf7b4ef6350f74a39",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s11",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memNIC.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memNIC.h",
      "x-sha256": "722ba9575b4d5e02b34c6223a60ce6c3f5c618f63f3cf9b60e40863c5b201a5c",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s12",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memNICFour.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memNICFour.h",
      "x-sha256": "1397cc780652498ae330c178883e6ef8ed9080f00681c203a3ad9819f6eea12a",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s13",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memNetBridge.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memNetBridge.h",
      "x-sha256": "3d27b9a6eff351a17b8f43f08603aa099d7c315427a8f3ee13d9e85cefc938a2",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s14",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/coherentMemoryController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/coherentMemoryController.h",
      "x-sha256": "3a829a71fb223396474251d725c07a59267564bf2308f88ae71fa03e83279597",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s15",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memoryCacheController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memoryCacheController.h",
      "x-sha256": "824feedf9dc886b55a1dc9d65dd91765fb262a7396b49c865393e7a4f663f3ba",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s16",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/README.md",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/README.md",
      "x-sha256": "4738d7fffdcd375def010194e0f93f4923fc8cb98611001d0562c5987119dc69",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s17",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/replacementManager.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/replacementManager.h",
      "x-sha256": "a844338e246d8eb5613cb5ae547682f919d809cc088950cf2353170db053d9c6",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s18",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/cacheListener.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/cacheListener.h",
      "x-sha256": "7baa6bd903c043554857487d46364be1cf36acd2e2747a54165e1ed64c2ffb43",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s19",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_weekly_memHierarchy_examples.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_weekly_memHierarchy_examples.py",
      "x-sha256": "1a9b0bc272e85a74570816e0b03c85cbc2a05798136299a95e65fe638f544385",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s20",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-1core-nocache.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-1core-nocache.py",
      "x-sha256": "e5084ba0f62d2b51da267186efb3f4fa2be18d7da16ae783f15d012e64bf368b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s21",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-1core-3level.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-1core-3level.py",
      "x-sha256": "a9ff38b99fcf2e3bc32d227eca5d9a510f6a76c63b2b40c23d82658ec9aab568",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s22",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-4core-shared-llc.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-4core-shared-llc.py",
      "x-sha256": "eb92baeff33ece28f48196924cdf7518c0d49e29da26203fd7a1a65c75ebaff2",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s23",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-4core-shared-distributed-llc.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-4core-shared-distributed-llc.py",
      "x-sha256": "741eff91755a032a9f4f81e78969053be70c51b32cb1129355a44c7c61a92c0e",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s24",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/cacheFactory.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/cacheFactory.cc",
      "x-sha256": "10a083ac03e618572c485e284bd53c84cb277c4aec72436c347295111c08ab29",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---
# memHierarchy model selection

memHierarchy supplies caches, buses, directories, memory controllers, scratchpads, and the StandardMem interface that CPU-side elements use. Its `README.md` only points to the project website; `sst-info memHierarchy` and the headers are the authoritative references for the 61 registered entries in this checkout.

## Components by role

| Role | Components | Notes |
|---|---|---|
| Test traffic generators | `standardCPU`, `streamCPU`, `trivialCPU`, `ScratchCPU`, `mmioEx` | `standardCPU` is the current generator (`memFreq`, `memSize`, `opCount`, `maxOutstanding`, `reqsPerIssue`, read/write/flush/LLSC/custom frequencies, `mmio_addr`, `rngseed`); `mmioEx` is a test MMIO device. |
| CPU-side interface | `standardInterface` (subcomponent) | Translates `StandardMem` requests; `lowlink` port or slot, `tlb` slot, `noncacheable_regions`; `port` and `memlink` are deprecated names. |
| Caches | `Cache`, `multithreadL1` | `multithreadL1` multiplexes `thread<N>` ports into one L1 `cache` port. |
| Interconnect | `Bus`, link managers `MemLink`, `MemNIC`, `MemNICFour`, `MemNetBridge`, `networkMemoryInspector` | See [systems](systems.md). |
| Coherence tracking | `DirectoryController` | Required in front of each memory when several caches share it over a network. |
| Memory | `MemController`, `CoherentMemController` (adds cache shootdowns), `MemCacheController` (memory-side cache), timing backends | Backends in [backends](backends.md). |
| Scratchpad | `Scratchpad` with scratch convertors | Explicitly managed local memory next to a memory path. |
| Ariel profiling | `Sieve`, `MemoryManagerSieve`, `BroadcastShim` | Malloc profiling; Pin-gated suite. |
| Extension subcomponents | `coherence.*`, `replacement.*`, `hash.*`, `emptyCacheListener`, `defCustomCmdHandler`, convertors | See [extension points](extension-points.md). |

## Cache parameters that matter first

| Parameter | Default | Role |
|---|---|---|
| `cache_frequency`, `cache_size`, `associativity`, `access_latency_cycles` | required | Clock, capacity (`16KiB`), ways, data-access latency in cycles. |
| `L1` | `false` | Must be true for level-1 caches; L1s have no MSHR size limit. |
| `cache_line_size` | 64 | Bytes per line; keep consistent across the hierarchy and CPUs. |
| `coherence_protocol` | `MESI` | `MESI`, `MSI`, or `NONE`. |
| `cache_type` | `inclusive` | `inclusive` (required for L1), `noninclusive`, `noninclusive_with_directory` (required for a noninclusive cache with several caches directly above it). |
| `replacement_policy` | `lru` | Read by the cache factory (not listed in the Cache ELI) and passed to the coherence manager; registered policies are `lru`, `lfu`, `mru`, `nmru`, `random` and `-opt` variants. The `replacement` slot overrides it, with slot 1 for the directory's policy in directory caches. The string form of `prefetcher` is read the same way, so `sst-info` does not show either parameter. |
| `mshr_num_entries` | -1 | Miss-status entries; -1 is effectively unlimited; `mshr_latency_cycles` (1). |
| `prefetcher`, `listener` slots | empty | CacheListener subcomponents; only `prefetcher` may send requests. |
| `max_requests_per_cycle`, `request_link_width`, `response_link_width`, `banks` | -1, 0B, 0B, 0 | Bandwidth limits; 0 means unlimited. |
| `num_cache_slices`, `slice_id`, `slice_allocation_policy` | 1, 0, `rr` | Distributed shared cache slices. |
| `noninclusive_directory_entries`, `noninclusive_directory_associativity` | 0, 1 | Directory sizing for `noninclusive_with_directory`. |
| `tag_access_latency_cycles`, `max_outstanding_prefetch`, `drop_prefetch_mshr_level` | derived | Tag-only latency and prefetch throttling; `prefetch_delay_cycles` defaults to 1. |
| `llsc_block_cycles`, `snoop_l1_invalidations`, `maxRequestDelay` | 0, false, 0 | LL/SC hold time, forwarding invalidations to processors, request timeout. |
| `debug`, `debug_level`, `debug_addr`, `verbose` | 0, 0, none, 1 | Debug output requires a core built with `--enable-debug`; `debug_addr` filters by address. |

`highlink` and `lowlink` are both port names and subcomponent-slot names on Cache: connect the port for a direct link, or fill the slot with a MemLink/MemNIC for network coupling or non-default link parameters. Older configurations use the deprecated `cpulink`/`memlink` slots and `high_network_0`/`low_network_0` ports, and `standardInterface`'s `port` is deprecated in favor of `lowlink`.

## Example progression

`examples/example-1core-nocache.py` (controller and backend only), `example-1core-1level.py` (one L1 with `standardInterface` in the `memory` slot of `standardCPU`, its `lowlink` to Cache `highlink`, Cache `lowlink` to MemController `highlink`, `simpleMem` in the `backend` slot), `example-1core-3level.py`, `example-4core-shared-llc.py` (bus to a shared L2), and `example-4core-shared-distributed-llc.py` (four L2 slices between two buses). All five run in the weekly examples suite with a completion check only.

## Where to look for a change

| Desired change | Inspect first |
|---|---|
| Sizes, frequencies, policies, protocols | Cache and controller parameters above; `sst-info memHierarchy.Cache`. |
| Memory timing | [backends](backends.md); `membackend/`. |
| Multi-core, directory, or networked composition | [systems](systems.md); `tests/testDistributedCaches.py`. |
| New policy, protocol, backend, or transport | [extension points](extension-points.md); `cacheController.h`, `coherencemgr/`, `membackend/memBackend.h`, `memLinkBase.h`. |
| Correctness and regressions | [validation](validation.md). |

Start with the direct-link example before distributed cache networks, and keep workload generation separate from the memory model ([model construction](../../using-sst/models.md)).
