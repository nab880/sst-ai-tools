---
{
  "type": "SST Guide",
  "title": "Extend an Ember motif",
  "description": "Preserve queued-event completion and message-buffer lifetimes.",
  "tags": [
    "ember",
    "extension-points"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:06:47.823650+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/mpi/motifs/emberpingpong.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/mpi/motifs/emberpingpong.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "6c232b0ee2553cac9465b9770a3de4e7cfba23c66e84d72877c5df028feda166"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/mpi/motifs/emberpingpong.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/mpi/motifs/emberpingpong.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "d943c49d96bd769b3d4888d8aab87fa4aa25e9426ba752d57b872b3800f6aabc"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/mpi/embermpigen.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/mpi/embermpigen.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "3dce203c8fbada9f8ec23eee0aa1a649ec4e4e4f8a5f7f6bd0db73dd8ec11319"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/emberengine.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/emberengine.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "0c179653219c018afa5a97d0f74cc01021ee53ccef95618459a1feba4ad9413d"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "16c80b881b2c8639639423157e53be1f2802a3e8120671d8702d1324a0074ec8"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ember/emberengine.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ember/emberengine.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "757bef71e798f27a2d51211987f02972631fec7757dbe730118f4467c5625648"
    }
  ]
}
---

# Extend an Ember motif

`EmberPingPongGenerator` in `mpi/motifs/emberpingpong.h/.cc` is a compact message-passing example derived from `EmberMessagePassingGenerator`. Its `generate(std::queue<EmberEvent*>&)` enqueues operations and maintains iteration state; the engine revisits it as events execute. Returning true means generation is finished, but queued events still execute. In this revision `EmberEngine::issueNextEvent` also completes a motif whenever a refill leaves its queue empty, even if `generate` returned false. A new generator must not use an empty/false result to mean “wait for work later.” The base `generate` overloads and `completed()` are `assert(0)`, so a generator must override `generate(std::queue<EmberEvent*>&)` (the three-argument form is dead) and `completed()`, which the engine calls at motif end before deleting the generator and chaining the next motif. The engine ends the simulation only when the generator's `primary()` is true. PingPong shows the nonparticipating-rank pattern: ranks other than 0 and `arg.rank2` return true on the first call.

Use `enQ_*` operations from the generator API. For nonblocking operations preserve request handles and buffer lifetimes through wait/test completion. Match communicator, rank, message count, datatype, tag, and collective ordering across participants. A communication deadlock is not necessarily a router fault.

Register the motif with ELI and add build entries following `Makefile.am`. Separate modeled compute delay from host execution time. Test zero-size messages and nonparticipating ranks where supported. Do not promise checkpoint support from a motif example alone; inspect the actual engine/generator state and restart path.

Read [validation](validation.md) and [core contracts](../../core/contracts.md) only for interfaces used by the change.
