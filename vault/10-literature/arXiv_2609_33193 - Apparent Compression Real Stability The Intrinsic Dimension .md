---
aliases: ["Apparent Compression, Real Stability: The Intrinsic Dimension of Learning a Quantum Wavefunction"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.33193"
url: "http://arxiv.org/abs/2609.33193v1"
published: "2026-09-27T04:19:21Z"
ingested: "2026-09-29T12:04:08Z"
authors:
  - "Lu Wei"
  - "Yufeng Wang"
  - "Chenfeng Cao"
  - "Haibin Ling"
---

# Apparent Compression, Real Stability: The Intrinsic Dimension of Learning a Quantum Wavefunction

## Abstract

> How many directions in weight space does training need? The intrinsic dimension answers this
> with the smallest number of random directions in which training still reaches a target accuracy,
> and small values have motivated parameter-efficient methods such as LoRA. We measure it for
> variational Monte Carlo (VMC), which trains a neural network to represent the ground state of a
> quantum many-body system. VMC is a demanding test, because the network generates its own
> training samples and every gradient is noisy, and a revealing one, because the exact answer is
> known and every run can be scored. We train only a small latent vector that a frozen random map
> turns into the network's weights, with no change to the standard natural-gradient optimizer. We
> find that a small dimension can be misleading, while the stability it brings is real. On a
> magnet with a hard sign pattern, a network that cannot represent signs reaches its best energy
> in 8 of 28,642 directions, but only because no such network can go lower; once signs are
> learnable, neither the signs nor the magnitudes are cheap. The dimension rises across a quantum
> phase transition, so it tracks how difficult a state is at far less compute than fitting a
> scaling law, yet it never falls below a floor set by the random subspace itself, even where the
> ground state is nearly trivial. Training in the subspace, in contrast, never diverged in our
> experiments, whereas full-parameter training with the same settings did, and a control with
> matched solvers attributes the difference to the reduced dimension.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

