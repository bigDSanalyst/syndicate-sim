---
aliases: ["A Hybrid Message-Passing and Electric-Field Representation for Electrostatic QM/MM Embedding with Machine Learning Interatomic Potentials"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.41523"
url: "http://arxiv.org/abs/2610.41523v1"
published: "2026-10-30T10:16:32Z"
ingested: "2026-11-02T14:41:37Z"
authors:
  - "Raphael T. Husistein"
  - "Shobhit S. Chaturvedi"
  - "Thomas Weymuth"
  - "Beatriz Piniello"
  - "Sélène Forget"
  - "Kresten Lindorff-Larsen"
  - "Gemma C. Solomon"
  - "Markus Reiher"
---

# A Hybrid Message-Passing and Electric-Field Representation for Electrostatic QM/MM Embedding with Machine Learning Interatomic Potentials

## Abstract

> Within a hybrid quantum mechanics/molecular mechanics approach a small region of a large
> atomistic system is described quantum mechanically, while the rest of the system is represented
> by a classical force field. Despite this, the computational cost of the quantum calculation
> severely limits the accessible simulation and sampling time. Replacing the quantum calculation
> with a machine learning interatomic potential (MLIP) trained on quantum reference data can
> greatly increase the accessible simulation time. However, the accuracy and efficiency strongly
> depend on the specific way in which the MLIP incorporates information about the classical
> (electrostatic) environment. Here, we demonstrate that existing strategies based purely on
> features derived from an external electric field fail to distinguish certain environments,
> ultimately limiting their accuracy. As a solution, we propose an extension to the equivariant
> TensorNet architecture that mitigates this shortcoming by incorporating classical atoms close to
> the quantum region into the message-passing scheme, combined with features derived from the
> electric field for describing the environment farther away. We show that this combination
> achieves higher accuracy than either approach alone.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

