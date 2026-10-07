---
{
  "type": "SST Installation Guide",
  "title": "Install adapted MVAPICH2 for Mercury",
  "description": "Build the simulator-specific MPI stack, prepare PMI-safe archives, and verify a small Mercury-hosted MPI application.",
  "tags": [
    "installation",
    "mv2",
    "mercury"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T18:59:42.628746+00:00"
  },
  "sources": [
    {
      "resource": "https://github.com/nab880/mv2-test/blob/0bd13efd074affc7c8e3cca5add42af699362748/build_linux.sh",
      "x-commit": "0bd13efd074affc7c8e3cca5add42af699362748",
      "x-sha256": "dc864c71a1d47af1926daa84ba215b4936be3cb590f18aeb14ed129f0e79fdb5",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s0"
    },
    {
      "resource": "https://github.com/nab880/mv2-test/blob/0bd13efd074affc7c8e3cca5add42af699362748/build_mac.sh",
      "x-commit": "0bd13efd074affc7c8e3cca5add42af699362748",
      "x-sha256": "c7960921198f7bccf9a6a8c6ddd00c1039f5240abd7e067d5a79ee26e44fbc6a",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s1"
    },
    {
      "resource": "https://github.com/nab880/mv2-test/blob/0bd13efd074affc7c8e3cca5add42af699362748/build_all_mac.sh",
      "x-commit": "0bd13efd074affc7c8e3cca5add42af699362748",
      "x-sha256": "4fe9b36caa9c9504724f1db1515ff780c13c7ab3a10b57b46de961cf4474aff1",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s2"
    },
    {
      "resource": "https://github.com/jmlapre/sst-hgcc/blob/41cd313574c994f6fefe2c361124e854b7e4ac0f/hgcclib.py",
      "x-commit": "41cd313574c994f6fefe2c361124e854b7e4ac0f",
      "x-sha256": "38014f9f689578219eed44aa4b51ef1c4ad3a5a9a88109428c3f2e830834ffc5",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s3"
    },
    {
      "resource": "https://github.com/jmlapre/sst-hgcc/blob/41cd313574c994f6fefe2c361124e854b7e4ac0f/hglink.py",
      "x-commit": "41cd313574c994f6fefe2c361124e854b7e4ac0f",
      "x-sha256": "d1bc8eea70077debc697fa0db9eccc766fa39158e9a4cbfb704f9baccfab33d5",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s4"
    },
    {
      "resource": "https://github.com/jmlapre/sst-hgcc/blob/41cd313574c994f6fefe2c361124e854b7e4ac0f/tests/mv2/_mv2_run_common.sh",
      "x-commit": "41cd313574c994f6fefe2c361124e854b7e4ac0f",
      "x-sha256": "31654eb79aaa0a9495c5e3292fc09f24e81856c310adb0ddd101957c90b33ddb",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s5"
    },
    {
      "resource": "https://github.com/nab880/mv2-test/blob/0bd13efd074affc7c8e3cca5add42af699362748/build_all_linux.sh",
      "x-commit": "0bd13efd074affc7c8e3cca5add42af699362748",
      "x-sha256": "4c9f0e73efbac4b3d921afdf1754e9a407e0f7d1b89b9986ed52b07d96a521e7",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s6"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-hgcc/blob/2a37f8c541f02344f7d540188e52efd1f080a6fc/support/mv2/mv2_mpi_wrappers.c",
      "x-commit": "2a37f8c541f02344f7d540188e52efd1f080a6fc",
      "x-sha256": "e80c96e0c40d0a26d2b0368917ccf55bd9900a62e661cda03dea4fb8e3179ab9",
      "x-review-scope": "External source inspected locally; freshness review is manual"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-hgcc/blob/2a37f8c541f02344f7d540188e52efd1f080a6fc/tests/mv2/collective-run-all.sh",
      "x-commit": "2a37f8c541f02344f7d540188e52efd1f080a6fc",
      "x-sha256": "c986cea93622ad7f34cd8e3839e6ac9aa7911116e03348b1bb7ea97fb60d4794",
      "x-review-scope": "External source inspected locally; freshness review is manual"
    }
  ]
}
---

# Install adapted MVAPICH2 for Mercury

## Choose the simulator-adapted stack

This guide refers to the inspected `mv2-test` fork and the MV2-enabled HGCC wrapper/linker. A stock MVAPICH2 installation linked to host PMI/libfabric is a different stack. This recipe was executed on the recorded devel install on October 7, 2026 (macOS ARM64); the [application guide](../elements/mercury/hgcc-mv2.md) records that run and the Iris provider patch it needed.

