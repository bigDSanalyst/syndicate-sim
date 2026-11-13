---
aliases: ["A New Framework for Quantum Reinforcement Learning"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.14731"
url: "http://arxiv.org/abs/2611.14731v1"
published: "2026-11-10T20:45:57Z"
ingested: "2026-11-13T13:52:45Z"
authors:
  - "Alireza Tavakoli"
  - "Mohsen Heidari"
---

# A New Framework for Quantum Reinforcement Learning

## Abstract

> Quantum reinforcement learning (QRL) has emerged as a promising approach for controlling quantum
> systems and accelerating learning tasks with quantum resources. However, most existing QRL
> formulations still retain a classical reinforcement learning interface: states and actions are
> often encoded in computational bases and rewards are extracted through measurements. This
> interface is restrictive for genuinely quantum environments: choosing a measurement can discard
> entanglement information, while repeated intermediate measurements collapse the evolving state
> and require costly re-preparation. This motivates a fully QRL framework in which the agent,
> environment, rewards, and return accumulation are all quantum. In this paper, we take a step
> toward this goal and introduce a new QRL framework in which both the policy and the environment
> are modeled by conditional quantum channels. We then propose a quantum policy-gradient algorithm
> for parameterized conditional quantum channels with a trainable control basis. We also derive
> finite- and infinite-horizon gradient estimators using a new parameter-shift rule. This rule is
> needed because policy parameters are shared across repeated interaction blocks and the infinite-
> horizon objective is not a finite circuit; rather than shifting every occurrence and evaluating
> the whole trajectory, our estimator shifts only one sampled policy block. Sampling this block
> from a geometric distribution yields an unbiased gradient estimator under bounded rewards.
> Finally, we establish convergence of the resulting stochastic gradient-ascent procedure to
> stationary points under standard smoothness and step-size assumptions.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

