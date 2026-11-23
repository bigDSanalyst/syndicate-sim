---
aliases: ["Practical insights into controlling exponential concentration in quantum machine learning"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.27486"
url: "http://arxiv.org/abs/2611.27486v1"
published: "2026-11-20T11:32:28Z"
ingested: "2026-11-23T17:17:41Z"
authors:
  - "Fernando Mondragon-Sampedro"
  - "Diego Alvarez-Estevez"
---

# Practical insights into controlling exponential concentration in quantum machine learning

## Abstract

> Quantum Machine Learning (QML) models are often limited by exponential concentration, where
> quantum observables become insensitive to input variations as system size increases. In this
> work, we provide a comparative empirical study of this phenomenon across Fidelity Quantum
> Kernels (FQK), Projected Quantum Kernels (PQK), and Quantum Extreme Learning (QEL), within a
> unified observable-based framework based on expectation-value variance. We investigate how
> measurement locality, entanglement, and circuit expressivity shape concentration across
> different architectures. Global fidelity-based kernels exhibit strong concentration driven by
> Hilbert space dimensionality, whereas local-observable approaches reduce but do not eliminate
> this effect. In PQK and QEL, concentration is primarily governed by entanglement and quantum
> dynamical expressivity, with reservoir depth emerging as a key factor in QEL architectures. We
> further study bandwidth scaling as a general mechanism for controlling encoding expressivity
> across all models. Our results indicate that bandwidth scaling effectively reduces concentration
> in moderate regimes by restricting the effective expressivity of the encoding, though this
> protective effect diminishes in highly expressive structural settings.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

