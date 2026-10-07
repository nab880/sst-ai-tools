---
{
  "type": "SST Guide",
  "title": "Implement statistics in elements and core",
  "description": "Declare, register, resolve, and extend statistic types and outputs in C++.",
  "tags": [
    "core",
    "statistics",
    "extension"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/claude",
    "at": "2026-10-07T09:15:58.488575+00:00"
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
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statbase.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statbase.cc",
      "x-sha256": "ebc534b9548148dbedc47105e48076b08c59cd9b3c610dee7270b6943f6a337c",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statengine.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statengine.h",
      "x-sha256": "6e94d7ce8e4829cb967a897ed18bbb501c5bdf34cb7928d61821879e9b956c36",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statengine.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statengine.cc",
      "x-sha256": "c0431f21a8a69e0c59b67937771fb4e32024a93160b683bb662c1bb060a5d659",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/stataccumulator.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/stataccumulator.h",
      "x-sha256": "bc5c8537334dbb50c161f79a8fdd66910ba2cff7cdbd6733d0bfe24ee011103c",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/stathistogram.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/stathistogram.h",
      "x-sha256": "556863c674fae372e975d001d313c0b16cfc605afd1ebd214071ccdf0980bca7",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statuniquecount.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statuniquecount.h",
      "x-sha256": "700fffda71f2ff800035f297c78ca2061308730a92f0325af4d795860d35280f",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statnull.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statnull.h",
      "x-sha256": "f9ee32156bff9119dec2fb5437c60cf108fc1cbaefaed88c18786e43a7d4049a",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statoutput.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statoutput.h",
      "x-sha256": "5112ab5a9dfc5ad1aaa9dd3557745ffdfb66f39070f7d278be7ab8a79d0e97de",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statoutputtxt.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statoutputtxt.h",
      "x-sha256": "e2c3bde1009da3ad4e75257c3ec447d0aab84480c0edce165e6a40e60c7110cc",
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
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statfieldinfo.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statfieldinfo.h",
      "x-sha256": "5e1e01481226dd11d1fe649fdc31b1f756d1a2045c4b5de54a3fa5ec3115ba8d",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s12",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statfieldinfo.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statfieldinfo.cc",
      "x-sha256": "08b8daa998e5ad4da1bc3c901f8c0269e26dc4442808dd10566d298600de383d",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s13",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/baseComponent.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/baseComponent.h",
      "x-sha256": "e3397e8b63f765bfedfd29cb9eed1db652b33f5c47071d1d3dd105a28c1ed000",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s14",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/baseComponent.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/baseComponent.cc",
      "x-sha256": "d8f7f86195d776d14d1190734a3e183f4b5aa01fb05373f27fb8bd1875534ed8",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s15",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/componentInfo.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/componentInfo.h",
      "x-sha256": "343dc4f7cf20817ed01cdcf1bc1b7717045bfc89b59b7ac67977658e69b621e5",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s16",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/eli/statsInfo.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/eli/statsInfo.h",
      "x-sha256": "d57a838e1eda6b8a22471ca371ddf02626f5250ec59637da6f47fe540340cd6d",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s17",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/eli/elibase.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/eli/elibase.h",
      "x-sha256": "84581584206f1d8760cfe4d3e933ce742c375a23429b571de88dbbb5d5606936",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s18",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/testElements/coreTest_StatisticsComponent.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/testElements/coreTest_StatisticsComponent.h",
      "x-sha256": "5d93e2dd90b74fba6fbc5d0b640eb6068a055e119dac8a59dc4d13fc507cfa21",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s19",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/testElements/coreTest_StatisticsComponent.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/testElements/coreTest_StatisticsComponent.cc",
      "x-sha256": "7201baa324c7313e384f901eddfcb016086dfa1425707aeafecb902c23df144c",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s20",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/testsuite_default_StatisticsComponent.py",
      "x-repository": "sst-core",
      "x-path": "tests/testsuite_default_StatisticsComponent.py",
      "x-sha256": "9b61535622ab37feee782be2805ab3798b0d2e37d56a32f09b918d1dfd425f2e",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s21",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/test_StatisticsComponent_basic.py",
      "x-repository": "sst-core",
      "x-path": "tests/test_StatisticsComponent_basic.py",
      "x-sha256": "f1e8cca6463f2380518fa497e96922b306b9f3d244f6f23c4365da75eb1e4532",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s22",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleElementExample/basicStatistics.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleElementExample/basicStatistics.h",
      "x-sha256": "1572092d4ce1ebbd7a8cc409f7aca311ec709b5b1c3872536e5dcf04f3047fb9",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s23",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleElementExample/basicStatistics.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleElementExample/basicStatistics.cc",
      "x-sha256": "3135d8af902b16fe7aca1134ee89f8d6cff07cdb996c2a88be081e8d1627ec75",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s24",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/otf2_output_stat.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/otf2_output_stat.h",
      "x-sha256": "a2d27d289323a94a27b1ea682b30892b42482ac5489c68368d89121d896dacc4",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s25",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statgroup.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statgroup.cc",
      "x-sha256": "d2fe2c476ed8d9f0c2ab57d9322777c420701328718d213f7a0f60d81c1b881f",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s26",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/statoutput.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/statoutput.cc",
      "x-sha256": "8766db1fb4645375c649e84a5e7cda3ea398936582108f55b99ce1d99c045d39",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    }
  ]
}
---
# Implement statistics in elements and core

