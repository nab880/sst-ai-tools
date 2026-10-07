---
{
  "type": "SST Guide",
  "title": "Choose the SST work boundary",
  "description": "Route model construction, element extensions, core changes, and installation work.",
  "tags": [
    "routing"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T09:42:17.525264+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/README.md",
      "x-repository": "sst-core",
      "x-path": "README.md",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "071eb8b019af3e5e496047d7ef9c942169b4571f4cc7bfbca0a3f80e9eb4f299"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/router.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/router.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "22c1ae45060949c0017f12bdf93b38f435d82b9e1b15c9d6bfebddbb8d20575e"
    }
  ]
}
---

# Choose the SST work boundary

| Intent | Boundary | Read next |
|---|---|---|
| Construct a system using existing behavior | Python configuration | [Model construction](using-sst/models.md) |
| Add simulated hardware behavior | Element C++ or element Python helper | [Element extension](development/extending-elements.md) |
| Change scheduling, shared APIs, registration machinery, or framework services | Core and affected element consumers | [Core extension](core/extending.md) |
| Compile or repair an installation | Core first, then elements against that install | [Build](development/build.md) |
| Collect or validate statistics | Python statistics configuration and the statistics API | [Statistics](using-sst/statistics.md) |
| Choose run-time flags | Command line and `sst.setProgramOption` | [Run-time options](using-sst/run-options.md) |
| Run across ranks or threads | Partitioning and link-latency synchronization | [Parallel execution](using-sst/parallel.md) |
| Checkpoint a long run | Serialization support and restart | [Checkpoint and restart](using-sst/checkpoint.md) |
| Build an element outside sst-elements | External library, registration, and discovery | [External elements](development/external-elements.md) |
| Add a communication motif | Ember generator C++ and `Makefile.am` | [Create an Ember motif](elements/ember/new-motif.md) |
| Run application code on Mercury | Skeleton source, `ext` library or `hg++`, Python driver | [Mercury skeleton applications](elements/mercury/skeleton-apps.md) |

For a network request, identify connectivity, route selection, arbitration, flow control, endpoint behavior, and traffic separately. Load [Merlin](elements/merlin/overview.md) only if its model is appropriate. Every element in the checked source has a [main-use-case profile](elements/index.md). Merlin, memHierarchy, Ember, Mercury, Vanadis, Carcosa, and Balar additionally have detailed extension/validation guides. Other implementations require targeted source inspection after selection. Do not infer that Merlin is the only network model.

Before implementation, establish the observable behavior, smallest useful model, and missing physical assumptions. Ask only about assumptions that change the implementation. Source headers and installed ELI metadata take precedence over these draft summaries.

Registering a new component, subcomponent, or motif through existing ELI macros belongs with that element; it does not require changing core registration machinery. Check the tracked core findings (repository evidence: `reviews/core/2026-10-06/index.md`) when the chosen path uses clocks, scoped parameters, polymorphic serialization, discrete traffic distributions, or statistics. Those findings apply to the recorded revisions; recheck their status when changing source versions.