Build [SST-HGCC and its SST prerequisites](hgcc-install.md) first, configuring HGCC with `--prefix` equal to the SST prefix: its `--mpi=mvapich2` link looks for `include/sst/elements` and `share/hgcc/mv2` under the HGCC prefix, and a separate HGCC prefix satisfies neither that linker nor the scripts below. The supplied MV2 scripts assume a **combined prefix** containing `sst-config`, `hgcc`, `hg++`, and `ssthg_clang`, and Iris `libfabric`/`libpmi` under `lib/sst-elements-library/ext`.

```bash
set -e
SST_INSTALL="/path/to/combined/install"
MV2_SOURCE="/path/to/simulator-adapted/mv2-test"
HGCC_SOURCE="/path/to/MV2-enabled/sst-hgcc"
export PATH="$SST_INSTALL/bin:$PATH"
hgcc --help
```

Confirm help exposes `--mpi=mvapich2`, `--mpi-prefix`, and `--app-name`. Confirm the linker implementation exists as well; a parsed flag without the corresponding link path is not enough.

## 1. Build adapted MVAPICH2

The inspected checkout provides `build_linux.sh` and `build_mac.sh`:

```bash
# Choose the script for the host, in a disposable build/source checkout.
NPROC=4 bash "$MV2_SOURCE/build_linux.sh" "$SST_INSTALL"
# On macOS, use build_mac.sh instead.
```

These scripts run distclean/autogen/configure, build and install, and patch generated libtool (plus Linux hwloc paths). They mutate their source/build tree, so inspect them and preserve unrelated work before execution. `build_all_linux.sh`/`build_all_mac.sh` rebuild sibling SST/toolchain trees too; avoid using the full-stack scripts as an inspection command or casually against existing working checkouts.

Important simulator choices in the inspected scripts:

| Setting | Purpose |
|---|---|
| `CC=hgcc`, `CXX=hg++` and PIC | Rewrite MPI-library code for Mercury and package it for application linkage |
| Mercury pthread/system replacement headers | Adapt selected thread/runtime calls to simulated execution |
| `--with-device=ch3:nemesis:ofi` | Use the inspected OFI transport path |
| `--with-ofi=<SST prefix>` | Bind the selected Iris libfabric installation |
| `--with-pmi=sst --with-pmi-sst=<prefix> --with-pm=no` | Use simulated PMI rather than launching ordinary host application processes |
| Static MPI archive; Fortran/ROMIO disabled | Match the inspected integration's link surface |

The scripts also supply `--host=x86_64-pc-none` and cached configure answers for sizes and weak symbols; available-function answers (`ac_cv_func_mmap`, `shm*`, `signal`, `rand`, `pthread_*`) are supplied only by the Linux scripts. Both pass `--disable-mpi` to hgcc, which suppresses injection of the Mask-MPI `mpi/` replacement headers; omitting it would layer the modeled `mpi.h` ahead of MVAPICH2's own. These are simulation/configure adaptations in this fork, not generic architecture detection. Review their ABI/probe assumptions for the actual host/toolchain; do not transplant them unchanged into an unrelated MPI release.

## 2. Prepare the archive expected by HGCC

The single MV2 build scripts install `libmpi.a`; the inspected full-stack scripts additionally produce `libmpi_nopmi.a`. HGCC's MV2 linker requires the latter. If using the single-script path, reproduce the explicit post-install preparation on a copy:

```bash
set -e
MV2_LIB="$SST_INSTALL/mvapich2/lib"
test -f "$MV2_LIB/libmpi.a"
cp "$MV2_LIB/libmpi.a" "$MV2_LIB/libmpi_nopmi.a"
while IFS= read -r member; do
  test -n "$member" || continue
  ar -d "$MV2_LIB/libmpi_nopmi.a" "$member"
done < <(ar t "$MV2_LIB/libmpi_nopmi.a" | rg -i simple_pmi || true)
ranlib "$MV2_LIB/libmpi_nopmi.a"
if ar t "$MV2_LIB/libmpi_nopmi.a" | rg -i simple_pmi; then
  echo "Embedded simple PMI members remain" >&2
  exit 1
fi
```

