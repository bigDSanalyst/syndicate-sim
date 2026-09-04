---
aliases: ["Quantum Hamiltonian Evolution for Coherent Quantum Learning"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.03640"
url: "http://arxiv.org/abs/2609.03640v1"
published: "2026-09-03T10:41:23Z"
ingested: "2026-09-04T10:31:30Z"
authors:
  - "Ignacio B. Acedo"
  - "Javier Gonzalez-Conde"
  - "Pablo Rodriguez-Grasa"
  - "Barry C. Sanders"
  - "Lirandë Pira"
---

# Quantum Hamiltonian Evolution for Coherent Quantum Learning

## Abstract

> We introduce Coherent Quantum Learning (CQL), a training framework for quantum learning models
> in which the model parameters are quantum degrees of freedom evolved under a Hamiltonian that
> encodes the loss function. Current quantum machine learning retains classical optimization:
> parameters are updated by a classical outer loop using gradient estimates from measurements, and
> quantum coherence has no role in the training dynamics, just as in any classical treatment of
> the same problem. In the quantum case, a parameter register initialized in superposition evolves
> unitarily, and probability amplitude concentrates near low-loss configurations through
> interference, without gradient computation or classical feedback. We give an explicit
> construction using block encodings and Hamiltonian simulation, applicable to arbitrary
> parameterized circuits. Numerical experiments on binary classification and interferometric phase
> estimation confirm that the evolved distribution peaks at the optimal parameters, matching
> gradient-based performance. The construction is compatible in principle with fault-tolerant
> implementations and extends to batched training via sequential Hamiltonian evolution.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

