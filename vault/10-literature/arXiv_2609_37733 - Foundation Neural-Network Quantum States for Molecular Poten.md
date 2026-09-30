---
aliases: ["Foundation Neural-Network Quantum States for Molecular Potential Energy Surfaces in Second Quantization"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.37733"
url: "http://arxiv.org/abs/2609.37733v1"
published: "2026-09-29T14:54:07Z"
ingested: "2026-09-30T11:52:15Z"
authors:
  - "Lizhong Fu"
  - "Jianan Wei"
  - "Wenguan Wang"
  - "Honghui Shang"
---

# Foundation Neural-Network Quantum States for Molecular Potential Energy Surfaces in Second Quantization

## Abstract

> Second-quantized neural-network quantum states have achieved accurate molecular energies, but
> extending them across molecular geometries requires a shared representation of the geometry-
> dependent wavefunction coefficients. We introduce geometry-conditioned foundation neural-network
> quantum states for molecular electronic structure in second quantization. A single
> autoregressive model learns a family of ground states from sparse anchor geometries and provides
> wavefunctions at untrained geometries without further optimization. Orbital alignment matches
> orbital identities and transports their phases, establishing an aligned orbital basis across
> geometries. Frozen energies reach chemical accuracy at every untrained query geometry for N$_2$,
> CO, and H$_4$. On additional molecular paths, the energy-trained wavefunctions yield dipoles,
> quadrupoles, and natural occupations without property labels. Across three paired N$_2$ training
> seeds, orbital alignment lowers the mean absolute energy error over all untrained query
> geometries from 34-37 mHa to 0.049-0.085 mHa. At approximately 1 mHa mean absolute error, frozen
> evaluation reduces the per-geometry cost by $986\times$ relative to independent optimization,
> yielding an estimated $25.8\times$ end-to-end GPU-cost reduction on a 161-point N$_2$ grid.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

