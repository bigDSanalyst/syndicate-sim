---
aliases: ["Unbiased sampling from Boltzmann distributions with noisy energies"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.01204"
url: "http://arxiv.org/abs/2609.01204v1"
published: "2026-09-01T13:12:14Z"
ingested: "2026-09-02T10:33:37Z"
authors:
  - "Iwo Sanderski"
  - "Gian Gentinetta"
  - "Giuseppe Carleo"
---

# Unbiased sampling from Boltzmann distributions with noisy energies

## Abstract

> Sampling from the Boltzmann distribution is central to computational physics, yet hard when the
> energy is known only through a stochastic estimate, such as with machine-learned molecular
> potentials, in variational Monte Carlo, or on quantum computers, because a noisy energy biases
> the sampled distribution. The penalty method of Ceperley and Dewing corrects this but requires
> the noise variance and becomes intractable when it is large. We introduce the Poisson product
> estimator, an unbiased, non-negative estimator of the Boltzmann weight that only needs an upper
> bound on the energy estimator and remains efficient at high noise. Using it to optimize a
> variational quantum circuit gradient-free, we recover the $H_3^+$ ground-state energy in a
> minimal basis and, by sampling rather than following a single trajectory, also map the
> variational energy landscape.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

