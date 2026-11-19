---
aliases: ["Gradient Blindness in Adaptive Architecture Search for IQP Born Machines"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.24174"
url: "http://arxiv.org/abs/2611.24174v1"
published: "2026-11-18T10:16:38Z"
ingested: "2026-11-19T15:11:48Z"
authors:
  - "Sebastian Wölckert"
  - "Gerhard Stenzel"
  - "Michael Poppel"
  - "Claudia Linnhoff-Popien"
  - "Jonas Stein"
---

# Gradient Blindness in Adaptive Architecture Search for IQP Born Machines

## Abstract

> Instantaneous quantum polynomial (IQP) Born machines learn a probability distribution from data
> with a circuit of commuting gates that a classical computer trains at hundreds of qubits.
> Adaptive algorithms grow a sparse circuit from a small seed by adding in every round the
> candidate gates with the largest loss gradient. Such algorithms never add a candidate whose
> gradient vanishes, so the choice of seed decides which circuits they can reach. Here we show
> that a candidate gate has a nonzero gradient for some angles of the circuit exactly when its
> generator is the sum of an odd number of linearly independent generators already in the circuit.
> The common seed of one-qubit gates therefore never adds a gate on an even number of qubits,
> which exact gradients on 12 qubits confirm. A seed of one-qubit gates plus the edges of the
> Chow-Liu tree sees every candidate, and its circuits match the full circuits on 12 and 16 qubits
> with 10 to 13 percent of their parameters. At 484 qubits, a heredity pool keeps the search over
> higher-order gates feasible, and the circuits grown from this seed reach a lower test loss than
> the dense two-body circuit with 6 percent of its parameters, although the higher-order gates add
> no gain.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

