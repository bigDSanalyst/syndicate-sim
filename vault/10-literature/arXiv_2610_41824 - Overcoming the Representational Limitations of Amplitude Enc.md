---
aliases: ["Overcoming the Representational Limitations of Amplitude Encoding for Quantum Neural Networks"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.41824"
url: "http://arxiv.org/abs/2610.41824v1"
published: "2026-10-30T14:44:49Z"
ingested: "2026-11-02T14:41:37Z"
authors:
  - "Vincent Gurgul"
  - "David Prinz"
---

# Overcoming the Representational Limitations of Amplitude Encoding for Quantum Neural Networks

## Abstract

> Quantum Neural Networks (QNNs) offer a framework for learning functions from classical data, but
> their expressive power depends critically on how inputs are encoded into quantum states. Angle
> encoding can require resources that scale with the number of features, whereas amplitude
> encoding represents $d$ features using only $\mathcal{O}(\log_2 d)$ qubits. This compactness
> comes at a representational cost: normalization makes conventional amplitude encoding invariant
> to nonzero real rescaling of the input, up to an unobservable global phase. We show that this
> invariance induces an exact, architecture-independent restriction on the resulting hypothesis
> class. No downstream quantum circuit can distinguish inputs differing by nonzero real scaling.
> We develop a general condition under which deterministic preprocessing can remove this ambiguity
> and show that nonlinearity alone is insufficient. Based on this analysis, we introduce a fixed
> nonlinear feature map that provably distinguishes all real inputs under subsequent amplitude
> encoding, without adding trainable parameters and while retaining logarithmic qubit scaling. We
> evaluate the resulting QNN on three canonical classification benchmarks and a nonlinear
> synthetic dataset against conventional amplitude and angle encoding, as well as a classical
> neural network. Across these tasks, the proposed encoding consistently improves classification
> accuracy over both quantum encoding baselines by 21$-$44 %. Our results establish normalization-
> induced scale invariance as a concrete representational bottleneck of amplitude encoding and
> demonstrate that it can be removed while preserving a compact quantum representation, marking a
> step toward quantum models capable of capturing arbitrary relationships in classical data.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

