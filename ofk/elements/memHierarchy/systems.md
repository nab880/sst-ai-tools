---
{
  "type": "SST Guide",
  "title": "Multi-core and networked memory systems",
  "description": "Compose caches, buses, directories, NICs, and memories into multi-core and networked systems.",
  "tags": [
    "memHierarchy",
    "coherence",
    "network"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/claude",
    "at": "2026-10-07T09:15:49.448680+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/cacheController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/cacheController.h",
      "x-sha256": "441c5e2f7f2a7a43121573eca67bec3eba3fd30d4dd3b44363227f4c10027006",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/directoryController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/directoryController.h",
      "x-sha256": "3c543eb0e1df469e950f028ab4d71a56e7f27ea9341d2396f74da730cef03b48",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/bus.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/bus.h",
      "x-sha256": "2ab6018116fcc4cbaa50fcc7531868d9f5a5fcb076cffdacf2aefe2806fc9933",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memNIC.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memNIC.h",
      "x-sha256": "722ba9575b4d5e02b34c6223a60ce6c3f5c618f63f3cf9b60e40863c5b201a5c",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memNICFour.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memNICFour.h",
      "x-sha256": "1397cc780652498ae330c178883e6ef8ed9080f00681c203a3ad9819f6eea12a",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memLink.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memLink.h",
      "x-sha256": "14ea829abc33e33978f03d68b611681e895d3fce95aa8ffcf7b4ef6350f74a39",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memNetBridge.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memNetBridge.h",
      "x-sha256": "3d27b9a6eff351a17b8f43f08603aa099d7c315427a8f3ee13d9e85cefc938a2",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/networkMemInspector.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/networkMemInspector.h",
      "x-sha256": "01e6c2ed3e262b1d6b2bee4dedc743bcb0e59fc0080dae1dfc123960fd042a0e",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memoryController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memoryController.h",
      "x-sha256": "252967f0759b504d26596bb3f77f8cb091464c78fbe24400d7362d500f4ed3a3",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/coherentMemoryController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/coherentMemoryController.h",
      "x-sha256": "3a829a71fb223396474251d725c07a59267564bf2308f88ae71fa03e83279597",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memoryCacheController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memoryCacheController.h",
      "x-sha256": "824feedf9dc886b55a1dc9d65dd91765fb262a7396b49c865393e7a4f663f3ba",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s11",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/multithreadL1Shim.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/multithreadL1Shim.h",
      "x-sha256": "981f076d2464cef3ac560a6840a0bdb41e9283dbddc7c017dbfb4d325eed7bbe",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s12",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/scratchpad.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/scratchpad.h",
      "x-sha256": "f7a159ec732875fe045940a8b9bc7e07093c5925c60cb4d1dbcc68d25837588b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s13",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/standardInterface.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/standardInterface.h",
      "x-sha256": "d463d514122fdde7b6ed8298817f48920de7d4e7bed6430274e47f277a12d449",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s14",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/testcpu/standardCPU.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/testcpu/standardCPU.h",
      "x-sha256": "f5ccb0ce81c5ec8b0191e3352d4ef75190290960194d8ec7fe37046556d9e99b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s15",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/testcpu/scratchCPU.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/testcpu/scratchCPU.h",
      "x-sha256": "38b36cba6766ef7ab4c3936f29faff15210916786a5cbffc785e52e4a7df83ab",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s16",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/testcpu/standardMMIO.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/testcpu/standardMMIO.h",
      "x-sha256": "def3c5167ce5a3de1b70a26c2f67bcf63fa7fd3bb8934a232b78af321c2b6e40",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s17",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/testcpu/streamCPU.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/testcpu/streamCPU.h",
      "x-sha256": "decb7a3c7834d8a99801dfa466ffa9e404dc6a20f5353859e69e6681362c5201",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s18",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/testcpu/trivialCPU.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/testcpu/trivialCPU.h",
      "x-sha256": "4831d2fa5744f26ef22a9c5670ac75097740cb2389ffdd891080b7a19111dd21",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s19",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memTypes.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memTypes.h",
      "x-sha256": "5ca515f68cf2dcd9542281a5f21ca50ba27c936866853b8a11e808fd2e717b34",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s20",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testDistributedCaches.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testDistributedCaches.py",
      "x-sha256": "fab36485b4c4408a2dedd676199debd0148b6296280c4cb9738400538bc9a645",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s21",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testKingsley.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testKingsley.py",
      "x-sha256": "a20eea41a6cc4f8e89e60e588910ad8768a89223dd93db8b70ef8ab813af1719",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s22",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_weekly_memHierarchy_examples.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_weekly_memHierarchy_examples.py",
      "x-sha256": "1a9b0bc272e85a74570816e0b03c85cbc2a05798136299a95e65fe638f544385",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s23",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHA.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHA.py",
      "x-sha256": "94ebfdff60f7fb4f055dc1e5f5711de9ddf7f3ea01675167a3bfa233d562d786",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s24",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHSieve.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testsuite_default_memHierarchy_memHSieve.py",
      "x-sha256": "bf317fe5831a30a8d74dfd126b1fa17b2d21cfebc1e03717e269ee89a32a7cca",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s25",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-1core-nocache.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-1core-nocache.py",
      "x-sha256": "e5084ba0f62d2b51da267186efb3f4fa2be18d7da16ae783f15d012e64bf368b",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s26",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-1core-1level.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-1core-1level.py",
      "x-sha256": "4c3faf5b97b155c781e41f14c948a3e4b2eea3acecd183f75b5d2363c6552c55",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s27",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-1core-3level.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-1core-3level.py",
      "x-sha256": "a9ff38b99fcf2e3bc32d227eca5d9a510f6a76c63b2b40c23d82658ec9aab568",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s28",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-4core-shared-llc.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-4core-shared-llc.py",
      "x-sha256": "eb92baeff33ece28f48196924cdf7518c0d49e29da26203fd7a1a65c75ebaff2",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s29",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-4core-shared-distributed-llc.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-4core-shared-distributed-llc.py",
      "x-sha256": "741eff91755a032a9f4f81e78969053be70c51b32cb1129355a44c7c61a92c0e",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s30",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/interfaces/stdMem.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/interfaces/stdMem.h",
      "x-sha256": "0774a9fdbd647d6ed9375f3c6a686fac54e9d998aac2100a41fd45f7712bc8c4",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s31",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/scratchpad.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/scratchpad.cc",
      "x-sha256": "d52d28611302b7a67740df1960511b0e40d05d32fc9e595bfafc4ff99a2bca35",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s32",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/simpleMemScratchBackendConvertor.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/simpleMemScratchBackendConvertor.h",
      "x-sha256": "66e69b59b2c9930a942d560c432876925ab94660807157b2dc306369869d5d1a",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s33",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/scratchBackendConvertor.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/scratchBackendConvertor.h",
      "x-sha256": "4aca19f7182eee5bf73a27638efb64841792b441f643a38ea059097fc725a1ac",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s34",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/tests/testScratchCache-1.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/tests/testScratchCache-1.py",
      "x-sha256": "f048bdb0f74234753a6bc4da059ddeaf5b74b9f26805bbd7ec0b594e20f9feba",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s35",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memNIC.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memNIC.cc",
      "x-sha256": "fd148d5b9837e0c8e37bb41551f29ab52fa768e5857d4093056c5ad6dab684cd",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s36",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memoryController.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memoryController.cc",
      "x-sha256": "3229cea5bf28f6d1ee083169a947215b0dbc704710ed7803436ce1a28e32ff29",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---
# Multi-core and networked memory systems

memHierarchy composes CPUs, caches, buses, directories, and memory controllers through three transport choices and one coherence design. Choose the transport per link, then the coherence structure, then the request types the workload needs.

## Transports

| Transport | Configuration | Use |
|---|---|---|
| Direct link | Connect the `highlink`/`lowlink` ports; the component loads a `memHierarchy.MemLink` manager itself (`latency` (0ps) is extra latency) | One-to-one connections. |
| Bus | `memHierarchy.Bus` with `bus_frequency` (required), ports `highlink<N>`/`lowlink<N>` (legacy `high_network_<N>`/`low_network_<N>`), `broadcast` (0), `idle_max` (6), `drain_bus` (0) | Several L1s to one L2, or several L2 slices to one memory; no routing, one shared medium. |
| Network | Fill the `highlink`/`lowlink` slot with `memHierarchy.MemNIC` and connect its `port` to a Merlin router; `group` (1), `sources` (group-1), `destinations` (group+1), `network_bw` (80GiB/s), `network_input_buffer_size`/`network_output_buffer_size` (1KiB), `min_packet_size` (8B), `range_check` (1), `linkcontrol` slot (`merlin.linkcontrol`); a different link control such as `kingsley.linkcontrol` must go in that slot, because the deprecated `network_link_control` parameter fatals on any value but `merlin.linkcontrol` | Any topology; groups define who talks to whom (L1=1, L2=2, directory=3, memory=4 in `tests/testDistributedCaches.py`). |
| Four-network NIC | `memHierarchy.MemNICFour` with `data`, `req`, `ack`, `fwd` slots, each with its own bandwidth and buffers | Separate virtual networks per message class. |

`memHierarchy.MemNetBridge` is a Merlin bridge translator for memory traffic between networks, and `networkMemoryInspector` is a SimpleNetwork inspector. The deprecated `cpulink`/`memlink` slots and the `directory*`/`cache*` ports still exist on `Cache` for old configurations.

## Coherence structure

Caches run a coherence manager chosen from `L1`, `cache_type`, and `coherence_protocol`; the `coherence` slot is filled automatically and is not for configuration. `cache_type` is `inclusive` (required for L1s), `noninclusive`, or `noninclusive_with_directory` (required when several upper caches sit directly above a noninclusive cache); `coherence_protocol` is `MESI` (default), `MSI`, or `NONE`. A shared lower cache serves several upper caches through a bus or network. Beyond one cache level per core, a `memHierarchy.DirectoryController` tracks sharers in front of each memory: `clock` (1GHz), `entry_cache_size` (0), `coherence_protocol` (MESI/MSI), `mshr_num_entries` (-1), `access_latency_cycles` (0), `addr_range_start`/`addr_range_end`, `interleave_size`/`interleave_step`, and a `node` number. Directories and memories cover disjoint address ranges; interleaving at line granularity across N memories uses `interleave_size = 64B`, `interleave_step = N*64B`, and `addr_range_start = i*64` as in `tests/testDistributedCaches.py`. Address ranges are checked at initialization when `range_check` is on.

A distributed shared cache is several `Cache` components with `num_cache_slices` (1), `slice_id` (0), and `slice_allocation_policy` (`rr`). `memHierarchy.multithreadL1` multiplexes `thread<N>` ports into one `cache` port with `requests_per_cycle`/`responses_per_cycle` limits for hardware threads sharing an L1. `memHierarchy.MemCacheController` is a memory-side cache (`num_caches`, `cache_num`); `memHierarchy.CoherentMemController` is a memory controller that supports cache shootdowns with the same parameter set as `MemController`.

## The shipped examples

1. `examples/example-1core-nocache.py`: standardCPU, standardInterface, MemController with `simpleMem`.
2. `example-1core-1level.py`: adds one L1 (`L1=1`, `coherence_protocol=MSI`, the default inclusive type).
3. `example-1core-3level.py`: three private levels on direct links.
4. `example-4core-shared-llc.py`: four `standardCPU` cores with `standardInterface`, four private L1s (`L1=1`, `mesi`, `lru`, 16KiB, 4-way, 3 cycles), a `Bus`, one shared L2 (384KiB, 12-way, 10 cycles), and a `MemController` with `simpleMem` (`access_time` 1000ns, 512MiB); links use `highlink`/`lowlink` ports with 500ps latency.
5. `example-4core-shared-distributed-llc.py`: the same cores and L1s, `bus0` fanning out to four L2 components configured as slices of one shared L2 (`num_cache_slices=4`, `slice_id` 0 to 3, `slice_allocation_policy=rr`), and `bus1` collecting them into one memory.

`testsuite_weekly_memHierarchy_examples.py` runs all five with a completion check only. For directory coherence over a network, start from `tests/testDistributedCaches.py` (eight cores with private L1s, a four-slice distributed shared L2, and two interleaved directories and memories with `simpleDRAM`, all on one Merlin single router); for a Kingsley mesh, `tests/testKingsley.py` behind `test_memHA_Kingsley`.

## Request types and who supports them

StandardMem defines `Read`, `Write`, `FlushAddr`, `FlushCache`, `ReadLock`/`WriteUnlock`, `LoadLink`/`StoreConditional`, `MoveData`, `CustomReq`/`CustomResp`, and `InvNotify`. Inside memHierarchy these become the `memTypes.h` commands (`GetS`, `GetX`, `GetSX`, `Write`, `FlushLine`, `FlushLineInv`, `FlushAll`, `PutS/M/E/X`, `Inv`, `Fetch`, `FetchInv`, and their responses). `standardCPU` generates each class by relative frequency: `read_freq` (75), `write_freq` (25), `flush_freq`, `flushinv_freq`, `flushcache_freq`, `llsc_freq`, `custom_freq`, plus `mmio_addr` for MMIO traffic and `noncacheableRangeStart/End`; `standardInterface` accepts `noncacheable_regions` as `[start0, end0, ...]`. `llsc_block_cycles` on a cache holds a line after a load-link. Custom commands reach a `MemController` through its `customCmdHandler` slot or the `customCmdHandler` parameter (the ELI spells it `customCmdMemHandler`); nothing is loaded by default and a custom event without a handler is fatal, so fill it with `memHierarchy.defCustomCmdHandler` or your own. `mmioEx` is the test MMIO device (`base_addr`, `iface` slot) used by the `StdMem_mmio*` cases. The reproduced `WriteUnlock::makeResponse` defect zeroes `vAddr` on locked writes ([validation](validation.md)).

## Scratchpads and other components

`memHierarchy.Scratchpad` (`clock`, `size`, `scratch_line_size`/`memory_line_size` (64B), `backing` (malloc), `memory_addr_offset` (size), `response_per_cycle`) sits between a `ScratchCPU` test generator (`scratchSize`, `maxAddr`, `reqsToIssue` (1000)) and memory, with `highlink`/`lowlink` ports (the `cpu`, `memory`, and `network` ports are deprecated); the `ScratchCache_1..4`, `ScratchDirect`, and `ScratchNetwork` memHA cases are its references. Fill its `backendConvertor` slot with `memHierarchy.simpleMemScratchBackendConvertor` as those tests do: the only registered scratch convertor has that name, while the parameter default in `scratchpad.cc` (`memHierarchy.scratchBackendConvertor`) and the ELI default text (`scratchpadBackendConvertor`) name unregistered spellings. `Sieve`, `MemoryManagerSieve`, and `BroadcastShim` form the Ariel malloc-profiling path tested by the Pin-gated memHSieve suite. `streamCPU` and `trivialCPU` are older test generators with `commFreq`/`memSize`/`num_loadstore`.

Next: [backends](backends.md) for timing, [extension points](extension-points.md) for new protocols or transports, [validation](validation.md) for the suites.
