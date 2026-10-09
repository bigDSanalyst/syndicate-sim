---
aliases: ["An Efficient Quantum Circuit for Flow Model Execution Using Quantum Neural Networks"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.11537"
url: "http://arxiv.org/abs/2610.11537v1"
published: "2026-10-08T09:07:01Z"
ingested: "2026-10-09T12:31:33Z"
authors:
  - "Rui Che"
  - "Ludvig af Klinteberg"
---

# An Efficient Quantum Circuit for Flow Model Execution Using Quantum Neural Networks

## Abstract

> Flow models generate trajectories from an initial distribution to a target distribution by
> solving an ordinary differential equation defined by a velocity field. Flow matching learns this
> velocity field by modeling the transport dynamics between the two distributions. Wavefunction
> flow establishes a formal connection between flow models and quantum dynamics by introducing a
> continuity Hamiltonian, which drives the Schrödinger evolution of quantum states. In this paper,
> we investigate accurate and efficient quantum simulation of the wavefunction flow, thereby
> realizing the efficient implementation of flow models on quantum computers. We first leverage a
> quantum read-only memory (QROM)-based phase kickback framework for the wavefunction flow
> simulation, generating probability densities that closely match those produced by the
> corresponding conventional flow model. To address the high circuit-resource cost, we further
> incorporate a trained quantum neural network (QNN) into the phase kickback framework, replacing
> QROM for data encoding. Numerical experiments demonstrate that our proposed method implements
> flow models on quantum computers more efficiently, since it maintains the accuracy of
> wavefunction flow simulation compared with the QROM-based framework, and significantly reduces
> the circuit resources.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

