---
{
  "type": "SST Guide",
  "title": "Configure and collect statistics",
  "description": "Enable, parameterize, output, and validate SST statistics from Python.",
  "tags": [
    "statistics",
    "configuration"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/claude",
    "at": "2026-10-07T09:15:56.730262+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statbase.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statbase.h",
      "x-sha256": "8e55ead677b51259dc9b5533f01670ce436eb2190f8709b8a80809c81e997892",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statengine.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statengine.h",
      "x-sha256": "6e94d7ce8e4829cb967a897ed18bbb501c5bdf34cb7928d61821879e9b956c36",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statengine.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statengine.cc",
      "x-sha256": "c0431f21a8a69e0c59b67937771fb4e32024a93160b683bb662c1bb060a5d659",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/stataccumulator.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/stataccumulator.h",
      "x-sha256": "bc5c8537334dbb50c161f79a8fdd66910ba2cff7cdbd6733d0bfe24ee011103c",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/stathistogram.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/stathistogram.h",
      "x-sha256": "556863c674fae372e975d001d313c0b16cfc605afd1ebd214071ccdf0980bca7",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statuniquecount.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statuniquecount.h",
      "x-sha256": "700fffda71f2ff800035f297c78ca2061308730a92f0325af4d795860d35280f",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statnull.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statnull.h",
      "x-sha256": "f9ee32156bff9119dec2fb5437c60cf108fc1cbaefaed88c18786e43a7d4049a",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statoutput.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statoutput.h",
      "x-sha256": "5112ab5a9dfc5ad1aaa9dd3557745ffdfb66f39070f7d278be7ab8a79d0e97de",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statoutputtxt.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statoutputtxt.h",
      "x-sha256": "e2c3bde1009da3ad4e75257c3ec447d0aab84480c0edce165e6a40e60c7110cc",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statoutputtxt.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statoutputtxt.cc",
      "x-sha256": "a278bd7990d52a303dd16ea83459969ed887f714287a19f693cd781b9f1a4f19",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statoutputcsv.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statoutputcsv.h",
      "x-sha256": "60d3934293a87cf54de864d4375457901cc30dc044ad81339e095a8aea286623",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s11",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statoutputcsv.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statoutputcsv.cc",
      "x-sha256": "7d1eaf35031585c9df3e211bccc701bb1d83cdfc1134dc65a3d90323828e3cfe",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s12",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statoutputjson.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statoutputjson.h",
      "x-sha256": "ad528ee1d328bb72f72e325217aa0b527b8f1602af6626c3af51442e9e086e2a",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s13",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statoutputjson.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statoutputjson.cc",
      "x-sha256": "9ebd008702f2b4bb0f51461479fd7d4e0d959369cdf5b4a0ec8a854cde8701d6",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s14",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statoutputhdf5.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statoutputhdf5.h",
      "x-sha256": "7429904e22b5c9f07ba38d78bf6612409e9e1258ca67beeceee848043453d033",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s15",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statfieldinfo.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statfieldinfo.cc",
      "x-sha256": "08b8daa998e5ad4da1bc3c901f8c0269e26dc4442808dd10566d298600de383d",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s16",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/model/python/pymodel.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/model/python/pymodel.cc",
      "x-sha256": "50756980d9a002a223f75593ed329a245007d4decdc32f6de37c280c23c36e70",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s17",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/model/python/pymodel_comp.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/model/python/pymodel_comp.cc",
      "x-sha256": "d1ca70c38da5f2ab2a22d202d816499ae622de07dfb134ad1868a18724e7f58c",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s18",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/model/python/pymodel_statgroup.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/model/python/pymodel_statgroup.cc",
      "x-sha256": "929a994462abf65627cb7c19dd36748d83de1eefa9b3573e22359dd103da8415",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s19",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/model/python/pymodel_stat.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/model/python/pymodel_stat.cc",
      "x-sha256": "16c53c61bff7fc87067a2638233e1aa7f063b77f8068be11c338bb29cb1a216c",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s20",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/baseComponent.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/baseComponent.h",
      "x-sha256": "e3397e8b63f765bfedfd29cb9eed1db652b33f5c47071d1d3dd105a28c1ed000",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s21",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/baseComponent.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/baseComponent.cc",
      "x-sha256": "d8f7f86195d776d14d1190734a3e183f4b5aa01fb05373f27fb8bd1875534ed8",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s22",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/model/configComponent.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/model/configComponent.cc",
      "x-sha256": "58bc93bd14ae489737da8a9af0cd6bbed51113de6850cc7beb4eadcd65c71ebe",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s23",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/eli/elibase.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/eli/elibase.h",
      "x-sha256": "84581584206f1d8760cfe4d3e933ce742c375a23429b571de88dbbb5d5606936",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s24",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/Makefile.am",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/Makefile.am",
      "x-sha256": "dc80d4e3429781aad2d5f33293d760ddea785edef88efbc3c5e98859a8d242bc",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s25",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/test_StatisticsComponent_basic.py",
      "x-repository": "sst-core",
      "x-path": "tests/test_StatisticsComponent_basic.py",
      "x-sha256": "f1e8cca6463f2380518fa497e96922b306b9f3d244f6f23c4365da75eb1e4532",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s26",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/testsuite_default_StatisticsComponent.py",
      "x-repository": "sst-core",
      "x-path": "tests/testsuite_default_StatisticsComponent.py",
      "x-sha256": "9b61535622ab37feee782be2805ab3798b0d2e37d56a32f09b918d1dfd425f2e",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s27",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/test_Component_createStats.py",
      "x-repository": "sst-core",
      "x-path": "tests/test_Component_createStats.py",
      "x-sha256": "2241c0090526fc088bd6da7d5630c98f3bceae576f732d3a218278b76e3fc698",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s28",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/test_Component_setStats.py",
      "x-repository": "sst-core",
      "x-path": "tests/test_Component_setStats.py",
      "x-sha256": "94155ae8018fdb5747cc239b8cd01389404e902ce213e9dae0ae8d933850a4e1",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s29",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/test_Component_enableAllStats.py",
      "x-repository": "sst-core",
      "x-path": "tests/test_Component_enableAllStats.py",
      "x-sha256": "6f0cf2d12a8b072b3c449db28de68da8e58adf185e1a06d33dcb6c9f764098ee",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s30",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleElementExample/basicStatistics.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleElementExample/basicStatistics.h",
      "x-sha256": "1572092d4ce1ebbd7a8cc409f7aca311ec709b5b1c3872536e5dcf04f3047fb9",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s31",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleElementExample/basicStatistics.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleElementExample/basicStatistics.cc",
      "x-sha256": "3135d8af902b16fe7aca1134ee89f8d6cff07cdb996c2a88be081e8d1627ec75",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s32",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleElementExample/tests/basicStatistics0.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleElementExample/tests/basicStatistics0.py",
      "x-sha256": "188c561f960d02fe020e8cd7684e9f6a64a31d14e387827ff9d1e179ae26273f",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s33",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleElementExample/tests/basicStatistics1.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleElementExample/tests/basicStatistics1.py",
      "x-sha256": "550f299b146ddef8022f0ff847f1b98c27fc058b0b54b72eb14b5d0cfa17173f",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s34",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/hr_router/hr_router.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/hr_router/hr_router.cc",
      "x-sha256": "1a2f345bb5af6cedbba6c90036025799f62e16053c5028828a5d715f8b7cedfd",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s35",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statoutput.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statoutput.cc",
      "x-sha256": "8766db1fb4645375c649e84a5e7cda3ea398936582108f55b99ce1d99c045d39",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    }
  ]
}
---
# Configure and collect statistics

