# sst-ai-tools

Reusable skills, source-grounded knowledge, and local tools for developing models with the Structural Simulation Toolkit. Start with a modeling question, select an abstraction and owning element, then construct or extend the model and validate its behavior.

The [element selector](ofk/elements/index.md) documents the main use cases of **all 34 element directories** in the checked SST source. Every profile describes its role, boundaries/prerequisites, common companions, source entry points, and validation path. Merlin, memHierarchy, Ember, Mercury, Vanadis, Carcosa, and Balar additionally have detailed overview, extension-point, and validation guides; memHierarchy also has backend and system-composition guides, Ember a motif catalog, and Iris fabric and collective-registry guides.

## Choose a workflow

| What you want to do | Skill | Example request |
|---|---|---|
| Construct a network model | [build-network-model](skills/build-network-model/SKILL.md) | “Model congestion in a 64-node network; help choose the fidelity and traffic.” |
| Construct a CPU/memory model | [build-cpu-model](skills/build-cpu-model/SKILL.md) | “Study cache stalls; decide whether synthetic traffic or program execution is appropriate.” |
| Configure/debug an existing system | [sst-configure-model](skills/sst-configure-model/SKILL.md) | “Connect this processor to two cache levels and validate its parameters.” |
| Compile or diagnose SST installation | [sst-build](skills/sst-build/SKILL.md) | “Check why elements loads the wrong core installation.” |
| Add behavior to an element | [sst-extend-element](skills/sst-extend-element/SKILL.md) | “Add a routing policy while preserving endpoint and initialization behavior.” |
| Change framework internals | [sst-extend-core](skills/sst-extend-core/SKILL.md) | “Change this event API and identify affected element consumers.” |
| Validate a change | [sst-test-change](skills/sst-test-change/SKILL.md) | “Select the smallest regressions covering this diff.” |
| Refresh source-dependent knowledge | [sst-refresh-knowledge](skills/sst-refresh-knowledge/SKILL.md) | “Review the guides whose referenced source changed.” |
| Create an Ember communication motif | [create-ember-motif](skills/create-ember-motif/SKILL.md) | “Add a motif where every rank sends to its two neighbors, then reduces.” |
| Create a Mercury skeleton application | [create-mercury-skeleton](skills/create-mercury-skeleton/SKILL.md) | “Write a two-rank MPI skeleton that exchanges 1 KiB messages and runs on Mercury.” |

The network/CPU skills ask about missing modeling priorities and constraints before consequential choices. They reuse answers, select workload and hardware layers separately, and continue through implementation and validation. See [common model combinations](USE_CASES.md) and [the knowledge index](ofk/index.md).

## Layout and setup

```text
sst-ai-tools/
  ofk/          OKF knowledge bundle and progressively loaded indexes
  skills/       Ten task workflows
  tools/        Inspection, catalog, test planning, validation, evaluation
  tests/        Tool behavior tests
  evaluation/   Agent prompts and evaluator-only rubrics
```

