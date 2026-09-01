---
aliases: ["Hardware-Efficient Exchange-Only QML: Singlet-Triplet Spin Chains via Inter-pair Coupling without Magnetic Gradients"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2608.29017"
url: "http://arxiv.org/abs/2608.29017v1"
published: "2026-08-29T03:13:07Z"
ingested: "2026-09-01T11:02:33Z"
authors:
  - "Yuichiro Minato"
---

# Hardware-Efficient Exchange-Only QML: Singlet-Triplet Spin Chains via Inter-pair Coupling without Magnetic Gradients

## Abstract

> Standard universal quantum computing using exchange-only qubits typically requires three
> physical spins per logical qubit, leading to significant hardware overhead. Conversely, two-spin
> units offer higher density but rely on local magnetic field gradients for control, increasing
> integration complexity. In this paper, we propose a resource-efficient quantum machine learning
> (QML) architecture that achieves high expressibility using minimal two-spin units and Heisenberg
> exchange interactions alone, without any magnetic gradients. We shift the paradigm from
> universal gate-based control to utilizing the intrinsic, time-domain dynamics of a spin chain as
> a learning resource. Numerical simulations on MNIST digit classification demonstrate that the
> symmetry-protected constraints of isolated spin pairs are bypassed by leveraging inter-pair
> exchange coupling. This interference-mediated state mixing significantly enhances the
> expressibility of the Hilbert space. The model reaches a test-set accuracy of 90.9% +/- 0.2%
> over five independent seeds on the full 10,000-image MNIST test set. Under an identical linear
> readout, the trained quantum feature map (88.1%) clearly outperforms a classical linear baseline
> on the same PCA inputs (83.2%) as well as an untrained (reservoir-style) version of the same
> dynamics (53.0%), demonstrating that the learned, input-dependent exchange pulses implement a
> genuinely non-linear and trainable feature map. The protocol is also robust to experimentally
> relevant imperfections: accuracy remains at 89.9% under 10% quasi-static pulse-area noise and at
> 89.8% when every observable is estimated from 10^3 measurement shots. These findings suggest
> that competitive QML can be executed on the simplest possible semiconductor spin-chain hardware,
> bypassing the need for leakage-prone encodings or complex micro-magnet integration.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

