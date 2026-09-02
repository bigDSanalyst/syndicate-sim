---
aliases: ["Fractal dimension predicts quantum kernel collapse in angle-encoded data"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.00475"
url: "http://arxiv.org/abs/2609.00475v1"
published: "2026-08-31T23:25:19Z"
ingested: "2026-09-02T10:33:37Z"
authors:
  - "Ana Paula Appel"
---

# Fractal dimension predicts quantum kernel collapse in angle-encoded data

## Abstract

> Angle-encoded quantum kernels on tabular data collapse when the feature map is wider than the
> intrinsic dimension of the data. We propose the correlation fractal dimension D2 as an a priori
> qubit budget: encode D2 coordinates chosen by FD-ASE instead of the PCA-95% width or all E
> attributes. On nine data sets and a statevector simulator (n= 32), a one-layer ZZ fidelity
> kernel at q=D2 stays geometrically alive while the same kernel at the PCA-95% width has already
> collapsed. The budget is map-dependent: product-state and IQP maps overshoot it; a second ZZ
> layer undershoots it. Packed dense-angle and re-uploading encodings still live at the fractal q,
> but not when PCA-95% features are stacked onto those qubits. Shrinking the angle bandwidth moves
> the ZZ knee later; stretching it kills the kernel earlier. On IBM Quantum (ibm_fez, 256 shots,
> n=8) the one-layer ZZ kernel at the fractal width matches the exact kernel (MAE 0.021); past
> that width both hardware and simulator have collapsed. The ceiling is a property of the map-data
> pair at a stated bandwidth, not of the classical table alone.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

