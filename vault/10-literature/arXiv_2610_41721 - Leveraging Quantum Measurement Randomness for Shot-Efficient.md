---
aliases: ["Leveraging Quantum Measurement Randomness for Shot-Efficient Diffusion Models"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.41721"
url: "http://arxiv.org/abs/2610.41721v1"
published: "2026-10-30T13:31:33Z"
ingested: "2026-11-02T14:41:37Z"
authors:
  - "Tianhao Guo"
  - "Dianxin Zheng"
  - "Yuhua Qian"
  - "Yaohui Zheng"
  - "Yuzhi Yang"
  - "Merouane Debbah"
  - "Chau Yuen"
---

# Leveraging Quantum Measurement Randomness for Shot-Efficient Diffusion Models

## Abstract

> In quantum computing, the readout always carries finite-shot sampling noise. Suppressing this
> noise through repeated measurements raises the cost of a quantum neural network (QNN).
> Meanwhile, a stochastic diffusion sampler deliberately adds randomness at each reverse
> (generation) step. This paper turns the measurement noise from a liability into a resource.
> Specifically, we use the noise quantum measurement produces anyway to replace part of the noise
> the sampler would otherwise inject. We characterize the measurement error as multinomial
> sampling noise propagated through a trainable linear readout. To connect the circuit's Born
> probabilities to the denoising task, we further formulate the diffusion process on a bounded
> zero-sum hyperplane mapped to the probability simplex. Therefore, we can employ a compensation
> noise to match the mean and covariance of the shot-noise-free linear update under some minimum
> shot conditions. Solving this condition for the shot count gives a state-dependent adaptive
> budget. For the denoising diffusion implicit model (DDIM), this budget increases as the sampler
> becomes more deterministic. On an eight-dimensional Gaussian mixture, the schedule achieves
> comparable generation quality with $303$ shots per sample against a high-shot reference of
> $1.6\times10^{6}$, about $5300\times$ fewer. Latent diffusion experiments on MNIST further
> validate the proposed mechanism for generation in a learned latent space.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

