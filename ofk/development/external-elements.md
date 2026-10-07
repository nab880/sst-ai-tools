---
{
  "type": "SST Guide",
  "title": "Build an out-of-tree element library",
  "description": "Compile, register, discover, and test an element library outside sst-elements.",
  "tags": [
    "build",
    "extension"
  ],
  "status": "draft",
  "generated": {
    "by": "sst-ai-tools/claude",
    "at": "2026-10-07T09:15:59.541737+00:00"
  },
  "sources": [
    {
      "id": "s0",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/elemLoader.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/elemLoader.cc",
      "x-sha256": "4798f5407343151204cd2d1d9e15bdd3081c4a46beaa04990d0fd9dc665ec5f1",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s1",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/configShared.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/configShared.cc",
      "x-sha256": "3b32a8efe56cd62003dfcaca0b4b47ec521f9f931e868dbd5e871ce434f23bd7",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s2",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/sstregistertool.cc",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/sstregistertool.cc",
      "x-sha256": "73a750763382a021dca741ff29433eca250648efb2663f8405f10cff3c338600",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s3",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/component.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/component.h",
      "x-sha256": "a19f764dda8bc2f128b21c6752a17d30cf7dcde7c4c00fbfdb38f872e87142d2",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s4",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/subcomponent.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/subcomponent.h",
      "x-sha256": "de0a2098e0db3bc1c8b21b89ef07bff6a373c9d697a04550208c8f937c1099f4",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s5",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/module.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/module.h",
      "x-sha256": "6b1df33dc0e672589f42869d17396bfd0b36df6a9a9bb0b3d443c991f364486a",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s6",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/eli/elibase.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/eli/elibase.h",
      "x-sha256": "84581584206f1d8760cfe4d3e933ce742c375a23429b571de88dbbb5d5606936",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s7",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/eli/defaultInfo.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/eli/defaultInfo.h",
      "x-sha256": "9df2f6fb292eddd3ef1ab375468a559bf5a4fb2e84974b38269673349adf0377",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s8",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/eli/paramsInfo.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/eli/paramsInfo.h",
      "x-sha256": "7686f04c1b4d87b9d5bd87cef1c69be4fdce349fd5663128f946b0207a93f4ab",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s9",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/eli/portsInfo.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/eli/portsInfo.h",
      "x-sha256": "f33fb17e38102ec2a3c60f457346c65794dfd98dcd731179722c64e1bad87eb4",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s10",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/eli/statsInfo.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/eli/statsInfo.h",
      "x-sha256": "d57a838e1eda6b8a22471ca371ddf02626f5250ec59637da6f47fe540340cd6d",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s11",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/eli/subcompSlotInfo.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/eli/subcompSlotInfo.h",
      "x-sha256": "1995903f375a24fe0944974f45973641a97102bb797b1a8638e71bc2005bee5b",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s12",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/eli/attributeInfo.h",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/eli/attributeInfo.h",
      "x-sha256": "444f28d24b525dcfb8e26acd2cb87ebe37bc1732775b90359ccad64bab6fbf82",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s13",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/testingframework/test_engine.py",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/testingframework/test_engine.py",
      "x-sha256": "8f5c1a9a1091d7817f58e78ce815f94a6a50946d7b2279b69ead030783b05a3a",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s14",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/src/sst/core/testingframework/sst_unittest.py",
      "x-repository": "sst-core",
      "x-path": "src/sst/core/testingframework/sst_unittest.py",
      "x-sha256": "644fec8123672c16293dae9a9f55a4e62a5a26321942ae0345ed0af5b7b60d33",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s15",
      "resource": "https://github.com/sstsimulator/sst-core/blob/09bc3927b1fc23e65f3aa0795739cad36f315d5a/scripts/sst-snippets.py",
      "x-repository": "sst-core",
      "x-path": "scripts/sst-snippets.py",
      "x-sha256": "7872adcdc10212dc6119fc21a8803d0a03cb3e366e0190e90d4953d126f18a54",
      "x-commit": "09bc3927b1fc23e65f3aa0795739cad36f315d5a"
    },
    {
      "id": "s16",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/simpleElementExample/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/simpleElementExample/Makefile.am",
      "x-sha256": "bc4ba4457b9f152217d1e2bf6feaaa10bca6e8d2f7d0d76369e479ca84e6daa9",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s17",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/src/sst/elements/carcosa/Makefile.am",
      "x-repository": "sst-elements",
      "x-path": "src/sst/elements/carcosa/Makefile.am",
      "x-sha256": "a47fe08eeb343d10ea6284f542d586bf9b011f8d09bd50821f886a7a63e3db2e",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    },
    {
      "id": "s18",
      "resource": "https://github.com/sstsimulator/sst-elements/blob/47b99537882df309fa2bdb2eb60c9a1e16efb5e5/config/sst_core_check_install.m4",
      "x-repository": "sst-elements",
      "x-path": "config/sst_core_check_install.m4",
      "x-sha256": "31d3068eb03ccfd6dddeb55009a300550d8f40f51218d0f544e086da343b1a21",
      "x-commit": "47b99537882df309fa2bdb2eb60c9a1e16efb5e5"
    }
  ]
}
---
# Build an out-of-tree element library

