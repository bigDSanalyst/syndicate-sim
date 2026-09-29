---
aliases: ["Simulation-Based Quantum System Inference with Neural Posterior Estimation"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.34995"
url: "http://arxiv.org/abs/2609.34995v1"
published: "2026-09-28T12:04:15Z"
ingested: "2026-09-29T12:04:08Z"
authors:
  - "Hang Zou"
  - "Anton Frisk Kockum"
  - "Martin Rahm"
  - "Simon Olsson"
---

# Simulation-Based Quantum System Inference with Neural Posterior Estimation

## Abstract

> Models of quantum systems faithfully map system parameters to observations, but the inverse
> problem of parameter inference from measurement data presents a fundamental challenge:
> computationally intractable likelihoods due to an exponentially large Hilbert space. Here, we
> introduce simulation-based quantum system inference, a unified, likelihood-free framework that
> learns parameter posteriors directly from classical simulation data. The central idea is to pair
> polynomial-cost classical simulators, such as Pauli propagation and tensor networks, with
> normalizing flows or other neural density estimators for accurate, reusable inference. A single
> model, trained once, maps any new measurement record to its posterior in one forward pass---
> turning per-experiment inference into a fixed, up-front cost. We numerically demonstrate the
> framework's versatility across Pauli noise learning, quantum error mitigation, quantum state
> tomography, and Hamiltonian learning, with examples involving 81-qubit shallow circuits and
> 735-parameter inference. In each case, the approach yields accurate estimates of identifiable
> parameters, while posterior uncertainty provides additional diagnostics of non-identifiability
> and indicates where further characterization is needed. Our framework reduces data-acquisition
> requirements in quantum experiments and accelerates parameter inference, providing a practical
> route to characterizing and improving large-scale quantum systems.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

