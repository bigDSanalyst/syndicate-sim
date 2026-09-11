---
aliases: ["A Quantum-Inspired Dequantization Method for Diagonally Weighted Matrix Functions: Application to Learning with Optimized Random Features"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.10729"
url: "http://arxiv.org/abs/2609.10729v1"
published: "2026-09-09T18:23:55Z"
ingested: "2026-09-11T10:32:59Z"
authors:
  - "Natsuto Isogai"
  - "Mio Murao"
  - "Hayata Yamasaki"
---

# A Quantum-Inspired Dequantization Method for Diagonally Weighted Matrix Functions: Application to Learning with Optimized Random Features

## Abstract

> Quantum-inspired classical algorithms have dequantized several quantum machine learning routines
> by replacing quantum linear-algebra subroutines with classical counterparts. However, the
> sampler based on quantum singular value transformation (QSVT) for learning with optimized random
> features is not covered by existing dequantization frameworks, because the matrix to be inverted
> is not itself available through sampling access. In this work, we develop a classical algorithm
> to address this type of quantum-advantage candidate. Our method samples heavy indices, reduces
> the transformation to a small principal block, and outputs a sparse classical representation
> with operator-norm guarantees. Applying this method dequantizes the sampler for optimized random
> features, giving a classical sampler with prescribed accuracy and polynomially related runtime.
> These results show that the factorization underlying a quantum block encoding can itself provide
> sufficient classical structure even when sampling-and-query access to the composite matrix is
> unavailable.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

