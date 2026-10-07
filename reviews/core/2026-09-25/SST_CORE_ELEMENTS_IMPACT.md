**Concrete sst-elements impact of the core review — 2026-09-25**

This follow-up distinguishes observed behavior in compiled element code from traced call paths and configuration-dependent exposure. It uses the same revisions as `SST_CORE_CORRECTNESS_REVIEW.md`. Tracked source is unchanged.

**Observed using actual element implementations**

1. **F03: Merlin HotSpot sends to the wrong endpoint.**

   [trafficgen.cc:190](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/trafficgen/trafficgen.cc#L190) constructs `DiscreteDist`; [trafficgen.h:281](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/trafficgen/trafficgen.h#L281) uses the core distribution; [trafficgen.h:290](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/trafficgen/trafficgen.h#L290) returns its result plus the range minimum. [trafficgen.cc:255](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/trafficgen/trafficgen.cc#L255) copies it into the actual network request's destination.

   Built the unmodified `trafficgen.cc` and ran the actual `merlin.trafficgen` component with an instrumented SimpleNetwork sink. For four peers, range `[0,4)`, target 3, and targetProbability=1, all three requests carried destination **4**, not 3. This verifies the producer's outgoing packets; a router/topology was not included, so topology-specific handling of destination 4 was not tested. The shipped `torus_5_trafficgen.py` uses Uniform, so it does not cover this HotSpot failure.

2. **F08: simpleElementExample loses histogram samples from its output bins.**

   [basicStatistics.cc:56](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/simpleElementExample/basicStatistics.cc#L56) registers `UINT32_statistic`; [basicStatistics.cc:102](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/simpleElementExample/basicStatistics.cc#L102) records the generated samples. Built the unmodified source and ran it for four samples with `minvalue=5`, `binwidth=50`, `numbins=10`. Result: `NumItemsCollected=4`, `NumItemsBinned=4`, `NumActiveBins=3`, `Sum=639`, **all ten displayed bins zero**. No values were out of bounds.

3. **F09: simpleElementExample rejects every floating sample from a width-1 histogram.**

   [basicStatistics.cc:70](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/simpleElementExample/basicStatistics.cc#L70) registers double `SUBID_statistic`; [basicStatistics.cc:112](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/simpleElementExample/basicStatistics.cc#L112) feeds values from `nextUniform()`, whose range is `[0,1)`. With `minvalue=0`, `binwidth=1`, `numbins=1`, all four generated samples were reported above the maximum: `NumItemsCollected=4`, `NumItemsBinned=0`, `NumOutOfBounds-MaxValue=4`. A single bin of width 1 should contain those samples. These two example runs use new, valid statistic configurations, not an assertion that the shipped default configuration already fails.

**Concrete call paths with explicit triggers; no full element workload reproduction yet**

4. **F02: a per-router congestion-management override is ignored.**

   [pymerlin-base.py:837](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/pymerlin-base.py#L837) stores the congestion options under `portcontrol.`. [pymerlin-base.py:854](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/pymerlin-base.py#L854) publishes those options as shared parameters; line 858 subscribes the router. [platform_file_dragon_128.py:51](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/tests/platform_file_dragon_128.py#L51) supplies a real platform with congestion management enabled.

   If the returned router receives a local `rtr.addParam('portcontrol.enable_congestion_management', False)`, `hr_router` extracts the scope at [hr_router.cc:478](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/hr_router/hr_router.cc#L478). The core precedence defect restores the shared True. [portControl.cc:528](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/interfaces/portControl.cc#L528) consumes that value, and [portControl.cc:175](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/interfaces/portControl.cc#L175) uses it to enable/disable congestion-management activity. The same mechanism affects per-router `portcontrol.output_arb` and nested arbitration parameters.

   This is a concrete configuration that invokes the reproduced core defect, not a claim that the checked-in platform test already supplies a conflicting local override. Standard top-level link bandwidth parameters are a poor example because the router explicitly reinserts some of them after scoped extraction.

5. **F07: cache/directory idle accounting undercounts a histogram's population.**

   [cacheController.cc:216](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/cacheController.cc#L216) backfills idle cycles into `MSHR_occupancy` with `addDataNTimes(cyclesOff, mshr_->getSize())`. [directoryController.cc:682](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/directoryController.cc#L682) does the same. [memBackendConvertor.cc:151](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/membackend/memBackendConvertor.cc#L151) does this for `outstanding_requests`.

   Enable `MSHR_occupancy` as `sst.HistogramStatistic` and let the cache sleep for 100 cycles. The backfill contributes 100 to the appropriate bin and the collection count, but only 1 to `NumItemsBinned`. The default Accumulator is not affected by this histogram-specific defect. This corrupts reported statistics, not the cache's actual MSHR contents.

6. **F01: a cache clock can synchronously reactivate its memory NIC clock.**

   [cacheFactory.cc:790](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/cacheFactory.cc#L790) registers the cache clock, and link loading passes its timebase into the NIC. [memNIC.cc:57](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/memNIC.cc#L57) registers the NIC using the supplied timebase, so sharing a core clock is part of normal construction.

   The synchronous path is [cacheController.cc:105](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/cacheController.cc#L105) -> [coherenceController.cc:390](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/coherencemgr/coherenceController.cc#L390) -> [memNIC.cc:121](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/memNIC.cc#L121). When the NIC had gone idle and a new send stays queued under backpressure, it calls `reregisterClock()` during core's handler iteration.

   The core probe established early firing and a reallocation crash. This element path establishes a normal source of callback-driven reactivation. It does **not** establish that a stock cache workload grows the vector or crashes: startup may already have reserved sufficient capacity. Early same-cycle retries still violate the returned next-cycle value. The crash and whether an early retry changes packet timing need a complete cache/NIC run before stronger claims.

7. **F05: locked-write response metadata is erased in the memory interface.**

   [standardInterface.cc:952](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/memHierarchy/standardInterface.cc#L952) constructs write responses via the original request's `makeResponse()`. For WriteUnlock that invokes the core assignment-to-zero bug. Vanadis issues this request type at [vbasiclsq.h:891](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/vanadis/lsq/vbasiclsq.h#L891) and displays the response address at [vbasiclsq.h:541](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/vanadis/lsq/vbasiclsq.h#L541).

   The concrete proven consequence is lost/corrupted address metadata and diagnostics. Vanadis matches stores by request ID and completes the locked operation through the stored pending entry; this review has not shown this core bug alone changing the written memory location or CPU result.

   A separate issue exists at that Vanadis constructor call: the current core signature has `(physAddr, size, data, posted, flags, virtAddr, instPtr, tid)`, while the call supplies seven positional arguments. It therefore places the store address into flags, the instruction address into virtAddr, the hardware thread into instPtr, and defaults tid to zero. This is source-confirmed interface misalignment, independently of F05; no Vanadis execution was performed to measure its effects.

**Findings without established current runtime impact in elements**

- **F04, polymorphic unique_ptr:** the actual ExtendedRequest type loses data in the core round-trip probe, but the `NetworkServiceSyntheticPacket`/owned-ingress wrappers in `networkService.h` are not directly serialized. Current router checkpointing uses explicit/manual state and raw serializable pointers. It would overstate the evidence to call the current network-service implementation broken by this finding.
- **F06, repeated enableStatistic:** Merlin's [pymerlin-base.py:475](https://github.com/sstsimulator/sst-elements/blob/9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1/src/sst/elements/merlin/pymerlin-base.py#L475) can apply multiple recorded statistic requests, and interface wrappers forward them to subcomponents. Repeated configuration of the same stat can lose new settings, but no existing model was demonstrated to do so.
- **F10, floating maximum:** requires a nonpositive-only observation window. Existing floating statistic registrations are exposure, not proof that an existing workload produces the failing stream. The simple example feeds positive uniform values and avoids it.
- **F11, variance getter:** no callers of `getVariance()` or `getStandardDeviation()` were found in this elements checkout. Its usual raw Sum/SumSQ/Count output does not call the getter.

**Validation artifacts**

Temporary files are in `/tmp/sst-elements-impact`. Each run was bounded by a simulation stop time and a 15-second wall-clock timeout. Both compiled element sources are unmodified. The `merlin` probe library contains only TrafficGen plus the capture sink; it is not a full Merlin build. The `simpleElementExample` library contains only basicStatistics.

```text
HotSpot: 3 outgoing requests; destinations [4,4,4]; intended [3,3,3].
Integer histogram: collected=4; binned=4; sum=639; sum of displayed bin counts=0.
Floating histogram: collected=4; binned=0; above maximum=4.
```

**Retained probe: hotspot.py**

```python
import sst
sst.setProgramOption('stop-at', '20ns')
gen = sst.Component('source', 'merlin.trafficgen')
gen.addParams({'id':0, 'num_peers':4, 'packets_to_send':3,
               'PacketDest.pattern':'HotSpot', 'PacketDest.RangeMin':0, 'PacketDest.RangeMax':4,
               'PacketDest.HotSpot.target':3, 'PacketDest.HotSpot.targetProbability':1.0})
gen.setSubComponent('networkIF', 'merlin.auditCapture')
```

**Retained probe: statistics.py**

```python
import sst
import sys
sst.setProgramOption('stop-at', '10ns')
c = sst.Component('sample', 'simpleElementExample.basicStatistics')
c.addParams({'run_cycles':3, 'subids':1})
sst.setStatisticLoadLevel(7)
sst.setStatisticOutput('sst.statOutputConsole')
if sys.argv[1] == 'floating':
    c.enableStatistic('SUBID_statistic', {'type':'sst.HistogramStatistic', 'minvalue':0, 'binwidth':1, 'numbins':1})
else:
    c.enableStatistic('UINT32_statistic', {'type':'sst.HistogramStatistic', 'minvalue':5, 'binwidth':50, 'numbins':10})
```

**Retained probe: capture.cc**

```cpp
#include <sst/core/interfaces/simpleNetwork.h>
#include <cstdio>
using SST::Interfaces::SimpleNetwork;
class CaptureNetwork : public SimpleNetwork {
public:
    SST_ELI_REGISTER_SUBCOMPONENT(CaptureNetwork, "merlin", "auditCapture", SST_ELI_ELEMENT_VERSION(1,0,0), "Local destination probe", SST::Interfaces::SimpleNetwork)
    CaptureNetwork(SST::ComponentId_t id, SST::Params&, int) : SimpleNetwork(id), bw("1GB/s") {}
    void sendUntimedData(Request* r) override { delete r; }
    Request* recvUntimedData() override { return nullptr; }
    bool send(Request* r, int) override {
        printf("ACTUAL_TRAFFICGEN src=%lld dest=%lld expected=3 valid_range=[0,4)\n", (long long)r->src, (long long)r->dest);
        delete r;
        return true;
    }
    Request* recv(int) override { return nullptr; }
    bool spaceToSend(int, int) override { return true; }
    bool requestToReceive(int) override { return false; }
    void setNotifyOnReceive(HandlerBase*) override {}
    void setNotifyOnSend(HandlerBase*) override {}
    bool isNetworkInitialized() const override { return true; }
    nid_t getEndpointID() const override { return 0; }
    const SST::UnitAlgebra& getLinkBW() const override { return bw; }
private:
    SST::UnitAlgebra bw;
};
```

**Build commands on this macOS host**

```sh
clang++ -std=c++17 -g -O0 -shared -undefined dynamic_lookup \
  -I/tmp/sst-core-audit.Cekb9v/src -I/tmp/sst-core-audit.Cekb9v/src/sst/core \
  -Isst-elements/src -Isst-elements/src/sst/elements/merlin \
  /tmp/sst-elements-impact/capture.cc sst-elements/src/sst/elements/merlin/trafficgen/trafficgen.cc \
  -o /tmp/sst-elements-impact/libmerlin.so
clang++ -std=c++17 -g -O0 -shared -undefined dynamic_lookup \
  -I/tmp/sst-core-audit.Cekb9v/src -I/tmp/sst-core-audit.Cekb9v/src/sst/core \
  -Isst-elements/src sst-elements/src/sst/elements/simpleElementExample/basicStatistics.cc \
  -o /tmp/sst-elements-impact/libsimpleElementExample.so
```
