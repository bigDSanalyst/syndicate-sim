---
aliases: ["Balancing Expressivity and Overfitting in Quantum Gaussian Process Regression"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.09407"
url: "http://arxiv.org/abs/2609.09407v1"
published: "2026-09-08T20:01:22Z"
ingested: "2026-09-10T10:32:22Z"
authors:
  - "Saasha Joshi"
  - "Udson C. Mendes"
  - "Luke C. G. Govia"
---

# Balancing Expressivity and Overfitting in Quantum Gaussian Process Regression

## Abstract

> Active learning is a paradigm of machine learning that can be utilized to model expensive black-
> box functions by training a surrogate model from actively queried training points. The
> performance of this framework depends heavily on the choice of the surrogate model. When the
> surrogate is Gaussian Process Regression (GPR), its performance is largely determined by the
> expressivity of the underlying kernel. In this work, we investigate the peculiarities of using a
> quantum kernel to change the computational dynamics of active learning with GPR, focusing on the
> sensitivity to regularization by hyperparameter tuning. While generic, unstructured kernels
> suffer from exponential concentration at large scale, we empirically demonstrate that even at
> small scale overfitting can collapse GPR performance. Kernel regularization can be used to
> counteract this effect, but due to the smoothness of the quantum fidelity kernel, regularization
> must be carefully chosen to balance expressivity and overfitting. Our qualitative results
> transfer to the practical application of restricted quantum kernels designed to avoid
> exponential concentration and also present the kinds of noise that may be valuable to kernel
> training in near-term quantum devices.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

