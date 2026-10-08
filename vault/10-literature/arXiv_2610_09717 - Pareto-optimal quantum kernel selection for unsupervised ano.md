---
aliases: ["Pareto-optimal quantum kernel selection for unsupervised anomaly detection on real malware beaconing data"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.09717"
url: "http://arxiv.org/abs/2610.09717v1"
published: "2026-10-07T09:13:12Z"
ingested: "2026-10-08T12:45:22Z"
authors:
  - "Boaz Micah"
  - "Nadia Milazzo"
  - "Maissa Beji"
  - "Borja Aizpurua"
  - "Llorenç Espinosa-Portalés"
  - "Esteban Payares"
  - "Ghada Ben Slama"
  - "Luc Andrea"
  - "Michel Kurek"
  - "Thomas Cope"
  - "Olivier Salomon"
---

# Pareto-optimal quantum kernel selection for unsupervised anomaly detection on real malware beaconing data

## Abstract

> Quantum kernel methods are leading candidates for a practical quantum advantage in machine
> learning, but assessing that potential requires two quantities usually reported separately: how
> well a kernel performs on the task, and how far its geometry departs from the classical kernels
> available for the same problem. We introduce a fully unsupervised, multi-objective protocol that
> optimises simultaneously the normalised pseudo discrepancy (NPD), a label-free proxy for anomaly
> detection quality, and the geometric difference (GD) to a tuned classical reference kernel,
> selecting models from the resulting Pareto front. We apply it to malware beaconing detection in
> real network traffic, using a one-class support vector machine with fidelity and projected
> quantum kernels over four data encodings, on simulators and on IQM's 20-qubit Garnet processor.
> NPD-guided selection alone finds a fidelity kernel that beats the tuned classical baseline, but
> with a geometric difference too small to certify the gain as quantum. Projected kernels reach
> far larger geometric differences; the Pareto-selected one only marginally exceeds the baseline
> (AUC $0.782$ versus $0.765$, $g_{C\to Q}\approx 89>\sqrt{N}$ relative to that reference kernel),
> still below the NPD-selected fidelity kernel ($0.840$).

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

