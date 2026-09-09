---
aliases: ["Hierarchical Fourier Approximation for Variational Quantum Distribution Learning"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.06307"
url: "http://arxiv.org/abs/2609.06307v1"
published: "2026-09-05T23:34:49Z"
ingested: "2026-09-09T10:42:59Z"
authors:
  - "Taha Hoseinpour Asli"
  - "Sajjad Hashemian"
  - "Ebrahim Ardeshir-Larijani"
---

# Hierarchical Fourier Approximation for Variational Quantum Distribution Learning

## Abstract

> We study variational quantum distribution learning through a hierarchy of Walsh--Fourier
> approximations on the Boolean cube. At each level, a selected set of target Fourier coefficients
> defines a spectral truncation, which is projected onto the probability simplex and used as the
> target of a quantum circuit Born machine. Parameters learned at one level initialize the next
> through a warm-start map. We prove an end-to-end expected learning guarantee where the
> approximation term is determined by the omitted Fourier mass, while a normalized unbiased
> estimator yields an explicit statistical bound for empirical truncations. We then instantiate
> the abstract discrepancy conditions for total variation distance and relate the resulting
> distributional error to quantum-state fidelity. The total-variation specialization incurs the
> explicit factor $2^{n-1}$ under our normalized $\ell_2$ convention and is therefore informative
> only for sufficiently concentrated Fourier tails. The framework does not establish global
> trainability or eliminate barren plateaus; rather, it identifies the conditions under which low-
> to-high spectral training admits a approximation--estimation--optimization analysis.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

