# mercury

- [Mercury application and node selection](overview.md) — Route Mercury work through its hg registration and node/OS/NIC layers.
- [Extend Mercury nodes and services](extension-points.md) — Separate modeled compute, application runtime, and NIC transport behavior.
- [Validate Mercury runtime and transport](validation.md) — Respect serial-only and architecture-specific runtime cases.
- [Main use cases](use-cases.md) — Node, OS, NIC, and modeled compute machinery.

- [SST-HGCC and MV2 application paths](hgcc-mv2.md) — Compile applications for Mercury and select modeled versus implementation-level MPI behavior.
- [Write and run a Mercury skeleton application](skeleton-apps.md) — Build a skeleton in tree or with SST-HGCC, drive it from Python, and validate it.

- [HGCC installation](../../development/hgcc-install.md) — Application-toolchain prerequisites and build procedure.
- [MV2 installation](../../development/mv2-install.md) — Adapted MPI build/link/runtime prerequisites.

- [MV2 Linux/macOS support](mv2-platforms.md) — Platform-specific linking, runtime workarounds and support boundaries.
- [MV2 timing](mv2-timing.md) — Clock replacement, active model costs, no-op stubs and sensitivity checks.
