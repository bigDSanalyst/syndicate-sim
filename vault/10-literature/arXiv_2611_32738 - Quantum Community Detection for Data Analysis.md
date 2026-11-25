---
aliases: ["Quantum Community Detection for Data Analysis"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.32738"
url: "http://arxiv.org/abs/2611.32738v1"
published: "2026-11-24T14:53:29Z"
ingested: "2026-11-25T16:44:39Z"
authors:
  - "Vicente P. Soloviev"
  - "Brian Coyle"
  - "Stefano Scali"
  - "Michal Krompiec"
---

# Quantum Community Detection for Data Analysis

## Abstract

> Community detection offers an alternative to conventional methods for data analysis tasks such
> as feature selection and clustering, and detecting communities with quantum algorithms is a
> promising avenue for quantum speedup. We investigate quantum spectral community detectors, such
> as the modularity-matrix algorithm deteQt, in pipelines for both tasks. We first generalise
> deteQt to multiple communities by recursive bisection, and show that it recovers planted
> communities, and hence redundant features, in synthetic and small datasets. We then propose
> projeQt, which applies a spectral filter to the encoded modularity matrix through the quantum
> singular value transformation, retaining higher-order eigenvectors that deteQt does not use.
> projeQt acts on the generalised modularity matrix and extracts several communities at once,
> without recursion, by k-means clustering of a Gram matrix built from quantum state overlaps. On
> MNIST we demonstrate both pipelines, selecting informative pixels and classifying images
> directly by clustering, and find them competitive with standard community detectors.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

