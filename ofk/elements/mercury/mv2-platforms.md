---
{
  "type": "SST Runtime Guide",
  "title": "MV2 on Linux and macOS",
  "description": "Describe the inspected platform-specific build, linkage, runtime workarounds, and validation boundaries.",
  "tags": [
    "mv2",
    "linux",
    "macos",
    "mercury"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T18:59:42.661532+00:00"
  },
  "sources": [
    {
      "resource": "https://github.com/nab880/mv2-test/blob/0bd13efd074affc7c8e3cca5add42af699362748/build_linux.sh",
      "x-commit": "0bd13efd074affc7c8e3cca5add42af699362748",
      "x-sha256": "dc864c71a1d47af1926daa84ba215b4936be3cb590f18aeb14ed129f0e79fdb5",
      "x-review-scope": "External checkout inspected locally; automatic freshness checking unavailable",
      "id": "s0"
    },
    {
      "resource": "https://github.com/nab880/mv2-test/blob/0bd13efd074affc7c8e3cca5add42af699362748/build_mac.sh",
      "x-commit": "0bd13efd074affc7c8e3cca5add42af699362748",
      "x-sha256": "c7960921198f7bccf9a6a8c6ddd00c1039f5240abd7e067d5a79ee26e44fbc6a",
      "x-review-scope": "External checkout inspected locally; automatic freshness checking unavailable",
      "id": "s1"
    },
    {
      "resource": "https://github.com/jmlapre/sst-hgcc/blob/41cd313574c994f6fefe2c361124e854b7e4ac0f/hglink.py",
      "x-commit": "41cd313574c994f6fefe2c361124e854b7e4ac0f",
      "x-sha256": "d1bc8eea70077debc697fa0db9eccc766fa39158e9a4cbfb704f9baccfab33d5",
      "x-review-scope": "External checkout inspected locally; automatic freshness checking unavailable",
      "id": "s2"
    },
    {
      "resource": "https://github.com/jmlapre/sst-hgcc/blob/41cd313574c994f6fefe2c361124e854b7e4ac0f/support/mv2/mv2_ld_glibc_stub.c",
      "x-commit": "41cd313574c994f6fefe2c361124e854b7e4ac0f",
      "x-sha256": "697067e28b45aaba0b4d13001f543e02cc249f162d2d5c39b5730ca861e01655",
      "x-review-scope": "External checkout inspected locally; automatic freshness checking unavailable",
      "id": "s3"
    },
    {
      "resource": "https://github.com/jmlapre/sst-hgcc/blob/41cd313574c994f6fefe2c361124e854b7e4ac0f/support/mv2/mv2_mpi_wrappers.c",
      "x-commit": "41cd313574c994f6fefe2c361124e854b7e4ac0f",
      "x-sha256": "e80c96e0c40d0a26d2b0368917ccf55bd9900a62e661cda03dea4fb8e3179ab9",
      "x-review-scope": "External checkout inspected locally; automatic freshness checking unavailable",
      "id": "s4"
    },
    {
      "resource": "https://github.com/jmlapre/sst-hgcc/blob/41cd313574c994f6fefe2c361124e854b7e4ac0f/tests/mv2/_mv2_run_common.sh",
      "x-commit": "41cd313574c994f6fefe2c361124e854b7e4ac0f",
      "x-sha256": "31654eb79aaa0a9495c5e3292fc09f24e81856c310adb0ddd101957c90b33ddb",
      "x-review-scope": "External checkout inspected locally; automatic freshness checking unavailable",
      "id": "s5"
    },
    {
      "resource": "https://github.com/jmlapre/sst-hgcc/blob/41cd313574c994f6fefe2c361124e854b7e4ac0f/tests/mv2/run_test_mv2_allreduce.py",
      "x-commit": "41cd313574c994f6fefe2c361124e854b7e4ac0f",
      "x-sha256": "5e311583388cf91186e7f04793b1436a8bb3cd43a1f2cd6db68a6531628ff75b",
      "x-review-scope": "External checkout inspected locally; automatic freshness checking unavailable",
      "id": "s6"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-hgcc/blob/2a37f8c541f02344f7d540188e52efd1f080a6fc/support/mv2/mv2_mpi_wrappers.c",
      "x-commit": "2a37f8c541f02344f7d540188e52efd1f080a6fc",
      "x-sha256": "e80c96e0c40d0a26d2b0368917ccf55bd9900a62e661cda03dea4fb8e3179ab9",
      "x-review-scope": "External source inspected locally; freshness review is manual"
    }
  ]
}
---

# MV2 on Linux and macOS

## Support status

The inspected MV2/HGCC integration has separate Linux and macOS build/link/run paths. That establishes source-level integration support, not successful end-to-end validation on every host. The prior repository campaign built SST core/elements on macOS and ran Mercury/Mask-MPI cases; it did not build or run MV2 on either platform. The October 7, 2026 run built and executed the macOS path end to end on ARM64 ([application guide](hgcc-mv2.md)); the Linux path remains unexecuted here.

