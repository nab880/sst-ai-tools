---
{
  "type": "SST Element Profile",
  "title": "simpleElementExample main use cases",
  "description": "Examples of SST component APIs and lifecycle.",
  "tags": [
    "simpleElementExample",
    "Teaching/framework example"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:04:25.983494+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleElementExample/README",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleElementExample/README",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "ab77aa3bbde59b550c3946988cf6b8044e3ee66a23b9f93ade9cfbb9d6f26aa2"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleElementExample/example0.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleElementExample/example0.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "d664ae044379a0212046dccba820a9fc50e2e9318d3df27028b6dda72ccd8240"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleElementExample/basicSimLifeCycle.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleElementExample/basicSimLifeCycle.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "83e3dd04a6f72f316f48544a11dbed96f115512096193d37c2f641a35f5777b6"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleElementExample/tests/testsuite_default_simpleComponents.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleElementExample/tests/testsuite_default_simpleComponents.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "872897afca6774363391413ac8eee236eede5632fd45b6b431c20691ba69dccd"
    }
  ],
  "x-element": "simpleElementExample",
  "x-role": "Teaching/framework example",
  "x-coverage": "use-case-profile"
}
---

# simpleElementExample: main use cases

Role: **Teaching/framework example**. Examples of SST component APIs and lifecycle.

## Use it for

- Learn registration, parameters, events, links, clocks, statistics, and subcomponents.
- Start a focused framework reproducer from the example covering the needed API.

## Boundaries and prerequisites

Examples teach mechanics and are not calibrated hardware models. Prefer an owning element example when implementing domain-specific behavior.

## Common companions

These examples exercise SST core directly; add domain elements only when the task needs them.

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/simpleElementExample/`. Read these selectively and verify ELI names against current source.

- `README`
- `example0.h`
- `basicSimLifeCycle.h`

## Validation starting point

Use each example script and its expected reference output; select the corresponding simpleComponents regression. `basicCheckpoint.py` has no active regression or reference file (its case is commented out), `basicClocks`/`basicParams` skip when ranks or threads exceed one, and the pass criterion is a sorted diff.

Native runner suites:

- `tests/testsuite_default_simpleComponents.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `tests/basicCheckpoint.py`
- `tests/basicClocks.py`

Use `python3 tools/sst_tools.py plan-tests --target simpleElementExample` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
