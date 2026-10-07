**SST core correctness review — 2026-09-25**

Reviewed core `f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9` and elements `9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1`. This is a local functional review of simulation behavior, using element call sites to identify infrastructure mismatches. No tracked source changes, dependency installations, commits, or remote operations were made.

Eleven distinct correctness defects were reproduced. Their severity depends on the feature/configuration being exercised. P1 below means a crash, invalid model input, or corrupted restoration can occur under the stated trigger; P2 means incorrect values or configuration behavior. The reproductions exercise the real compiled core; element integration paths are identified separately. Full applications in sst-elements were not built or executed during the initial pass. A subsequent [element-impact follow-up](SST_CORE_ELEMENTS_IMPACT.md) runs the actual TrafficGen and basicStatistics implementations and narrows the claims for other findings.

| ID | Priority | Feature | Observed failure |
|---|---|---|---|
| F01 | P1 | Clock activation during a callback | Newly activated handler fires early; vector growth crashes the simulation |
| F02 | P1 | Shared/scoped parameters | Scoped extraction replaces local overrides with shared defaults |
| F03 | P1 | Discrete distributions | Returns an index outside the configured outcomes; shifts hotspot destinations |
| F04 | P1, conditional | Polymorphic unique_ptr serialization | Restores ExtendedRequest as Request and leaves bytes unread |
| F05 | P2 | StandardMem locked-write responses | makeResponse resets the virtual address in both request and response |
| F06 | P2 | Subcomponent statistic configuration | Re-enabling a named statistic loses new settings |
| F07 | P2 | Batched histogram samples | 100 samples produce NumItemsBinned=1 |
| F08 | P2 | Histogram origin | Non-aligned minvalue makes valid samples disappear from output bins |
| F09 | P2 | Floating-point histogram range | The final bin rejects valid fractional samples |
| F10 | P2 | Floating-point accumulator maximum | Negative-only data reports a tiny positive maximum |
| F11 | P2, limited current exposure | Accumulator variance API | Returns the unnormalized numerator instead of variance |

**F01 — Clock callbacks can invalidate their own dispatch loop**

