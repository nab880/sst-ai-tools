#include <sst/core/interfaces/simpleNetwork.h>
#include <cstdio>
using SST::Interfaces::SimpleNetwork;
class CaptureNetwork : public SimpleNetwork {
public:
    SST_ELI_REGISTER_SUBCOMPONENT(CaptureNetwork, "audit", "Capture", SST_ELI_ELEMENT_VERSION(1,0,0), "Local destination probe", SST::Interfaces::SimpleNetwork)
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
