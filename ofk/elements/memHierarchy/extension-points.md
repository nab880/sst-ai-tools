---
{
  "type": "SST Guide",
  "title": "memHierarchy extension boundaries",
  "description": "Keep timing, request translation, and coherence behavior in their existing layers.",
  "tags": [
    "memHierarchy",
    "extension"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T09:15:51.331624+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/simpleMemBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/simpleMemBackend.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "bcaf188f435c1d3daeadab9cb5aaf2bae17da9420f1b622a122298bf03fbd9f9"
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
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/replacementManager.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/replacementManager.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "a844338e246d8eb5613cb5ae547682f919d809cc088950cf2353170db053d9c6"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/memBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/memBackend.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "5460dadfccd92f7cea436d1fe6d1f70f13bd24470fcf9b0a360dc6e825b9d944"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/memBackendConvertor.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/memBackendConvertor.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "db3a7d3ccca91b72f601ae7fa4382c6c51a5ec768cb90953debb5265e4f9e221"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/simpleMemBackendConvertor.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/simpleMemBackendConvertor.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "1466e78f899e733a4afe9b6f1c3f95268f94c6caf12236afe1e531083dab5418"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memoryController.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memoryController.cc",
      "x-sha256": "3229cea5bf28f6d1ee083169a947215b0dbc704710ed7803436ce1a28e32ff29",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/simpleMemBackend.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/simpleMemBackend.cc",
      "x-sha256": "7a67e616695c0bdb79dc25bbd5f77e092f6c1699cdfe27c50a94b8d4b4e0be1f",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/coherencemgr/coherenceController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/coherencemgr/coherenceController.h",
      "x-sha256": "f608d24be6ec2bacb5b0517f453322f024063721dff84fb0b3e0d09954d5821d",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/coherencemgr/MESI_Directory.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/coherencemgr/MESI_Directory.h",
      "x-sha256": "2a9368dbfdd11c5599e4791bc9df27a09cf190861cd32b9f91cd98bdda4783b3",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/hash.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/hash.h",
      "x-sha256": "b04ee8a8a986dd206e954d4a9dba4578f3ca0d807a50632837c0369cb0153e42",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s11",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/cacheListener.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/cacheListener.h",
      "x-sha256": "7baa6bd903c043554857487d46364be1cf36acd2e2747a54165e1ed64c2ffb43",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s12",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/customcmd/customCmdMemory.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/customcmd/customCmdMemory.h",
      "x-sha256": "105972d4c32ade19fd7e9c68c7821efa348b2c15d538aac5acad9e45587ffe03",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s13",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/customcmd/defCustomCmdHandler.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/customcmd/defCustomCmdHandler.h",
      "x-sha256": "35d0d6e015d08be430f56bff56594a5a522e34121278b7a2cd0e85e9fca05829",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s14",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memEventCustom.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memEventCustom.h",
      "x-sha256": "f0e2e5a968b169a60cbe25e5ddf8836f20a6f50a96b346db621a7136b9f37688",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s15",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memLinkBase.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memLinkBase.h",
      "x-sha256": "73d853c83012d657d6fda789bc833c4845240a38270fcbdeec898ab9864855cd",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s16",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memNICBase.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memNICBase.h",
      "x-sha256": "5a73e9c4ff87e9f5a976d64fddd6109dd2b3b12ba49b79e24a787d6632a52f8f",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s17",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memNIC.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memNIC.h",
      "x-sha256": "722ba9575b4d5e02b34c6223a60ce6c3f5c618f63f3cf9b60e40863c5b201a5c",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s18",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memNICFour.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memNICFour.h",
      "x-sha256": "1397cc780652498ae330c178883e6ef8ed9080f00681c203a3ad9819f6eea12a",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s19",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memEventBase.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memEventBase.h",
      "x-sha256": "f9b0c0a7b1007f77f155ce703ecbf615e0745fedf8dea976067d093a3c107240",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s20",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memEvent.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memEvent.h",
      "x-sha256": "e7263e82d893557e2c9f2453df5d7dbddc94434dcdfe59bea3bd32fd740250db",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s21",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/moveEvent.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/moveEvent.h",
      "x-sha256": "840231a053d0ef6f670091222d866b0689e57599b57ca33c935c3cfdcb79ffac",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s22",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/memTypes.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/memTypes.h",
      "x-sha256": "5ca515f68cf2dcd9542281a5f21ca50ba27c936866853b8a11e808fd2e717b34",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s23",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/cacheController.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/cacheController.h",
      "x-sha256": "441c5e2f7f2a7a43121573eca67bec3eba3fd30d4dd3b44363227f4c10027006",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s24",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/Makefile.am",
      "x-sha256": "0aa84e22bf953e62466fc78d9451001d5138756f70645f5da8276ac27982f3ea",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s25",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/configure.m4",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/configure.m4",
      "x-sha256": "0041644bcc9a489c2c803a214300b597e81af751b1f513ff08d09ba6fd848dcd",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s26",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/delayBuffer.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/delayBuffer.h",
      "x-sha256": "e329895bb2d3cd8d6e4cc027d35c0f40c92d1bc7cb93ee898a1520f698a56815",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s27",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/requestReorderSimple.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/requestReorderSimple.h",
      "x-sha256": "48819c1e4df153f8bab4fad062c90f3bf3b6e77a708ef4d2c5c255dfa8ab2d1d",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s28",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/requestReorderByRow.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/requestReorderByRow.h",
      "x-sha256": "44ba08b30e741f7cb878338381c33f462be075b6fda3650dd454ff6aa1cf56d6",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s29",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/goblinHMCBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/goblinHMCBackend.h",
      "x-sha256": "af1fef73987f2e3f9d6f14cccb633b38e6b31b70da5f3a1ec62744724bd2f9f7",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s30",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/ramulatorBackend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/ramulatorBackend.h",
      "x-sha256": "e9f1fde7a92f05d52fa6ef2d784ebe7082d0f5995d14607406a7787d4c940a22",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s31",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/membackend/ramulator2Backend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/membackend/ramulator2Backend.h",
      "x-sha256": "46c0f8bd658e7ec5587a2996164a1256b5fb8bb40b15dac9006652f9239e8397",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s32",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/directoryController.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/directoryController.cc",
      "x-sha256": "6fe8e247fa22eb799c2cdf40a16165bd48f8ec9ecea8a2bb9f31af10fb1c18c3",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---
# memHierarchy extension boundaries

| Behavior | Source entry point |
|---|---|
| Constant or detailed memory access timing | `membackend/simpleMemBackend.h`, then `membackend/memBackend.h` and the matching convertor |
| Cache/coherence transitions | `cacheController.h`, `coherencemgr/` |
| Replacement behavior | `replacementManager.h` and concrete policies |
| Address hashing | `hash.h` |
| Prefetching and observation | `cacheListener.h` |
| Custom memory commands | `customcmd/customCmdMemory.h`, `memEventCustom.h` |
| StandardMem request translation | `standardInterface.h`, core `interfaces/stdMem.h` |
| Network transport | `memNICBase.h`, `memNIC.h`, `memLinkBase.h` |
| Events and commands | `memEventBase.h`, `memEvent.h`, `moveEvent.h`, `memTypes.h` |

Do not change coherence semantics to implement only backend timing. For a protocol change, establish legal states/transitions, outstanding request tracking, responses, retries, and writeback behavior from the selected existing controller. Trace address ranges, line alignment, and request IDs end to end.

## Backends

`membackend/simpleMemBackend.h` registers `memHierarchy.simpleMem` and is a concrete timing example, not the backend API definition. `memBackend.h` defines `SimpleMemBackend` for timing requests, `FlagMemBackend` for requests carrying flags, and `ExtMemBackend` for additional instruction/custom data. Match `getBackendConvertorType()` to the chosen API. A false `issueRequest` return means the convertor retains the work for retry; complete accepted requests through the matching `handleMemResponse` callback. The convertor splits requests and enforces the per-cycle cap, but both limits are backend parameters (`request_width`, `max_requests_per_cycle`, read through `getRequestWidth()`/`getMaxReqPerCycle()`), and the split width is the smaller of the backend and controller widths; distinguish backend transactions from CPU request counts. The controller selects the convertor solely from `getBackendConvertorType()`. `simpleMem` overrides `max_requests_per_cycle` to 1 and is unclocked, and `MemBackend::issueCustomRequest` fatals unless a backend overrides it. Wrapping backends (`DelayBuffer`, `reorderSimple`, `reorderByRow`) show how to compose a new policy around an existing timing model through a `backend` slot; external simulators (`goblinHMC`, `ramulator`, `ramulator2`) are guarded by configure conditionals in `Makefile.am` and `configure.m4`.

## Coherence managers

A cache fills its `coherence` slot automatically from `L1`, `cache_type`, and `coherence_protocol`; the registered managers are `coherence.mesi_l1`, `coherence.mesi_inclusive`, `coherence.mesi_private_noninclusive`, `coherence.mesi_shared_noninclusive`, `coherence.incoherent`, and `coherence.incoherent_l1`. `coherencemgr/MESI_Directory.{h,cc}` exists in the tree but is not a registered manager; `directoryController.cc` implements its MESI/MSI logic inline and notes that it will eventually move into a coherence manager. `coherencemgr/coherenceController.h` (constructor `(Params&, bool)`) declares one virtual handler per command (`handleGetS`, `handleGetX`, `handleGetSX`, `handleWrite`, `handlePutS/E/M/X`, `handleFlushLine`, `handleFlushLineInv`, `handleFlushAll`, `handleForwardFlush`, `handleFetch`, `handleInv`, and the rest of the `memTypes.h` table), each taking the event and whether it came from the MSHR. A new protocol derives from `CoherenceController`, implements the handlers for every command it can receive, and must be selectable from the cache's parameter logic; the ELI says not to fill the slot directly. `memTypes.h` is an X-macro table listing each command's response, request class, and data flags; add commands there, in the event classes, and in every manager that must ignore or handle them.

## Replacement, hashing, listeners, custom commands

- `ReplacementPolicy` (`replacementManager.h`, constructed with `(uint64_t, uint64_t)`): `checkCompatibility(ReplacementInfo*)`, `update(id, info)`, `replaced(id)`, `getBestCandidate()`, `findBestCandidate(vector<ReplacementInfo*>&)`; `ReplacementInfo`/`CoherenceReplacementInfo` carry line state and are serializable. Registered: `replacement.lru`, `lfu`, `mru`, `nmru`, `random` and the `-opt` variants.
- `HashFunction` (`hash.h`): `hash(ID, value)`; registered `hash.none`, `hash.linear`, `hash.xor`, selected through the `hash` slot.
- `CacheListener` (`cacheListener.h`): `notifyAccess(const CacheListenerNotification&)`, `registerResponseCallback(handler)`, `printStats(Output&)`. A listener in the `prefetcher` slot may issue requests through the callback; one in the `listener` slot cannot. Cassini's prefetchers are the concrete examples.
- `CustomCmdMemHandler` (`customcmd/customCmdMemory.h`): `receive(MemEventBase*)` returning `MemEventInfo` and `ready(MemEventBase*)` returning `StandardMem::CustomData*`; loaded into a controller's `customCmdHandler` slot or named by the `customCmdHandler` parameter; nothing loads by default, and a third pure virtual, `finish(MemEventBase*, uint32_t)`, completes the handler contract. `defCustomCmdHandler` is the shipped implementation, paired with the custom memory event and StandardMem `CustomReq`.

## Transports

`MemLinkBase` (`memLinkBase.h`) is the link-manager API: `sendUntimedData`, `setRecvHandler`, `isClocked`, the `init`/`complete`/`setup`/`finish` lifecycle, and status printing. `MemNICBase` adds endpoint discovery (`addSource`, group/source/destination bookkeeping) over `SimpleNetwork`; `MemNIC` and `MemNICFour` are its registered forms. A new transport implements `MemLinkBase`'s pure virtuals (`send`, `recvUntimedData`, `findTargetDestination`, `getTargetDestination`, `getAvailableDestinationsAsString`, the `getSources`/`getDests`/`getPeers` accessors, and `isDest`/`isSource`/`isPeer`/`isReachable`), preserves untimed-phase region/endpoint exchange (`MemEventInit`, `MemEventInitCoherence`, `MemEventInitEndpoint`, `MemEventInitRegion`), and is selected by filling the `highlink`/`lowlink` slot.

## Events

`MemEventBase` is the serializable base; `MemEvent` carries command, addresses, payload, and flags; `MoveEvent` and the custom event in `memEventCustom.h` cover data movement and custom commands. All are `ImplementSerializable`; keep that when adding fields so checkpoints stay valid ([checkpoint and restart](../../using-sst/checkpoint.md)).

Update `Makefile.am` and registration for new sources, keep the element's statistics declared (`SST_ELI_DOCUMENT_STATISTICS` in `cacheController.h` is the model), and follow [validation](validation.md).