Use Python 3.11 or newer. Inspection, catalog, source checks, test planning, and evaluation preparation use only the standard library. Repository/skill validation and development checks use the pinned dependencies in `requirements-dev.txt`:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python tools/validate.py --workspace ..
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/ruff check tools tests
.venv/bin/ruff format --check tools tests
```

Commands assume this repository is the current directory and sibling `sst-core`/`sst-elements` checkouts exist. `--workspace` selects another parent directory; `--core` and `--elements` override individual roots. For links, skills, and knowledge metadata checks without SST source, use `tools/validate.py --repository-only`; it reports local sources whose contents were not checked. Actual simulations require a working SST installation and the selected element's input artifacts and dependencies.

## Local tools

```sh
python3 tools/sst_tools.py inspect --workspace ..
python3 tools/sst_tools.py catalog --workspace ..
python3 tools/sst_tools.py check --workspace ..
python3 tools/sst_tools.py plan-tests --workspace .. --target kingsley
python3 tools/sst_tools.py plan-tests --workspace .. --target zodiac
python3 tools/sst_tools.py plan-tests --workspace .. --target hermes
```

`inspect` reports source revisions, dirty state, and executable locations on PATH. `catalog` reports roles, profiles, documentation coverage, suite locations, and profiles whose element identity no longer matches the source tree. `check` verifies knowledge structure, links, recorded source content (including the exact letter case of cited paths, which case-insensitive filesystems otherwise mask), and missing element profiles. All return JSON.

`plan-tests` accepts core or any element directory, discovers suites under `test/` and `tests/`, and emits argument arrays with explicit suite files without executing. These include non-default and nested suites; narrow the selection and inspect prerequisites before running, especially for expensive sweeps. Runner category filters still apply. Elements without native suites receive standalone-configuration candidates or an integration-required result. Check the installed runner's help and working directory before executing a plan. An empty test discovery, skipped suite, or simulator exit alone does not prove behavioral correctness.

## Agent use

Point an agent at `skills/<name>/SKILL.md`, or symlink the skill directories into its skill location while preserving this repository. Resolve the actual skill file location so relative references still reach `ofk/` and `tools/`. Copying an individual skill directory breaks shared references. No global agent configuration is installed automatically.

Give the agent the source roots, modeling question, and constraints already known. It should load the small relevant guide/profile and current implementation, rather than read the whole corpus. For example:

> Use build-cpu-model from this repository. I want to measure memory bandwidth under sequential and random access patterns, not instruction timing. Keep the workload finite and avoid external application toolchains.

## Knowledge maintenance and source updates

`ofk/` retains the requested directory name; documents follow [Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md). The local tools require this repository's JSON-shaped YAML frontmatter convention, a subset of valid OKF that is readable with the standard library. Local SST sources record a canonical commit URL, repository/path, and SHA-256 of the checked content, detecting committed and local edits. External toolchain references require separate review and are reported as unchecked. See [contribution and refresh procedure](CONTRIBUTING.md).

After intentionally updating SST checkouts, run the catalog/check commands, inspect changed-source diffs, and reconcile affected claims. A new source hash is not semantic verification. Only after review, record the updated provenance:

```sh
python3 tools/sst_tools.py record-source --document ofk/elements/merlin/use-cases.md --workspace ..
```

Update generated metadata after meaningful prose edits. Add verified events only after actual independent confirmation. Structural validators do not prove model fidelity or correctness. These tools do not pull, upgrade dependencies, or change SST sources automatically.

## Evaluation and coverage limits

[EVALUATION.md](EVALUATION.md) provides eight paired baseline/pilot tasks, private scoring rubrics, isolated source snapshots, and session-usage accounting. Prepared experiments stay frozen; create a new experiment to evaluate new knowledge.

The use-case catalog covers every element in this source revision; it does not claim complete API documentation, release-independent compatibility, calibrated hardware fidelity, or tested runtime support for every element. All knowledge remains draft and source-grounded. Focused devel runtime validation is recorded in [RUNTIME_VALIDATION.md](RUNTIME_VALIDATION.md): core and 32 enabled elements build, selected native and standalone checks run, and a Carcosa registration assertion fails. External-runtime, disabled-test, and wider coverage gaps remain; paired AI token-efficiency measurements are still outstanding.

## Cross-cutting guides

Beyond the element profiles, the bundle covers workflows every SST user meets: [statistics](ofk/using-sst/statistics.md) and the [statistics API](ofk/core/statistics-api.md), [run-time options](ofk/using-sst/run-options.md), [parallel execution and partitioning](ofk/using-sst/parallel.md), [checkpoint and restart](ofk/using-sst/checkpoint.md), and [out-of-tree element libraries](ofk/development/external-elements.md). memHierarchy additionally has a [backend catalog](ofk/elements/memHierarchy/backends.md) and a [multi-core and networked systems guide](ofk/elements/memHierarchy/systems.md); Ember has a [motif catalog](ofk/elements/ember/motifs.md). All are source-grounded drafts; the installed `sst -h` and `sst-info` remain authoritative for other revisions.

## Mercury, SST-HGCC, and MV2

See [the application integration guide](ofk/elements/mercury/hgcc-mv2.md) for HGCC compilation/rewriting, Mask-MPI versus adapted MVAPICH2, runtime/transport relationships, and validation criteria. External toolchain references are pinned but reported as `external_sources_not_checked`; local SST provenance checks remain enabled. The HGCC compile route, Mask-MPI skeletons, and the adapted MVAPICH2 route were all exercised on the devel install on October 7, 2026 (see [RUNTIME_VALIDATION.md](RUNTIME_VALIDATION.md)); MV2 passes only with a local Iris provider patch and wrapper additions that upstream does not carry.

## Toolchain installation and Iris extensions

- [SST-HGCC installation](ofk/development/hgcc-install.md)
- [Adapted MV2 installation](ofk/development/mv2-install.md)
- [Iris fabrics and new providers](ofk/elements/iris/fabrics.md)
- [Iris collective algorithms and registration](ofk/elements/iris/collectives.md)

These are source-reviewed guides; writing them did not install external dependencies or run additional HGCC/MV2/provider tests.

## MV2 platform and timing details

See [Linux/macOS integration](ofk/elements/mercury/mv2-platforms.md) and [MV2 timing](ofk/elements/mercury/mv2-timing.md). The guides distinguish source support from executed validation, MPI timer backends from modeled costs, and active callbacks from no-op or unconsumed controls.

## Review tracking

The [review archive](reviews/index.md) retains the September 25 core correctness review and its element-impact follow-up. It includes commit-pinned source links, original-file hashes, and a machine-readable finding tracker. The [October 6 reassessment](reviews/core/2026-10-06/index.md) reproduces all eleven findings on the recorded devel revisions and retains executable probes/evidence.
