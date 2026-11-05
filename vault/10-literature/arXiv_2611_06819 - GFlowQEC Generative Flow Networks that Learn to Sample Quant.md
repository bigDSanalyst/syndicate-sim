---
aliases: ["GFlowQEC: Generative Flow Networks that Learn to Sample Quantum LDPC Codes"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.06819"
url: "http://arxiv.org/abs/2611.06819v1"
published: "2026-11-04T17:31:57Z"
ingested: "2026-11-05T13:56:21Z"
authors:
  - "Nuno Batista"
  - "Gabriel Falcao"
  - "Penousal Machado"
---

# GFlowQEC: Generative Flow Networks that Learn to Sample Quantum LDPC Codes

## Abstract

> Choosing a quantum error-correcting code for a real device means scoring candidates with
> circuit-level simulations so slow that only a few hundred can be run. So every evaluation
> counts, and a search is judged by how many good codes it finds per paid evaluation. Quantum LDPC
> codes built from a few group elements protect many logical qubits, but good ones are rare in a
> huge space. We introduce GFlowQEC, to our knowledge the first generative flow network (GFlowNet)
> for quantum code design. It builds a code one group element at a time and learns to propose
> codes in proportion to a power of their score. We train it once on scores from earlier searches,
> freeze it, and let it propose lifted-product codes with 180 physical qubits, scored by their
> distances. Ranking ten of its draws per paid call, it finds more than twice as many new top-
> scoring codes (inequivalent to any it was trained on) as tuned parallel tempering, even when
> tempering starts from GFlowQEC's training codes. It finds more than three and a half times as
> many as a supervised screen ranking ten random candidates per call. When both rank a hundred,
> the screen beats GFlowQEC, and does best ranking GFlowQEC's draws. Soft Q-learning, which shares
> the GFlowNet's optimal policy, does as well at one noise bias and better at the other, so the
> gain does not depend on the GFlowNet's training loss. Trained proposers can make a budget of
> expensive evaluations go further when good codes are rare.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

