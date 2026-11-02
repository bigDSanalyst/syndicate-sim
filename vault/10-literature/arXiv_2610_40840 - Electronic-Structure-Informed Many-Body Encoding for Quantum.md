---
aliases: ["Electronic-Structure-Informed Many-Body Encoding for Quantum Machine Learning"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.40840"
url: "http://arxiv.org/abs/2610.40840v1"
published: "2026-10-29T18:19:44Z"
ingested: "2026-11-02T14:41:37Z"
authors:
  - "Liangnuo Zhang"
  - "Tanner Culpitt"
  - "Qiwei Yin"
  - "Linghua Zhu"
  - "Xiaosong Li"
---

# Electronic-Structure-Informed Many-Body Encoding for Quantum Machine Learning

## Abstract

> Data encoding is a central challenge in quantum machine learning (QML), as it determines how
> classical information is mapped onto quantum states and influences the expressive power and
> efficiency of parameterized quantum circuits. Here, we introduce a physics-informed quantum
> encoding strategy that exploits the intrinsic many-body structure of electronic systems to
> establish a direct correspondence between the body order of input descriptors and the locality
> of quantum gates. Specifically, $n$-body electronic descriptors obtained from a single mean-
> field electronic-structure calculation are encoded through $n$-qubit gates, yielding a
> systematic hierarchy of quantum circuits with increasing many-body expressivity. Using reduced-
> density-matrix descriptors, we construct quantum machine-learning models incorporating one-
> through four-body encodings and benchmark their performance in predicting electron-correlation
> energies along bond-stretching potential energy surfaces. We demonstrate that increasing the
> body order of the encoding systematically improves prediction accuracy toward the full
> configuration interaction limit. Remarkably, disconnected many-particle densities constructed
> from lower-order electronic information achieve accuracy comparable to explicitly correlated
> two-particle densities in key cases, providing a computationally inexpensive route to higher-
> body quantum encodings. These findings establish a connection between the many-body structure of
> classical data and the design of quantum feature maps, offering a systematic, physically
> interpretable framework for enhancing the expressivity and predictive performance of quantum
> machine-learning circuits.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

