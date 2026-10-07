---
{
  "type": "SST Installation Guide",
  "title": "Install SST-HGCC for Mercury applications",
  "description": "Build a compatible HGCC toolchain against SST and LLVM development tooling, then verify application execution.",
  "tags": [
    "installation",
    "hgcc",
    "mercury"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/codex",
    "at": "2026-10-07T16:50:06.429408+00:00"
  },
  "sources": [
    {
      "resource": "https://github.com/sstsimulator/sst-hgcc/blob/2a37f8c541f02344f7d540188e52efd1f080a6fc/INSTALL.md",
      "x-commit": "2a37f8c541f02344f7d540188e52efd1f080a6fc",
      "x-sha256": "833bca35d363215f63aa762e9a3675e07a0a99df806f46d5bbd3c9de6944d49a",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s0"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-hgcc/blob/2a37f8c541f02344f7d540188e52efd1f080a6fc/README.md",
      "x-commit": "2a37f8c541f02344f7d540188e52efd1f080a6fc",
      "x-sha256": "2e282cc0a70f797c92bcdb311be0d42ae1a8d87559efb630bcf9c3ab0f5c390f",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s1"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-hgcc/blob/2a37f8c541f02344f7d540188e52efd1f080a6fc/acinclude/check_clang.m4",
      "x-commit": "2a37f8c541f02344f7d540188e52efd1f080a6fc",
      "x-sha256": "993ad1e6c2a0f8f7a417bec3dfb8679e72a91d3c36d5cbd052f5134590110d90",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s2"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/configure.ac",
      "x-repository": "sst-core",
      "x-path": "configure.ac",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a",
      "x-sha256": "ec37eb689d7899b5c79ff9731534896afe9fb38781365683911432add5aed676",
      "id": "s3"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/configure.ac",
      "x-repository": "sst-elements",
      "x-path": "configure.ac",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "55cad6ffe9b18511024733e784e9144d104ae197d6cbe180d7085bee381588bb",
      "id": "s4"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/select_build.py",
      "x-repository": "sst-elements",
      "x-path": "select_build.py",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "60004a71ba14e6333b2d59c1036304ae570908c2a9758ca0b6dbe03d8a68b590"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/compute_library/node_cl.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "35b4e39ba9e5ebdb6c8a80f19efa880c433e1407fa0a74e029fb7c8e41e48f74",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/compute_library/node_cl.h"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/mercury/components/compute_library/operating_system_cl.h",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5",
      "x-sha256": "f01ef1d6bfbfa7d78ceb4031a5b6bfc34795904ac175f50db114e3acc854f734",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/mercury/components/compute_library/operating_system_cl.h"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-hgcc/blob/2a37f8c541f02344f7d540188e52efd1f080a6fc/hgcclib.py",
      "x-commit": "2a37f8c541f02344f7d540188e52efd1f080a6fc",
      "x-sha256": "75ac9fdbf4934a494e32cacc732425c90310db1a5dbec5e3e007ba565a65a471",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s8"
    },
    {
      "resource": "https://github.com/sstsimulator/sst-hgcc/blob/2a37f8c541f02344f7d540188e52efd1f080a6fc/tests/Makefile.am",
      "x-commit": "2a37f8c541f02344f7d540188e52efd1f080a6fc",
      "x-sha256": "c708ec081ec71d90f65c4a867772fb3e4352afd99174f6aa805e811ed61a8a0b",
      "x-review-scope": "External source inspected locally; freshness review is manual",
      "id": "s9"
    }
  ]
}
---

# Install SST-HGCC for Mercury applications

## Installation scope

This is a source-derived recipe, not an installation performed by this documentation change. Use a fresh checkout/build directory and an explicit prefix. The previous runtime prefix contains SST core/elements, not a validated HGCC/MV2 toolchain.

Choose HGCC source before building. Both inspected checkouts, upstream `sstsimulator/sst-hgcc` at `2a37f8c5` and the older `jmlapre/sst-hgcc` at `41cd3135`, carry the same MV2 wrapper, linker, support, and fixture files (`hglink.py` and `support/mv2/*` are byte-identical); the upstream README simply does not document `--mpi=mvapich2`, and the older revision ships no README. A compiler wrapper called hgcc does not by itself establish MV2 support; confirm installed help. See [the application path guide](../elements/mercury/hgcc-mv2.md).

## Prerequisites

- Python, Autotools, a working C/C++17 compiler/linker, and the SST core prerequisites.
- Compatible SST core and elements installations with Mercury, Iris, and the network elements needed by the workload.
- LLVM/Clang **development tooling**, including libTooling headers/libraries for `ssthg_clang`. An Apple/system clang executable alone is insufficient. The upstream INSTALL.md (`2a37f8c5`) uses LLVM 22, while the older `41cd3135` INSTALL.md prescribes 18.1.8; confirm compatibility with the selected HGCC revision and installed `llvm-config` rather than assuming an arbitrary LLVM version works.
- Optional lit/FileCheck tooling for rewriter tests. Check skipped checks explicitly if it is absent.

Set paths to selected source and installed development tooling. The commands below do not install system packages:

```bash
set -e
SST_WORKSPACE="/path/to/workspace"
SST_INSTALL="$SST_WORKSPACE/install-hgcc"
HGCC_SOURCE="/path/to/selected/sst-hgcc"
LLVM_INSTALL="/path/to/llvm-with-libTooling"
BUILD_JOBS=4
export PATH="$LLVM_INSTALL/bin:$SST_INSTALL/bin:$PATH"
"$LLVM_INSTALL/bin/llvm-config" --version
"$LLVM_INSTALL/bin/clang++" --version
```

