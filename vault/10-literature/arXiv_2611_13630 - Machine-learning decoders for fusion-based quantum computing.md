---
aliases: ["Machine-learning decoders for fusion-based quantum computing in real time"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.13630"
url: "http://arxiv.org/abs/2611.13630v1"
published: "2026-11-10T06:18:48Z"
ingested: "2026-11-11T13:29:45Z"
authors:
  - "Daniel Barter"
  - "Jacob C. Bridgeman"
  - "Chris Dawson"
  - "Terry Farrelly"
  - "Shane Fleming"
  - "Mercedes Gimeno-Segovia"
  - "Paul Hartke"
  - "Timothy Hein"
  - "Sean Howell"
  - "Gregory Hyegang Jun"
  - "Siddhartha Kamalakara"
  - "Yehua Liu"
  - "Jose M. Monsalve Diaz"
  - "Eddie Richter"
  - "Sam Roberts"
---

# Machine-learning decoders for fusion-based quantum computing in real time

## Abstract

> Fault-tolerant quantum computation requires decoders that combine accuracy, throughput, low
> latency, and scalability to large numbers of physical qubits. In photonic fusion-based
> architectures, erasures from photon loss and probabilistic fusion measurements are a dominant
> error mechanism, motivating decoders that remain accurate at high erasure rates. We introduce
> PRISM, a transformer-based machine-learning decoder designed to exploit the known locations of
> erasures in protocols subject to both Pauli and erasure errors. We benchmark PRISM across a wide
> range of fault-tolerant protocols based on surface codes, color codes, and quantum low-density
> parity-check codes, with distances up to 24. Across these benchmarks, PRISM matches the logical
> error rates of integer-programming-based decoders while being significantly faster, including at
> error rates up to 50% of threshold. We further optimize the decoder and its real-time hardware
> implementation to reduce latency while maintaining accuracy. Our optimized implementation on an
> AMD VP1902 FPGA can decode logical blocks of distance 8 in both space and time, demonstrating a
> latency of 6.59 microseconds and an amortized decoding time of 1.56 microseconds per logical
> block is possible. These results show that machine-learning decoding can provide accurate, low-
> latency inference for erasure-dominated fault-tolerant quantum architectures.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

