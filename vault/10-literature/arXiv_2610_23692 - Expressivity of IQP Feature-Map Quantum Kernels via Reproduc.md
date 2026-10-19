---
aliases: ["Expressivity of IQP Feature-Map Quantum Kernels via Reproducing Kernel Hilbert Spaces"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.23692"
url: "http://arxiv.org/abs/2610.23692v1"
published: "2026-10-16T16:20:46Z"
ingested: "2026-10-19T12:01:38Z"
authors:
  - "Valeria Repetto"
  - "Stefano Melchionna"
  - "Romina D'Aurizio"
---

# Expressivity of IQP Feature-Map Quantum Kernels via Reproducing Kernel Hilbert Spaces

## Abstract

> Quantum kernels are among the most promising methods in quantum machine learning, providing a
> natural way to embed data into high-dimensional Hilbert spaces via quantum circuits and
> capturing non-linear relationships in data. Their learning behaviour is governed by the function
> class they represent, which is formally characterized by the structure of the associated
> Reproducing Kernel Hilbert Space (RKHS). However, a theoretical characterization of this
> function class, and of how it depends on the choice of feature map and its hyperparameters, is
> still lacking. In this work, we focus on the Instantaneous Quantum Polynomial (IQP) feature map
> and derive a Fourier representation of the associated RKHS generators as finite sums of
> trigonometric functions evaluated on polynomially transformed input variables, with a finite set
> of accessible frequencies determined by the circuit construction and scaled by the bandwidth
> hyperparameter. This representation identifies three bandwidth regimes with qualitatively
> distinct expressive properties from localised, through multimodal, to periodic. Numerical
> experiments on synthetic datasets with controlled periodic and multimodal structure, across data
> dimensions and feature-map configurations, reproduce the three regimes in both supervised
> classification and unsupervised anomaly detection, benchmarked against a classical Gaussian
> kernel. These results make the relationship between expressivity and data structure explicit for
> IQP kernels: expressive power translates into a practical benefit only when the accessible
> frequencies match with the structure of the data, which provides a criterion for selecting the
> bandwidth when the periodic or multimodal structure of data is known.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

