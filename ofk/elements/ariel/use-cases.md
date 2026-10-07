---
{
  "type": "SST Element Profile",
  "title": "ariel main use cases",
  "description": "Application-driven memory traffic with CPU/frontend integration.",
  "tags": [
    "ariel",
    "Execution/frontend"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T19:00:11.117273+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ariel/arielcpu.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ariel/arielcpu.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "d63203c13553fc18e7daec83e8cf7c23a1982add98bb82a54a1e8e5ef2dd7744"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ariel/arielfrontend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ariel/arielfrontend.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "8111fe359a6dc8b809946d82f43a0e5c0ae45b5e72ebc449c3af578ef1bfb86c"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ariel/configure.m4",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ariel/configure.m4",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "93b208c6a84935e32bcaf310af5878d782eba154f30321389b9c9dd4643a1f1d"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ariel/tests/testsuite_default_Ariel.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ariel/tests/testsuite_default_Ariel.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "625d309de584d0fb24539a2b45c1d86c03a81f8c3119c41e01221de3e133d2c3"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ariel/frontend/pin3/pin3frontend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ariel/frontend/pin3/pin3frontend.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "05c7398803150e3f4f85c8cf94614ab2ecc5222c9fd11dd00e91096d9c39d118"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ariel/frontend/epa/epafrontend.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ariel/frontend/epa/epafrontend.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "824ceaa16adfecfe9a0201ca56a008fa52df0735d7f706791c32622ee2ca25d4"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/ariel/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/ariel/Makefile.am",
      "x-sha256": "6232fe0cb6f8bcc8d9348c92a909152997354adc155b3a8d04a918377ee09c38",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ],
  "x-element": "ariel",
  "x-role": "Execution/frontend",
  "x-coverage": "use-case-profile"
}
---

# ariel: main use cases

Role: **Execution/frontend**. Application-driven memory traffic with CPU/frontend integration.

## Use it for

- Explore application-driven cache/memory behavior using the supported frontend.
- Generate memory traces or vary modeled CPU/memory settings while keeping the application fixed.

## Boundaries and prerequisites

The registered CPU is `ariel.ariel`. Its default `frontend`, `ariel.frontend.pin`, is compiled only when elements were configured with Pin 3 (`HAVE_PINTOOL` and `HAVE_PIN3`), so a build without Pin registers only `ariel.frontend.epa`, for an already instrumented PEBIL/EPAX application. The application executes on the host; frontend/host compatibility and shared-memory support constrain the choice. Request issue limits model CPU pressure on memory, without a detailed target-ISA pipeline.

## Common companions

[memHierarchy](../memHierarchy/use-cases.md), [samba](../samba/use-cases.md), [opal](../opal/use-cases.md), [osseous](../osseous/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/ariel/`. Read these selectively and verify ELI names against current source.

- `arielcpu.h`
- `arielfrontend.h`
- `configure.m4`

## Validation starting point

Check application output and exit, emitted memory traffic, frontend compatibility, and the selected Ariel suite. The default suite separates Pin cases (gated by `INTEL_PIN_DIRECTORY`) from EPA cases (gated by `PEBIL_ROOT`/`EPAX_ROOT`). With `EPAX_ROOT`, EPA cases run only when pre-instrumented `*.arielinst` binaries already exist; otherwise setup fails with `epax commands not implemented yet`. The pass criterion is weak: no FATAL plus stdout/stderr line counts within 15 of the reference. Setup also runs `make` for the stream examples and the OpenMP barrier test. Several OpenMP cases skip on macOS. Intel Pin has no Apple Silicon build, so the Pin cases cannot run on an ARM64 macOS host at all; the October 7, 2026 gap-closure pass left them as the one native skip that no local change resolves.

Native runner suites:

- `tests/testsuite_default_Ariel.py`
- `tests/testsuite_mpi_Ariel.py`
- `tests/testsuite_testio_Ariel.py`

Use `python3 tools/sst_tools.py plan-tests --target ariel` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). This profile is a selection/use-case guide, not a complete extension manual; inspect the owning interface and nearby source example before editing.
