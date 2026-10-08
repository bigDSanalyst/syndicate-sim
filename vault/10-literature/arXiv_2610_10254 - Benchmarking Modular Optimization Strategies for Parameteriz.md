---
aliases: ["Benchmarking Modular Optimization Strategies for Parameterized Quantum Circuits"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.10254"
url: "http://arxiv.org/abs/2610.10254v1"
published: "2026-10-07T15:32:48Z"
ingested: "2026-10-08T12:45:22Z"
authors:
  - "Carla Cotea"
  - "Stefan Balauca"
  - "Andreea Arusoaie"
---

# Benchmarking Modular Optimization Strategies for Parameterized Quantum Circuits

## Abstract

> Training parameterized quantum circuits requires balancing optimization progress with limited
> evaluation budgets and the statistical uncertainty of near-term quantum hardware. We present a
> modular benchmarking framework that separates quantum search-direction estimation from classical
> parameter-update rules, allowing their interactions and sensitivities to be examined
> independently. We evaluate a suite of gradient-based, stochastic, and derivative-free optimizers
> across combinatorial optimization using the Quantum Approximate Optimization Algorithm (QAOA),
> supervised quantum machine learning using Iris classification and a quantum convolutional neural
> network (QCNN) for binary MNIST classification, and quantum chemistry using the variational
> quantum eigensolver (VQE) for molecular hydrogen. By separating objective evaluations from
> sample-circuit costs under finite-shot simulation and physical execution on a 156-qubit
> processor, we compare optimizer behavior across workloads with different parameter counts and
> measurement requirements. Four selected simulator and hardware case studies report terminal and
> best observed objectives separately, alongside post-training classifier accuracies. The
> comparisons include selected MaxCut and hydrogen trajectories and illustrate workload-dependent
> objective changes and evaluation costs, while the simulator benchmark compares both peak and
> mean performance across three seeds. The hardware runs do not establish an optimizer ranking or
> isolate a causal effect of device noise.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