This guide covers the C++ side of SST statistics: declaring, registering, collecting, and extending. Configuration from Python is in [configure and collect statistics](../using-sst/statistics.md).

## Declare and register

Declare every statistic in the component's or subcomponent's ELI block:

```cpp
SST_ELI_DOCUMENT_STATISTICS(
    { "UINT64_statistic", "Statistic that records unsigned 64-bit values", "unitless", 2 },
    { "SUBID_statistic",  "One instance per sub-ID",                        "unitless", 4 })
```

The four fields are name, description, units, and enable level. Register in the constructor:

```cpp
Statistic<uint64_t>* stat_U64 = registerStatistic<uint64_t>("UINT64_statistic");
std::vector<Statistic<double>*> per_id;
for (int i = 0; i < n; ++i)
    per_id.push_back(registerStatistic<double>("SUBID_statistic", std::to_string(i)));
```

Registering a name that is not in the ELI is fatal (`attempting to register a statistic ... not found in ELI`). Registering the same name and sub-ID twice returns the first object. The data type is the template argument; the built-in types are instantiated for `int32_t`, `uint32_t`, `int64_t`, `uint64_t`, `float`, and `double` only. `registerMultiStatistic<Args...>` creates a `Statistic<std::tuple<Args...>>`, which only a custom statistic type can implement, and `Statistic<void>` exists for statistics without data.

Collect with `stat->addData(value)` or `stat->addDataNTimes(n, value)`. `addData` checks `isEnabled()` (false outside the `startat`/`stopat` window), calls the type's `addData_impl`, and increments the collection count that drives event-based output; a null statistic stays enabled but its `addData_impl` is empty, and all disabled statistics of one data type share a single static `NullStatistic`.

## How a registration is resolved

`BaseComponent::registerStatistic_impl` decides, in this order, who owns the statistic:

1. Look the name up in this component's ELI to get its enable level. If it is absent and the subcomponent was loaded with `SHARE_STATS`, retry on the parent; otherwise fatal.
2. If Python explicitly enabled the name, the parent component creates it (`createExplicitlyEnabledStatistic`); a statistic marked shared by `createStatistic`/`setStatistic` is created once and returned to every slot bound to it.
3. If Python enabled all statistics, create it when its ELI level is at or below the component's load level, otherwise return a disabled statistic.
4. If the subcomponent was loaded with `INSERT_STATS`, retry on the parent with the level already resolved.
5. Otherwise return a disabled statistic.

A component's load level is copied from the engine's global level only when enable-all is active; otherwise it is 0. Disabled statistics are `NullStatistic` instances whose `addData_impl` is empty.

## Engine behavior

`StatisticProcessingEngine::registerStatisticWithEngine` parses `rate`: units of `s` or `hz` make the statistic periodic, `event` makes it event-based, anything else is fatal, and the type's `isStatModeSupported(periodic)` must agree. Periodic statistics join a default group keyed by the output period, each with its own clock; event-based statistics get a collection-count limit and reset the count on output. `startat`/`stopat` are converted to simulation time and toggle `isEnabled`. Groups reject event-based statistics, but `createStatistic` ignores the registration failure, so such a statistic exists, joins no group or output, and silently never outputs. Registration after wire-up (for example from a clock handler) is fatal unless the output's `supportsDynamicRegistration()` is true; in this revision that is only the console and text outputs, and only with inline headers enabled.

