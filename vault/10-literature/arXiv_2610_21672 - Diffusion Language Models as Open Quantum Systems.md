---
aliases: ["Diffusion Language Models as Open Quantum Systems"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.21672"
url: "http://arxiv.org/abs/2610.21672v1"
published: "2026-10-15T10:57:07Z"
ingested: "2026-10-16T10:37:59Z"
authors:
  - "Akinori Tanaka"
  - "Yukinao Akamatsu"
  - "Takuki Tomita"
  - "Yuji Hirono"
---

# Diffusion Language Models as Open Quantum Systems

## Abstract

> Diffusion language models generate text by reversing a classical diffusion process over token
> sequences. We show that their continuous-time forward and reverse dynamics can be embedded in
> the framework of open quantum systems, which describes quantum systems interacting with their
> environment. This connection provides a basis for extending diffusion sampling to superpositions
> of sentence states and for modifying the underlying generation dynamics. We construct a
> $τ$-leaping unraveling scheme that simulates stochastic trajectories of these states while
> updating multiple token positions at each step. This enables generation conditioned on
> superposed prompts or thoughts, which we call Superposition of Prompts (SoP) and Superposition
> of Thoughts (SoT). The same formulation yields Quantum-Inspired Remasking (QIR): perturbing the
> masked-diffusion dynamics produces a confidence-based rule for revising previously generated
> tokens. Experiments with pretrained diffusion language models show that superposition-based
> generation can retain information from conditioning components not selected at the final
> measurement, while QIR improves LLM-assessed text quality when applied at an appropriate stage
> of generation.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

