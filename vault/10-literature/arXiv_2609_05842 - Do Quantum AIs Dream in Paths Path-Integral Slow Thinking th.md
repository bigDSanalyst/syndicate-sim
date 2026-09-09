---
aliases: ["Do Quantum AIs Dream in Paths? Path-Integral Slow Thinking through Grover Interference"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.05842"
url: "http://arxiv.org/abs/2609.05842v1"
published: "2026-09-05T03:12:16Z"
ingested: "2026-09-09T10:42:59Z"
authors:
  - "Xiansheng Cai"
  - "Xiu-Hao Deng"
  - "Kun Chen"
---

# Do Quantum AIs Dream in Paths? Path-Integral Slow Thinking through Grover Interference

## Abstract

> Reinforcement learning with verifiable rewards enables large language models to think slowly,
> but the same training can induce policy collapse: probability concentrates onto a few successful
> trajectories and exploratory diversity erodes. We ask whether quantum AI can realize slow
> thinking differently. We formulate slow thinking as coherent dynamics over reasoning
> trajectories, a discrete path integral in which action sequences coexist in superposition and
> recombine before measurement. In our trainable realization, an exact verifier partitions the
> ensemble into collective accepted and rejected components that interfere under Grover amplitude
> amplification. A finite Grover evolution is maximized when the pre-amplification success
> probability lies at an analytically determined value below one, so inference itself defines an
> interior training target and removes the monotonic pressure toward unit success. In exact
> statevector simulations of a 2x3 sliding puzzle, Grover training reaches accuracy 0.95 on a
> 32-question training set at one round, against 0.73 for the strongest classical control. On
> held-out questions specialization has a cost: an untrained uniform policy read out through the
> same amplification remains the strongest reference on this solution-dense benchmark, and quantum
> training preserves far more held-out accuracy than classical training - at four rounds with
> matched circuit applications the two quantum models reach 3.2 and 3.9 times the strongest
> classical controls. The number of training questions supported by fixed-size policies trained at
> each amplification budget also grows faster with the budget than with matched classical
> repetition. These results establish a Grover-based realization of path-integral slow thinking:
> the interior target preserves exploratory path diversity, and ensemble-level interference
> converts it into verified performance.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

