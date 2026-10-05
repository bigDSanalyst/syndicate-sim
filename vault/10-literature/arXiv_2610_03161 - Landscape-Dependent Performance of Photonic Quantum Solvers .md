---
aliases: ["Landscape-Dependent Performance of Photonic Quantum Solvers in QUBO Feature Selection for Financial Risk Detection"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.03161"
url: "http://arxiv.org/abs/2610.03161v1"
published: "2026-10-02T11:38:23Z"
ingested: "2026-10-05T13:31:08Z"
authors:
  - "Nirvik Sahoo"
  - "Paul Robert Griffin"
---

# Landscape-Dependent Performance of Photonic Quantum Solvers in QUBO Feature Selection for Financial Risk Detection

## Abstract

> Feature selection for imbalanced classification tasks such as credit card fraud and consumer
> default detection requires balancing predictive relevance, inter-feature redundancy, and
> computational feasibility. We benchmark three computing paradigms, classical branch-and-bound
> optimization (Gurobi), photonic entropy computing (QCI Dirac-3), and simulated photonic boson
> sampling (Piquasso), across thirteen feature-selection methods on two datasets: ULB Credit Card
> Fraud (30 features) and AmEx consumer default (159 features). Each method is routed to the
> solver matched to its mathematical structure. On ULB, Dirac-3 MI-Spearman matches the all-
> features model using 13 of 30 features (mean F1 0.873 +/- 0.023 over five runs, best run 0.896),
> and Piquasso is the best method at k=5. On AmEx, performance rises steadily with the feature
> budget and every paradigm approaches F1 = 0.80 only near the full feature set. Most differences
> between Gurobi and Dirac-3 on identical methods fall within run-to-run variation; the large gaps
> occur where the certified optimum generalizes poorly, most sharply for distance correlation on
> AmEx at k=25 (Gurobi F1 = 0.422 vs. a Dirac-3 mean of 0.746). At matched budgets, F1 varies
> about ten times more across methods on ULB than on AmEx, which we trace to how concentrated the
> predictive signal is in each feature space.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

