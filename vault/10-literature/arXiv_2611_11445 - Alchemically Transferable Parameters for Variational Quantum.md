---
aliases: ["Alchemically Transferable Parameters for Variational Quantum Eigensolvers"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.11445"
url: "http://arxiv.org/abs/2611.11445v1"
published: "2026-11-08T15:15:39Z"
ingested: "2026-11-11T13:29:45Z"
authors:
  - "Jonas Motyl"
  - "Jakob S. Kottmann"
---

# Alchemically Transferable Parameters for Variational Quantum Eigensolvers

## Abstract

> Machine-learned circuit parameters could remove one of the main bottlenecks of variational
> quantum eigensolvers: the classical optimization loop, with its typical barren plateaus, local
> minima, and costly energy and gradient evaluations, is replaced by a direct prediction. Prior
> work showed that machine-learning models paired with a structured circuit design can transfer
> across system size and structure within hydrogenic systems. The next step: Extending them to
> organic molecules would seem to require re-training on use-case-specific training sets. In this
> work, we show that this is not necessary by establishing an alchemical approach. A geometric
> projection places surrogate hydrogen atoms along the bond directions of the target molecule and
> so maps its local bonding environment onto small hydrogenic fragments. Existing hydrogenic
> solvers can then be reused as they are. The only new quantity is a single projection radius per
> bond type, which is fitted once on a small reference molecule and reused unchanged thereafter.
> We demonstrate the approach on the separable-pair circuit designs that have been used in prior
> work and extend the approach to multi-circuit approaches that span effective bases for quantum
> subspaces.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

