---
aliases: ["Resource-Tunable Quantum Circuit Implementation of Nonlinear Element-Wise Transformations"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.39295"
url: "http://arxiv.org/abs/2609.39295v1"
published: "2026-09-30T08:39:30Z"
ingested: "2026-10-01T12:22:27Z"
authors:
  - "Chunlin Yang"
  - "Yuqi Li"
  - "Hongmei Yao"
  - "Zhaobing Fan"
---

# Resource-Tunable Quantum Circuit Implementation of Nonlinear Element-Wise Transformations

## Abstract

> Nonlinear transformations are important in quantum machine learning and other quantum numerical
> applications, which can be reduced to the implementation of element-wise polynomials through
> polynomial approximation. Existing works establish the feasibility of transformations and
> improve query or auxiliary-space efficiency, but circuit depth remains linear in scale with
> degree. In this work, we develop a resource-tunable quantum framework that decomposes a
> $(2^d-1)$-degree polynomial into $m$ lower-degree factors, with $m$ controlling the degree of
> parallelism. By varying $m$ from $1$ to $2^d-1$, the framework provides a trade-off among query
> complexity, additional gate complexity, ancilla count, and normalization, ranging from a binary-
> tree implementation to a $\mathcal{O}(n+d)$-depth construction with highly parallel oracle
> queries that match the query lower bound. The effects of polynomial approximation and
> implementation errors are further analyzed. We demonstrate the framework for nonlinear
> activation functions such as sigmoid and tanh, as well as pixel-wise image transformations.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