| Area | Linux path | macOS path |
|---|---|---|
| Adapted MV2 build | `mv2-test/build_linux.sh` | `mv2-test/build_mac.sh` |
| Application artifact | ELF shared library (`-shared`) | Mach-O bundle (`-bundle -undefined dynamic_lookup`), often named `.so` by the integration |
| Prepared MPI archive | `libmpi_nopmi.a` with whole-archive/no-whole-archive linking | Same prepared archive with `-force_load` |
| MPI/runtime symbol handling | `-Bsymbolic-functions`, explicit `libhg`, runtime rpaths, conditional glibc offset-symbol stub, plus the shared `mv2_mpi_wrappers.o` (MPI-to-PMPI wrappers and `hgcc_*` stubs) | The same wrapper object with dynamic lookup; matching rpaths and bundle dependencies |
| Runtime-library inspection | `ldd`, `readelf`, `nm` | `otool -L`, `nm`; do not infer ELF from the `.so` suffix |
| Search paths in supplied runner | The runner exports `LD_LIBRARY_PATH`, `DYLD_LIBRARY_PATH`, `SST_LIB_PATH`, and `PYTHONPATH` unconditionally; only `LD_LIBRARY_PATH` includes the Mercury library directory | Same unconditional exports; `DYLD_LIBRARY_PATH` covers the prefix, Iris ext directory, and test directory |
| Additional source adaptations | Cached configure answers, libtool Linux-case patch, hwloc CRT-symbol path workaround | Cached configure answers and libtool Darwin-case patch; verify SDK/linker |
| Optional registration-load workaround | Driver can preload Mercury/dependencies/app with `SST_HG_MV2_PRELOAD=1` | Driver returns before that Linux-only preload path |
| Runner layout workaround | Uses `setarch -R` whenever the command exists unless `SST_HG_MV2_NO_SETARCH=1` | Same single code path; it falls through only because `setarch` is absent |

Both paths require a compatible HGCC rewriter/toolchain, SST Mercury/Iris, simulated PMI, and the `sstmac` provider. Build/runtime dependencies must come from the intended prefix. Host MPI used by SST itself is a separate dependency from the adapted MV2 archive linked into the virtual application.

## Linux details

The linker retains the prepared MV2 archive and binds application-local functions with `-Bsymbolic-functions`, while supplying Iris `libpmi`/`libfabric` and Mercury `libhg`. This helps keep embedded MPI implementation symbols separate from a host MPI library already used by the simulator. Verify actual exported/bound symbols rather than relying only on link-command intent.

The conditional Linux/glibc support source supplies `__offset_program_invocation_name`. The build script also disables selected hwloc CRT program-name paths. These are compatibility adaptations, not models of process-launch cost or communication timing.

The supplied runner documents layout sensitivity and can use `setarch "$(uname -m)" -R` for that process. Environments that disallow it can use `SST_HG_MV2_NO_SETARCH=1`; record the changed launch condition and test startup/rank-state behavior. Do not turn a per-run workaround into a global host setting. `SST_HG_MV2_PRELOAD=1` is another optional, Linux-only registration workaround; normal library registration/loading should be checked first.

The runner's memory/preflight thresholds protect the host allocation; they are not simulated memory capacity or modeled MPI delays. Keep those controls separate from platform timing parameters.

## macOS details

The application remains a Mach-O bundle even if its filename ends in `.so`. HGCC force-loads the prepared static MV2 archive, links the MPI-to-PMPI wrappers for the calls listed in `support/mv2/mv2_mpi_wrappers.c` (compiled with `HGCC_NO_REPLACEMENTS` against the MPI include directory, and linked on Linux as well), and resolves some runtime symbols dynamically. The wrapper list is finite (for example, it omits MPI_Wtime); check each required application entry point and its binding. On the recorded install this was not theoretical: `sst` links the host Open MPI, an unwrapped `MPI_Irecv` resolved there at first call and dereferenced an MVAPICH2 datatype handle (`0x4c00011d`), and `MPI_Comm_set_errhandler` did the same with `MPI_COMM_WORLD` (`0x440000f8`). Run `nm -u lib<app>.so | grep ' _MPI_'` on every built bundle and add wrappers until the list is empty. Use `otool -L` and symbol inspection on the produced bundle and intended dependencies.

Use mutually compatible compiler, LLVM/libTooling, C++ runtime, SDK, and linker settings. A source recipe's `--host=x86_64-pc-none` and cached configure sizes are simulator/probe adaptations; they do not establish native x86_64-only execution or automatic Apple Silicon validation. The October 7, 2026 ARM64 macOS run passed the shipped send/receive and all nine collective cases, so the rewriter and archive path work on Apple Silicon once the Iris provider patch and wrapper additions recorded in the application guide are in place.

The inspected Python preload helper deliberately does nothing on Darwin. Keep Linux preload/ELF flags out of the macOS path, and inspect actual loader behavior rather than assuming Linux search-path or symbol-binding rules apply.

## Check before comparing platforms

```bash
uname -s
uname -m
hgcc --help
hg++ --flags
# Set APP_LIBRARY to the built application artifact.
# Linux:
ldd "$APP_LIBRARY"
readelf -Ws "$APP_LIBRARY" | rg 'MPI_|PMPI_|hgcc_|sst_hg_user_main'
# macOS, as alternatives to the Linux inspection commands:
otool -L "$APP_LIBRARY"
nm -g "$APP_LIBRARY" | rg 'MPI_|PMPI_|hgcc_|sst_hg_user_main'
```

Run only the inspection commands appropriate to the host. Record revisions, flags, library/provider identities and virtual-rank placement. Verify numerical results, per-rank globals/TLS, blocking/progress and natural completion before comparing modeled latency. Then follow [the timing guide](mv2-timing.md) to establish that clock reads and costs actually use simulated state.

Installation procedures are in [HGCC installation](../../development/hgcc-install.md) and [adapted MV2 installation](../../development/mv2-install.md). These platform notes do not claim additional executed tests.
