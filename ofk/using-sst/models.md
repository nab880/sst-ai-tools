---
{
  "type": "SST Guide",
  "title": "Construct a system model",
  "description": "Assemble existing SST components and verify configuration against implementation.",
  "tags": [
    "configuration",
    "experiments"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:06:47.584030+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/memHierarchy/examples/example-1core-1level.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/memHierarchy/examples/example-1core-1level.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "4c3faf5b97b155c781e41f14c948a3e4b2eea3acecd183f75b5d2363c6552c55"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/params.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/params.cc",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "693b79ba6a17d4a46df431b1ca134edcfbf407e98cc088467f8526b40d6af65e"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/model/configComponent.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/model/configComponent.cc",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "58bc93bd14ae489737da8a9af0cd6bbed51113de6850cc7beb4eadcd65c71ebe"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/stataccumulator.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/stataccumulator.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "bc5c8537334dbb50c161f79a8fdd66910ba2cff7cdbd6733d0bfe24ee011103c"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/stathistogram.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/stathistogram.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "556863c674fae372e975d001d313c0b16cfc605afd1ebd214071ccdf0980bca7"
    }
  ]
}
---

# Construct a system model

Choose components by supported behavior, not names alone. Read the selected element's use-case profile and available detailed guides, one nearby working configuration, and the ELI declarations for parameters, ports, statistics, and subcomponent slots. Compare consequential ELI defaults and accepted values with the implementation; declarations can lag actual behavior.

Use `sst.Component`, `addParams`, `setSubComponent`, and `sst.Link.connect` as demonstrated by the selected example. Match port names and units exactly. Keep workload generation separate from the modeled interconnect or memory system. Start with a finite workload and explicit completion behavior.

Record configuration, seed, source revisions, executable location, rank/thread counts, and output. For experiments distinguish modeled latency/throughput from host simulator execution time. Do not label a stopped-at-time-limit run as successful workload completion.

For the reassessed source revisions (core `09bc3927`, elements `47b99537`), verify effective scoped parameters when combining shared parameter sets with local overrides. Specify each subcomponent statistic's complete configuration in its initial enable call: repeated enable calls can lose newly supplied parameters. The mechanism is `Params::insert(const Params&)`, which uses `std::map::insert` and never overwrites an existing key, and a subcomponent re-enable writes a separate `statistics_` entry on the subcomponent rather than the root entry created by the first enable. Independently check histogram bins and accumulator extrema/variance against a tiny known sample before using them to accept a model or publish results. The repository evidence in `reviews/core/2026-10-06/index.md` records the affected paths and results; [core contracts](../core/contracts.md) summarizes the parameter issue for standalone knowledge bundles.

Entry points: [element selector](../elements/index.md), then the selected overview and [test procedure](../development/testing.md). Use Ember for motifs, Mercury for application runtime, Vanadis for CPU binaries, Carcosa for injection, and Balar for GPU integration; load the coupled-element guides only as needed.
