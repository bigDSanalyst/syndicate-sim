---
aliases: ["Spectral Quantum Memory for Implicit Neural Representations"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.04574"
url: "http://arxiv.org/abs/2611.04574v1"
published: "2026-11-03T09:35:50Z"
ingested: "2026-11-04T13:43:35Z"
authors:
  - "Daniel A. Moroz-Broitman"
  - "Eliya Nachmani"
---

# Spectral Quantum Memory for Implicit Neural Representations

## Abstract

> Implicit neural representations (INRs) model signals as continuous functions from coordinates to
> values, but their performance depends strongly on how spectral capacity is allocated. Yet most
> Quantum INR (QINR) architectures treat spectral components as independent outputs of separate
> quantum blocks. We introduce the Spectral Quantum Memory Model (SQMM), a memory coupled quantum
> INR in which sequential hybrid data reuploading layers (bands) communicate through a shared
> coherent quantum memory register. Each band reads the memory, computes on its own coordinate
> upload, and writes part of its state back, so later bands can build on the computation of
> earlier ones. When memory read and write layers are input independent, we prove that the memory
> state forms an operator valued Fourier series whose support is contained in the Minkowski sum of
> the initial memory spectrum and the local band spectra. Downstream bands then condition their
> Fourier coefficients on the spectral content stored by earlier bands, and the memory coupling
> creates no new primitive frequencies. This theory motivates a spectral memory alignment loss
> that encourages memory to encode the spectrum expressed by the deployed prefix of the model.
> Across audio and image reconstruction benchmarks, SQMM improves over compact QINR and INR
> baselines.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

