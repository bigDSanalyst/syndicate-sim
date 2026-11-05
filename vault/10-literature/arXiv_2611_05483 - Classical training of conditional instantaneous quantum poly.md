---
aliases: ["Classical training of conditional instantaneous quantum polynomial-time Born machines"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.05483"
url: "http://arxiv.org/abs/2611.05483v1"
published: "2026-11-03T19:00:03Z"
ingested: "2026-11-05T13:56:21Z"
authors:
  - "Oriol Balló-Gimbernat"
  - "Emiliano Tolotti"
  - "Laia Domingo"
  - "Fernando Vilariño"
  - "Adan Garriga"
---

# Classical training of conditional instantaneous quantum polynomial-time Born machines

## Abstract

> Instantaneous quantum polynomial-time (IQP) Born machines are attractive quantum generative
> models, as certain IQP circuit families are conjectured to be hard to sample, yet they can be
> trained classically. Previously proposed conditional IQP Born machines make the parameters of
> the diagonal layer condition dependent. We introduce conditional IQP Born machines, in which the
> condition is encoded in the input state and a single IQP unitary is shared across conditions.
> Efficient sampling and amplitude-ratio evaluation for the reference state entering the diagonal
> layer suffice to obtain unbiased classical estimates of a conditional maximum mean discrepancy
> objective and its gradients. We show that input conditioning can represent conditional families
> that no diagonally conditioned IQP model with the same number of qubits can reproduce. For the
> sixteen-qubit Curie-Weiss spin model, a single conditional model captures the magnetization
> transition at held-out temperatures. Its mean total variation distance is six times lower than
> that of diagonal conditioning under the same protocol and comparable to that of classical
> generative models with up to seven times as many parameters. We also train conditional models
> classically with up to 2048 qubits, which reproduce the mean squared magnetization of the target
> away from the crossover. These results extend classically trained IQP Born machines to
> conditional generation.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

