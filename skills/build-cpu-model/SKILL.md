---
name: build-cpu-model
description: Build an SST CPU model by eliciting fidelity and workload constraints, choosing execution or request-generation elements, and validating the resulting simulation.
---

# Build an SST CPU model

Resolve the real path of this skill directory first, then use `../..` as the sst-ai-tools root; preserve the sibling knowledge/tools when installing. Resolve the user's SST source roots and existing installation. Here, building means constructing a simulation model; compile/install only as needed within the authorized task.

## Establish what the model must capture

Extract supplied requirements first. Ask a short, grouped set of questions about missing decisions:

- What question should the model answer? Must it capture instruction semantics, pipeline/branch behavior, memory ordering and cache stalls, application throughput, or only memory traffic? Which outputs will determine success?
- Must it run a real program, replay an existing trace, or generate synthetic traffic? What ISA/ABI, program/input, core/thread count, cache/memory organization, and OS/syscall requirements are known?
- What limits apply to fidelity, host runtime/memory, simulation scale, available binaries/toolchains/traces, external dependencies, or changes to SST C++? Are accelerators or faults part of the requested experiment?

Ask only about missing information that changes selection or behavior, with understandable choices instead of requiring element names. Continue independent source/install inspection while awaiting answers when asynchronous input is available. Do not commit to a binary/ISA or fidelity choice before a required answer arrives. Use explicit, configurable assumptions for incidental values; do not make every pipeline/cache parameter a prerequisite. Reuse earlier answers without another questionnaire.

## Select, construct, and validate

Read [CPU selection](../../ofk/using-sst/cpu-selection.md), then only task-relevant element guides and a nearby working model. Select a workload/execution model separately from cache, memory, and interconnect models. Explain why its abstraction captures the requested effects and which effects it omits. A request generator or trace replay must not be presented as detailed instruction execution.

Verify the selected ISA/ABI, decoder, OS interface, executable/trace format, and frontend prerequisites against current source. Check memory interfaces, address ranges, units, and core/hardware-thread mapping. Keep modeled hardware parallelism distinct from SST host ranks/threads. If existing functionality cannot capture a required effect, identify the smallest extension and implement it within scope; do not substitute a different fidelity level silently.

Produce a parameterized Python model and reproducible command. Record input artifacts, source/installation identity, assumptions, omitted mechanisms, and measurable acceptance criteria in a concise untracked model note in the user's project root. Do not install external toolchains or alter dependencies merely to conceal an unmet constraint.

Use [model construction](../../ofk/using-sst/models.md) and [testing](../../ofk/development/testing.md). Start with a deterministic workload: verify architectural output and normal program exit for execution models, or request sequence/count/data behavior for traffic models. Validate timing only at the abstraction level modeled; simulator completion alone is insufficient. Deliver the working model and evidence, or the concrete prerequisite blocker with completed unaffected work, rather than stopping at a recommendation.
