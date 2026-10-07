---
{
  "type": "SST Guide",
  "title": "Validate Vanadis program execution",
  "description": "Pair ISA-compatible programs with observable architectural results.",
  "tags": [
    "vanadis",
    "validation"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T19:00:11.031939+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/tests/testsuite_default_vanadis.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/tests/testsuite_default_vanadis.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "7d6bbd8ef2d5ccae675c4a7329af8bbe2c65d4dacd0c2aa24792757d4901a5d9"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/vanadis/tests/basic_vanadis.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/vanadis/tests/basic_vanadis.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "3a9574055711fca2ec2190c90edcd156b9b4321bfc079ed425528957c8cef674"
    }
  ]
}
---

# Validate Vanadis program execution

`tests/testsuite_default_vanadis.py` constructs a matrix over `tests/small/{basic-io,basic-math,basic-ops,misc,rocc,multicore}`: single-threaded programs, fork/clone/pthread/OpenMP multicore cases, and one RoCC case that uses `rocc_vanadis.py`, with ISA-specific reference files. Outside the nightly category it skips every matrix row numbered above 15, so only the leading basic-io rows run; the whole suite also skips when SST ranks or threads exceed one. `MakeTests` and `updateFiles` default false in the checked suite; do not toggle reference regeneration to hide failures.

Use `tests/basic_vanadis.py` and the matrix's executable/environment setup for a tiny hello-world or opcode case. Verify expected process output and exit behavior, not only simulator completion. Confirm binary existence, target ISA/ABI, loader, and supported syscalls before interpreting a failure. A musl cross compiler need not be a GCC build: `zig cc -target riscv64-linux-musl -static` from a self-contained Zig download produced RVC double-float ELFs with the same header flags as the shipped binaries, and they ran under Vanadis in the October 7, 2026 rdmaNic exercise; statistics golds remain tied to the toolchain that produced them.

The matrix generates exact test method names of the form `test_vanadis_short_tests_<index>_<dir>_<exe>_<isa>_<golddir>` after hyphens become underscores; the gold-directory tag is usually empty, leaving a trailing underscore. Use the runner's discovered name with `-e` and confirm that at least one case executed; a short guessed name does not select a parameterized case. Keep the matrix row's executable and environment settings together when extracting a standalone smoke test.

Hardware cores/threads in the modeled system differ from SST's host rank/thread settings. Cover relevant combinations intentionally. For LSQ or memory changes include data-correctness cases and a [memHierarchy](../memHierarchy/validation.md) integration check. For ISA changes compare boundary-value architectural results with known expected values.

Use [test planning](../../development/testing.md) with target `vanadis`; keep reference updates independently justified.
