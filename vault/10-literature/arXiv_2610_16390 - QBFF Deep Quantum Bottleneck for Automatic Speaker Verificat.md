---
aliases: ["QBFF: Deep Quantum Bottleneck for Automatic Speaker Verification Anti-Spoofing"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.16390"
url: "http://arxiv.org/abs/2610.16390v1"
published: "2026-10-12T08:37:29Z"
ingested: "2026-10-14T11:06:59Z"
authors:
  - "Anton Firc"
  - "Nouhaila Innan"
  - "Vojtěch Staněk"
  - "Kamil Malinka"
  - "Martin Perešini"
  - "Zbyněk Lička"
  - "Walid El Maouaki"
  - "Alberto Marchisio"
  - "Muhammad Shafique"
---

# QBFF: Deep Quantum Bottleneck for Automatic Speaker Verification Anti-Spoofing

## Abstract

> A central goal of quantum machine learning is to identify applications in which small quantum
> circuits can improve task performance while remaining executable on real hardware. We
> investigate deepfake (synthetic) speech detection, a largely unexplored application in this
> area, where reliable confidence scores are as important as discrimination performance because
> deployment decisions are made at fixed thresholds and overconfident errors can be costly. We
> introduce QBFF, which routes a compressed speech representation through a small 8-qubit
> variational circuit (VQC) used as a drop-in bottleneck, with a matched classical bottleneck as
> the control. The quantum circuit yields better-calibrated confidence in most matched
> comparisons, including out-of-distribution evaluation, though the downstream deployment-cost
> benefit is model-dependent. We then run the same circuit on a real IBM quantum processor. To our
> knowledge, this is the first anti-spoofing pipeline to run on a QPU; hardware execution
> demonstrates feasibility, with lower subset EER and $C_{llr}$ but higher mean actDCF than the
> matched classical reference. Together, these results show that hardware-executable quantum
> bottlenecks can improve score reliability, with gains that vary by evaluation setting.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

