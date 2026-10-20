---
aliases: ["Prototype-Guided Optimization of Quantum Data Embeddings with Linear Cost"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.24403"
url: "http://arxiv.org/abs/2610.24403v1"
published: "2026-10-17T03:13:05Z"
ingested: "2026-10-20T10:53:29Z"
authors:
  - "Seokhoon Jeong"
  - "Daniel K. Park"
---

# Prototype-Guided Optimization of Quantum Data Embeddings with Linear Cost

## Abstract

> In supervised quantum machine learning with classical data, classification performance
> critically depends on the geometry induced by quantum data embedding. Existing data-adaptive
> approaches rely on pairwise fidelity evaluations between samples, which scale as $O(B^2)$ for
> $B$ samples and create a computational bottleneck in iterative embedding optimization. To
> address this issue, we propose a prototype-guided framework for efficient data-adaptive quantum
> embedding. Using class-prototype separation and sample-to-prototype compactness, we derive a
> measurable lower certificate for class-ensemble distinguishability and construct a prototype-
> based objective requiring only $O(B)$ fidelity evaluations. We integrate this objective into an
> end-to-end pipeline that combines task-specific quantum circuit architecture optimization with
> continuous refinement of the data-embedding parameters. Across five benchmark datasets with up
> to 20 qubits, our method retains competitive quantum kernel support vector machine (SVM)
> performance while reducing fidelity-evaluation cost, with particularly strong gains over budget-
> matched pairwise optimization on T-MNIST. Geometric analyses examine how the learned embeddings
> relate to kernel alignment and classification margins, revealing dataset-dependent benefits and
> limitations. We further derive a prototype-based classifier in the reproducing kernel Hilbert
> space that provides an explicit witness for the SVM objective and a low-cost proxy for model
> selection, and extend the framework to multiple prototypes for multimodal class structures.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

