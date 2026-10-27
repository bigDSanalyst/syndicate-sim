---
aliases: ["Fully quantum training of parametric circuits with Quantum Hamiltonian Descent"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.33144"
url: "http://arxiv.org/abs/2610.33144v1"
published: "2026-10-23T16:52:05Z"
ingested: "2026-10-27T11:33:18Z"
authors:
  - "Marco Burato"
  - "Leonardo Banchi"
---

# Fully quantum training of parametric circuits with Quantum Hamiltonian Descent

## Abstract

> Parametric quantum circuits are usually trained by classical, local optimizers, which use the
> quantum computer only to evaluate the cost function, or its gradient, one point at a time.
> Quantum Hamiltonian Descent (QHD) takes a different route: in this quantum algorithm for
> continuous optimization, the parameters become the position of a quantum particle, with the cost
> function as its potential, and two time schedules control kinetic and potential energy so that
> the wavefunction explores the whole landscape and tunnels towards the global minimum. QHD,
> however, assumes a classically computable cost function, and its digital implementation is
> poorly understood: standard error bounds grow exponentially with the number of qubits per
> parameter, and the schedules are borrowed from classical optimization. Here we propose to train
> parametric circuits with QHD entirely on the quantum computer, through an online step in which
> the qubits encoding the parameters coherently control the circuit on a second register. We prove
> that, for cost functions with a smooth periodic extension, including those of parametric
> circuits, the simulation error admits a bound independent of the grid resolution, and that for
> circuits the bound grows at most linearly with the number of parameters. We also show that the
> ideal dynamics depends on the two schedules only through a single curve, which controls the
> adiabaticity of the search, and that the remaining freedom can be used to minimize the gate
> count. Simulations on benchmark functions and parametric circuits show that, at equal cost,
> schedules designed in this way markedly increase the probability of finding the global minimum.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

