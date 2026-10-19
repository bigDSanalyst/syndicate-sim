---
aliases: ["Quantum-Classical Neural Networks for Solving Lindblad Master Equations"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.22691"
url: "http://arxiv.org/abs/2610.22691v1"
published: "2026-10-15T21:59:04Z"
ingested: "2026-10-19T12:01:38Z"
authors:
  - "Rafael Florencio Díaz"
  - "Julio Guerrero García"
  - "Elvira Romera Gutiérrez"
---

# Quantum-Classical Neural Networks for Solving Lindblad Master Equations

## Abstract

> Variational quantum algorithms have emerged as a promising approach for simulating open quantum
> systems, yet their expressive power and trainability remain poorly understood. We propose a
> variational framework for solving Lindblad master equations by minimizing a residual cost
> function using a compositional ansatz obtained by combining a classical neural network with a
> parameterized quantum circuit. The density matrix is represented through a purification on an
> enlarged Hilbert space, ensuring positivity, Hermiticity, and unit trace by construction, while
> all gradients are evaluated exactly via the parameter-shift rule. Beyond the algorithmic
> formulation, we derive an upper bound for the covering number of the proposed compositional
> model and compare it with that of purely quantum neural networks. Our analysis shows that the
> classical parametrization enlarges the effective hypothesis class while providing finer control
> over its complexity, thereby establishing a theoretical connection between expressivity,
> covering numbers, effective dimension, and the barren plateau phenomenon. Numerical experiments
> validate both the accuracy of the proposed method for representative Lindblad master equations
> and the theoretical predictions regarding gradient concentration. These results provide a
> unified variational and theoretical framework for the simulation of dissipative quantum dynamics
> using compositional quantum machine learning models.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

