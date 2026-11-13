---
aliases: ["TGen-SQD: Physics-Informed Transferable Configuration Generator for Sample-Based Quantum Diagonalization"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.16080"
url: "http://arxiv.org/abs/2611.16080v1"
published: "2026-11-11T22:45:06Z"
ingested: "2026-11-13T13:52:45Z"
authors:
  - "Niloy Deb Roy Mishu"
  - "Lei Jiang"
  - "Mohsen Heidari"
  - "Ruizhe Zhang"
  - "Fan Chen"
---

# TGen-SQD: Physics-Informed Transferable Configuration Generator for Sample-Based Quantum Diagonalization

## Abstract

> Sample-based quantum diagonalization (SQD) avoids iterative variational circuit optimization,
> but its accuracy and cost depend on selecting a compact determinant subspace that captures the
> ground state. Existing machine-learning selectors use task-specific physical cues and typically
> retrain for each Hamiltonian. We introduce TGen-SQD, a physics-informed generator jointly
> trained across multiple Hamiltonians. It learns from configuration-interaction-weighted data and
> uses orbital- and system-level descriptors to guide generation. After training, its weights
> remain frozen for inference on seen and zero-shot geometries. On a 20-qubit H10 chain, TGen-SQD
> achieves mean energy errors of 40.18 +/- 1.52 and 43.97 +/- 1.20 mHa on seen and unseen
> geometries, respectively, 12.7% and 11.7% lower than the state-of-the-art PIGen-SQD baseline
> under matched shot and proposal budgets.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

