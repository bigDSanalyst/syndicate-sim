---
aliases: ["Steering the Fidelity in State Preparation on Noisy Bosonic Systems with Risk-Seeking Optimization"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.18495"
url: "http://arxiv.org/abs/2610.18495v1"
published: "2026-10-13T14:52:00Z"
ingested: "2026-10-14T11:06:59Z"
authors:
  - "Riccardo Piantoni"
  - "Riccardo Pellini"
  - "Maurizio Ferrari Dacrema"
  - "Paolo Cremonesi"
---

# Steering the Fidelity in State Preparation on Noisy Bosonic Systems with Risk-Seeking Optimization

## Abstract

> In order to execute quantum algorithms on bosonic quantum computers, it is necessary to encode
> their inputs into a desired target quantum state, with a process called state preparation. In
> real settings, state preparation methods operate in stochastic scenarios, where the prepared
> state is represented as a mixed state, that is a probabilistic ensemble of pure states.
> Therefore, existing state preparation methods optimize a variational ansatz by averaging over
> all possible sequences of photon loss events contained in the prepared ensemble, yielding an
> output state which approximates the desired target with a certain average fidelity. Such an
> approach, however, does not take into account directly the distribution of fidelities across
> states in the ensemble. In this work, we aim to maximize the fidelity of only a subset of pure
> states sampled from the prepared ensemble, at the cost of reducing the average fidelity overall.
> This trade-off is relevant when the goal is to obtain high-fidelity states with a certain
> probability, rather than maximizing the average fidelity of the prepared ensemble. We borrow and
> adapt objective functions from risk-sensitive optimization, a framework that optimizes specific
> characteristics of a distribution rather than only its expectation, and that has been
> successfully applied in Reinforcement Learning. In the considered experimental settings, our
> results show that the infidelities of some pure states in the prepared ensemble can be reduced
> by up to four orders of magnitude when using risk-seeking objectives, compared to those achieved
> using the standard optimization of the average fidelity. Furthermore, we show that it is
> possible to control the trade-off between the probability of obtaining high-fidelity states and
> the lowest infidelity threshold reached, providing the flexibility to select the operating point
> that best suits a certain application.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

