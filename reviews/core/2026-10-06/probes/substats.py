import sst
import sys

c = sst.Component("loader", "coreTestElement.SubComponentLoader")
s = c.setSubComponent("mySubComp", "coreTestElement.SubCompReceiver")
s.enableStatistic("numRecv", {"rate": "10ns"})
if len(sys.argv) > 1 and sys.argv[1] == "twice":
    s.enableStatistic("numRecv", {"type": "sst.HistogramStatistic", "binwidth": 2})
a = sst.Component("sender", "coreTestElement.SubComponentLoader")
t = a.setSubComponent("mySubComp", "coreTestElement.SubCompSender")
t.addParam("sendCount", 3)
sst.Link("wire").connect((t, "sendPort", "1ns"), (s, "recvPort", "1ns"))
sst.setStatisticLoadLevel(1)

sst.setProgramOption("stop-at", "30ns")
