---
aliases: ["Programming Quantum Circuit Parameters with Large Language Models"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.17246"
url: "http://arxiv.org/abs/2611.17246v1"
published: "2026-11-12T18:34:23Z"
ingested: "2026-11-13T13:52:45Z"
authors:
  - "Tiago de Souza Farias"
  - "Caio Moraes Porto"
  - "Matheus da Silva Fonseca"
  - "Nicolas Armando Cabrera Carpi"
  - "Anderson de Araujo Oliveira"
  - "Celso Jorge Villas-Boas"
---

# Programming Quantum Circuit Parameters with Large Language Models

## Abstract

> Large language models (LLMs) have recently demonstrated the ability to generate parameters for
> variational quantum circuits without conventional optimization. However, the conditions under
> which this approach is effective remain unclear. Here, we investigate a frozen, general-purpose
> LLM that generates complete circuit parameter vectors from symbolic circuit and Hamiltonian
> descriptions, with optional iterative energy feedback. We evaluate the approach on general
> random Hamiltonians, structured parent Hamiltonians, and molecular systems. For general
> Hamiltonians, LLM-generated parameters exhibit larger energy errors than conventional Adam
> optimization, while additional feedback generally provides limited improvement. In contrast, for
> structured Hamiltonians, the LLM can generate promising low-energy parameter configurations,
> suggesting that identifiable physical and mathematical structure facilitates parameter
> inference. We also show that direct LLM predictions of minimum energies can violate the
> Hamiltonian spectral lower bound, whereas generated circuit parameters allow independent
> evaluation of physically realizable energy expectation values. Finally, we investigate blind
> circuit interpretation and find that the LLM can predict measurement outcomes even when it fails
> to identify the underlying quantum algorithm. These findings highlight the role of problem
> structure, the limitations of iterative LLM optimization, and the importance of independently
> verifiable predictions in quantum parameter programming.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

