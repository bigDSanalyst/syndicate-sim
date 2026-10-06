---
aliases: ["Finding Gaussian Structure in Bosonic States"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.06810"
url: "http://arxiv.org/abs/2610.06810v1"
published: "2026-10-05T17:54:36Z"
ingested: "2026-10-06T12:42:28Z"
authors:
  - "Alvan Arulandu"
  - "Sitan Chen"
  - "Ziyun Chen"
  - "Jerry Li"
  - "Eric Ma"
---

# Finding Gaussian Structure in Bosonic States

## Abstract

> We study agnostic tomography of pure bosonic Gaussian states: given copies of an arbitrary
> $n$-mode bosonic state $ρ$, the goal is to output a pure Gaussian state whose infidelity with
> $ρ$ is at most $\mathrm{opt} + ε$, where $\mathrm{opt}$ is the minimum infidelity achievable by
> any pure Gaussian state. We give efficient protocols achieving this in both the high and low
> fidelity regimes. When $\mathrm{opt}$ is below some universal constant, our protocol has runtime
> and copy complexity which is strongly polynomial in $n, 1/ε$ and $\log \log E$, where $E$ is the
> energy of the closest pure Gaussian state. For arbitrary $\mathrm{opt}$, our protocol uses
> $(n+1)^{\mathrm{poly}(1/ε)} \mathrm{poly}\left(1+\log\log(E)\right)$ copies and runtime. As a
> corollary, we obtain the first truly tolerant Gaussianity testing protocol for distinguishing
> whether $\mathrm{opt} > c + ε$ or $\mathrm{opt} < c - ε$, for any threshold $c\in(0,1)$. We also
> prove $\mathrm{poly}(n,1/ε)$ runtime is impossible, unless $\mathrm{NP}\subseteq\mathrm{BQP}$.
> Our protocols follow a shared paradigm: first, we iteratively use general Gaussian measurements
> combined with techniques from classical robust statistics to obtain a good warm start estimate,
> then we leverage non-Gaussian measurements to refine this warm start using convex and non-convex
> optimization methods. Interestingly, we prove that non-Gaussian measurements are necessary to
> match the strong agnostic guarantees we obtain, and in fact these guarantees are provably
> superior to what is possible for robustly estimating classical Gaussians.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

