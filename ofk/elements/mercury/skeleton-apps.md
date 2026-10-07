---
{
  "type": "SST Guide",
  "title": "Write and run a Mercury skeleton application",
  "description": "Build a Mercury skeleton in tree or with SST-HGCC, drive it from Python, and validate it.",
  "tags": [
    "mercury",
    "application",
    "hgcc"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/claude",
    "at": "2026-10-07T16:50:05.408378+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/common/skeleton.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/common/skeleton.h",
      "x-sha256": "669f5cd6fc371637708596709b020d16b901cbe88f55cc3b9b4b336c66ce9fed",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/common/hgcc_wrappers.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/common/hgcc_wrappers.cc",
      "x-sha256": "b83ed65c0a98e226c0954e8e5851ae883ea4ea7a57c70e96a79b2b778c67a15c",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/common/util.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/common/util.cc",
      "x-sha256": "5cb52fef8bfa2a28442e8ca2b881e1441ae45b52c33b072f0a17dace6264a0fb",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/tests/ostest.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/tests/ostest.cc",
      "x-sha256": "6d5d3b695706d5d4a7d649cb765353a31241ec7ace2fbb68cbc72206f5d3a4ad",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/tests/ostest-nano.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/tests/ostest-nano.cc",
      "x-sha256": "7d080a03d09da070ce713a7f5797f7336eb5945c11f11cef43f85c94a5544ab4",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/tests/ostest.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/tests/ostest.py",
      "x-sha256": "2bde9630e877cd43b625b2e8b8aa4c6833437e741430aa490e00fafa96cf98f8",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/tests/refFiles/ostest.out",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/tests/refFiles/ostest.out",
      "x-sha256": "088a4f05d0f972260a25b96738cc936d6214e8e390a2b4bf4d0b8d907df1cefd",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/tests/testsuite_default_hg.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/tests/testsuite_default_hg.py",
      "x-sha256": "2a20990c96f2da713333b4b30fdea279ae2561e134d75cb0ba47260e853d35a7",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/Makefile.am",
      "x-sha256": "76ac810ac435e0b2232aa8b78005c23ad678e9b5d2c5e0a397a937c621b26aaa",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/operating_system/process/app.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/operating_system/process/app.cc",
      "x-sha256": "0f7b51e1ec5cd87d2ebd7abc58494ee55935e4c31aa20b9727abbc9fe77d41e0",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/operating_system/launch/app_launcher.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/operating_system/launch/app_launcher.cc",
      "x-sha256": "807ae0d230a796c3e7cae36f61c8a4dd6bc5532b2439fa9c40a9b21123c3a593",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s11",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/operating_system_call_forward.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/operating_system_call_forward.h",
      "x-sha256": "335669b2049427a52e309199ed273a1ae08d66846a0609c92ab0b09e064cfaeb",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s12",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/operating_system_api.h",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/operating_system_api.h",
      "x-sha256": "099f623599e41512f19b25be00b5538977d1aa05b5ce4fb9db493853e55419da",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s13",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/pymercury.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/pymercury.py",
      "x-sha256": "28b879fca429a047cfac23554d31aef4c02b6f1271831d8cb06b14c54e24e718",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s14",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/tests/sendrecv.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/tests/sendrecv.cc",
      "x-sha256": "f47b95c97edcf0f17a098369f645673829a5517a5c6d986df4edcdd87c6d85fa",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s15",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/tests/test_sendrecv.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/tests/test_sendrecv.py",
      "x-sha256": "6bf30c326aa0adf6477492ba41a3a40b353d6e27bfba2aab852d95a0ac898c5f",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s16",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/tests/platform_file_mask_mpi_test.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/tests/platform_file_mask_mpi_test.py",
      "x-sha256": "5247517a82863c2694bf1aa23dc6859a0f89aaf599123cd4d5493e37086895d2",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s17",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/Makefile.am",
      "x-sha256": "44ee4746144aacd370a551efb702f49ca3ee08787075cf1227a13f5054277a39",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s18",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/factory.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/factory.h",
      "x-sha256": "0362df40bff8c0e0d892c89a54940a6666bf2a43bf7abd93a2baef4171d8192b",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s19",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/configShared.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/configShared.cc",
      "x-sha256": "3b32a8efe56cd62003dfcaca0b4b47ec521f9f931e868dbd5e871ce434f23bd7",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-hgcc/blob/2a37f8c541f02344f7d540188e52efd1f080a6fc/README.md",
      "x-commit": "2a37f8c541f02344f7d540188e52efd1f080a6fc",
      "x-sha256": "2e282cc0a70f797c92bcdb311be0d42ae1a8d87559efb630bcf9c3ab0f5c390f",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s20"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-hgcc/blob/2a37f8c541f02344f7d540188e52efd1f080a6fc/examples/mercury_hello/hello.py",
      "x-commit": "2a37f8c541f02344f7d540188e52efd1f080a6fc",
      "x-sha256": "1a67fa9bd87d97f62af36ca67becc39b13f0b5dcbd79b0e156005b294cd75ecd",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s21"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-hgcc/blob/2a37f8c541f02344f7d540188e52efd1f080a6fc/examples/mercury_hello/hello.cc",
      "x-commit": "2a37f8c541f02344f7d540188e52efd1f080a6fc",
      "x-sha256": "3a7fb2184185af381111fc8a7b2f7e1c39509edf47cdd10d7f7e4bc29fb2c459",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s22"
    },
    {
      "id": "s23",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/skeletons/halo3d-26.cc",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/skeletons/halo3d-26.cc",
      "x-sha256": "24db48a19829aca7280b5d9c267a6908fa608a0d70fb95ebfd5f60f2fb90d445",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s24",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/tests/test_halo3d26.py",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/tests/test_halo3d26.py",
      "x-sha256": "84d80bf34d6f9662ac4e773e7e54f4f5cfe52928de5765402be7e29169820788",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s25",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mask-mpi/tests/refFiles/test_halo3d26.out",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mask-mpi/tests/refFiles/test_halo3d26.out",
      "x-sha256": "882a859b35dfcc6214120b07717c60a8e0caa3a0890129d35f3f5957ac2b6f5a",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---
# Write and run a Mercury skeleton application

A Mercury skeleton is ordinary C or C++ with a `main`, built into a shared library that Mercury loads and runs once per simulated rank. The application sees simulated time through `ssthg_*` calls and, for MPI programs, the Mask-MPI API. Two build routes exist: the in-tree route compiles the source with the elements build and installs it beside the other `ext` libraries, and the SST-HGCC route compiles it out of tree with `hg++`, rewriting `main` and optionally skeletonizing compute.

## Source conventions

```cpp
#define ssthg_app_name hello          // becomes the registered app name
#include <mercury/common/skeleton.h>  // <skeleton.h> under hg++
#include <iostream>
using namespace SST::Hg;

int main(int argc, char** argv) {
  for (int i = 0; i < argc; i++) std::cout << argv[i] << "\n";
  std::cout << "Hello from Mercury!\n";
  ssthg_sleep(5);                     // advances simulated time, blocks this rank
  return 0;
}
```

`ssthg_app_name` must be defined before the `main` (or explicit `USER_MAIN`) definition, where the macro expands; `ostest.cc` defines it before the include and `mask-mpi/skeletons/halo3d-26.cc` after the includes. `skeleton.h` turns `main` into the `USER_MAIN` macro, which registers the function with `userSkeletonMainInitFxn` under `SST_APP_NAME_QUOTED` (the app name, or `__FILE__ __DATE__` when `SST_HG_EXTERNAL` is set). `tests/ostest.cc` and `tests/ostest-nano.cc` are the complete examples. The app-facing calls in `skeleton.h` are `ssthg_sleep(seconds)`, `ssthg_usleep(microseconds)`, and `ssthg_nanosleep(nanoseconds)`; the C wrappers in `common/hgcc_wrappers.cc` map `hgcc_sleep`, `hgcc_usleep`, `hgcc_getenv`, `SSTMAC_gettimeofday`, `HGCC_clock_gettime`, and `hgcc_ts_nanosleep` onto simulated time for rewritten code. `sst_hg_blocking_call` and `sst_hg_advance_time` are the hooks that HGCC pragmas emit. Everything else runs natively on the host.

For MPI, include `<mask_mpi.h>` and use the supported calls (`MPI_Init`, `MPI_Comm_rank`, `MPI_Comm_size`, point-to-point and collective calls as listed in the Mask-MPI profile); `mask-mpi/tests/sendrecv.cc`, the other `mask-mpi/tests/*.cc` files, and `mask-mpi/skeletons/halo3d-26.cc` (a 27-point stencil that writes `int USER_MAIN(int argc, char* argv[])` directly and parses `-nx`/`-pex` style arguments from `app1.argv`) are the shipped MPI skeletons.

## Route 1: in-tree ext library

Add the source to an element's `Makefile.am` as an `ext` library, exactly as Mercury and Mask-MPI do:

```make
ext_LTLIBRARIES = libhello.la
extdir = $(pkglibdir)/ext
AM_CPPFLAGS += -I$(top_srcdir)/src/sst/elements
libhello_la_SOURCES = tests/hello.cc
libhello_la_LDFLAGS = -module -avoid-version
```

Rebuild and install elements (`make install` from the elements build directory, or from the element's subdirectory; automake regenerates the Makefile from the edited `Makefile.am`). The library lands in `<prefix>/lib/sst-elements-library/ext/libhello.so`, which `sstsimulator.conf` registers as `SST_ELEMENT_LIBRARY_EXT_LIBDIR`, so it is on the normal element search path; `sst-info <name>` prints nothing and exits 1 for such a library because it registers no ELI entries, so verify by running it. This route needs no HGCC; `main` is rewritten by the `skeleton.h` macro alone, globals are shared by all ranks in the process, and no compute is skeletonized.

## Route 2: SST-HGCC

With the toolchain from [HGCC installation](../../development/hgcc-install.md):

```sh
hg++ -c hello.cc
hg++ hello.o -o libhello.so          # --app-name=hello overrides the name derived from -o
```

`hg++` always produces a shared library, rewrites `main` to `sst_hg_user_main_<mangled>` with a registration wrapper, privatizes globals and TLS per rank, and skeletonizes compute by default (`--skeletonize`; `--disable-mpi` skips the virtual MPI headers). The toolchain's `examples/mercury_hello/` holds a two-rank MPI hello with its driver. Put the resulting library on SST's library path (`--add-lib-path`, `SST_LIB_PATH`, or the `ext` directory); see [applications with HGCC and MV2](hgcc-mv2.md) for the MPI implementation choice.

## The driver

Mercury resolves `app1.name` against the registered main functions (an unknown name fails with `no user app with the name ... registered`) and loads `lib<app1.exe_library_name>.so` through the core's `requireLibrary`, so the library must be findable by the same rules as any element library. `app1.argv` is a space-separated string; `argv[0]` is the app name. `app1.env.<KEY>` sets environment entries, and `app1.stdout`/`stderr`/`cout`/`cerr` redirect output. Each `lib:Name` entry in `app1.libraries` is loaded as ELI `lib.Name` and keyed by `Name`; `app1.dependencies` lists library files to require first.

Single node, plain OS (`tests/ostest.py`):

```python
import sst, sst.hg
node0 = sst.Component("Node0", "hg.Node")
os0 = node0.setSubComponent("os_slot", "hg.OperatingSystem")
link0 = sst.Link("link0")
link0.connect((node0, "network", "1ns"), (node0, "network", "1ns"))
os0.addParams({"app1.name": "ostest", "app1.exe_library_name": "ostest", "app1.argv": "arg1 arg2"})
```

Multi-rank MPI over Merlin (`mask-mpi/tests/test_sendrecv.py` with `platform_file_mask_mpi_test.py`):

```python
PlatformDefinition.loadPlatformFile("platform_file_mask_mpi_test")   # hg.NodeCL / hg.OperatingSystemCL
PlatformDefinition.setCurrentPlatform("platform_mask_mpi_test")
platform = PlatformDefinition.getCurrentPlatform()
platform.addParamSet("operating_system", {
    "app1.name": "sendrecv", "app1.exe_library_name": "sendrecv",
    "app1.dependencies": ["sumi"],
    "app1.libraries": ["computelibrary:ComputeLibrary", "mask_mpi:MpiApi"],
})
topo = topoSingle(); topo.num_ports = 32
ep = HgJob(0, 2)            # two nodes, one rank each
system = System(); system.setTopology(topo); system.allocateNodes(ep, "linear"); system.build()
```

The platform file is loaded by module name, so run from its directory or put it on `PYTHONPATH`. `HgJob(job_id, numNodes, numCores=1)` sets the application rank count; `ncores` in the OS parameter set is compute capacity, not rank count ([extension points](extension-points.md)). Compute-modeling and MPI runs need the `hg.NodeCL`/`hg.OperatingSystemCL` pair and `computelibrary:ComputeLibrary` ([overview](overview.md)).

## Validate

`tests/refFiles/ostest.out` shows the oracle for the plain OS case: the `argv` echo (`ostest`, `arg1`, `arg2`), the program's lines, and `Simulation is complete, simulated time: 5 s`, where the 5 s comes from `ssthg_sleep(5)`. The hg suite compares a sorted diff against that file and only logs a non-empty stderr. For an MPI skeleton, print per-rank results that encode the expected values (the Mask-MPI tests do), check that every rank reported, and check that simulated time grew only through modeled calls: a native busy loop costs no simulated time. Context switching is host-architecture specific (fcontext for x86_64 and arm64 only), and OS tests skip above one rank or thread ([validation](validation.md)). Timing semantics of sleeps, clocks, and compute hooks are in [MV2 timing](mv2-timing.md).

## Executed check on the recorded devel install

The in-tree route was exercised on the isolated devel build (sst-elements `47b99537`, macOS ARM64). The shipped `mask-mpi/tests/test_halo3d26.py` first reproduced its reference output exactly (`halo3d-26 executed successfully`, `Simulation is complete, simulated time: 1.1873 ms`, eight ranks as `HgJob(0,8)` with `app1.argv` `-pex 2 -pey 2 -pez 2`). Then `skeletons/halo3d-26.cc` was copied to `skeletons/halo3d-test.cc` with `ssthg_app_name halo3dtest` and a changed success line, `libhalo3dtest.la` was added to `ext_LTLIBRARIES` with matching `_SOURCES` and `_LDFLAGS` lines in `mask-mpi/Makefile.am`, and `test_halo3d26.py` was copied with `app1.name` and `app1.exe_library_name` set to `halo3dtest`. `make -C <build>/src/sst/elements/mask-mpi install` regenerated the Makefile and built the library, but linking needed `SDKROOT` set to the SDK the install was configured with (`MacOSX26.5.sdk`); the default macOS 27 SDK fails with `tapi error: malformed file ... unknown architecture`. The new driver then printed `halo3d-test executed successfully` with the same 1.1873 ms, in about one second. The platform file loads by module name, so the driver ran from `mask-mpi/tests`. The `hg++` route was then exercised with the pinned upstream HGCC (`2a37f8c5`) built against the same devel install (configure, make, and install took about 80 seconds once `sst-config` was on `PATH` and `SDKROOT` named the install's SDK). `hg++ -c hello.cc` and `hg++ hello.o -o libmercury_hello.so` built the toolchain's two-rank example, and `sst --add-lib-path=<build dir> hello.py` printed `Hello from rank 0` and `Hello from rank 1` on stderr with 1.32435 us of simulated time. The same two commands built the Halo3D skeleton copied as `halo3dhg.cc` with `#define ssthg_app_name halo3dhg` and no `--app-name` flag; its driver, run next to a copy of the platform file, printed `halo3d-hg executed successfully` with the same 1.1873 ms as the in-tree build, so skeletonization changed nothing for this stencil's modeled time. Both compiles warned that `hg++` bumps `-std=c++11` to `-std=c++17` because libc++ requires it; configuring HGCC with `--with-std=17` silences that. The compiled library resolves `userSkeletonMainInitFxn` from `libhg` at load time, and `--add-lib-path` is all the driver needs to find a library outside the `ext` directory. Evidence is under the repository's ignored `.runtime/guide-exercise-2026-10-07/` directory.
