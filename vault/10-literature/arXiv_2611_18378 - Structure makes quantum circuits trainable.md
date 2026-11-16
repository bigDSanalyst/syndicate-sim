---
aliases: ["Structure makes quantum circuits trainable"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.18378"
url: "http://arxiv.org/abs/2611.18378v1"
published: "2026-11-13T16:22:31Z"
ingested: "2026-11-16T14:40:17Z"
authors:
  - "Wenbo Xie"
  - "Wojciech Szpankowski"
  - "Ananth Grama"
---

# Structure makes quantum circuits trainable

## Abstract

> The scalability of variational quantum algorithms is limited by barren plateaus, where gradients
> vanish exponentially in system size. This worst-case result raises fundamental questions about
> the trainability of quantum AI models. We present a major advance towards resolving this
> trainability question by answering whether a given quantum circuit has a barren plateau. We do
> this using an analytical framework that bounds the gradient variance for arbitrary input states
> $ρ$ and observables $\mathcal{M}$ by decomposing the unitary representation of the associated
> compact Lie group. When the circuit segments on both sides of a gate form $2$-designs, we obtain
> the variance exactly and prove a sufficient condition for trainability: if $ρ^{\otimes 2}$ and
> $\mathcal{M}^{\otimes 2}$ are sufficiently concentrated on the same irreducible invariant
> subspace of polynomial dimension, and the differentiated gate moves this subspace by an inverse-
> polynomial amount, then the gradient variance is at least inverse-polynomial. We further present
> a sampling algorithm that estimates the gradient variance from runs of the ansatz, without
> constructing the representation-theoretic projectors. Our algorithm decides whether the variance
> exceeds a tolerance $τ$ with the number of runs polynomial in $1/τ$, including cases in which
> the bounds are inconclusive. This resolves the question of the trainability of the circuit
> before expensive training procedures.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

