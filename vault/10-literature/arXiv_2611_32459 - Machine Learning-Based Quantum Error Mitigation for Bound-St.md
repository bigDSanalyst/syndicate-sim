---
aliases: ["Machine Learning-Based Quantum Error Mitigation for Bound-State Simulations"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.32459"
url: "http://arxiv.org/abs/2611.32459v1"
published: "2026-11-24T11:53:18Z"
ingested: "2026-11-25T16:44:39Z"
authors:
  - "Sumit Choudhary"
  - "Tarunpreet Kaur"
  - "Harjeet Kaur"
  - "Harpreet Singh"
---

# Machine Learning-Based Quantum Error Mitigation for Bound-State Simulations

## Abstract

> Noise in quantum devices remains a major challenge for reliable quantum simulations, making
> quantum error mitigation an important tool for improving their accuracy. Machine learning-based
> quantum error mitigation (ML-QEM) provides a useful approach, but its performance depends on the
> training datasets and may produce reconstructed quantum states that are not physically valid. In
> this work, we introduce an ML-QEM framework that uses residual learning with convex projection
> to ensure that reconstructed density matrices satisfy physically valid density matrices. We
> study the effect of different training datasets and regression models using Haar-random and
> variational quantum eigensolver (VQE) ansatz states. We compare the proposed approach with
> conventional ML-QEM, readout error mitigation, and zero-noise extrapolation. The method is
> tested on IBM quantum hardware for three- and four-qubit simulations of the bound $Λ$-deuteron
> and $Λ$-$α$ hypernuclear systems, respectively. For the three-qubit system, ridge regression
> trained on VQE-ansatz states gives a ground-state energy of -0.134 MeV, close to the ideal value
> of -0.135 MeV, with a state fidelity of 0.999. For four-qubit system, kernel ridge regression
> gives ground-state energies of -3.014 and -3.045 MeV, with corresponding state fidelities of
> 0.995 and 0.998. These results show that physically constrained reconstruction, along with the
> choice of training datasets and regression models, can improve ML-QEM performance for the
> quantum simulations studied in this work.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

