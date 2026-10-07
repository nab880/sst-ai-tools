---
name: build-network-model
description: Build an SST network model by eliciting modeling priorities and constraints, selecting network and workload elements, and validating the resulting simulation.
---

# Build an SST network model

Resolve the real path of this skill directory first, then use `../..` as the sst-ai-tools root; preserve the sibling knowledge/tools when installing. Resolve the user's SST source roots and existing installation. Here, building means constructing a simulation model; compile/install only as needed within the authorized task.

## Establish what the model must capture

Extract answers already supplied by the user. Ask a short, grouped set of questions about missing information that changes the model:

- What question should the model answer, and which results matter: latency, throughput, congestion, fairness, collective completion, or resilience? Which mechanisms must it capture: routing, arbitration, buffering, backpressure, protocol overhead, or failures?
- Is this an on-chip interconnect, node-to-node network, or another system? What topology, endpoint count, traffic/application, message sizes, and hardware measurements or target parameters are available?
- What constraints apply to fidelity, simulated scale/duration, host runtime/memory, existing binaries/traces, external dependencies, or changes to SST C++?

Offer understandable choices when helpful; do not require the user to name an element or supply every numeric parameter. If user input is supported asynchronously, continue source/install inspection while awaiting answers. Do not finalize an element choice or implement behavior that depends on an unanswered material constraint. For unspecified incidental values, use explicit, configurable assumptions. If the prompt already answers these questions, proceed without repeating them.

## Select, construct, and validate

Read [network selection](../../ofk/using-sst/network-selection.md), then only the chosen element's relevant guides and one working configuration. Separate the network model from its endpoint/workload model. State the selection rationale in terms of the user's priorities, and identify effects the model will omit. Do not default to Merlin solely because it has a curated guide.

Choose existing functionality when it captures the requested mechanisms. If new behavior needs C++, identify the precise extension point and complete it within the user's scope; do not silently substitute different behavior. Surface a missing prerequisite or a consequential scope choice before dependent work, while progressing on unaffected work.

Produce a parameterized Python model and reproducible run command. Verify registration, ports, slots, units, VN/VC compatibility, endpoint mapping, and termination against current source/ELI. Record workload/seed, assumptions, configuration, installation identity, and required artifacts in a concise untracked model note in the user's project root.

Use [model construction](../../ofk/using-sst/models.md) and [testing](../../ofk/development/testing.md). Validate small deterministic delivery/count cases and the mechanism important to the user; congestion studies need a contention case, routing changes need route checks. Check natural completion and distinguish simulated metrics from host runtime. Deliver the model, validation evidence, limitations, and any concrete blocker; do not stop at a proposed element list.