Core: [clock.cc:324](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/clock.cc#L324), with the mutation at [clock.cc:226](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/clock.cc#L226).

`Clock::execute()` keeps a vector iterator across calls to user handlers. A callback can synchronously call another component/subcomponent, which calls `reregisterClock()`. That path pushes into the same `handlers_` vector. Growth invalidates the iterator used when dispatch resumes. Even without growth, the loop includes the newly appended handler in the current cycle, contrary to the next cycle returned by `reregisterClock()`.

Reproduction: register one active handler and sixteen dormant handlers at 1 GHz. From the first handler's cycle-1 callback, reactivate the sixteen dormant handlers. The actual core process exits with signal 11. A one-dormant-handler control avoids reallocation and prints:

```text
CLOCK main cycle=1
CLOCK promised=2
CLOCK other cycle=1
CLOCK main cycle=2
```

Element path: [cacheController.cc:101](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/cacheController.cc#L101) calls `sendOutgoingEvents()`, which calls `link_down_->send()` in [coherenceController.cc:390](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/coherencemgr/coherenceController.cc#L390). For a memory NIC, [memNIC.cc:121](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/memNIC.cc#L121) can re-register its clock synchronously when a send remains queued. The failure requires the caller and awakened handler to share the same core clock, and the crash also requires vector reallocation. This element path was traced, not executed as a full cache/NIC model.

Fix direction: defer additions/removals until dispatch completes, preserving the documented next-cycle semantics and stable handler indices. Cover activation while both the normal dispatch loop and the compaction loop are executing; add grouped-clock equivalents before assuming those are covered. Reserving more vector capacity alone does not fix early firing or mutation semantics.

**F02 — Scoped parameters reverse override precedence**

Core: [params.cc:218](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/params.cc#L218), especially the overwriting insertion at line 222. The ordinary lookup at [params.cc:35](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/params.cc#L35) stops at the first match.

The parameter search order is local parameters followed by shared sets in subscription order. `get_scoped_params()` walks that order but inserts every matching key using the default `overwrite=true`. The last shared set wins instead of the local value; shared-set precedence is also reversed.

Reproduction through the public Python configuration API: add global `backend.clock=1GHz`, subscribe the component, and set its local `backend.clock=2GHz`. In C++:

```text
params.find("backend.clock")                    -> 2GHz
params.get_scoped_params("backend").find("clock") -> 1GHz
```

Element impact: [memoryController.cc:125](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/memoryController.cc#L125) extracts backend settings; [cacheFactory.cc:424](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/cacheFactory.cc#L424) extracts NIC settings; [hr_router.cc:478](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/hr_router/hr_router.cc#L478) extracts port-control settings. Merlin's [pymerlin-base.py:854](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/pymerlin-base.py#L854) uses shared parameter sets. Combining shared defaults and local scoped overrides can silently simulate a different configuration from the one requested.

Fix direction: preserve first-match precedence during scoped extraction, e.g. non-overwriting inserts. Test local plus shared collisions, two shared sets, and nested scope extraction.

**F03 — DiscreteDistribution uses the wrong cumulative boundary**

Core: constructors at [discrete.h:49](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/rng/discrete.h#L49) and [discrete.h:71](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/rng/discrete.h#L71), sampling at [discrete.h:103](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/rng/discrete.h#L103).

The constructors store each interval's lower bound before adding that outcome's probability. Sampling searches for the first bound greater than or equal to the random value and returns that bound's index. For almost all draws, the result is shifted by one; the final interval returns `probCount`.

A deterministic RNG and probabilities `[0.25, 0.75]` produce:

| Uniform draw | Expected outcome index | Actual |
|---|---:|---:|
| 0.10 | 0 | 1 |
| 0.50 | 1 | 2 |
| 0.99 | 1 | 2 |

Element impact: [trafficgen.h:281](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/trafficgen/trafficgen.h#L281) passes a probability vector into this distribution; `getNextValue()` adds the minimum to the returned index. [trafficgen.cc:190](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/trafficgen/trafficgen.cc#L190) selects this generator for HotSpot. Thus hotspot selection shifts, and the last outcome can select the exclusive upper bound, including an invalid endpoint for a destination range.

The existing discrete-distribution reference output already contains shifted bin indices (`100` through `500` for five outcomes, because the test multiplies samples by 100). Its passing result does not establish correct indexing.

Fix direction: use cumulative upper bounds and a consistent half-open sampling rule. Test the first/last outcomes, exact boundaries, zero-probability entries, and a single-outcome distribution. Update reference outputs only after checking the mathematical contract.

**F04 — unique_ptr does not preserve the dynamic serializable type**

Core: [serialize_unique_ptr.h:137](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/serialization/impl/serialize_unique_ptr.h#L137) allocates `new OWNER_TYPE()`, and [serialize_unique_ptr.h:154](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/serialization/impl/serialize_unique_ptr.h#L154) serializes the referenced object without the raw polymorphic-pointer mechanism.

Packing invokes the derived object's virtual serializer. Unpacking constructs the static pointee type, so its serializer reads only the base fields. The restored object's dynamic type changes, and the stream cursor remains before the derived fields. A subsequent field would read the wrong bytes. An abstract static pointee type also cannot be constructed by this implementation.

Reproduction used the actual [ExtendedRequest.h](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/interfaces/ExtendedRequest.h), with a `reorder` metadata entry and sequence number 77, owned by `unique_ptr<SimpleNetwork::Request>`. Pointer tracking was enabled:

```text
unique_ptr<Request>: consumed 65 of 100 bytes; restored ExtendedRequest=false
raw Request*:        consumed 108 of 108 bytes; restored ExtendedRequest=true
```

A separate derived-Event probe has the same failure, so this is not specific to Merlin metadata.

Applicability: [networkService.h:103](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/networkService.h#L103) uses `unique_ptr<Request>`, and the ingress wrapper owns `unique_ptr<internal_router_event>`. Those wrappers themselves have no serializer. The current router serializes its processor as a raw pointer and its synthetic requester explicitly at [hr_router.cc:267](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/hr_router/hr_router.cc#L267). This review does **not** establish that the existing network-service checkpoint path hits the failing unique_ptr serializer. It establishes a concrete infrastructure trap if polymorphic owned state is serialized directly with `SST_SER`.

Fix direction: route serializable pointees through dynamic type construction and reconcile ownership with pointer tracking. Test a derived Event, the actual ExtendedRequest, a raw alias before/after the unique owner, null pointers, and a following sentinel field to detect incomplete stream consumption.

**F05 — WriteUnlock::makeResponse mutates the virtual address**

Core: [stdMem.h:857](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/interfaces/stdMem.h#L857).

The response constructor argument is `vAddr = 0`, an assignment expression. A request with virtual address `0x8000` has `vAddr==0` after `makeResponse()`, and the response also contains zero. Physical address and request ID preservation do not compensate for the lost virtual metadata.

Element impact: Vanadis constructs these requests with virtual-address information at [vbasiclsq.h:891](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/vanadis/lsq/vbasiclsq.h#L891). The memory interface calls the original request's `makeResponse()` at [standardInterface.cc:952](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/standardInterface.cc#L952). This causes incorrect response metadata and changes the saved request unexpectedly; downstream functional impact depends on the consumer.

Fix direction: pass `vAddr` without assigning to it. Test that creating a response preserves the request and copies ID, physical/virtual address, size, flags, instruction pointer, and thread ID.

**F06 — Re-enabling a subcomponent statistic writes to the wrong owner**

Core: [configComponent.cc:314](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/model/configComponent.cc#L314) and [configComponent.cc:328](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/model/configComponent.cc#L328).

On the first enable, a subcomponent puts its statistic into its ancestor's statistic map via `insertStatistic()`. On a repeated enable, it reuses the ID but updates its own `statistics_` map. Runtime lookup and configuration output use the ancestor's map, so newly provided parameters disappear.

Reproduction using the installed core SubCompReceiver:

```python
sub.enableStatistic('numRecv', {'rate': '10ns'})
sub.enableStatistic('numRecv', {'type': 'sst.HistogramStatistic', 'binwidth': 2})
```

Exported JSON still contains only `{'rate': '10ns'}`. The bounded simulation emits an Accumulator, despite the requested histogram. `type` and `binwidth` were new keys, so this is independent of any debate about overwriting existing parameter values.

Element impact: helper APIs such as [pymerlin-interface.py:84](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/interfaces/pymerlin-interface.py#L84) forward statistic enabling to subcomponents. A helper enabling a statistic and a later configuration layer adding its parameters can trigger this mismatch. No particular existing configuration was shown to make both calls.

Fix direction: resolve the statistic's owning map for both first and subsequent enable calls. Test repeated calls on top-level, one-level, and nested subcomponents, including export/reload behavior.

**F07 — Batched histogram samples undercount NumItemsBinned**

Core: [stathistogram.h:137](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/statapi/stathistogram.h#L137).

`addData_impl_Ntimes(N, value)` increments bin counts and sums by N, but increments `m_itemsBinnedCount` by one. For `addDataNTimes(100, 3)`:

```text
NumItemsCollected=100; NumItemsBinned=1; Bin0:0-9=100; Sum=300
```

Element impact: [cacheController.cc:216](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/cacheController.cc#L216), [directoryController.cc:682](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/directoryController.cc#L682), and [memBackendConvertor.cc:151](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/membackend/memBackendConvertor.cc#L151) use `addDataNTimes` to account for idle cycles. Configuring these statistics as histograms makes the summary disagree with the actual bin population and can invalidate derived utilization/distribution calculations.

Fix direction: increment the in-range binned count by N and define N=0 as a no-op. Compare batched additions against repeated individual additions, including out-of-range values.

**F08 — Histogram insertion ignores minvalue when choosing a bin**

Core: [stathistogram.h:143](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/statapi/stathistogram.h#L143), compared with output lookup at [stathistogram.h:313](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/statapi/stathistogram.h#L313).

Insertion uses `floor(value/binwidth)*binwidth`. Output names and looks up bins beginning at `minvalue + k*binwidth`. If minvalue is not aligned to a multiple of binwidth, these key sets do not match.

Reproduction: `minvalue=5`, `binwidth=10`, `numbins=2`; add 5 and 14. Both belong to bin `5-14`, but output says:

```text
NumItemsCollected=2; NumItemsBinned=2; NumActiveBins=2
Bin0:5-14=0; Bin1:15-24=0
```

Element usage: [basicStatistics2.py:73](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/simpleElementExample/tests/basicStatistics2.py#L73) demonstrates configurable histogram bounds. Its particular minimum is aligned, so that example avoids the bug. Any element statistic configured with an unaligned minimum can encounter it.

Fix direction: compute bins relative to minvalue. Test positive and negative unaligned minima, boundaries, and agreement between total binned samples and output bin sums. Avoid introducing floating-point precision loss for large integer counters while fixing the origin.

**F09 — Floating histograms apply an integer-only upper-bound rule**

Core: [stathistogram.h:208](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/statapi/stathistogram.h#L208), used by the out-of-bounds check at line 126.

The inclusive maximum is `minvalue + binwidth*numbins - 1` for every sample type. That works for integer values, but excludes part of the final bin for floating-point values. Core explicitly instantiates float/double histogram types.

Reproduction: a double histogram with `minvalue=0`, `binwidth=1`, `numbins=2`, given 1.5, reports `NumOutOfBounds-MaxValue=1`, `NumItemsBinned=0`, and an upper limit of 1. The natural final bin is `[1,2)`.

Element exposure: CramSim registers a double `txnsPerCycle` statistic at [c_TxnGen.cc:102](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/cramSim/c_TxnGen.cc#L102); simpleElementExample and the HMC backend also register floating statistics. The failure requires configuring such a statistic as a histogram with a sample in the rejected fractional interval; the default accumulator does not exercise it.

Fix direction: use a half-open numeric range internally, with consistent presentation for floating bins, while preserving integer configuration behavior. Test fractional samples near both edges and the exact exclusive upper boundary.

**F10 — Floating-point accumulator maxima initialize incorrectly**

Core: [stataccumulator.h:62](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/statapi/stataccumulator.h#L62), repeated in reset at [stataccumulator.h:167](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/statapi/stataccumulator.h#L167).

`numeric_limits<float/double>::min()` is the smallest positive normal value. It is not the most negative value. Therefore a stream containing only negative values, or only zero values, never updates the initial maximum.

Reproduction with double values `[-3,-1]`: `getMax()` returns `2.2250738585072014e-308`, and text output rounds that to `0.000000`; the correct maximum is -1. Resetting the statistic reintroduces the same defect.

Element exposure: floating statistics are used by simpleElementExample, CramSim, and the HMC power/thermal outputs. Actual impact requires all observed values to be nonpositive; no negative power/throughput workload is asserted here. All-zero intervals also have the wrong underlying maximum, though usual text formatting hides it.

Fix direction: initialize/reset with `numeric_limits<NumberBase>::lowest()`. Cover negative-only, zero-only, mixed-sign, and reset-then-negative streams.

**F11 — getVariance returns an unnormalized quantity**

Core: [stataccumulator.h:147](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/statapi/stataccumulator.h#L147), propagated by `getStandardDeviation()` at line 154.

The return expression is `sum_sq*count - sum*sum`, lacking the normalization. For `[-3,-1]`, it returns 4. Population variance is 1; sample variance is 2. The current result is neither. Standard deviation is consequently wrong too.

This was reproduced through the real registered accumulator and its public getter. The normal statistic output writes raw Sum/SumSQ/Count, so postprocessing those raw fields correctly is not affected by this getter defect. No caller of `getVariance()` or `getStandardDeviation()` was found in the elements checkout; current element exposure is therefore lower than the preceding findings.

Fix direction: establish/document the intended population or sample convention and implement its normalization with suitable intermediate precision. Test known distributions, constant values, zero/one samples, and numerical stability.

**Coverage and validation**

The core was exported into a temporary source tree and built with Apple clang/C++17 and the existing Python 3.14 installation. MPI, HDF5, and curses were disabled for this build. No dependencies were added. The probe library compiled with `-Wall -Wextra` without diagnostics. Production formatting/linting was not applicable because no tracked code changed; clang-format was not available.

| Existing test run | Discovered tests | Passed | Skipped | Failures |
|---|---:|---:|---:|---:|
| Primary, one thread | 146 | 134 | 12 | 0 |
| Clocks/links/shared/checkpoint, two threads | 102 | 91 | 11 | 0 |
| Additional component/output/module/partitioner/profiling/mempool/realtime coverage | 121 | 121 | 0 | 0 |

These are test invocations across overlapping selections, not 369 distinct tests. Skips chiefly cover MPI/repartitioning and tests restricted to serial execution. Exact test commands and logs are retained below. Passing reference tests do not negate the independently reproduced defects.

| Subsystem | Review performed and limits |
|---|---|
| Clocks, activation, event scheduling | Read dispatch/compaction/scheduling and element wake paths; reproduced F01; one/two-thread clock/link tests passed. Group mutation needs further focused coverage. |
| Links, polling, untimed init/complete | Read send/recv, default timebase, latency additions, ownership and restart routing; existing link/checkpoint tests passed. No additional confirmed link defect. |
| Time conversion and UnitAlgebra | Read rounding/range checks and component timebase behavior; UnitAlgebra and component tests passed. Not an exhaustive numerical proof. |
| Parameters and Python model setup | Traced shared/local/scoped precedence and statistic configuration; reproduced F02/F06; parameter and configuration round-trip suites passed. |
| Components, subcomponents, ELI, modules | Traced loading/port sharing/stat ownership and primary-component lifecycle; component/subcomponent/module tests passed. Reviewed paths do not cover every ELI combination. |
| SimpleNetwork and service envelopes | Read Request ownership, clone/invariant/serialization and Merlin wrapping/transport state; existing serialization tests passed. The documented shallow native-payload copy contract was not mislabeled as a new defect. |
| StandardMem | Inspected response constructors/conversion and traced locked writes; reproduced F05. Full Vanadis/memHierarchy workloads were not run. |
| Serialization and checkpointing | Read container/variant/optional/smart-pointer handling and restart reconstruction; reproduced F04 with real ExtendedRequest. Existing serialization and single/two-thread checkpoint suites passed. |
| Statistics and outputs | Read collection counts, accumulators, histograms, start/stop scheduling, outputs and configuration ownership; reproduced F06–F11; existing statistics/output tests passed. HDF5 was not built. |
| RNG/distributions | Read distribution construction/sampling and Merlin generators; reproduced F03; existing RNG tests passed. |
| Shared state and parallel synchronization | Read SharedArray/Map/Set publication/change exchange, link lookahead and serialization exchange; two-thread shared/link/checkpoint tests passed. MPI rank execution was not tested. |
| Partitioners, event queues, memory pools | Source inspection and selected partitioner/mempool tests; no additional confirmed element-triggered failure. Thread-safe queue empty-pop remains a follow-up below. |
| Primary termination and real-time/profiling controls | Read refcount/exit flow; existing real-time, profiling and relevant component tests passed. |
| IPC/tunnels | Inspected circular-buffer locking/capacity handling. No Ariel/Pin or external-process integration test was run. |
| Interactive inspection | Existing debug-console checkpoint tests were included by the checkpoint wildcard. Mapping mode was read for serialization types, not exhaustively exercised. |

This is broad subsystem coverage with deep checks of selected boundaries, not a claim that every core feature or element combination is bug-free.

**Source-review follow-ups, not counted as reproduced findings**

- [sharedArray.h:381](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/shared/sharedArray.h#L381): `mutex_read()` returns a reference after releasing the mutex. Audit whether supported concurrent resize/read callers can consume a dangling reference; a concurrency reproduction is still needed.
- [timeVortexPQ.cc:87](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/impl/timevortex/timeVortexPQ.cc#L87): the thread-safe specialization's empty `pop()` returns before unlocking. The branch is visible, but a supported normal simulation path reaching it was not established.
- [objectComms.h:123](https://github.com/sstsimulator/sst-core/blob/f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9/src/sst/core/objectComms.h#L123): size exchange copies `sizeof(int)` bytes from a `size_t`, then uses int counts/displacements. Large-message limits and endianness assumptions need an MPI-specific review/run.
- Polymorphic shared_ptr handling, stateful container comparators, and callback-driven grouped-clock changes deserve separate round-trip/dispatch probes. No conclusion was inferred solely from the unique_ptr result.

**Suggested repair order**

1. F01 clock dispatch mutation, then F02 parameter precedence and F03 discrete sampling: these have direct paths to active element behavior.
2. F05 StandardMem response metadata and F06 subcomponent stat ownership.
3. F07–F10 statistic correctness; add mathematical invariants alongside reference-file tests.
4. F04 before adding direct smart-pointer checkpointing to polymorphic service state; verify current checkpoint paths explicitly before broad changes.
5. F11 variance API normalization, with an explicit convention and caller audit.

Each item should be fixed separately with focused behavioral tests. The report records proposed directions; no fixes have been applied.

**Reproduction artifacts and commands**

Temporary build: `/tmp/sst-core-audit.Cekb9v`; installed executable: `/tmp/sst-core-audit.Cekb9v/install/bin/sst`. Probe sources, logs, JSON output, and runner: `/tmp/sst-audit-probes`. These temporary files may be removed by OS cleanup; the complete probe sources are embedded below for retention.

```sh
# After exporting this core revision into the temporary source directory:
./autogen.sh
./configure --prefix="$PWD/install" --disable-mpi --disable-curses --disable-hdf5 \
  --with-python=/opt/homebrew/bin/python3-config
make -j6
make install

# Build the external probe on the reviewed macOS host:
clang++ -std=c++17 -g -O0 -Wall -Wextra -shared -undefined dynamic_lookup \
  -I/tmp/sst-core-audit.Cekb9v/src \
  -I/Users/nbutche/Documents/GitHub/inc-testing/sst-elements/src \
  /tmp/sst-audit-probes/audit.cc -o /tmp/sst-audit-probes/libaudit.so
python3 /tmp/sst-audit-probes/run_probes.py
```

The runner exits successfully when it observes the listed defects and passing controls. This means the reproduction succeeded, not that the core behavior is correct. Every subprocess has a 15-second timeout and models have finite stop times.

Existing suite selections:

```sh
/tmp/sst-core-audit.Cekb9v/install/bin/sst-test-core -q \
  -o /tmp/sst-audit-probes/baseline \
  -w '*Clocks' '*Links' '*Serialization' '*ParamComponent' '*StatisticsComponent' \
     '*RNGComponent' '*UnitAlgebra' '*SharedObject' '*SubComponent' '*Checkpoint' '*config_input_output'
/tmp/sst-core-audit.Cekb9v/install/bin/sst-test-core -q -t 2 \
  -o /tmp/sst-audit-probes/threaded -w '*Clocks' '*Links' '*SharedObject' '*Checkpoint'
/tmp/sst-core-audit.Cekb9v/install/bin/sst-test-core -q \
  -o /tmp/sst-audit-probes/secondary \
  -w '*partitioner' '*Component' '*Output' '*Module' '*PortModule' '*profiling' '*MemPoolTest' '*RealTime'
```

**Retained source: audit.cc**

```cpp
#include <sst/core/component.h>
#include <sst/elements/merlin/interfaces/ExtendedRequest.h>
#include <sst/core/interfaces/stdMem.h>
#include <sst/core/interfaces/simpleNetwork.h>
#include <sst/core/rng/discrete.h>
#include <sst/core/statapi/stataccumulator.h>
#include <sst/core/serialization/serialize.h>
#include <cstdio>
#include <memory>
#include <vector>

using namespace SST;

class FixedRNG : public RNG::Random {
public:
    double value = 0.5;
    double nextUniform() override { return value; }
    uint32_t generateNextUInt32() override { return 0; }
    uint64_t generateNextUInt64() override { return 0; }
    int32_t generateNextInt32() override { return 0; }
    int64_t generateNextInt64() override { return 0; }
    ImplementSerializable(FixedRNG)
};

class AuditEvent : public Event {
public:
    int extra = 42;
    void serialize_order(Core::Serialization::serializer& ser) override {
        Event::serialize_order(ser);
        SST_SER(extra);
    }
    ImplementSerializable(AuditEvent)
};

template<class T> void roundtrip(T& input, T& output) {
    Core::Serialization::serializer ser;
    ser.enable_pointer_tracking();
    ser.start_sizing();
    SST_SER(input);
    std::vector<char> buffer(ser.size());
    ser.start_packing(buffer.data(), buffer.size());
    SST_SER(input);
    ser.start_unpacking(buffer.data(), buffer.size());
    SST_SER(output);
    printf("serializer bytes consumed=%zu buffer=%zu\n", ser.size(), buffer.size());
    ser.finalize();
}

class Audit : public Component {
public:
    SST_ELI_REGISTER_COMPONENT(Audit, "audit", "Probe", SST_ELI_ELEMENT_VERSION(1,0,0), "Audit probe", COMPONENT_CATEGORY_UNCATEGORIZED)
    SST_ELI_DOCUMENT_PARAMS({"mode", "Probe mode", "basic"})
    SST_ELI_DOCUMENT_STATISTICS(
        {"batch", "Batched samples", "items", 1},
        {"offset", "Offset bins", "items", 1},
        {"floating", "Floating bins", "items", 1},
        {"accum", "Accumulator", "items", 1})
    Audit(ComponentId_t id, Params& p) : Component(id) {
        mode = p.find<std::string>("mode", "basic");
        if (mode == "basic") {
            Params q = p;
            printf("PARAM direct=%s scoped=%s expected=2GHz,2GHz\n", q.find<std::string>("backend.clock").c_str(), q.get_scoped_params("backend").find<std::string>("clock").c_str());
            FixedRNG rng;
            const double probabilities[] = {0.25, 0.75};
            RNG::DiscreteDistribution d(probabilities, 2, &rng);
            for (double value : {0.1, 0.5, 0.99}) {
                rng.value = value;
                printf("DISCRETE u=%g index=%g expected=%d\n", value, d.getNextDouble(), value < .25 ? 0 : 1);
            }
            Interfaces::StandardMem::WriteUnlock request(0x1000, 1, {7}, false, 0, 0x8000);
            std::unique_ptr<Interfaces::StandardMem::Request> response(request.makeResponse());
            auto* w = dynamic_cast<Interfaces::StandardMem::WriteResp*>(response.get());
            printf("WRITE_UNLOCK request=%llx response=%llx expected=8000,8000\n", (unsigned long long)request.vAddr, (unsigned long long)w->vAddr);
            auto* batch = registerStatistic<uint64_t>("batch");
            batch->addDataNTimes(100, 3);
            auto* offset = registerStatistic<uint64_t>("offset");
            offset->addData(5);
            offset->addData(14);
            auto* floating = registerStatistic<double>("floating");
            floating->addData(1.5);
            auto* stat = dynamic_cast<Statistics::AccumulatorStatistic<double>*>(registerStatistic<double>("accum"));
            stat->addData(-3.0);
            stat->addData(-1.0);
            printf("ACCUM max=%.17g variance=%g expected=-1,1\n", stat->getMax(), stat->getVariance());
        } else if (mode == "unique_request") {
            std::unique_ptr<Interfaces::SimpleNetwork::Request> input = std::make_unique<Merlin::ExtendedRequest>();
            static_cast<Merlin::ExtendedRequest*>(input.get())->setMetadata("reorder", Merlin::ReorderMetadata(77));
            std::unique_ptr<Interfaces::SimpleNetwork::Request> output;
            roundtrip(input, output);
            printf("UNIQUE_REQUEST extended=%d expected=1\n", dynamic_cast<Merlin::ExtendedRequest*>(output.get()) != nullptr);
        } else if (mode == "raw_request") {
            Interfaces::SimpleNetwork::Request* input = new Merlin::ExtendedRequest();
            static_cast<Merlin::ExtendedRequest*>(input)->setMetadata("reorder", Merlin::ReorderMetadata(77));
            Interfaces::SimpleNetwork::Request* output = nullptr;
            roundtrip(input, output);
            printf("RAW_REQUEST extended=%d expected=1\n", dynamic_cast<Merlin::ExtendedRequest*>(output) != nullptr);
            delete input;
            delete output;
        } else if (mode == "unique") {
            std::unique_ptr<Event> input = std::make_unique<AuditEvent>();
            std::unique_ptr<Event> output;
            roundtrip(input, output);
            printf("UNIQUE derived=%d expected=1\n", dynamic_cast<AuditEvent*>(output.get()) != nullptr);
        } else if (mode == "raw") {
            Event* input = new AuditEvent();
            Event* output = nullptr;
            roundtrip(input, output);
            printf("RAW derived=%d expected=1\n", dynamic_cast<AuditEvent*>(output) != nullptr);
            delete input;
            delete output;
        } else if (mode == "clock" || mode == "clock_one") {
            registerAsPrimaryComponent();
            primaryComponentDoNotEndSim();
            main_handler = new Clock::Handler<Audit, &Audit::tick>(this);
            tc = registerClock("1GHz", main_handler);
            for (int i = 0; i < (mode == "clock_one" ? 1 : 16); ++i) {
                auto* handler = new Clock::Handler<Audit, &Audit::other>(this);
                registerClock("1GHz", handler);
                unregisterClock(tc, handler);
                sleeping.push_back(handler);
            }
        }
    }
    bool tick(Cycle_t cycle) {
        printf("CLOCK main cycle=%llu\n", (unsigned long long)cycle);
        fflush(stdout);
        if (cycle == 1) {
            for (auto* h : sleeping) printf("CLOCK promised=%llu\n", (unsigned long long)reregisterClock(tc, h));
        }
        if (cycle == 2) { primaryComponentOKToEndSim(); return true; }
        return false;
    }
    bool other(Cycle_t cycle) {
        printf("CLOCK other cycle=%llu\n", (unsigned long long)cycle);
        return true;
    }
private:
    std::string mode;
    TimeConverter tc;
    Clock::HandlerBase* main_handler = nullptr;
    std::vector<Clock::HandlerBase*> sleeping;
};
```

**Retained source: probe.py**

```python
import sst
import sys
c = sst.Component('probe', 'audit.Probe')
sst.addGlobalParams('audit-defaults', {'backend.clock':'1GHz'})
c.addGlobalParamSet('audit-defaults')
c.addParam('backend.clock', '2GHz')
c.addParam('mode', sys.argv[1] if len(sys.argv) > 1 else 'basic')
sst.setStatisticLoadLevel(1)
sst.setStatisticOutput('sst.statOutputConsole')
c.enableStatistic('batch', {'type':'sst.HistogramStatistic', 'minvalue':0, 'binwidth':10, 'numbins':2})
c.enableStatistic('offset', {'type':'sst.HistogramStatistic', 'minvalue':5, 'binwidth':10, 'numbins':2})
c.enableStatistic('floating', {'type':'sst.HistogramStatistic', 'minvalue':0, 'binwidth':1, 'numbins':2})
c.enableStatistic('accum')
```

**Retained source: substats.py**

```python
import sst
import sys
c = sst.Component('loader', 'coreTestElement.SubComponentLoader')
s = c.setSubComponent('mySubComp', 'coreTestElement.SubCompReceiver')
s.enableStatistic('numRecv', {'rate':'10ns'})
if len(sys.argv) > 1 and sys.argv[1] == 'twice':
    s.enableStatistic('numRecv', {'type':'sst.HistogramStatistic', 'binwidth':2})
a = sst.Component('sender', 'coreTestElement.SubComponentLoader')
t = a.setSubComponent('mySubComp', 'coreTestElement.SubCompSender')
t.addParam('sendCount', 3)
sst.Link('wire').connect((t, 'sendPort', '1ns'), (s, 'recvPort', '1ns'))
sst.setStatisticLoadLevel(1)

sst.setProgramOption('stop-at', '30ns')
```

**Retained source: run_probes.py**

```python
import json
from pathlib import Path
import subprocess

root = Path('/tmp/sst-audit-probes')
sst = '/tmp/sst-core-audit.Cekb9v/install/bin/sst'
results = {}
for mode in ['basic', 'raw', 'unique', 'raw_request', 'unique_request', 'clock_one', 'clock']:
    with (root / (mode + '.log')).open('w') as log:
        p = subprocess.run([sst, '--add-lib-path=' + str(root), '--stop-at=5ns', str(root / 'probe.py'), '--', mode], stdout=log, stderr=subprocess.STDOUT, timeout=15)
    results[mode] = {'exit': p.returncode, 'output': (root / (mode + '.log')).read_text()}
with (root / 'substats.log').open('w') as log:
    p = subprocess.run([sst, '--output-json=' + str(root / 'substats.json'), str(root / 'substats.py'), '--', 'twice'], stdout=log, stderr=subprocess.STDOUT, timeout=15)
params = json.loads((root / 'substats.json').read_text())['components'][0]['subcomponents'][0]['statistics'][0]['params']
results['substats'] = {'exit': p.returncode, 'params': params}
(root / 'results.json').write_text(json.dumps(results, indent=2))
basic = results['basic']['output']
checks = {
    'clock wake crashes': results['clock']['exit'] in [-11, 139],
    'clock wake fires before returned next cycle': 'CLOCK promised=2\nCLOCK other cycle=1' in results['clock_one']['output'],
    'scoped precedence reversed': 'direct=2GHz scoped=1GHz' in basic,
    'discrete index out of range': 'u=0.5 index=2 expected=1' in basic,
    'write unlock loses virtual address': 'request=0 response=0 expected=8000,8000' in basic,
    'batched histogram count wrong': 'NumItemsCollected.u64 = 100; NumItemsBinned.u64 = 1;' in basic,
    'offset histogram bins empty': 'Bin0:5-14.u64 = 0; Bin1:15-24.u64 = 0;' in basic,
    'floating histogram sample excluded': 'NumOutOfBounds-MaxValue.u64 = 1; Bin0:0-0' in basic,
    'floating accumulator max wrong': 'max=2.2250738585072014e-308' in basic,
    'accumulator variance wrong': 'variance=4 expected=-1,1' in basic,
    'unique pointer loses ExtendedRequest type': 'UNIQUE_REQUEST extended=0' in results['unique_request']['output'],
    'raw pointer preserves ExtendedRequest type': 'RAW_REQUEST extended=1' in results['raw_request']['output'],
    'repeated subcomponent statistic loses new parameters': params == {'rate':'10ns'},
}
for name, confirmed in checks.items():
    print(('CONFIRMED ' if confirmed else 'UNEXPECTED ') + name)
if not all(checks.values()):
    raise SystemExit(1)
```

**Observed probe summary**

```text
CONFIRMED clock wake crashes
CONFIRMED clock wake fires before returned next cycle
CONFIRMED scoped precedence reversed
CONFIRMED discrete index out of range
CONFIRMED write unlock loses virtual address
CONFIRMED batched histogram count wrong
CONFIRMED offset histogram bins empty
CONFIRMED floating histogram sample excluded
CONFIRMED floating accumulator max wrong
CONFIRMED accumulator variance wrong
CONFIRMED unique pointer loses ExtendedRequest type
CONFIRMED raw pointer preserves ExtendedRequest type
CONFIRMED repeated subcomponent statistic loses new parameters
```
