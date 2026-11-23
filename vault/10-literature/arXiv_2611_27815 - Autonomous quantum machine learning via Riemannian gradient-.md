---
aliases: ["Autonomous quantum machine learning via Riemannian gradient-based optimization"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.27815"
url: "http://arxiv.org/abs/2611.27815v1"
published: "2026-11-20T16:42:26Z"
ingested: "2026-11-23T17:17:41Z"
authors:
  - "Kasidit Srimahajariyapong"
  - "Thiparat Chotibut"
  - "Suwannachad Suwannajitt"
  - "Tithivich Paka"
  - "Ricard Puig"
  - "Yudai Suzuki"
  - "Marek Gluza"
  - "Zoë Holmes"
  - "Supanut Thanasilp"
---

# Autonomous quantum machine learning via Riemannian gradient-based optimization

## Abstract

> Quantum machine learning models typically rely on repeated quantum measurements and classical
> optimization during training, making the quantum-to-classical information-extraction process a
> fundamental bottleneck for scalability. We propose a framework for autonomous self-training
> quantum machine learning, based on Riemannian gradient optimization, in which the optimization
> proceeds entirely within the quantum domain without requiring quantum measurements or classical
> feedback. We derive the Riemannian gradient update rules for a broad class of learning tasks and
> identify sufficient conditions under which the resulting training dynamics can be realized fully
> autonomously. Within this regime, we establish an exponential convergence guarantee, in the
> training iterations, for sufficiently small step sizes, and further analyze the training cost in
> terms of the growth of the circuit depth. Importantly, we further show that the trained model
> can automatically discover symmetries hidden in the training data without $\textit{a priori}$
> specification. For the canonical examples of quantum phase classification and unitary learning
> with a hidden symmetry, our numerical study indicates that learning can be achieved at low
> circuit depths with only a few distinct training examples. Our results thus establish autonomous
> quantum machine learning as a promising paradigm that removes the classical optimization loop
> while retaining strong theoretical guarantees and practical performances.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

