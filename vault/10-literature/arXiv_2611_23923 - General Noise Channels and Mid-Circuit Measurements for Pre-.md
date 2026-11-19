---
aliases: ["General Noise Channels and Mid-Circuit Measurements for Pre-Trajectory Sampling with Batched Execution"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.23923"
url: "http://arxiv.org/abs/2611.23923v1"
published: "2026-11-18T06:15:37Z"
ingested: "2026-11-19T15:11:48Z"
authors:
  - "Louis Follet"
  - "Paavai Pari"
  - "Isidor Schoch"
  - "Thien Nguyen"
  - "Justin G. Lietz"
  - "Daniel Lowell"
  - "Brucek Khailany"
  - "Krysta M. Svore"
  - "Dirk R. Englund"
  - "Taylor L. Patti"
---

# General Noise Channels and Mid-Circuit Measurements for Pre-Trajectory Sampling with Batched Execution

## Abstract

> Many studies of quantum protocols require fast sampling of large amounts of measurement data
> from noisy quantum circuits, such as for training machine-learning decoders for quantum error
> correction. Exact simulation of realistic noise is expensive, while stabilizer-based simulators
> are fast but approximate, for example through Pauli twirling, which generally alters the output
> statistics. Pre-trajectory sampling with batched execution (PTSBE) accelerates exact trajectory
> simulation by sampling noise before state evolution. This method requires the outcome
> probability of every stochastic event to be independent of the state, which excludes mid-circuit
> measurements and general Kraus channels. We present a generalization of PTSBE to measurement and
> Kraus operators without approximation. Each event is partially pre-sampled, while deferred
> outcomes are drawn during grouped execution via multinomial branching and cached-state reuse. We
> implement the method for GPUs as an extension of CUDA-Q. On distance-3 topological code memories
> under amplitude damping, it is up to 24x faster than conventional trajectory sampling in CUDA-Q.
> On 30-qubit random circuits with mid-circuit measurements, it is up to 83x faster and
> outperforms the near-Clifford simulator Clifft when more than about 25% of the gates are non-
> Clifford. With repeated sampling of each final state, its sampling rate per trajectory exceeds
> that of CUDA-Q by nearly five orders of magnitude. Our method also allows us to compare exact
> amplitude damping with its Pauli-twirled channel on a surface-code memory, revealing that
> twirling overestimates the detection rate by 21% and raises the logical error rate of a lookup
> decoder by 8%. This work makes exact, high-throughput simulation practical for general noisy
> circuits, from data generation for training decoders to studying measurement-based fault-
> tolerant protocols under realistic noise.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

