---
aliases: ["LiftDiff: Guided Discrete Diffusion for Quantum Code Construction"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.25213"
url: "http://arxiv.org/abs/2610.25213v1"
published: "2026-10-18T12:10:36Z"
ingested: "2026-10-20T10:53:29Z"
authors:
  - "Yotam Peled"
  - "Eliya Nachmani"
---

# LiftDiff: Guided Discrete Diffusion for Quantum Code Construction

## Abstract

> The realization of fault-tolerant quantum computation relies on Quantum Error-Correcting Codes
> (QECC). Of particular interest are codes that combine a high encoding rate with sufficient
> distance. Existing algebraic constructions, such as lifted product (LP) codes, build a large
> quantum low-density parity-check (qLDPC) code from a classical base matrix. In this work we
> introduce LiftDiff, a generative approach to the discovery of QECC. A discrete denoising
> diffusion model is trained to generate base matrices over the group algebra
> $\mathbb{F}_2[\mathbb{Z}_\ell]$, which are then expanded into LP codes. The reverse diffusion
> process is guided by an energy function that evaluates quantum code properties, including girth,
> degree, sparsity and decoding performance, steering the sampler toward matrices that yield LP
> codes with favorable parameters. Our method discovers codes with parameters such as
> $[[169,13,11]]$, $[[143,15,9]]$, and $[[260,24,10]]$, including a $[[247,19,14]]$ code that
> achieves the highest ${kd^2}/{n}$ among the baselines. Moreover, several discovered codes
> outperform the Gross code across a broad range of the tested physical error rates under both
> code-capacity and circuit-level noise.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