An element library is a shared object named `lib<name>.so` (or `.dylib`, tried second) whose ELI registrations use `<name>` as their library string. SST loads it on demand from its library search path, so a library does not need to live inside sst-elements or be rebuilt with it.

## Minimal library

```cpp
// mycomp.h
#include <sst/core/component.h>
class MyComp : public SST::Component {
public:
    SST_ELI_REGISTER_COMPONENT(MyComp, "mylib", "MyComp", SST_ELI_ELEMENT_VERSION(1, 0, 0),
        "One-line description", COMPONENT_CATEGORY_UNCATEGORIZED)
    SST_ELI_DOCUMENT_PARAMS({ "clock", "Clock frequency", "1GHz" })
    SST_ELI_DOCUMENT_PORTS({ "port", "Only port", { "" } })
    SST_ELI_DOCUMENT_STATISTICS({ "events", "Events seen", "events", 1 })
    MyComp(SST::ComponentId_t id, SST::Params& params);
};
```

Categories are `COMPONENT_CATEGORY_UNCATEGORIZED`, `PROCESSOR`, `MEMORY`, `NETWORK`, and `SYSTEM`. Subcomponents use `SST_ELI_REGISTER_SUBCOMPONENT(cls, lib, name, version, desc, interface)` against an API declared with `SST_ELI_REGISTER_SUBCOMPONENT_API`; modules use `SST_ELI_REGISTER_MODULE`. `SST_ELI_DOCUMENT_SUBCOMPONENT_SLOTS` and `SST_ELI_DOCUMENT_ATTRIBUTES` complete the documentation that `sst-info` prints. The library string must match the file name: `"mylib"` loads from `libmylib.so`.

## Compile and link with the installed core's flags

`sst-config` prints the core's build settings; the element-relevant keys on the recorded devel install are:

```text
sst-config --CXX               /usr/bin/clang++ -std=c++17
sst-config --ELEMENT_CXXFLAGS  -std=c++17 -ffp-contract=off -fPIC -DHAVE_CONFIG_H -I<prefix>/include
sst-config --ELEMENT_LDFLAGS   -shared -fno-common -Wl,-undefined -Wl,dynamic_lookup
sst-config --prefix            <prefix>
```

The flag values are host specific (the `-undefined dynamic_lookup` pair is the macOS form); always query them rather than copying. A minimal Makefile:

```make
CXX      := $(shell sst-config --CXX)
CXXFLAGS := $(shell sst-config --ELEMENT_CXXFLAGS)
LDFLAGS  := $(shell sst-config --ELEMENT_LDFLAGS)

libmylib.so: mycomp.o
	$(CXX) $(LDFLAGS) -o $@ $^

%.o: %.cc
	$(CXX) $(CXXFLAGS) -c $< -o $@

install: libmylib.so
	sst-register mylib mylib_LIBDIR=$(CURDIR)
```

