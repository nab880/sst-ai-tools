"""Run historical core reproducers without changing the SST source checkouts."""

import argparse
import hashlib
import json
import os
import platform
import signal
import subprocess
import time
from pathlib import Path


def run(command, cwd, stdout, stderr, env, timeout=20):
    started = time.monotonic()
    with stdout.open("w") as out, stderr.open("w") as err:
        process = subprocess.Popen(
            command, cwd=cwd, env=env, stdout=out, stderr=err, start_new_session=True
        )
        try:
            code = process.wait(timeout=timeout)
            timed_out = False
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
            code = process.returncode
            timed_out = True
    return {
        "command": command,
        "cwd": str(cwd),
        "exit_code": code,
        "timed_out": timed_out,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "stdout": str(stdout),
        "stderr": str(stderr),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    repo = Path(__file__).resolve().parents[3]
    parser.add_argument("--prefix", type=Path, default=repo / ".runtime/devel/install")
    parser.add_argument("--workspace", type=Path, default=repo.parent)
    parser.add_argument("--output", type=Path, default=repo / ".runtime/reassessment-2026-10-06")
    parser.add_argument(
        "--compiler", default="/usr/bin/clang++" if platform.system() == "Darwin" else "c++"
    )
    parser.add_argument("--sdk", default="")
    args = parser.parse_args()
    work = args.output.resolve()
    work.mkdir(parents=True, exist_ok=True)
    prefix = args.prefix.resolve()
    probes = Path(__file__).resolve().parent / "probes"
    env = os.environ.copy()
    env["OMPI_MCA_btl"] = "self,tcp"
    if platform.system() == "Darwin":
        env["OMPI_MCA_btl_tcp_if_include"] = "lo0"
        env.pop("OMPI_MCA_btl_tcp_if_exclude", None)
    if args.sdk:
        env["SDKROOT"] = args.sdk
    revisions = {}
    for name in ("sst-core", "sst-elements"):
        revisions[name] = subprocess.check_output(
            ["git", "-C", str(args.workspace / name), "rev-parse", "HEAD"], text=True
        ).strip()
    compile_command = [
        args.compiler,
        "-std=c++17",
        "-O0",
        "-g",
        "-Wall",
        "-Wextra",
        "-fPIC",
        "-shared",
        "-I" + str(prefix / "include"),
        "-I" + str(args.workspace.resolve() / "sst-elements/src"),
        str(probes / "audit.cc"),
        str(probes / "capture.cc"),
        "-o",
        str(work / "libaudit.so"),
    ]
    if platform.system() == "Darwin":
        compile_command[
            compile_command.index("-shared") + 1 : compile_command.index("-shared") + 1
        ] = ["-undefined", "dynamic_lookup"]
    compiled = run(compile_command, work, work / "build.out", work / "build.err", env, timeout=120)
    results = {
        "workspace_revisions": revisions,
        "runtime_identity": {
            "prefix": str(prefix),
            "source_revision_binding": "Not verified by this runner; compare build provenance before attributing results to workspace revisions.",
            "sha256": {
                str(path.relative_to(prefix)): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in [
                    prefix / "bin/sst",
                    prefix / "libexec/sstsim.x",
                    prefix / "lib/sst-elements-library/libmerlin.so",
                    prefix / "lib/sst-elements-library/libsimpleElementExample.so",
                    *sorted((prefix / "include/sst/core").rglob("*.h")),
                ]
                if path.is_file()
            },
        },
        "build": compiled,
        "runs": {},
        "probe_sha256": {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(probes.iterdir())
            if p.is_file()
        },
    }
    results_path = work / "results.json"
    results_path.write_text(json.dumps(results, indent=2) + "\n")
    if compiled["exit_code"]:
        print((work / "build.err").read_text()[-5000:], flush=True)
        raise SystemExit("Probe compilation failed")
    executable = str(prefix / "bin/sst")
    common = [executable, "--add-lib-path=" + str(work)]
    tasks = []
    for mode in ("basic", "raw", "unique", "raw_request", "unique_request", "clock_one", "clock"):
        tasks.append((mode, common + ["--stop-at=5ns", str(probes / "probe.py"), "--", mode]))
    for mode in ("once", "twice"):
        tasks.append(
            (
                "substats_" + mode,
                common
                + [
                    "--output-json=" + str(work / ("substats_" + mode + ".json")),
                    str(probes / "substats.py"),
                    "--",
                    mode,
                ],
            )
        )
    tasks.append(("hotspot", common + [str(probes / "hotspot.py")]))
    for mode in ("integer", "floating"):
        tasks.append(
            ("element_stats_" + mode, common + [str(probes / "statistics.py"), "--", mode])
        )
    for name, command in tasks:
        print("RUN", name, flush=True)
        result = run(command, work, work / (name + ".out"), work / (name + ".err"), env)
        results["runs"][name] = result
        results_path.write_text(json.dumps(results, indent=2) + "\n")
        print(
            "RESULT", name, result["exit_code"], "timeout=" + str(result["timed_out"]), flush=True
        )
    print("Evidence:", results_path, flush=True)


if __name__ == "__main__":
    main()
