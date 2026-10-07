---
{
  "type": "SST Guide",
  "title": "Select and run SST validation",
  "description": "Use installed SST test runners with focused source suites.",
  "tags": [
    "testing"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T04:06:47.310546+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/testingframework/test_engine.py",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/testingframework/test_engine.py",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "8f5c1a9a1091d7817f58e78ce815f94a6a50946d7b2279b69ead030783b05a3a"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/CONTRIBUTING.md",
      "x-repository": "sst-core",
      "x-path": "CONTRIBUTING.md",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "00060f1dc1e27dac1b4e2e5dbcca5b65d9cc0c9612834047fcab22f697b2c4bd"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/merlin/tests/testsuite_default_merlin.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/merlin/tests/testsuite_default_merlin.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "f2f31edb4736e799e7da720c3a0f629295948ed3d8db9108dfb12b103ced4577"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/stataccumulator.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/stataccumulator.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "bc5c8537334dbb50c161f79a8fdd66910ba2cff7cdbd6733d0bfe24ee011103c"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/statapi/stathistogram.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/statapi/stathistogram.h",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "556863c674fae372e975d001d313c0b16cfc605afd1ebd214071ccdf0980bca7"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/testingframework/test_engine_globals.py",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/testingframework/test_engine_globals.py",
      "x-sha256": "d4b1e8af5d412dc25c21433ad6d0a2f193d16fc6647a63b2685ad7e29ae70093",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/testingframework/sst_unittest_support.py",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/testingframework/sst_unittest_support.py",
      "x-sha256": "625ffc183d13d56e2e55040a3e9c7c21e9329b12d28522440ed8e27d80b8fc8f",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    }
  ]
}
---

# Select and run SST validation

The installed runners are `sst-test-core` and `sst-test-elements`. In the checked source, `-p` selects suite files/directories, `-w` selects suite filename wildcards, `-e` selects exact test method names, `-l` lists suites, and `-r`/`-t` set rank/thread counts. Quote `-w` patterns: the runner wraps them as `testsuite_<pattern>.py`. Directory discovery defaults to `default` suites; `-y all` selects all suite types and is mutually exclusive with `-w`. `-m` controls test categories separately from filenames: undecorated tests are tagged `pr`, the default category set is `{pr}`, and a `categorize`d test raises `SkipTest` under any other selection, so a discovered case can still be skipped as nightly. Confirm the installed runner's `--help` before running a different version.

Examples from the tools repository root (adjust the workspace):

```sh
python3 tools/sst_tools.py plan-tests --workspace .. --target merlin
python3 tools/sst_tools.py plan-tests --workspace .. --target memHierarchy
python3 tools/sst_tools.py plan-tests --workspace .. --target core
```

These emit plans without executing. Supported targets are core and every element directory in the checked source. Discover profiles and actual suite paths with `catalog`. The planner handles `test/` and `tests/`; a support library without suites/configurations requires consumer integration validation. Mercury suites use hg filenames; explicit paths avoid wildcard confusion. Carcosa has no runner suites in this checkout, so its plan lists standalone configurations and requires a separate behavioral oracle. Balar can invoke costly external-toolchain builds; inspect prerequisites and select a case first. Narrow by changed behavior before running a broad suite. Element tests use `SSTTestCase`, `run_sst`, and reference comparisons; read the relevant template before introducing a new test. Investigate output differences before refreshing references. Parallel runs should test the same completion and correctness properties, with supported rank/thread counts.

For C++ changes use the repository format configuration; core's guide identifies clang-format 12 and `scripts/clang-format-test.sh`. Check current conventions for elements separately. Report missing runner, compiler, formatter, or dependency as a validation gap.

Check the executed test count and each skip reason. Parameterized suites generate full method names; a guessed short `-e` selector can execute zero cases. Listing a suite, importing a model, or reaching a configured time limit is not a behavioral pass. Use a natural-completion and correctness oracle appropriate to the workload.

The core reassessment (repository evidence: `reviews/core/2026-10-06/index.md`, when available) retained focused failures despite broad native-suite passes. Reuse its relevant probes for clocks, parameter precedence, destination generation, serialization, and statistics. In particular, independently check histogram bins and accumulator extrema/variance before using those statistics as a correctness or performance oracle; the recorded revisions have reproduced defects in those paths. The mechanisms are visible in source: the histogram computes a bin start as `floor(value / binWidth) * binWidth` while output labels bins from `minvalue`, the accumulator's `getVariance` returns `count * sum_sq - sum * sum` without normalization, and its maximum starts at `numeric_limits::min()`, the smallest positive value for floating types.
