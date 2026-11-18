---
aliases: ["Charge self-consistent DFT+QDMFT framework with a Krylov-based quantum impurity solver"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.21829"
url: "http://arxiv.org/abs/2611.21829v1"
published: "2026-11-16T19:50:09Z"
ingested: "2026-11-18T15:01:54Z"
authors:
  - "M. Karabin"
  - "T. Sohail"
  - "E. A. Coello Pérez"
  - "S. Ghosh"
  - "M. Sajjan"
  - "H. Terletska"
  - "M. Eisenbach"
---

# Charge self-consistent DFT+QDMFT framework with a Krylov-based quantum impurity solver

## Abstract

> We integrate a quantum impurity solver into a charge self-consistent density functional theory
> (DFT) plus quantum dynamical mean-field theory framework. The solver optimizes adaptive circuits
> to approximate the ground state of the impurity model and its particle and hole excitations, and
> reconstructs the impurity Green's function from their Hamiltonian moments. Higher-order moments
> are predicted from low-order ones using a machine-learning model, while regularized optimization
> mitigates violations of causality in the resulting self-energy. The latter is used to update the
> charge density until self-consistency is achieved. We demonstrate the framework through body-
> centered cubic lithium calculations and compare the results with a reference one using a
> continuous-time quantum Monte Carlo solver. These calculations converge with root-mean-square
> charge-density residuals below $\boldsymbol{2\times10^{-3}}$ and yield a nearly vanishing
> impurity self-energy, consistent with the noninteracting limit used for weakly correlated
> lithium.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