At each output the engine calls the output's `output(stat, end_of_sim)`; after any non-final output it resets the trigger count of event-based statistics and, when `resetOnOutput` is set, calls `clearStatisticData()`. The end-of-simulation output never clears. On checkpoint restart the engine re-registers each statistic from serialized `rate`/`startat`/`stopat` factors rather than parameters.

## Implement a statistic type

Derive from `Statistic<T>` (or use the template-declaration macros for a class template) and implement:

| Override | Purpose |
|---|---|
| constructor `(BaseComponent*, const std::string& statName, const std::string& statSubId, Params&)` | Read type parameters; override `getStatTypeName()` (the `setStatisticTypeName` member path is deprecated for removal in SST 16). |
| `addData_impl(T)` and optionally `addData_impl_Ntimes(uint64_t, T)` | Accumulate; the default N-times path calls `addData_impl` N times. |
| `clearStatisticData()` | Implement `resetOnOutput`. |
| `registerOutputFields(StatisticFieldsOutput*)` | Call `registerField<FieldT>("Name")` once per field and keep the handles. |
| `outputStatisticFields(StatisticFieldsOutput*, bool end_of_sim)` | Call `outputField(handle, value)` per field. |
| `isStatModeSupported(bool periodic)` | Reject periodic or event-based use when unsupported. |
| `serialize_order` | Serialize state for checkpoints, calling the base first. |

Field types are limited to the `outputField` overloads: `int32_t`, `uint32_t`, `int64_t`, `uint64_t`, `float`, `double`; outputs name them with the short suffixes registered in `statfieldinfo.cc`. Register the class and instantiate it for each data type:

```cpp
SST_ELI_DECLARE_STATISTIC_TEMPLATE(MyStat, "mylib", "MyStat", SST_ELI_ELEMENT_VERSION(1,0,0),
    "One-line description", "SST::Statistic<T>")
// in a .cc file, once per supported T:
SST_ELI_INSTANTIATE_STATISTIC(MyStat, uint64_t);
```

Python then selects it with `"type": "mylib.MyStat"`. The core's built-ins follow this pattern in `stataccumulator.h`, `stathistogram.h` (which uses the `_DERIVED` form to fix the bin data type), `statuniquecount.h`, and `statbase.cc`. Non-numeric statistics derive from `CustomStatistic` and use `SST_ELI_REGISTER_CUSTOM_STATISTIC`; `mask-mpi/otf2_output_stat.h` is the only element example in this checkout.

## Implement an output

Derive from `StatisticFieldsOutput` for field-oriented outputs. The pure virtuals are `checkOutputParameters`, `startOfSimulation`, `endOfSimulation`, `implStartOutputEntries(StatisticBase*)`, and `implStopOutputEntries`; the `outputField` overloads default to a fatal "does not support" error for each type you do not override, `printUsage` has a default, `implRegisteredField` observes field registration, and `acceptsGroups` and `supportsDynamicRegistration` default to false. `StatisticFieldsOutput` already implements the group hooks (`startOutputGroup`/`stopOutputGroup`, `startRegisterGroup`/`stopRegisterGroup`), so a group-capable field output only needs `acceptsGroups()` to return true. Register with `SST_ELI_REGISTER_DERIVED(SST::Statistics::StatisticOutput, cls, "lib", "name", version, desc)` as `statoutputcsv.h` does; Python selects `lib.name`. Outputs run once per rank, so multi-rank file naming is the output's responsibility (the core outputs append `_<rank>`).

## Known defects on the recorded revisions

See [core contracts](../core/contracts.md) for reproduced behavior: parameter re-enables that lose settings, `addDataNTimes` undercounting binned items, histogram bin-origin and floating-range errors, the accumulator maximum seeded with `numeric_limits::min()`, and an unnormalized variance getter. When extending these classes, add regression tests for exactly those paths.

## Tests and examples

- `src/sst/core/testElements/coreTest_StatisticsComponent.{h,cc}`: integer and floating variants, a shared statistic, and `register_dynamic` for post-wire-up registration.
- `tests/testsuite_default_StatisticsComponent.py` with `test_StatisticsComponent_basic.py` and single reference files for CSV, TXT, and HDF5; the suite merges per-rank output files before comparing.
- `simpleElementExample/basicStatistics.{h,cc}`: duplicate-name registration, sub-IDs, and the three `basicStatistics*.py` configurations.

Follow [validation](../development/testing.md) for runner selection and [core extension](extending.md) for API-change expectations.
