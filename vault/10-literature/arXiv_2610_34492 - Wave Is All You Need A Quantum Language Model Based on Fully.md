---
aliases: ["Wave Is All You Need: A Quantum Language Model Based on Fully Connected Quantum Boltzmann Machine"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.34492"
url: "http://arxiv.org/abs/2610.34492v1"
published: "2026-10-25T18:35:48Z"
ingested: "2026-10-27T11:33:18Z"
authors:
  - "Jun Liu"
---

# Wave Is All You Need: A Quantum Language Model Based on Fully Connected Quantum Boltzmann Machine

## Abstract

> This work proposes a self-attention mechanism based on the fully connected quantum Boltzmann
> machine (FC-QBM), and further constructs a fully connected quantum Boltzmann machine language
> model (FC-QBM-LM) using the mechanism as the core engine. By performing unitary evolution on
> semantic quantum states, the mechanism implicitly implements positional encoding and self-
> attention computation, eliminating the need to decompose continuous semantic streams into
> discrete matrices for explicit matrix multiplication, with the measurement results naturally
> satisfying the normalization condition. Specifically, this work rigorously derives the
> computational principle of the self-attention mechanism based on FC-QBM, and demonstrates that
> this mechanism is mathematically equivalent to the classical self-attention mechanism. The
> mathematical principles governing the training and generation of FC-QBM-LM are thoroughly
> derived, and the two corresponding algorithms are subsequently developed. An 8-qubit FC-QBM-LM
> is finally constructed and trained on the corpus of Tang poetry. Under the 8-qubit setting, the
> quantum layer implements the entire positional encoding and self-attention computation pipeline
> with only 44 parameters. In the noiseless scenario, the model exhibits favorable convergence.
> Furthermore, the quantum circuit proposed in this work, which terminates with Y-axis rotation
> gates, achieves better convergence than the counterpart terminating with X-axis rotation gates.
> Under the small-sample regime and across eight distinct noise intensity levels, the model
> demonstrates strong noise robustness, retaining over 99% of its noiseless convergence
> performance. Experiments on five-character quatrain generation reveal that the model
> preliminarily exhibits three core capabilities: associative and divergent thinking, content
> generation across imagery and human-aligned word ordering.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

