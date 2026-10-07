---
{
  "type": "SST Element Profile",
  "title": "shogun main use cases",
  "description": "Round-robin crossbar with message-rate limits.",
  "tags": [
    "shogun",
    "Interconnect"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:58.956304+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/shogun/shogun.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/shogun/shogun.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "af5ce9b9ebe8a822934526a76a442107375c68a08a46972409a1c2764e73a1fa"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/shogun/shogun_nic.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/shogun/shogun_nic.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "976737d8c990f6397fd1d644d4c8681da43699ee89cb831bb9bcddfffa27eb52"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/shogun/tests/testsuite_default_shogun.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/shogun/tests/testsuite_default_shogun.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "33ec6cf962b3ba0236a0921d4d256c1e269adf4be6822b1bcdbecc0e24138134"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/shogun/shogun.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/shogun/shogun.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "20a57a404d2ae3e02b3f811a294474872f4d69a3c4c1533049a53a9f9cce5043"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/shogun/shogun_nic.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/shogun/shogun_nic.cc",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "dfd637543e0de1497e7f751d257dc23f426a9b5e0e59258b8aedcbea11a91495"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/shogun/arb/shogunrrarb.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/shogun/arb/shogunrrarb.cc",
      "x-sha256": "addd1f282aac1f0531119c6747972ba6627abe0783b2ae6276828a321a619b37",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "shogun",
  "x-role": "Interconnect",
  "x-coverage": "use-case-profile"
}
---

# shogun: main use cases

Role: **Interconnect**. Round-robin crossbar with message-rate limits.

## Use it for

- Connect endpoints through an arbitrated crossbar for memory-system studies.
- Explore crossbar contention by varying its clock, queue depth, and message issue/ejection limits.

## Boundaries and prerequisites

Use `shogun.ShogunXBar` with `shogun.ShogunNIC` implementing SimpleNetwork. The implementation always constructs round-robin arbitration even though ELI advertises an `arbitration` parameter. Capacity is modeled in messages/slots per cycle, not serialization time proportional to packet bytes; `out_msg_per_cycle = -1` is documented as unlimited but any negative value is clamped to 256, while `in_msg_per_cycle = -1` is honored, and `ShogunNIC::getLinkBW()` returns a hard-coded `1GB/s`. A bandwidth comparison with a flit-based mesh must account for these differences.

## Common companions

[memHierarchy](../memHierarchy/use-cases.md), [miranda](../miranda/use-cases.md); no shipped configuration pairs Shogun with Vanadis.

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/shogun/`. Read these selectively and verify ELI names against current source.

- `shogun.h`
- `shogun_nic.h`

## Validation starting point

Check endpoint delivery, fairness/contention when required, finite completions, and targeted Shogun tests. `tests/hierarchy_test_multi.py` exists with a reference file but is not in the suite.

Native runner suites:

- `tests/testsuite_default_shogun.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/basic_miranda.py`
- `tests/hierarchy_test.py`

Use `python3 tools/sst_tools.py plan-tests --target shogun` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
