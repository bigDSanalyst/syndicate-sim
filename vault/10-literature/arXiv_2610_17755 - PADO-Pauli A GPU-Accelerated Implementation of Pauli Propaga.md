---
aliases: ["PADO-Pauli: A GPU-Accelerated Implementation of Pauli Propagation"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.17755"
url: "http://arxiv.org/abs/2610.17755v1"
published: "2026-10-13T05:38:29Z"
ingested: "2026-10-14T11:06:59Z"
authors:
  - "Hyunwoo Kim"
  - "Youngseok Lee"
---

# PADO-Pauli: A GPU-Accelerated Implementation of Pauli Propagation

## Abstract

> Variational quantum algorithms utilize parameterized circuits many times during training, at new
> parameter values, over batches of data, and with gradients. Pauli propagation approximates the
> expectation values of such circuits classically by evolving the observable in the Heisenberg
> picture as a truncated sum of Pauli strings. We present PADO-Pauli, a GPU engine for Pauli
> propagation that compiles a circuit and its observables once into sparse matrices in which each
> rotation angle contributes only a cosine and a sine factor, so every later evaluation reuses the
> compiled program. It evaluates batches of parameters and data inputs embedded as rotation
> angles. By default its gradients come from a vector-Jacobian product registered with PyTorch's
> automatic differentiation, so they flow through the angles to any classical layer that produces
> them. PADO-Pauli also provides truncation by Pauli weight and coefficient size, and noise
> channels. Zero-filtering removes terms that do not contribute to an expectation value in the
> all-zero reference state and makes the batched forward pass about 1.5 times faster. Compared to
> cuPauliProp on an NVIDIA A100, PADO-Pauli evaluates up to 10 times faster on 4 to 12 qubits and
> uses up to 3.1 times less memory on 16 qubits. We check its accuracy against exact statevector
> simulation up to 28 qubits. These features make PADO-Pauli a practical toolkit for training
> variational quantum algorithms, including quantum machine learning models.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

