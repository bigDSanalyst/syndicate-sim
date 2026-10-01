---
aliases: ["Does the Readout Bypass Leak the Input? A Feature-Visibility Audit of Hybrid Quantum-Classical Models"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.38720"
url: "http://arxiv.org/abs/2609.38720v1"
published: "2026-09-30T00:54:03Z"
ingested: "2026-10-01T12:22:27Z"
authors:
  - "Guilin Zhang"
  - "Kai Zhao"
  - "Xiquan Cui"
  - "Henry Heng"
  - "Xu Chu"
  - "Aletta Johanna Blanken"
---

# Does the Readout Bypass Leak the Input? A Feature-Visibility Audit of Hybrid Quantum-Classical Models

## Abstract

> Readout-side residual hybrids concatenate raw inputs with measured quantum features. Under
> single-example gradient sharing, a biased first linear layer admits standard analytic recovery
> of its input, so the bypass exposes raw coordinates without requiring inversion of the quantum
> circuit. We audit this mechanism using two tabular datasets, four architectures, and metrics
> conditioned on feature visibility. Iterative gradient matching gives median full-record PSNR of
> 73-96 dB for residual and input-only heads. Quantum-only heads score 8-11 dB on the full record
> but 54-96 dB on the six input coordinates they actually encode. These are reconstruction results
> for the tested six-input, six-observable circuits, not a general statement about quantum
> encodings. A loss-threshold membership attack remains near chance. The contribution is a
> visibility-conditioned privacy audit: omitted coordinates must not be credited as protection
> supplied by quantum processing, and near-exact PSNR differences must not be interpreted as
> meaningful privacy rankings. Our findings concern individual gradients and do not establish
> leakage under aggregation or multiple local training steps.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

