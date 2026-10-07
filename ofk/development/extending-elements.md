---
{
  "type": "SST Guide",
  "title": "Extend an element",
  "description": "Choose the smallest supported extension point and complete build/test integration.",
  "tags": [
    "extension"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T03:24:43.647652+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleElementExample/basicLinks.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleElementExample/basicLinks.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "0bebf79b5158f88d0b3a64883ec9f1184ddf99e0135d90c74ee927b9f1426d6f"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/Makefile.am",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "b853c0d246415fbcb2cbc8cf3b30bcd1f5b2cc1303b3b9917fb3d75ac4a5118e"
    }
  ]
}
---

# Extend an element

Translate the request into a behavior contract and pick an existing extension point before creating a component. Read the selected element's use-case profile, its extension guide where available, its base class, and one matching concrete implementation. Use `simpleElementExample` for component mechanics only when the element lacks a closer pattern.

Implement registration and parameter documentation alongside behavior; register new source/header files in the relevant `Makefile.am` using its existing convention. Preserve event ownership, untimed initialization, finite-workload completion, and any required checkpoint state.

Validate the behavior with a minimal Python configuration, an existing neighboring regression, and a targeted test that would fail without the change. Use the [element selector](../elements/index.md), then the selected extension-points guide. Keep motif generation, application runtime, CPU execution, fault policy, GPU integration, and network/memory behavior in their owning layers.
