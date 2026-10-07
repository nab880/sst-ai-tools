import sst
import sys

c = sst.Component("probe", "audit.Probe")
sst.addGlobalParams("audit-defaults", {"backend.clock": "1GHz"})
c.addGlobalParamSet("audit-defaults")
c.addParam("backend.clock", "2GHz")
c.addParam("mode", sys.argv[1] if len(sys.argv) > 1 else "basic")
sst.setStatisticLoadLevel(1)
sst.setStatisticOutput("sst.statOutputConsole")
c.enableStatistic(
    "batch", {"type": "sst.HistogramStatistic", "minvalue": 0, "binwidth": 10, "numbins": 2}
)
c.enableStatistic(
    "offset", {"type": "sst.HistogramStatistic", "minvalue": 5, "binwidth": 10, "numbins": 2}
)
c.enableStatistic(
    "floating", {"type": "sst.HistogramStatistic", "minvalue": 0, "binwidth": 1, "numbins": 2}
)
c.enableStatistic("accum")
