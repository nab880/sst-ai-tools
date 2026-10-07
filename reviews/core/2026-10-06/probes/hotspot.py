import sst

sst.setProgramOption("stop-at", "20ns")
gen = sst.Component("source", "merlin.trafficgen")
gen.addParams(
    {
        "id": 0,
        "num_peers": 4,
        "packets_to_send": 3,
        "PacketDest.pattern": "HotSpot",
        "PacketDest.RangeMin": 0,
        "PacketDest.RangeMax": 4,
        "PacketDest.HotSpot.target": 3,
        "PacketDest.HotSpot.targetProbability": 1.0,
    }
)
gen.setSubComponent("networkIF", "audit.Capture")
