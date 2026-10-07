# Contributing and maintaining knowledge

Keep source-grounded knowledge in `ofk/`, workflow instructions in `skills/`, and deterministic operations in `tools/`. Prefer a shared workflow plus element-specific knowledge over duplicating a skill for every element.

## Add or revise an element profile

Use `ofk/elements/<source-directory>/use-cases.md`. Document the element's role, two or three main use cases, boundaries/prerequisites, common companions, exact source entry points, and a meaningful validation path. Directory names are case-sensitive and may differ from ELI registration names. Distinguish hardware models, workloads, interface/support libraries, and teaching examples.

Give the concept a type/title/description, draft status, generated metadata, and source entries. Follow existing JSON-shaped YAML frontmatter. Local SST sources need canonical resource URLs and the producer extension fields `x-repository`, `x-path`, `x-commit`, and `x-sha256`. Use the actual source file content, including local changes, and cite paths with the checkout's exact letter case; the checker rejects case mismatches that macOS would otherwise accept, because GitHub and Linux will not resolve them. External toolchain sources omit `x-repository`/`x-path`; pin their resource URL and record available hashes/revisions, but review them separately because the local checker does not verify their contents. Set `x-element`, `x-role`, and `x-coverage` for catalog discovery. Keep full manuals and large copied code out of these profiles.

Link the profile from its directory index and the element selector. Add detailed overview, extension-point, or validation documents when source inspection can support useful guidance; do not create empty templates or imply every element has detailed coverage. Links inside OKF must resolve within the bundle. Refer to optional repository evidence outside `ofk/` with a clearly identified inline path, since isolated pilot runs copy only knowledge, skills, and tools. Keep links in portable root documentation independent of ignored `.runtime` artifacts; describe those local paths explicitly.

## Refresh after source changes

1. Inspect source roots and dirty state. Update checkouts only within the user's requested scope; preserve unrelated work and installation identity.
2. Run `tools/sst_tools.py catalog` and `check`. New elements require profiles; changed content requires review of affected claims. Missing sources may indicate moves/removals rather than a reason to drop claims blindly.
3. Read relevant diffs, base APIs, configurations, and test contracts. Correct descriptions, entry points, limitations, and test selection before refreshing hashes.
4. Run `record-source` for each reconciled document. Update `generated.at` after a meaningful content edit. Keep status draft unless an actual review supports changing it; record verification only when performed.
5. Validate links, metadata, coverage, and tooling. Run behavioral SST checks when implementation or instructions change; report missing runtime coverage.

Source hashes are freshness signals, not proof of semantic accuracy. A source commit URL may describe the committed version while a local hash includes edits; inspect the local file when hashes differ from the committed artifact. Prepared evaluation snapshots remain immutable; prepare new runs for new knowledge.

## Skills and tools

Skills should route quickly, ask only about consequential missing constraints, and describe a concrete completion criterion. Keep shared knowledge in one place. Maintain skill directories with their sibling resources when installing.

Runtime helpers should remain standard-library-only where practical. PyYAML and Ruff are development dependencies. Ask before adding/upgrading production dependencies. Add tests for meaningful invariants such as source freshness, safe paths, missing coverage, no-suite integration paths, and measurement accounting.

```sh
.venv/bin/python tools/validate.py --workspace ..
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/ruff check tools tests
.venv/bin/ruff format --check tools tests
```

Keep comments and commit messages short. Keep working notes untracked in the project root. Do not stage, commit, push, or create a pull request merely because documentation changed; follow the user's requested repository actions.
