---
{
  "type": "SST Element Profile",
  "title": "vanadis main use cases",
  "description": "Binary execution with ISA, pipeline, LSQ, and OS interfaces.",
  "tags": [
    "vanadis",
    "Execution/CPU"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:00:40.969460+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/vanadis.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/vanadis.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "3a9ad3cdaa2503ded0096c1fd324890b4d708129a8261e18e14a8c0be7b8bef0"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/decoder/vdecoder.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/decoder/vdecoder.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "7aaea70caa9ea3524b4e22cfa909444316fd9c9bf57927f7127bd868825423c8"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/tests/basic_vanadis.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/tests/basic_vanadis.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "3a9574055711fca2ec2190c90edcd156b9b4321bfc079ed425528957c8cef674"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/tests/testsuite_default_vanadis.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/tests/testsuite_default_vanadis.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "7d6bbd8ef2d5ccae675c4a7329af8bbe2c65d4dacd0c2aa24792757d4901a5d9"
    }
  ],
  "x-element": "vanadis",
  "x-role": "Execution/CPU",
  "x-coverage": "detailed"
}
---

# vanadis: main use cases

Role: **Execution/CPU**. Binary execution with ISA, pipeline, LSQ, and OS interfaces.

## Use it for

- Run compatible MIPS/RISC-V programs through the selected CPU/decoder/OS setup.
- Explore modeled pipeline, instruction, memory-ordering, and accelerator/fault integration behavior.

## Boundaries and prerequisites

Binary ISA/ABI/syscall compatibility and implemented mechanisms determine fidelity. Modeled hardware threads differ from host simulation threads. `tests/basic_vanadis.py` resolves its default executable as `./small/<dir>/<exe>/<isa>/<exe>` relative to the working directory, so run it from `tests/` or pass `--exe`/`VANADIS_EXE`.

## Common companions

[memHierarchy](../memHierarchy/use-cases.md), [mmu](../mmu/use-cases.md), [kingsley](../kingsley/use-cases.md), [carcosa](../carcosa/use-cases.md), [golem](../golem/use-cases.md), [balar](../balar/use-cases.md)

## Source entry points

Paths below are relative to `sst-elements/src/sst/elements/vanadis/`. Read these selectively and verify ELI names against current source.

- `vanadis.h`
- `decoder/vdecoder.h`
- `tests/basic_vanadis.py`

## Validation starting point

Verify architectural output and normal exit for a deterministic program, plus the selected ISA/pipeline/OS regression.

Native runner suites:

- `tests/testsuite_default_vanadis.py`

Configuration candidates (inspect inputs and working-directory assumptions before running):

- `examples/vanadis_L1_L2_L3.py`
- `tests/basic_vanadis.py`

Use `python3 tools/sst_tools.py plan-tests --target vanadis` from sst-ai-tools for a read-only plan. See [shared testing](../../development/testing.md). For implementation detail read [overview](overview.md), [extension points](extension-points.md), and [validation](validation.md) as needed.
