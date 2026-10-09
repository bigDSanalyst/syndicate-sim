---
aliases: ["Beyond QAOA: A Review of AI and Quantum Computing for Adaptive Combinatorial Optimization"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.11759"
url: "http://arxiv.org/abs/2610.11759v1"
published: "2026-10-08T11:44:46Z"
ingested: "2026-10-09T12:31:33Z"
authors:
  - "Hoong Chuin LAU"
---

# Beyond QAOA: A Review of AI and Quantum Computing for Adaptive Combinatorial Optimization

## Abstract

> Near-term quantum approaches to combinatorial optimization are limited by qubit counts, circuit
> fidelity, sampling cost, and the difficulty of encoding constraints, while machine learning is
> increasingly used to configure and control quantum optimization workflows. We call such
> workflows adaptive: decisions conventionally fixed in advance, from formulation and penalties to
> shot budgets, backends, and whether to invoke a quantum processor at all, are made by learned
> policies that respond to the instance, the progress of the solve, or the hardware. This review
> examines three paradigms, AI for quantum optimization, quantum for AI-driven optimization, and
> AI-quantum co-optimization, and organizes the literature by the decision being learned rather
> than by application. A structured review of 119 papers, 67 coded in detail, shows that the
> evidence is considerably stronger for AI-assisted quantum optimization than for the reverse
> direction: learning already reduces quantum evaluations, improves initialization, supports
> decomposition and penalty control, and mitigates noise, whereas evidence that quantum
> computation improves learned optimizers remains largely confined to small-scale simulation.
> Experimental controls are thin: 25 of 57 studies include no classical baseline, the quantum
> contribution is fully isolated in 10 of 24 studies where an ablation applies, and the median
> experiment uses 17 qubits. We introduce an M0-M5 evidence hierarchy, from simulation to matched-
> resource practical advantage, and find no broadly convincing result at the highest level. We
> argue that scaling is increasingly a systems problem: the question is not only whether a problem
> fits on a quantum processor, but how classical and quantum resources should be allocated across
> the optimization process. The review is aimed at researchers in quantum computing, machine
> learning, and operations research.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

