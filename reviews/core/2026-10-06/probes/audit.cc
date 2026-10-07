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