This removes embedded simple-PMI archive members so the intended Iris PMI implementation can supply the simulated process interface. Keep the original archive. A build configured with `--with-pmi=sst` compiles no such members (the executed build's 611-member archive had none), so the copy is byte-identical and the loop is a no-op; the `PMI_*` symbols are simply undefined and bind to `libpmi` at link time. Verify actual symbols and selected libraries, since object naming can vary across MPI revisions.

## 3. Build and run a small application

```bash
hgcc --mpi=mvapich2 --mpi-prefix="$SST_INSTALL/mvapich2" \
  --app-name=test_mv2_allreduce -std=gnu11 -fPIC \
  "$HGCC_SOURCE/tests/mv2/test_mv2_allreduce.c" \
  -o libtest_mv2_allreduce.so
```

The linker supplies registration support, MPI wrappers/platform stubs, whole-archive/force-load treatment of the prepared archive, and Iris PMI/libfabric. Linux and macOS use different link mechanics; use the matching wrapper implementation instead of copying flags from the other platform. Check unresolved libraries with the host's loader-inspection tool.

The inspected test directory contains matching `run_test_mv2_*.sh` scripts that compile the workload, establish prefix/library paths, and execute the corresponding SST Python driver:

```bash
export SST_HG_MV2_PREFIX="$SST_INSTALL/mvapich2"
bash "$HGCC_SOURCE/tests/mv2/run_test_mv2_allreduce.sh" "$SST_INSTALL"
```

That runner selects `FI_PROVIDER=sstmac` and exports `SST_LIB_PATH`, `LD_LIBRARY_PATH`, `DYLD_LIBRARY_PATH`, and `PYTHONPATH` unconditionally so SST can resolve the application and transport libraries. The runner passes no `--mpi-prefix`, so hgcc resolves `SST_HG_MV2_PREFIX` and otherwise `<hgcc prefix>/mvapich2`; exporting it explicitly replaces any value already in the environment. The runner's own preflight checks only `$PREFIX/mvapich2/lib/libmpi.a`, not `libmpi_nopmi.a`, so a missing prepared archive surfaces later from the hgcc linker. The runner compiles in its source test directory; use a writable isolated HGCC checkout. App registration name, library name, virtual-rank allocation, and dependencies must match the driver. Inspect installed `fi_getinfo`/provider behavior or the actual application initialization; exporting FI_PROVIDER alone does not prove the selected provider loaded.

`collective-run-all.sh` runs the nine collective cases; it takes operation names as arguments and reads the prefix from `SST_HG_PREFIX`, so passing the prefix as an argument makes it skip a nonexistent test. Before running anything, check `nm -u lib<app>.so | grep ' _MPI_'`: the wrapper table in `support/mv2/mv2_mpi_wrappers.c` covers 28 calls, and any `MPI_*` entry point outside it binds at run time to the host Open MPI linked into `sst` and crashes on MVAPICH2's handle constants. MVAPICH2 tuning variables such as `MV2_USE_SHMEM_COLL` reach the rewritten library only through Mercury's per-application environment, which the stock `HgOS` Python class does not accept; the application guide shows the driver-side forwarding hook.

## 4. Acceptance and troubleshooting

- Verify eight virtual application ranks and SUM=36 on every rank for the supplied Allreduce case, then natural completion. Check the application's `PASS: test_mv2_allreduce (8 ranks, SUM=36)` marker; the runner's separate `PASS: run_test_mv2_allreduce completed.` only establishes a successful shell command.
- Add send/receive, repeated collectives, and message-size variations. Preserve application computation needed by each numerical oracle.
- Test rank/TLS state isolation, blocking/wakeup, and request/progress behavior before interpreting timings.
- Diagnose missing `libmpi_nopmi.a`, application registration, wrong PMI/libfabric, missing `macro:libfabric`, and wrong provider separately. The [Iris fabric guide](../elements/iris/fabrics.md) explains those layers.
- A run that ends at `18.4467 Ms` with the shell-level PASS has stalled: that is 2^64 ps, the time of a drained event queue after every rank blocked, and the unpatched Iris provider produces exactly this on the first receive.
- Do not infer application MPI rank count from host `mpirun -n`. Host MPI partitions SST; the Mercury job configuration supplies virtual application ranks.

The October 7, 2026 run used sst-core `09bc3927`, sst-elements `47b99537` with the provider patch, HGCC `2a37f8c5` with the wrapper additions, mv2-test `0bd13efd`, Homebrew LLVM 22.1.4, and the `sstmac` provider; record the same identities for any other run.

## Platform support and timer selection

The integration provides separate [Linux/macOS paths](../elements/mercury/mv2-platforms.md), with different ELF/Mach-O linking and runtime adaptations. Review [timing behavior](../elements/mercury/mv2-timing.md) before choosing the MPI timer backend or claiming simulated MPI_Wtime. The library must be rebuilt with the relevant replacement/binding; application-only rebuilding is insufficient.