Build against the same core that the `sst` on your PATH uses (`sst-config --prefix` must match `which sst`); the compile flags encode the core's C++ standard, `-ffp-contract=off`, and `HAVE_CONFIG_H`, and an element compiled against a different core install is an ABI mismatch, not a load-path problem.

## Register and discover

`sst-register <name> VAR=VALUE` adds or updates one key in the `[name]` section of `<prefix>/etc/sst/sstsimulator.conf` per invocation, so run it once per pair; the usage text's promise to auto-register `$PWD/include` and `$PWD/lib` without a pair is not implemented in `sstregistertool.cc`, which reads the pair unconditionally. When the prefix file is not writable it falls back to `~/.sst/sstsimulator.conf`. The loader accepts any key ending in `LIBDIR`, which is why `mylib_LIBDIR=...` works. `sst-register -l` lists sections and marks entries whose paths no longer exist as `INVALID`, `-u <name>` removes one, and `-au` removes every invalid entry. The in-tree build registers `SST_ELEMENT_LIBRARY` with its `LIBDIR`, `BINDIR`, `BUILDDIR`, and `EXT_LIBDIR`, plus `SST_ELEMENT_SOURCE` and `SST_ELEMENT_TESTS` sections used by the test runners.

The loader searches, in order, the command-line paths (`--add-lib-path` directories are searched first despite the help's "appends"; `--lib-path` replaces everything that follows), the `SST_LIB_PATH` environment variable, and the directories registered in `sstsimulator.conf` (`configShared.cc` implements this order). `SST_CORE_DL_BIND_POLICY` changes the `dlopen` binding mode. Set `SST_CORE_DL_VERBOSE` to print every `dlopen` attempt and failure, which is the fastest way to find a name or path mismatch. Verify with `sst-info mylib` and use `sst.Component("c0", "mylib.MyComp")` in Python.

## In-tree alternative

Adding a directory under `sst-elements/src/sst/elements/<name>/` with a `Makefile.am` (`comp_LTLIBRARIES = lib<name>.la`, `compdir = $(pkglibdir)`, `-module -avoid-version` link flags as in `simpleElementExample/Makefile.am`) and optionally a `configure.m4` integrates with the elements build, `select_build.py` selection, and `sst-test-elements` discovery through the registered `SST_ELEMENT_TESTS` paths. Elements configure locates `sst-config`, `sst-register`, and `sst-snippets.py` under the core prefix (`config/sst_core_check_install.m4`); `scripts/sst-snippets.py` extracts tagged code snippets for documentation from a JSON description and generates no element code. Prefer the in-tree route when the library must ship with sst-elements or needs its dependency probes; prefer out-of-tree for private or fast-iteration work.

## Failure modes

- `sst-info` or `sst` cannot find the library: the ELI library string, the file name, and a registered or `--add-lib-path` directory must agree; `.so` is tried before `.dylib`.
- A library that references another element's symbols without linking it can fail to load in `sst-info` on macOS while a simulation that loads the dependency first succeeds; see [build](build.md) for the Carcosa/memHierarchy case.
- Missing `-fPIC` or flags copied from another host produce link or load errors; regenerate them from `sst-config`.
- A registration macro inside a header included by two translation units duplicates symbols; keep one registration per class.

## Test an external library

Use a standalone Python configuration with a reference output, or write `testsuite_<type>_<name>.py` files that import `sst_unittest` from the installed testing framework and run them with `sst-test-elements -p /path/to/your/tests`: `-p` accepts any file or directory, and `get_testsuite_dir()` resolves relative to the suite file. Compare outputs after sorting when ranks or threads exceed one. See [testing](testing.md) and, for API changes that touch core, [core extension](../core/extending.md).
