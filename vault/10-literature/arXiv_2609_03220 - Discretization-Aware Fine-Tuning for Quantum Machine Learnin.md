---
aliases: ["Discretization-Aware Fine-Tuning for Quantum Machine Learning with Chemical Foundation Models"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.03220"
url: "http://arxiv.org/abs/2609.03220v1"
published: "2026-09-02T23:36:29Z"
ingested: "2026-09-04T10:31:30Z"
authors:
  - "Shunji Matsuura"
  - "Sonika Johri"
---

# Discretization-Aware Fine-Tuning for Quantum Machine Learning with Chemical Foundation Models

## Abstract

> A key challenge in practical quantum machine learning (QML), particularly for discriminative
> tasks such as classification, is the limited capacity of near-term quantum devices to encode
> high-dimensional classical data into small quantum registers. In optimized basis-encoded (bit-
> bit) settings, this constraint leads to cross-class collisions, where samples with different
> labels are mapped to the same discrete bit-string and thus become indistinguishable to any
> downstream model. In this work, we investigate how data representation affects QML performance
> under such severe information bottlenecks. We introduce discretization-aware fine-tuning (DAFT),
> a method that adapts a pre-trained chemical foundation model to produce representations that
> remain informative after quantization. DAFT reduces collision probability through a
> differentiable soft collision loss. We evaluate both quantum and classical models under a
> controlled setting in which they receive identical discretized bit-string inputs, isolating the
> effect of representation from model architecture. On the blood-brain barrier penetration (BBBP)
> molecular property prediction benchmark using ChemBERTa-77M, DAFT reduces collision counts by
> several orders of magnitude and improves quantum classification accuracy by more than 12
> percentage points compared to a frozen backbone. Importantly, without DAFT, classical models
> outperform QML under the same input constraints. With DAFT, however, this comparison reverses at
> higher qubit counts. At 10 qubits, the quantum model surpasses a matched classical baseline
> trained on identical bit-strings (0.883 vs. 0.855, $p = 0.026$). These results show that, in
> information-constrained regimes, achieving a quantum advantage critically depends on aligning
> continuous representations with discrete quantum encodings.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

