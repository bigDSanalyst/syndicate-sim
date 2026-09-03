---
aliases: ["A variational quantum eigensolver-based cutting plane framework for semidefinite programming problems"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.02139"
url: "http://arxiv.org/abs/2609.02139v1"
published: "2026-09-02T05:49:11Z"
ingested: "2026-09-03T10:37:34Z"
authors:
  - "Gizem Ozbaygin"
  - "Burak Kocuk"
  - "Diego A. Moran R"
---

# A variational quantum eigensolver-based cutting plane framework for semidefinite programming problems

## Abstract

> Semidefinite programming plays a key role in optimization, with broad impact across control
> theory, machine learning, and combinatorial optimization. Although semidefinite programs are
> polynomially solvable, several commonly used algorithms rest on a linear-algebraic step whose
> running time grows cubically with the matrix dimension and which requires the matrix itself to
> be held in memory, at quadratic cost. In this study, we propose replacing it with a variational
> quantum eigensolver, whose qubit requirement is logarithmic in the matrix dimension, and present
> the first end-to-end implementation of such an approach within a cutting-plane framework,
> together with an operator-derived ansatz whose entanglement structure is read directly from the
> Pauli support of the candidate matrix. Evaluated on the control family of SDPLIB against an
> identical scheme driven by an exact eigendecomposition, the variational oracle produces valid
> cuts throughout, closing 32 to 82% of the initial optimality gap against a near-constant 75 to
> 82% for the exact oracle. Implementing and measuring the method end to end surfaces several
> effects not visible from theoretical analyses alone: where memory is actually consumed, how the
> padding required to fit a matrix onto a quantum register can mislead the variational optimizer,
> and why the candidate matrices prove dense in the Pauli basis, reducing the operator-derived
> ansatz to full entanglement. We report these findings and discuss their implications for near-
> term hybrid quantum-classical approaches.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

