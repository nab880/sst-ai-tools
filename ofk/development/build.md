---
{
  "type": "SST Guide",
  "title": "Build and diagnose SST",
  "description": "Keep core installation, element build, and runtime discovery consistent.",
  "tags": [
    "build"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T19:00:11.886084+00:00"
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
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/config/sst_core_check_install.m4",
      "x-repository": "sst-elements",
      "x-path": "config/sst_core_check_install.m4",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "31d3068eb03ccfd6dddeb55009a300550d8f40f51218d0f544e086da343b1a21"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/select_build.py",
      "x-repository": "sst-elements",
      "x-path": "select_build.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "60004a71ba14e6333b2d59c1036304ae570908c2a9758ca0b6dbe03d8a68b590"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/Makefile.am",
      "x-sha256": "a47fe08eeb343d10ea6284f542d586bf9b011f8d09bd50821f886a7a63e3db2e",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/config/sst_check_curses.m4",
      "x-repository": "sst-core",
      "x-path": "config/sst_check_curses.m4",
      "x-sha256": "6c5be95f6dc45d2fb83e633f1e6bbd7ff417c2a440e147083bfa6a2fac913232",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/tests/testsuite_default_sstinfo.py",
      "x-repository": "sst-core",
      "x-path": "tests/testsuite_default_sstinfo.py",
      "x-sha256": "a5f680495bdc06ebb50eaa645ac8581b589a47995fbb3b2ebc56a8a2588312e5",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    }
  ]
}
---

# Build and diagnose SST

Inspect source roots, existing build directories, installation prefix, compiler, MPI availability, and executable locations first. Preserve existing configuration arguments when rebuilding.

The maintained local starting point is Autotools: `autogen.sh` generates configure, then configure/build/install core before elements. Elements accepts `--with-sst-core=DIR`; verify that DIR is the intended core installation, not merely its source checkout. Use each checkout's configure help for supported options. Prefer an isolated build and prefix for a new configuration.

Elements configure locates `sst-config`, `sst-register`, and `sst-snippets.py` under that prefix, and imports the compiler/MPI commands and flags from `sst-config`. Changing only the elements shell's `CC`/`CXX` may therefore select a different compiler than intended; inspect the core configuration first. Record both source revisions and verify their API compatibility instead of treating matching branch names as proof of a matched installation.

Core's ncurses probe (`config/sst_check_curses.m4`) takes the first `ncursesN-config` on `PATH`. On the recorded macOS host that was `/usr/bin/ncurses5.4-config`, whose `-lncursesw` is absent from the SDK, so the link test failed silently, `HAVE_CURSES` stayed undefined, and `sst-info -i` plus its testsuite case were skipped. Configuring with `--with-ncurses=/opt/homebrew/opt/ncurses` defines it; `tests/testsuite_default_sstinfo.py` then passes as long as `TERM` is set, since ncurses exits with `cannot initialize terminal type` otherwise.

With library arguments, `sst-elements/select_build.py` rewrites `.ignore` files and reruns `autogen.sh`; it is a mutation, not an inspection command. Invoked bare or with `help` it only prints usage (category names, not the element list), and a library absent from its `deps` map is rejected with "Build will not be modified", so a new element needs a `deps` entry before the script can select it. Its dependency map includes commonly used combinations, not only mandatory dependencies. Do not invoke it just to discover available elements.

For loader errors, compare installed binaries, library search/registration configuration, and `sst-info` output with the intended build. `sst-info` loads each element library on its own, so a library that references another element's symbols without linking it (Carcosa references memHierarchy's convertor type) can fail there with an unresolved-symbol `dlopen` error on macOS while a simulation that loads memHierarchy first runs normally; libraries that register only API types (Hermes) are reported as not found. Treat a simulation-level load as the authoritative check. For compiler failures retain the first meaningful diagnostic and a reproducible command. A successful source build does not prove the runtime loads that build.

Use `python3 tools/sst_tools.py inspect --workspace /path/to/workspace` for a read-only inventory. Follow [testing](testing.md) after changes.
