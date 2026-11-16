---
aliases: ["Quantum Data Processing Unit for Neutral-Atom Quantum Computers"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.17652"
url: "http://arxiv.org/abs/2611.17652v1"
published: "2026-11-13T01:57:48Z"
ingested: "2026-11-16T14:40:17Z"
authors:
  - "Pranav Srinivas Murali"
  - "Russell Marroquin Solares"
  - "Warren Zhou"
  - "Wanda Hou"
  - "Anil Bilgin"
  - "Yi-Zhuang You"
---

# Quantum Data Processing Unit for Neutral-Atom Quantum Computers

## Abstract

> Quantum computers need real-time classical processing to convert measurement data into feedback
> within device-specific timing constraints. We introduce the quantum data processing unit (QDPU),
> an architecture between a quantum device and its controller. Its core is a machine-learned
> quantum data model (QDM), adapted to the measurement response and noise characteristics of the
> device. We implement an FPGA pipeline for neutral-atom array assembly that performs occupancy
> detection and rearrangement scheduling in FPGA logic. One calibrated matched-filter lane
> classifies a $50\times50$ array in 12.5 $μ$s. An atom-loss model using a software reference
> planner evaluates a $35\times35$ target with a 60 s trap lifetime and 0.1% loss per moved atom.
> Removing an assumed 150 ms host round trip raises the predicted assembly success from 8% to 85%
> and reduces the wall-clock time per successful assembly from 19 s to 0.16 s. A GPU-based outer
> loop is proposed for refitting model parameters between runs. Its NVQLink transport is measured
> on the board: over 10 GbE to an NVIDIA DGX Spark, the median FPGA-to-host-to-FPGA round trip is
> 2.74 $μ$s for 128-byte messages forwarded by a CPU core. A separate 12-bit learned qLDPC kernel
> is placed and routed for the same FPGA target, with a derived latency of 0.84 ms per round for a
> $[[1122,148]]$ lifted-product code under code-capacity noise. A quantised GraphMP ranking kernel
> for the same code runs on the board with a median host-to-FPGA-to-host latency of 50.5 $μ$s with
> one shot in flight, excluding host-side BP+OSD post-processing. Together, these implementations
> illustrate a shared architecture with workload-specific models and timing requirements.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

