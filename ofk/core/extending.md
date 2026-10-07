---
{
  "type": "SST Guide",
  "title": "Extend SST core",
  "description": "Assess framework changes across core and element consumers.",
  "tags": [
    "core",
    "extension"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:06:47.780220+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/CONTRIBUTING.md",
      "x-repository": "sst-core",
      "x-path": "CONTRIBUTING.md",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "00060f1dc1e27dac1b4e2e5dbcca5b65d9cc0c9612834047fcab22f697b2c4bd"
    }
  ]
}
---

# Extend SST core

Use `rg` for the changed symbol in both repositories before editing a public interface. Identify framework behavior versus simulated behavior; hardware-specific behavior usually belongs in elements.

The core contribution guide specifies C++17, SST Output where possible, avoiding static variables and third-party dependencies, and compatibility for a major release cycle after API deprecation; public API changes are to be discussed with and approved by the core team ahead of time, and new features must add core-suite tests. Check the current guide before proposing an API change. Locate tests in `sst-core/tests`, and add an element integration case when an element consumes the changed API.

Read [contracts](contracts.md) only for the interfaces involved, then [validation](../development/testing.md). Check the repository finding tracker (`reviews/core/2026-09-25/findings.json`, when available) for an existing reproducer before designing a regression. A passing broad suite does not close a finding: demonstrate that its focused reproducer fails before the change and passes afterward, and preserve the archived baseline evidence. Report callers checked, compatibility impact, and serial/parallel coverage. Follow the user's working agreements for documentation and repository actions.
