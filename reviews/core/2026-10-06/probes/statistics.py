import sst
import sys

sst.setProgramOption("stop-at", "10ns")
c = sst.Component("sample", "simpleElementExample.basicStatistics")
c.addParams({"run_cycles": 3, "subids": 1})
sst.setStatisticLoadLevel(7)
sst.setStatisticOutput("sst.statOutputConsole")
if sys.argv[1] == "floating":
    c.enableStatistic(
        "SUBID_statistic",
        {"type": "sst.HistogramStatistic", "minvalue": 0, "binwidth": 1, "numbins": 1},
    )
else:
    c.enableStatistic(
        "UINT32_statistic",
        {"type": "sst.HistogramStatistic", "minvalue": 5, "binwidth": 50, "numbins": 10},
    )