## 1. Build or verify SST core/elements

Skip rebuilding when an existing compatible installation is intentionally selected. Otherwise, from source checkouts containing the intended revisions:

```bash
(cd "$SST_WORKSPACE/sst-core" && ./autogen.sh)
mkdir -p "$SST_WORKSPACE/build-hgcc/core"
(
  cd "$SST_WORKSPACE/build-hgcc/core"
  "$SST_WORKSPACE/sst-core/configure" \
    --prefix="$SST_INSTALL" CC=clang CXX=clang++
  make -j"$BUILD_JOBS"
  make install
)

(cd "$SST_WORKSPACE/sst-elements" && python3 select_build.py network-ext)
mkdir -p "$SST_WORKSPACE/build-hgcc/elements"
(
  cd "$SST_WORKSPACE/build-hgcc/elements"
  "$SST_WORKSPACE/sst-elements/configure" \
    --prefix="$SST_INSTALL" --with-sst-core="$SST_INSTALL" \
    CC=clang CXX=clang++
  make -j"$BUILD_JOBS"
  make install
)
```

The `network-ext` selection uses the checkout's dependency map to enable the communication/Mercury stack and regenerate Autotools inputs, while disabling unrelated elements. It mutates selection files: use an isolated checkout and add other requested model elements to the selection if needed. This avoids treating CUDA/RTL-dependent elements as prerequisites for an HGCC application toolchain.

Use the current configure help for supported options; core already selects C++17, so do not blindly copy HGCC's `--with-std` option into core configure. The [SST build guide](build.md) covers element selection and installation identity. For a smaller build select the required libraries in an isolated source copy before autogen; `select_build.py` modifies source/build selection and is not an inspection command. Optional GPU/RTL elements may need separate external artifacts.

Verify `sst`, `sst-config`, Mercury's `hg.NodeCL` / `hg.OperatingSystemCL` registrations, and Iris libraries under the selected prefix. These compute-capable node/OS types are the pair used by the HGCC application examples. For the common combined-prefix MV2 layout, both `libfabric` and `libpmi` should exist in `$SST_INSTALL/lib/sst-elements-library/ext`. Inspect that directory and `sst-info -l hg`; OS runtime tests alone do not establish application rewriting or MV2 support.

## 2. Build SST-HGCC

```bash
(cd "$HGCC_SOURCE" && ./autogen.sh)
mkdir -p "$SST_WORKSPACE/build-hgcc/toolchain"
(
  cd "$SST_WORKSPACE/build-hgcc/toolchain"
  "$HGCC_SOURCE/configure" \
    --prefix="$SST_INSTALL" --with-std=17 \
    --with-sst-core="$SST_INSTALL" --with-sst-elements="$SST_INSTALL" \
    --with-clang="$LLVM_INSTALL" CC=clang CXX=clang++
  make -j"$BUILD_JOBS"
  make install
)
```

The Clang prefix must provide the headers and libraries configure probes, not only a compiler binary. Keep host compiler/LLVM library ABI and the SST linkage consistent. On the recorded devel install, HGCC's configure stopped with `sst-config not found` until the SST prefix's `bin` was on `PATH`; `--with-sst-core` alone does not satisfy that probe, and on macOS `SDKROOT` must name the SDK the SST install was built with. With those set, the upstream `2a37f8c5` checkout configured, built, and installed against that install in about 80 seconds into a separate prefix, and `hg++ --flags` then pointed at the devel include and library directories. Built without `--with-std=17`, every `hg++` compile warns that it bumps `-std=c++11` to `-std=c++17`; the recipe above passes the option for that reason. The resulting toolchain compiled and ran the `mercury_hello` example and a Halo3D Mask-MPI skeleton ([skeleton applications](../elements/mercury/skeleton-apps.md)).

On macOS inspect the selected SDK/linker before configure. This repository's SST runtime validation used the existing macOS 26.5 SDK because its default macOS 27 SDK failed a linker probe. That is host-specific evidence, not a portable SDK requirement. HGCC supports a `--with-sdk` option in the inspected source; use a verified SDK path and supported linker flags for your installation. Do not assume `xcrun`'s default is automatically usable or that every compiler accepts the same lld option.

## 3. Verify compilation and Mercury execution

```bash
hgcc --help
hg++ --version
hg++ --flags
(
  cd "$SST_WORKSPACE/build-hgcc/toolchain"
  make check
  make installcheck
)
```

Inspect whether lit/FileCheck and SST integration tests actually ran: both check targets silently skip when `lit` or `sst` is missing unless configured with `--enable-strict-tests`, and `make installcheck` also runs the `run-examples` target. The documented `test_tls` integration should establish per-rank global/TLS isolation, not merely library loading. Build a small Mercury application from the same checkout and verify registered application/library names, virtual rank count, expected output, and natural completion.

The inspected generic README documents `make examples`, `make install-examples`, and `make run-examples` as separate optional targets; examples are not automatically built by normal `make install`. Keep numerical/control-flow computation needed by your correctness oracle when selecting rewriting/skeletonization settings.

## Next: MV2 or modeled MPI

Use [MV2 installation](mv2-install.md) for an adapted MVAPICH2 stack. For ordinary modeled MPI applications, use the compatible Mask-MPI path and [Mercury application guide](../elements/mercury/hgcc-mv2.md). Keep application MPI ranks separate from host MPI ranks used to distribute SST.
