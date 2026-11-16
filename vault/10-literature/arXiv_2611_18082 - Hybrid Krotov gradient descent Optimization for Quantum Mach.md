---
aliases: ["Hybrid Krotov gradient descent Optimization for Quantum Machine Learning"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.18082"
url: "http://arxiv.org/abs/2611.18082v1"
published: "2026-11-13T12:06:04Z"
ingested: "2026-11-16T14:40:17Z"
authors:
  - "Maximilian Fröhlich"
  - "Martin Eigel"
  - "Michael Hintermüller"
---

# Hybrid Krotov gradient descent Optimization for Quantum Machine Learning

## Abstract

> We introduce and study a Krotov-inspired discrete adjoint optimization scheme for quantum
> machine learning and focus on a hybrid online-to-batch schedule. The method transfers the
> forward/costate/local-update logic of continuous-time optimal control to parameterized quantum
> circuits by replacing time locality with gate-index locality. For a broad class of fixed-
> generator variational gates and terminal-state losses, we show that the batch Krotov direction
> coincides with the exact gradient of the empirical loss. Under standard smoothness assumptions,
> this yields monotonic descent and convergence of the batch method, and convergence of the tail
> of the hybrid method after a finite switch to the batch phase. Empirically, we benchmark hybrid
> Krotov against the tuned PennyLane optimizer suite and L-BFGS-B on a four-bit parity classifier
> and on the Pérez-Salinas data re-uploading classifier for the crown problem. Across matched
> hyperparameter sweeps with three seeds per configuration, hybrid Krotov dominates every tuned
> first-order baseline and matches the strongest structured PennyLane methods on parity, while
> approaching the accuracy of L-BFGS-B on Pérez-Salinas at first-order per-iteration cost.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

