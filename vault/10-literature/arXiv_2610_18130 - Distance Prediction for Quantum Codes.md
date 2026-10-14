---
aliases: ["Distance Prediction for Quantum Codes"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.18130"
url: "http://arxiv.org/abs/2610.18130v1"
published: "2026-10-13T10:39:44Z"
ingested: "2026-10-14T11:06:59Z"
authors:
  - "Nadav Schneider"
  - "Eliya Nachmani"
---

# Distance Prediction for Quantum Codes

## Abstract

> The distance of a quantum code is a fundamental metric that dictates its error-correction
> capability. While quantum low-density parity-check (qLDPC) families such as Bivariate Bicycle
> (BB) codes offer a promising pathway to low-overhead fault-tolerant quantum computing, computing
> their distance is challenging. Current exact solvers and even search heuristics that provide a
> distance upper bound suffer from severe computational bottlenecks, restricting the discovery of
> optimal codes. In this paper, we construct a dataset of BB codes with corresponding distance
> upper bounds obtained through high-budget heuristic searches. We introduce BB-Net, an attention-
> based neural network architecture for predicting the distance of BB codes. It achieves 96.39%
> accuracy on the reference distances in the test set, compared with 94.86% for state-of-the-art
> heuristics with a budget of up to $10^{4}$ times more computational runtime. On a subset with
> certified exact distances, BB-Net achieves 98.94%. By relieving the distance-calculation
> bottleneck, BB-Net enables faster screening of large code spaces, particularly in ML-driven
> search pipelines, and thereby can accelerate the discovery of novel quantum error-correcting
> codes, an important capability for advancing scalable fault-tolerant quantum computing. Our code
> is publicly available: https://github.com/NadavSc/BBNet

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

