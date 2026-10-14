---
aliases: ["Lifting: Quantum State Discrimination Framework for Mid-Circuit Measurements"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.18482"
url: "http://arxiv.org/abs/2610.18482v1"
published: "2026-10-13T14:43:40Z"
ingested: "2026-10-14T11:06:59Z"
authors:
  - "Chi Zhang"
  - "Neel Vora"
  - "Yilun Xu"
  - "Gang Huang"
  - "Fan Chen"
  - "Lei Jiang"
---

# Lifting: Quantum State Discrimination Framework for Mid-Circuit Measurements

## Abstract

> Quantum computing promises new capabilities beyond classical computation. Mid-circuit
> measurements (MCMs) enable error correction and outcome-dependent control, but their reliability
> is limited by noise on superconducting hardware. These operations depend on accurate quantum
> state discrimination (QSD), which assigns measured signals to state labels. Neural network-based
> (NN-based) QSD improves this assignment, yet its error remains bounded below by the Bayes risk
> of the available readout distributions. A complementary challenge is state deterioration as
> successive measurements accumulate and circuit execution advances, making static calibration
> less representative of the workload. We present Lifting, a QSD framework that addresses both
> challenges through repetition encoding, neural decoding, and in situ calibration. Encoding
> supplies joint in-phase and quadrature (I-Q) readout signals from the target and auxiliary
> qubits, while contextual calibration trains the decoder for the conditions encountered during
> execution. Our theoretical analysis shows that retaining additional channels from a fixed joint
> distribution cannot increase Bayes risk and establishes sufficient conditions for contraction of
> an overlap-based upper bound. Experiments across three IBM processors evaluate the framework on
> repeated stabilizer measurement, parity-check, and teleportation workloads.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

