---
aliases: ["Quantum Machine Learning for Cybersecurity Applications: Simulation and Hardware Validation"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.32911"
url: "http://arxiv.org/abs/2609.32911v1"
published: "2026-09-26T20:02:51Z"
ingested: "2026-09-29T12:04:08Z"
authors:
  - "Zirui Zhu"
  - "Zisheng Chen"
  - "Xiangyang Li"
---

# Quantum Machine Learning for Cybersecurity Applications: Simulation and Hardware Validation

## Abstract

> Under tight feature and compute budgets, classical threat detection pipelines often degrade on
> near-decision-boundary events. Small quantum processors are now available, but existing work
> inadequately shows whether quantum components improve end-to-end threat detection under the
> above resource constrained conditions. This paper tries to address this gap with a hybrid
> architecture that uses a compact multilayer perceptron layer to compress the information in data
> and then routes the processed features to a few qubit quantum heads implemented in quantum
> support vector machine (QSVM) and variational quantum circuit (VQC) models. On a simulation
> platform, we benchmark these hybrid models against classical models with comparable parameter
> budgets on two representative cybersecurity tasks, network intrusion detection on NSL-KDD
> dataset and spam filtering on Ling-Spam dataset. To validate their precision on real quantum
> hardware, we deploy the best 4-qubit QSVM model on an IBM Quantum device with noise-aware
> execution, evaluated on a smaller sub-dataset. In the results, shallow quantum heads
> consistently match, and on difficult near-boundary cases modestly reduce missed attacks and
> false alarms compared to classical models using the same features. Hardware validation results
> track the simulation behavior closely enough that the remaining gap is dominated by device noise
> rather than model design. Furthermore, we conduct adversarial attacks to test the robustness of
> one QSVM model. Taken together, the study shows that even on small, noisy devices, carefully
> engineered quantum components may function as competitive, budget-aware components in practical
> cyber threat detection applications.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

