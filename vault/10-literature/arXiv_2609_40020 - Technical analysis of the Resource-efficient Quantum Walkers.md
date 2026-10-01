---
aliases: ["Technical analysis of the Resource-efficient Quantum Walkers Quantum Random Access Memory"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.40020"
url: "http://arxiv.org/abs/2609.40020v1"
published: "2026-09-30T15:58:43Z"
ingested: "2026-10-01T12:22:27Z"
authors:
  - "Giuseppe De Riso"
  - "Giuseppe Catalano"
  - "Seth Lloyd"
  - "Vittorio Giovannetti"
  - "Dario De Santis"
---

# Technical analysis of the Resource-efficient Quantum Walkers Quantum Random Access Memory

## Abstract

> Quantum Random Access Memory (qRAM) is a critical component for achieving quantum advantage in
> algorithms ranging from database search to quantum machine learning. In a recently introduced
> model [arXiv:2508.02855], we proposed a resource-efficient qRAM architecture based on discrete-
> time quantum walkers. This article serves as a comprehensive technical follow-up, providing the
> full mathematical derivations, detailed protocol specifications, and in-depth resource analysis.
> Moreover, we extend the original proposal with novel techniques for the purpose of making the
> qRAM implementation more realistic. Our model resolves the primary drawbacks of leading qRAM
> proposals: it avoids the exponential number of active nodes $\mathcal{O}(2^n)$ required by the
> "Bucket Brigade" architecture by employing a number of quantum walkers that scales linearly with
> the address and message sizes, $n$ and $m$, respectively. Simultaneously, it overcomes the
> spatial bottlenecks of previous quantum-walker schemes by eliminating the need for multiple
> parallel trees. We propose two algorithmic paradigms: the long- and the short-range approaches,
> which differ by the length of interaction of the main routing gates employed in the qRAM. We
> formalize the routing, message-copy, and walker retrieval phases for both variants and we show
> how, while the long-range scheme employs controlled gates having a multitude of target systems,
> the short-range approach decomposes these interactions into sequences of 2- and 3-body local
> gates, which improves the architecture's feasibility for near-term experimental implementation.
> Finally, our comprehensive resource analysis confirms that the short-range approach achieves the
> optimal $\mathcal{O}(n+m)$ circuit depth. Within these two paradigms, we explore the potential
> of different types of quantum walkers, namely bosons, dual-rail qubits and four-level qudits.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

