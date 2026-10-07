# SST element selector

Every element directory in the checked source has a use-case profile. Coverage means documentation coverage, not runtime verification. Choose the causal mechanism and workload separately; names and directory capitalization do not establish ELI registration names.

| Element | Role | Main use | Documentation |
|---|---|---|---|
| [ariel](ariel/use-cases.md) | Execution/frontend | Application-driven memory traffic with CPU/frontend integration | Use-case profile |
| [balar](balar/use-cases.md) | Accelerator | CUDA/GPGPU-Sim integration through MMIO and DMA | Detailed guides |
| [cacheTracer](cacheTracer/use-cases.md) | Observation | Observe memory events, address distributions, and boundary latency | Use-case profile |
| [carcosa](carcosa/use-cases.md) | Fault injection | Inject faults and coordinate interception with CPU/memory models | Detailed guides |
| [cassini](cassini/use-cases.md) | Cache policy/observation | Prefetching and cache-access instrumentation | Use-case profile |
| [cramSim](cramSim/use-cases.md) | Memory device/controller | Detailed memory transaction and command modeling | Use-case profile |
| [ember](ember/use-cases.md) | Workload | Communication/computation motifs for network studies | Detailed guides |
| [firefly](firefly/use-cases.md) | Protocol/NIC/runtime | Communication protocol and NIC behavior for workload integration | Use-case profile |
| [gensa](gensa/use-cases.md) | Neuromorphic accelerator | Spiking processor with memory and network interfaces | Use-case profile |
| [golem](golem/use-cases.md) | Processing using memory | Matrix-vector arrays and CPU coprocessor integration | Use-case profile |
| [hermes](hermes/use-cases.md) | API/support library | Shared communication and service interfaces | Use-case profile |
| [iris](iris/use-cases.md) | Communication support library | SUMI collective/transport and PMI/libfabric support | Profile plus fabric/collective guides |
| [kingsley](kingsley/use-cases.md) | Interconnect | Two-dimensional mesh on-chip network | Use-case profile |
| [llyr](llyr/use-cases.md) | Dataflow accelerator | Configurable graph-based dataflow execution | Use-case profile |
| [mask-mpi](mask-mpi/use-cases.md) | Application API/runtime | MPI API modeling over the Mercury-related runtime | Use-case profile |
| [memHierarchy](memHierarchy/use-cases.md) | Cache/memory system | Caches, coherence, controllers, and memory interfaces | Detailed guides |
| [mercury](mercury/use-cases.md) | Application runtime | Node, OS, NIC, and modeled compute machinery | Detailed guides |
| [merlin](merlin/use-cases.md) | Interconnect | Configurable routers, topologies, link control, and traffic | Detailed guides |
| [messier](messier/use-cases.md) | Memory technology | Nonvolatile memory controller, banks, and ranks | Use-case profile |
| [miranda](miranda/use-cases.md) | Synthetic workload | Address-generation and memory-access patterns | Use-case profile |
| [mmu](mmu/use-cases.md) | Address translation | MMU/TLB components for execution-model integration | Use-case profile |
| [opal](opal/use-cases.md) | Memory allocation manager | Physical-memory allocation for shared/disaggregated systems | Use-case profile |
| [osseous](osseous/use-cases.md) | RTL integration/template | External RTL-model component integration | Use-case profile |
| [prospero](prospero/use-cases.md) | Trace workload | Memory-trace replay with supported reader formats | Use-case profile |
| [rdmaNic](rdmaNic/use-cases.md) | NIC/offload | RDMA-style host, memory, and network integration | Use-case profile |
| [samba](samba/use-cases.md) | Address translation | TLB hierarchy and page-walk modeling | Use-case profile |
| [serrano](serrano/use-cases.md) | CGRA accelerator | Standalone coarse-grained iterator/add/output graphs | Use-case profile |
| [shogun](shogun/use-cases.md) | Interconnect | Round-robin crossbar with message-rate limits | Use-case profile |
| [simpleElementExample](simpleElementExample/use-cases.md) | Teaching/framework example | Examples of SST component APIs and lifecycle | Use-case profile |
| [simpleSimulation](simpleSimulation/use-cases.md) | Teaching/simulation example | Monolithic and distributed car-wash models | Use-case profile |
| [thornhill](thornhill/use-cases.md) | Compute/support library | Detailed compute callbacks and memory-heap integration | Use-case profile |
| [vanadis](vanadis/use-cases.md) | Execution/CPU | Binary execution with ISA, pipeline, LSQ, and OS interfaces | Detailed guides |
| [vaultsim](vaultsim/use-cases.md) | Stacked-memory model | Fixed-delay memory vaults and logic-layer organization | Use-case profile |
| [zodiac](zodiac/use-cases.md) | Trace workload | SIRIUS MPI trace replay for network simulation | Use-case profile |

Start with the selected profile, then load detailed guides where present. Profile-only elements require source inspection for implementation and dependency details. All guides remain draft.
