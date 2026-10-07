---
{
  "type": "SST Guide",
  "title": "Validate a Merlin change",
  "description": "Check delivery, ownership, initialization, and progress for network changes.",
  "tags": [
    "merlin",
    "testing"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:58.172849+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/tests/testsuite_default_merlin.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/tests/testsuite_default_merlin.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "f2f31edb4736e799e7da720c3a0f629295948ed3d8db9108dfb12b103ced4577"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/tests/torus_5_trafficgen.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/tests/torus_5_trafficgen.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "91a230131118c917ffa42341de17909ca86e7de4937f3a40f62435101d0e4919"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/rng/discrete.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/rng/discrete.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "acdd6a8b0105dcd8c850893b0213ecd8460501016993c7dda1931b32614f108c"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/trafficgen/trafficgen.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/trafficgen/trafficgen.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "d0b2d8edf1317317afc7a868f4da10403b8a5d61e69141e3914b8ae09ae6fff6"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/trafficgen/trafficgen.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/trafficgen/trafficgen.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "1283e25f9963bd88c232618759deed3e61917142fcbe58c14795fe883b89baff"
    }
  ]
}
---

# Validate a Merlin change

Start with `tests/testsuite_default_merlin.py` to see exact runner expectations. `torus_5_trafficgen.py` provides a traffic-generator configuration; topology-specific tests include torus, dragonfly, fattree, and hyperx. These are regression entry points, not necessarily minimal reproducers.

For a new behavior, create the smallest topology that exercises it. Verify destination delivery, expected packet counts, finite workload completion, legal port/VC selection, and initialization traffic. Exercise saturation/backpressure when altering routing, arbitration, or credits. Include an invalid-parameter case when validation behavior changes.

Compare the existing baseline with the changed behavior under the same seed and configuration; for HotSpot/Normal destinations the seed does not take effect, so use Uniform or an external fixed draw. `torus_5_trafficgen.py` writes `TestOutput.csv` into the working directory, and TrafficGen asserts only `dest >= 0`, so an out-of-range destination reaches the network unchecked. Do not infer deadlock freedom from a single light-load run. Run supported serial and parallel cases when partition-crossing events or shared state change. See [test selection](../../development/testing.md).

Check generated destinations before attributing a delivery failure to routing. On the reassessed revisions (core `09bc3927`, elements `47b99537`), core `DiscreteDistribution` produces incorrect indices; Merlin's `HotSpot` traffic path reproduced destination `4` for a configured endpoint range `[0,4)` and target `3`. A seed does not repair this bias or out-of-range result. Validate a selected generator's bounds and intended distribution before using it for congestion experiments. The repository evidence is in `reviews/core/2026-10-06/index.md` when available.
