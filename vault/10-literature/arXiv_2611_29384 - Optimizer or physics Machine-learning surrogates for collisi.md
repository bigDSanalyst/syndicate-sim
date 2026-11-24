---
aliases: ["Optimizer or physics? Machine-learning surrogates for collision-based preparation of multipartite entangled quantum states"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.29384"
url: "http://arxiv.org/abs/2611.29384v1"
published: "2026-11-22T10:56:49Z"
ingested: "2026-11-24T16:55:37Z"
authors:
  - "Duc-Kha Vu"
  - "Minh Tam Nguyen"
  - "Özgür E. Müstacaplıoğlu"
  - "Fatih Ozaydin"
---

# Optimizer or physics? Machine-learning surrogates for collision-based preparation of multipartite entangled quantum states

## Abstract

> Repeated partial-SWAP collisions can prepare symmetric Dicke states, including the $W$ state,
> without measurement or postselection. The collision sequence uses only two global collision
> angles, and its fidelity is evaluated after a final layer of local phase rotations is optimized
> numerically, so each candidate pair requires a many-qubit simulation and a phase fit. We study
> when learned surrogates reduce the number of such evaluations, and what limits the best-found
> fidelity, for 65 Dicke targets with 11--20 qubits in noiseless simulations. At 50 evaluations
> per target, Gaussian-process Bayesian optimization (GP-BO) exceeds fixed Sobol and grid designs
> by 0.088 and 0.063 in mean best-found fidelity. Bounded Nelder--Mead reaches 0.760 against 0.762
> for GP-BO, and has the higher three-seed mean on 41 of the 61 targets with a reference value; in
> this two-parameter problem, adaptivity matters far more than the choice between the two methods.
> A neural-network ensemble pretrained on 750 observations from smaller systems needs 32\% fewer
> new evaluations per target than GP-BO at comparable fidelity, but the full neural search takes
> 1.6 times the wall time of GP-BO in our implementation. In a separate source-only test, the best
> of five neural proposals per target exceeds the best of five population-model proposals by 0.070
> in mean fidelity. Exact symmetries and state diagnostics help explain why the leading adaptive
> methods reach similar family-mean fidelities. The collisions conserve the magnitude of the bare
> Dicke overlap and the total-spin weights, and for the best controls on a 12-target diagnostic
> panel, 79% of the infidelity is an amplitude deficit that a final phase layer cannot remove,
> which motivates interleaved phase control.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

