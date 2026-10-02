---
aliases: ["Fourier Symmetrization for Geometric Quantum Machine Learning"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.01874"
url: "http://arxiv.org/abs/2610.01874v1"
published: "2026-10-01T15:31:16Z"
ingested: "2026-10-02T11:49:48Z"
authors:
  - "Letao Wang"
  - "Abdel Lisser"
  - "Sreejith Sreekumar"
  - "Zeno Toffano"
---

# Fourier Symmetrization for Geometric Quantum Machine Learning

## Abstract

> Geometric quantum machine learning incorporates symmetry into quantum models, but how symmetry
> shapes their expressivity and guides effective model design remains insufficiently understood.
> We address this question through the Fourier representation of quantum Fourier models (QFMs).
> Symmetry organizes the frequency spectrum into orbits and sums the Fourier coefficients within
> each orbit into a symmetrized coefficient. When QFM trainable layers form independent exact
> 2-designs, the variance of each symmetrized coefficient equals the sum of the coefficient
> variances in its orbit. For single-layer QFMs with $\varepsilon$-approximate 2-design trainable
> layers, we bound the deviation from this identity. The resulting bound for individual Fourier
> coefficients can be exponentially tighter than an existing bound. The hyperoctahedral group
> provides an example of orbit growth that can mitigate vanishing expressivity of the symmetrized
> coefficients. Symmetrization of QFMs over an elementary abelian 2-group also yields pure
> multivariate Chebyshev polynomial basis functions. We introduce randomized encoding, which
> implements invariant models without ancilla qubits or the additional circuit depth for quantum
> twirling. We evaluate the models as quantum physics-informed neural networks (QPINNs) on two-
> dimensional screened Poisson and stationary viscous Hamilton-Jacobi equations. Under hard
> boundary constraints, QPINNs using exact symmetrization and randomized encoding achieve the
> lowest mean errors in the two benchmarks, respectively.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