A statistic is declared by an element in its ELI (`SST_ELI_DOCUMENT_STATISTICS`: name, description, units, enable level), created by the component code with `registerStatistic<T>(name, subId)`, and given a collection type, output rate, and window from the Python configuration. Until a configuration enables it, a statistic is a `sst.NullStatistic` object whose `addData` does nothing, so enabling costs nothing in element code and omitting an enable produces no output rather than an error.

## Discover what a component offers

`sst-info <library>.<component>` lists `Statistics (N total)` as `name: description (units = "...") Enable level = L`. The enable level is compared against the load level described below. Statistic names are fixed by the element; sub-IDs (for example a per-port `xbar_stalls` in Merlin's router) are chosen by the code at registration and appear as `StatisticSubId` in outputs.

## Enable statistics from Python

| Call | Effect |
|---|---|
| `sst.setStatisticLoadLevel(level)` | Global load level, conventionally 0 to 10 (not range-checked); the default is 0, under which enable-all creates only statistics declared at enable level 0. |
| `comp.setStatisticLoadLevel(level[, apply_to_children])` and `sst.setStatisticLoadLevelForComponentName(name, level[, apply_to_children])` / `...ForComponentType(type, level[, apply_to_children])` | Per-component override of the global level. |
| `comp.enableAllStatistics([params][, apply_to_children])` | Enables every declared statistic whose ELI enable level is at or below the component's load level. |
| `comp.enableStatistics([names], [params][, apply_to_children])` and `comp.enableStatistic(name[, params])` | Enables named statistics regardless of load level; `enableStatistic` returns a handle with `addParam(key, value)` / `addParams(dict)`. |
| `sst.enableAllStatisticsForAllComponents([params])` | Enable-all on every component. |
| `sst.enableAllStatisticsForComponentName(name[, params][, apply_to_children])`, `sst.enableStatisticForComponentName(name, stat[, params][, apply_to_children])`, `sst.enableStatisticsForComponentName(name, names[, params][, apply_to_children])` (one name or a list) | Enable by component name; the `...Type` variants (`enableAllStatisticsForComponentType`, `enableStatisticForComponentType`, `enableStatisticsForComponentType`) take an ELI type such as `memHierarchy.Cache` instead of a name. |
| `obj = comp.createStatistic(name, params)` then `comp.setStatistic(slot, obj)` | Creates one statistic object and binds several statistic slots to it, so they share one accumulator; `setStatistic` cannot bind an enable-all pseudo-statistic. |

Enable calls on a subcomponent object (`comp.setSubComponent(...)`) address that subcomponent's declared statistics; `apply_to_children` on a parent enables its subcomponents too. The resolution order is fixed in `baseComponent.h`: an explicitly enabled name is always created; an enable-all creates the statistic only when its ELI enable level is at or below the component's load level; a subcomponent loaded with `INSERT_STATS` defers to its parent; anything else is a null statistic. A component with no enable at all has load level 0 regardless of the global level.

## Per-statistic parameters

`params` is a dictionary of strings. The engine recognizes four parameters on every statistic and each type adds its own.

| Parameter | Default | Meaning |
|---|---|---|
| `type` | `sst.AccumulatorStatistic` when omitted | `sst.AccumulatorStatistic`, `sst.HistogramStatistic`, `sst.UniqueCountStatistic`, or `sst.NullStatistic`; a custom type is `<library>.<name>`. |
| `rate` | `0ns` | Output period. A time or frequency (`5 ns`, `25khz`) is periodic; `N events` outputs after N collections; `0ns` outputs only at the end of simulation. Any other unit is fatal. |
| `startat`, `stopat` | `0ns` | Simulated times between which `addData` is accepted; `0ns` means unbounded. |
| `resetOnOutput` | `False` | Clear the data after each periodic or event-triggered output; the end-of-simulation output does not clear. |
| `minvalue`, `binwidth`, `numbins` (histogram) | `0`, `5000`, `100` | Bin origin, width, and count. |
| `dumpbinsonoutput`, `includeoutofbounds` (histogram) | `true`, `true` | Emit one `Bin<i>:<lo>-<hi>` field per bin; track samples below/above the range in two extra counters. |

Built-in types accept `int32_t`, `uint32_t`, `int64_t`, `uint64_t`, `float`, and `double` data; the data type is fixed by the element's `registerStatistic<T>` call, not by Python.

## Select an output

`sst.setStatisticOutput("<type>", {params})` chooses one output for all default statistics; `sst.setStatisticOutputOption(key, value)` and `sst.setStatisticOutputOptions(dict)` adjust it. The default is the console.

| Output type | Parameters and defaults | Notes |
|---|---|---|
| `sst.statOutputConsole` | `outputtopheader=False`, `outputinlineheader=True`, `outputsimtime=False`, `outputrank=False` | One line per statistic per output, `name : Type : Field.type = value; ...`. |
| `sst.statOutputTXT` | `filepath=./StatisticOutput.txt`, `compressed=False` (needs libz), same header/simtime/rank flags with `outputsimtime=True`, `outputrank=True` | Same line format as the console. |
| `sst.statOutputCSV` | `separator=", "`, `filepath=./StatisticOutput.csv`, `outputtopheader=True`, `outputsimtime=True`, `outputrank=True` | Header columns are the component name, `StatisticName`, `StatisticSubId`, the statistic type, optional `SimTime` and `Rank`, then one `Field.type` column per registered field. |
| `sst.statOutputJSON` | `filepath=./StatisticOutput.json`, `outputsimtime=True`, `outputrank=True` (parsed but unused; `rank` is emitted only with more than one rank) | A `components` array whose entries hold `name`, `simtime`, and `statistics` records of `{ "stat": name, "values": [...] }`. |
| `sst.statOutputHDF5` | `filepath=./StatisticOutput.h5` | Compiled only when core's configure finds HDF5; the core test exercises it with `--model-options="hdf5"`. |

Field names carry a type suffix from `i32`, `i64`, `u32`, `u64`, `f32`, and `f64` (`Sum.u64`, `Max.f64`). With more than one MPI rank, the text, CSV, and JSON outputs insert `_<rank>` before the file extension and write one file per rank; the core test combines the per-rank files before comparing. Statistic output files are placed relative to `--output-directory` when that option is set.

## What each type reports

| Type | Fields |
|---|---|
| Accumulator | `Sum`, `SumSQ`, `Count`, `Min`, `Max` |
| Histogram | `BinsMinValue`, `BinsMaxValue`, `BinWidth`, `TotalNumBins`, `Sum`, `SumSQ`, `NumActiveBins`, `NumItemsCollected`, `NumItemsBinned`, then `NumOutOfBounds-MinValue` and `NumOutOfBounds-MaxValue` when enabled, then `Bin<i>:<lo>-<hi>` per bin when `dumpbinsonoutput` is true |
| UniqueCount | `UniqueItems`, the size of the set of distinct values seen |
| Null | nothing |

`Count` for an accumulator and `NumItemsCollected` for a histogram count data items: `addData` adds one and `addDataNTimes(N, v)` adds N; only the histogram's `NumItemsBinned` counts an `addDataNTimes` call once on these revisions (see below).

## Statistic groups

A group gives a set of statistics their own output and period:

```python
g = sst.StatisticGroup("l1")
g.addComponent(l1cache)
g.addStatistic("CacheHits", {"type": "sst.AccumulatorStatistic"})
g.setFrequency("10us")
g.setOutput(sst.StatisticOutput("sst.statOutputCSV", {"filepath": "l1.csv"}))
```

Groups must be periodic; an event-based `rate` inside a group is rejected during registration. The console, text, CSV, and HDF5 outputs accept groups; a group on the JSON output is fatal. Output type names are lower-cased before lookup, which is why `sst.statOutputCSV` resolves to the ELI name `statoutputcsv`. Only the console and text outputs accept a statistic registered after wire-up, and only when `outputinlineheader` is true; registering late on any other output is fatal. Statistics outside any group use the default output selected with `setStatisticOutput`.

## When output happens

Periodic statistics output every `rate` and again at the end of simulation; the engine creates one clock per distinct period. Event-based statistics output after every `N` collections and reset their count. Every enabled statistic outputs at the end of simulation. `--timing-info` and the heartbeat options report host-side simulator timing, which is not a statistic.

## Validate before trusting a number

The recorded devel revisions reproduce these statistic defects (details and evidence in [core contracts](../core/contracts.md)):

- Re-enabling a subcomponent statistic with new parameters keeps the first parameters, because `Params::insert` never overwrites an existing key. Give the complete configuration in the first enable call.
- `addDataNTimes(N, value)` into a histogram increments `NumItemsBinned` once while adding `N` to the bin.
- Histogram bins start at `floor(value / binwidth) * binwidth` while the labels start at `minvalue`; a `minvalue` that is not a multiple of `binwidth` shifts samples out of the displayed bins.
- A floating-point histogram rejects samples that belong in its last bin as above-maximum.
- A floating-point accumulator starts `Max` at the smallest positive double, so negative-only data reports a near-zero maximum.
- The accumulator variance getter returns `Count * SumSQ - Sum * Sum` without normalization; compute variance from the raw `Sum`, `SumSQ`, and `Count` fields.

Before using a statistic as an oracle, run a tiny workload with a known sample and confirm `Count`, `Sum`, bin placement, and extrema by hand. The statistics in element profiles (hit counts, event counts, latencies) are only as trustworthy as the element's `addData` placement; inspect it when a value matters.

## Entry points

- Core: `tests/test_StatisticsComponent_basic.py` (load levels, rates, `startat`/`stopat`, `resetOnOutput`, event-based rates, dynamic registration, groups with CSV/TXT/HDF5 outputs) run by `tests/testsuite_default_StatisticsComponent.py`; `tests/test_Component_enableAllStats.py`, `test_Component_setStats.py`, and `test_Component_createStats.py` for the enable-all, handle, and shared-statistic forms.
- Elements: `simpleElementExample/basicStatistics.{h,cc}` with `tests/basicStatistics0.py` (enable by type, CSV), `basicStatistics1.py` (periodic rate), and `basicStatistics2.py`.
- Implementation side: [statistics API](../core/statistics-api.md). Run selection: [testing](../development/testing.md); model assembly: [model construction](models.md).
