---
aliases: ["Flowers: A Warp Drive for Neural PDE Solvers"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2603.04430"
url: "http://arxiv.org/abs/2603.04430v2"
published: "2026-02-17T15:06:28Z"
ingested: "2026-08-31T12:36:30Z"
authors:
  - "Till Muser"
  - "Alexandra Spitzer"
  - "Matti Lassas"
  - "Maarten V. de Hoop"
  - "Ivan Dokmanić"
---

# Flowers: A Warp Drive for Neural PDE Solvers

## Abstract

> We introduce Flowers, a neural architecture for learning PDE solution operators built entirely
> from multihead warps. Aside from pointwise channel mixing and a multiscale scaffold, Flowers use
> no Fourier multipliers, no dot-product attention, and no convolutional mixing. Each head
> predicts a displacement field and warps the mixed input features. Motivated by physics and
> computational efficiency, displacements are predicted pointwise, without any spatial
> aggregation, and nonlocality enters only through sparse sampling at source coordinates, one per
> head. Stacking warps in multiscale residual blocks yields Flowers, which implement adaptive,
> global interactions at linear cost. We theoretically motivate this design through three
> complementary lenses: flow maps for conservation laws, waves in inhomogeneous media, and a
> kinetic-theoretic continuum limit. Flowers achieve excellent performance on a broad suite of 2D
> and 3D time-dependent PDE benchmarks, particularly flows and waves. A compact 17M-parameter
> model consistently outperforms Fourier, convolution, and attention-based baselines of similar
> size, while a 150M-parameter variant improves over recent transformer-based foundation models
> with much more parameters, data, and training compute.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

