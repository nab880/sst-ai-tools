---
{
  "type": "SST Guide",
  "title": "Component and event contracts",
  "description": "Locate lifecycle, registration, ownership, and serialization contracts.",
  "tags": [
    "core",
    "ownership"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:06:46.837545+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/interfaces/simpleNetwork.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/interfaces/simpleNetwork.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "36f3eda75ec37357c11c147a3346c6b23b07f1627156cb2502febec3d0733e7f"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/component.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/component.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "a19f764dda8bc2f128b21c6752a17d30cf7dcde7c4c00fbfdb38f872e87142d2"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleElementExample/basicEvent.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleElementExample/basicEvent.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "1e6d7c471f31af4649c94d252f206f0fac3d622a02aa5abfc79a89f19d067f5b"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/baseComponent.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/baseComponent.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "e3397e8b63f765bfedfd29cb9eed1db652b33f5c47071d1d3dd105a28c1ed000"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/event.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/event.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "e676ee994bf509f442634b5360833a97b7ab2fc9db9a5a0beb95b7bcf50b2146"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/portModule.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/portModule.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "284ef4c28362ccc7fbe274cb2efd36ee52e5e127e618d5c46f045e97301054d2"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/clock.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/clock.cc",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "4dd4d639b0892c7fcecd5e75197c4861ed20d5351cfe517422effa84afa89e36"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/params.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/params.cc",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "693b79ba6a17d4a46df431b1ca134edcfbf407e98cc088467f8526b40d6af65e"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/interfaces/stdMem.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/interfaces/stdMem.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "0774a9fdbd647d6ed9375f3c6a686fac54e9d998aac2100a41fd45f7712bc8c4"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/serialization/impl/serialize_unique_ptr.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/serialization/impl/serialize_unique_ptr.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "d34b926951cf0c3f462f26e99a32b857676a7859e912b9c0dd8506529da5b504"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/interfaces/linkControl.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/interfaces/linkControl.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "d61c8793dd5133afa155d7b84f49e02d1be71f1f9d18a29850cac2b5de4600ce"
    }
  ]
}
---

# Component and event contracts

Use these source entry points rather than loading core recursively:

- `src/sst/core/component.h` and `baseComponent.h`: component services, links, clocks, subcomponents, and primary-component termination. `registerOrderedClock()` (added in core PR #1632) places handlers in a `Clock::Group` that fires them in registration order for a given frequency, while plain `registerClock`/`reregisterClock` handlers use the flat handler vector; the two paths have separate activation code.
- `src/sst/core/event.h`: event interface and serialization.
- `src/sst/core/interfaces/simpleNetwork.h`: network requests; request destruction deletes its attached payload. `takePayload()` transfers the payload; `inspectPayload()` does not.
- `src/sst/core/interfaces/stdMem.h`: the StandardMem request/response contract.
- Elements `simpleElementExample/basicSimLifeCycle.cc`: initialization, setup, timed execution, completion, and finish examples.
- Elements `simpleElementExample/basicEvent.h`: custom event serialization.

Distinguish untimed initialization traffic from timed traffic. Trace ownership at each send, queue, receive, retry, and destruction; inspect the actual interface's success/failure contract rather than assuming all send APIs transfer ownership identically. Preserve units and the distinction between virtual networks and virtual channels.

For example, Merlin `LinkControl::send` owns the request after success and retains caller ownership after failure. There are two failure states: a VN out of range returns false before any mutation, whereas an insufficient-credit failure occurs after `vn` has been rewritten and `dest` translated through the NID map; retained ownership does not promise an unchanged request. Validate VN bounds before calling `spaceToSend`, and inspect address remapping when designing retries.

`PortModule` is an interception/serialization interface, not a `BaseComponent`: it has no component `init`, `setup`, or `finish` callback. Its header marks the API as not final until the SST 15 release and notes known performance issues for send-side attachment, so prefer receive-side interception. Defining an `init(unsigned)` method in a derived injector does not make core call it. When canceling receive delivery, the interceptor must delete the event and set its pointer to null; replacing an event requires copying its delivery information before deleting the original. See `portModule.h` for both send and receive contracts.

For checkpointable state, call the base `serialize_order`, include required members and event state, and follow the adjacent implementation's serialization registration. Validate restart behavior before claiming checkpoint support.

On the reassessed devel revisions (core `09bc3927`, elements `47b99537`), focused probes reproduced these contract defects:

- Reactivating a dormant clock handler from inside a callback can invoke it too early or crash when handler storage grows. Exercise callback-time mutation explicitly before relying on it.
- `get_scoped_params` can reverse local/shared parameter precedence. Check the effective scoped value when using global parameter sets and local overrides.
- Serializing a polymorphic object through `std::unique_ptr<Base>` can lose its dynamic type and leave unread bytes. Test dynamic type, derived state, and complete stream consumption; passing raw-pointer controls do not validate unique-pointer serialization.
- `StandardMem::WriteUnlock::makeResponse` assigns zero to the request's `vAddr` and passes zero to the response. Check virtual-address metadata where consumers require it; this probe alone does not establish incorrect physical-memory writes.

These observations constrain affected paths, not every use of clocks, parameters, requests, or checkpointing. Full repository evidence is in `reviews/core/2026-10-06/index.md`; it may be absent from an installed knowledge bundle. Use the relevant focused regression when fixing or depending on a path.
