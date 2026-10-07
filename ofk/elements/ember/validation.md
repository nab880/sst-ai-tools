---
{
  "type": "SST Guide",
  "title": "Validate Ember workloads",
  "description": "Choose a small motif case before expensive parameter sweeps.",
  "tags": [
    "ember",
    "validation"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:06:48.080966+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/tests/testsuite_default_ember_sweep.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/tests/testsuite_default_ember_sweep.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "685ab6d46c649d043a5bc80609fd703b2d72aa08a14909b1fe7e3ad0d29f1e98"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/test/emberLoad.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/test/emberLoad.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "162a44de6f921e5fddc13f0a103d2eb53e2045a42ae41e061630cdfe1ad5a79d"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/configure.m4",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/configure.m4",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "566e40bc6286a574c12242c3e43cb345b6869e8fd8fa74e46ac08ebcc4aeca1c"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/mpi/motifs/emberpingpong.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/mpi/motifs/emberpingpong.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "d943c49d96bd769b3d4888d8aab87fa4aa25e9426ba752d57b872b3800f6aabc"
    }
  ]
}
---

# Validate Ember workloads

`tests/testsuite_default_ember_sweep.py` builds a broad parameterized matrix including PingPong, AllPingPong, Barrier, and Allreduce. Read its test construction and the `test/emberLoad.py` invocation before selecting a small case. `SST_TEST_ES_LIST` accepts an inclusive `start-stop` range, including `9-9` for one index; a bare `9`, `9-`, or `-9` does not filter the sweep (the parser requires a `-` after the first character and at least three characters). Map indices to generated cases before using it.

Other devel suites distinguish QoS, OTF2, SHMEM, nightly, and sweep behavior. OTF2 configuration is checked in `configure.m4`; unavailable optional support means a skipped/blocked case, not proof of correctness.

Check participant counts, completed iterations, message matching, and natural completion. For new motifs use a deterministic small rank count and verify the intended communication schedule. Preserve buffer ownership across nonblocking operations. Report simulated latency/bandwidth separately from host runtime. Confirm neighboring motif tests before large sweeps.

The sweep compares the simulation-complete line with its parameter-hashed reference and only logs a non-empty stderr file; that does not independently validate payload values. The matrix already covers `messagesize 0` and iteration counts 1 and 10, but not zero iterations. Add an application/data oracle when correctness depends on payload contents. For PingPong, use positive iterations and a distinct valid `arg.rank2` (normally rank 1 with at least two ranks); zero iterations reach timing calculations before timestamps are established and divide by the iteration count.

Use [test planning](../../development/testing.md) with target `ember`; narrow the emitted suite selection before execution.
