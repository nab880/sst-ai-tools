---
name: create-mercury-skeleton
description: Write, build, run, and validate a Mercury skeleton application, in-tree or with SST-HGCC, including Mask-MPI programs.
---

# create-mercury-skeleton

This skill belongs to the sst-ai-tools repository. Resolve the real path of this skill directory first, then use `../..` as the repository root; this also works when the skill directory is symlinked into an agent's skill directory. Keep this repository intact when installing; sibling OFK documents and tools are required. Resolve SST source roots from the user or the sibling workspace, not the shell's current directory.

Read [the skeleton guide](../../ofk/elements/mercury/skeleton-apps.md). Establish what the application must model: plain OS behavior, MPI communication through Mask-MPI, or an adapted MPI implementation, and whether compute must be skeletonized. Choose the in-tree `ext` library route when no HGCC toolchain is available or required; choose `hg++` when `main` rewriting, per-rank globals, or skeletonized compute matter ([HGCC installation](../../ofk/development/hgcc-install.md), [HGCC and MV2](../../ofk/elements/mercury/hgcc-mv2.md)).

Write the source with `ssthg_app_name` and the skeleton header, copy a shipped example (`mercury/tests/ostest.cc` or `mask-mpi/tests/sendrecv.cc`), and keep real computation that the correctness oracle needs. Build the library (on macOS keep `SDKROOT` set to the SDK the install was configured with), put it on the element search path or pass `--add-lib-path`, and write the driver with matching `app1.name`, `app1.exe_library_name`, libraries, dependencies, and rank count. Run it from the platform file's directory; `sst-info` prints nothing for an application library, so the run is the check. For an adapted-MVAPICH2 application also run `nm -u` on the bundle and add wrappers for every unresolved `MPI_*` symbol first, since unwrapped calls bind to the host MPI. Then verify per-rank output, natural completion, and that simulated time advanced only through modeled calls; add a reference-output case following the hg or Mask-MPI suites when the user wants a regression.

Use `python3 <tools-root>/tools/sst_tools.py --help` for deterministic helpers. Load only task-relevant knowledge. Documents are drafts; inspect current source for implementation details. Do not update, pull, install dependencies, or publish merely because the task uses this skill; follow the user's requested scope.
