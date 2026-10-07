"""Classify retained core probe evidence against the tested behavior contracts."""

import argparse
import json
import math
import re
import shutil
from pathlib import Path


def statistic(text, name):
    return next(line for line in text.splitlines() if f"probe.{name} :" in line)


def counter(line, name):
    return int(re.search(re.escape(name) + r"\.[a-z0-9]+ = (\d+)", line).group(1))


def analyze(folder):
    results = json.loads((folder / "results.json").read_text())
    if results["build"]["exit_code"] != 0 or results["build"]["timed_out"]:
        raise ValueError("Probe compilation did not complete normally")
    required = {
        "basic",
        "raw",
        "unique",
        "raw_request",
        "unique_request",
        "clock_one",
        "clock",
        "substats_once",
        "substats_twice",
        "hotspot",
        "element_stats_integer",
        "element_stats_floating",
    }
    if not required.issubset(results["runs"]):
        raise ValueError("Required probe run records are missing")
    for name, run in results["runs"].items():
        if run["timed_out"] or (name != "clock" and run["exit_code"] != 0):
            raise ValueError(f"Probe did not complete normally: {name}")

    def text(name):
        return (folder / f"{name}.out").read_text()

    basic = text("basic")
    findings = {}

    def add(identifier, reproduced, observed, expected, modes):
        findings[identifier] = {
            "status": "reproduced" if reproduced else "requires-investigation",
            "observed": observed,
            "expected": expected,
            "runs": modes,
        }

    clock_control = text("clock_one")
    early = "CLOCK promised=2\nCLOCK other cycle=1" in clock_control
    crash = results["runs"]["clock"]["exit_code"] == -11
    add(
        "F01",
        early and crash,
        {
            "promised_cycle": 2,
            "observed_cycle": 1 if early else None,
            "growth_exit_code": results["runs"]["clock"]["exit_code"],
        },
        {"reactivated_cycle": 2, "growth_crash": False},
        ["clock_one", "clock"],
    )
    direct, scoped = re.search(r"PARAM direct=(\S+) scoped=(\S+)", basic).groups()
    add(
        "F02",
        direct == "2GHz" and scoped == "1GHz",
        {"direct": direct, "scoped": scoped},
        {"direct": "2GHz", "scoped": "2GHz"},
        ["basic"],
    )
    draws = [
        (float(draw), int(index))
        for draw, index in re.findall(r"DISCRETE u=([\d.]+) index=(\d+)", basic)
    ]
    destinations = [
        int(value) for value in re.findall(r"ACTUAL_TRAFFICGEN.*dest=(\d+)", text("hotspot"))
    ]
    add(
        "F03",
        draws == [(0.1, 1), (0.5, 2), (0.99, 2)] and destinations == [4, 4, 4],
        {"draws_and_indices": draws, "hotspot_destinations": destinations},
        {"indices": [0, 1, 1], "hotspot_destinations": [3, 3, 3]},
        ["basic", "hotspot"],
    )

    def serialization(name):
        output = text(name)
        consumed, size = re.search(r"consumed=(\d+) buffer=(\d+)", output).groups()
        dynamic = int(re.search(r"(?:derived|extended)=(\d+)", output).group(1))
        return {
            "consumed": int(consumed),
            "buffer": int(size),
            "dynamic_type_preserved": bool(dynamic),
        }

    serialized = {
        name: serialization(name) for name in ("raw", "unique", "raw_request", "unique_request")
    }
    controls_ok = all(
        serialized[name]["dynamic_type_preserved"]
        and serialized[name]["consumed"] == serialized[name]["buffer"]
        for name in ("raw", "raw_request")
    )
    unique_bad = all(
        not serialized[name]["dynamic_type_preserved"]
        and serialized[name]["consumed"] < serialized[name]["buffer"]
        for name in ("unique", "unique_request")
    )
    add(
        "F04",
        controls_ok and unique_bad,
        serialized,
        {"dynamic_type_preserved": True, "complete_stream_consumption": True},
        list(serialized),
    )
    request, response = re.search(
        r"WRITE_UNLOCK request=([0-9a-f]+) response=([0-9a-f]+)", basic
    ).groups()
    request, response = int(request, 16), int(response, 16)
    add(
        "F05",
        request == 0 and response == 0,
        {"request_vaddr": request, "response_vaddr": response},
        {"request_vaddr": 0x8000, "response_vaddr": 0x8000},
        ["basic"],
    )
    configs = {}
    for mode in ("once", "twice"):
        tree = json.loads((folder / f"substats_{mode}.json").read_text())
        parent = next(c for c in tree["components"] if c["name"] == "loader")
        child = next(c for c in parent["subcomponents"] if c["slot_name"] == "mySubComp")
        configs[mode] = child["statistics"][0]["params"]
    add(
        "F06",
        configs["once"] == {"rate": "10ns"} and configs["twice"] == configs["once"],
        configs,
        {"twice_contains": {"rate": "10ns", "type": "sst.HistogramStatistic", "binwidth": 2}},
        ["substats_once", "substats_twice"],
    )
    batch = statistic(basic, "batch")
    observed = {key: counter(batch, key) for key in ("NumItemsCollected", "NumItemsBinned")}
    observed["bin_population"] = int(re.search(r"Bin0:0-9\.u64 = (\d+)", batch).group(1))
    add(
        "F07",
        observed == {"NumItemsCollected": 100, "NumItemsBinned": 1, "bin_population": 100},
        observed,
        {"NumItemsCollected": 100, "NumItemsBinned": 100, "bin_population": 100},
        ["basic"],
    )
    offset = statistic(basic, "offset")
    observed = {
        "collected": counter(offset, "NumItemsCollected"),
        "binned": counter(offset, "NumItemsBinned"),
        "displayed_bins": [int(value) for value in re.findall(r"Bin\d+:[^=]+ = (\d+)", offset)],
    }
    element_integer = next(
        line
        for line in text("element_stats_integer").splitlines()
        if "sample.UINT32_statistic :" in line
    )
    integer_observed = {
        "collected": counter(element_integer, "NumItemsCollected"),
        "binned": counter(element_integer, "NumItemsBinned"),
        "displayed_bins": [
            int(value) for value in re.findall(r"Bin\d+:[^=]+ = (\d+)", element_integer)
        ],
    }
    add(
        "F08",
        observed == {"collected": 2, "binned": 2, "displayed_bins": [0, 0]}
        and integer_observed == {"collected": 4, "binned": 4, "displayed_bins": [0] * 10},
        {"probe": observed, "element": integer_observed},
        {"collected": 2, "binned": 2, "displayed_bins": [2, 0]},
        ["basic", "element_stats_integer"],
    )
    floating = statistic(basic, "floating")
    observed = {
        "collected": counter(floating, "NumItemsCollected"),
        "binned": counter(floating, "NumItemsBinned"),
        "above_max": counter(floating, "NumOutOfBounds-MaxValue"),
    }
    element_floating = next(
        line
        for line in text("element_stats_floating").splitlines()
        if "sample.SUBID_statistic.0 :" in line
    )
    floating_observed = {
        "collected": counter(element_floating, "NumItemsCollected"),
        "binned": counter(element_floating, "NumItemsBinned"),
        "above_max": counter(element_floating, "NumOutOfBounds-MaxValue"),
    }
    add(
        "F09",
        observed == {"collected": 1, "binned": 0, "above_max": 1}
        and floating_observed == {"collected": 4, "binned": 0, "above_max": 4},
        {"probe": observed, "element": floating_observed},
        {"collected": 1, "binned": 1, "above_max": 0},
        ["basic", "element_stats_floating"],
    )
    maximum, variance = (
        float(value) for value in re.search(r"ACCUM max=(\S+) variance=(\S+)", basic).groups()
    )
    add(
        "F10",
        maximum > 0 and not math.isclose(maximum, -1),
        {"maximum": maximum},
        {"maximum": -1},
        ["basic"],
    )
    add(
        "F11",
        variance == 4,
        {"variance": variance},
        {"population_variance": 1, "sample_variance": 2},
        ["basic"],
    )
    assert len(findings) == 11
    identity = {
        key: results[key]
        for key in ("revisions", "workspace_revisions", "runtime_identity")
        if key in results
    }
    return {
        **identity,
        "findings": findings,
        "raw_controls_passed": controls_ok,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--archive", type=Path, required=True)
    args = parser.parse_args()
    analysis = analyze(args.input)
    destination = args.archive.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    for path in sorted(args.input.iterdir()):
        if path.suffix in (".out", ".err", ".json"):
            shutil.copy2(path, destination / path.name)
    (destination / "assessment.json").write_text(json.dumps(analysis, indent=2) + "\n")
    print(
        json.dumps(
            {
                "findings": len(analysis["findings"]),
                "reproduced": sum(
                    f["status"] == "reproduced" for f in analysis["findings"].values()
                ),
                "raw_controls_passed": analysis["raw_controls_passed"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
