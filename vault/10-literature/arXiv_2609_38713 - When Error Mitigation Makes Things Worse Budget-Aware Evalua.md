---
aliases: ["When Error Mitigation Makes Things Worse: Budget-Aware Evaluation, Extrapolation Failure, and the Calibration Trust Boundary"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.38713"
url: "http://arxiv.org/abs/2609.38713v1"
published: "2026-09-30T00:49:42Z"
ingested: "2026-10-01T12:22:27Z"
authors:
  - "Guilin Zhang"
  - "Kai Zhao"
  - "Xiquan Cui"
  - "Henry Heng"
  - "Xu Chu"
  - "Aletta Johanna Blanken"
---

# When Error Mitigation Makes Things Worse: Budget-Aware Evaluation, Extrapolation Failure, and the Calibration Trust Boundary

## Abstract

> Error mitigation is expected to turn noisy quantum measurements into more useful estimates. We
> show that it can instead amplify error. Under control-offset miscalibration, the evaluated
> unconstrained zero-noise extrapolation (ZNE) estimators are worse than no mitigation on 38-63%
> of simulated instances and produce extreme tail errors. A small IBM Heron study finds worsening
> on 80-88% of 18 instances across two depths, with mean error 3.0-4.1 times the raw error. In
> simulation, the median changes little, so median-only monitoring misses the failures. We then
> compare methods at the same online shot budget per evaluation and report offline training cost
> separately. After that cost is amortized, a budget-conditioned neural corrector occupies the
> low-budget end of the simulated accuracy-cost frontier and falls back to the raw estimate when
> an ensemble disagrees; its hardware transfer remains unsuccessful. Finally, we treat provider-
> reported calibration as an input that is not bound to the execution-time device state. A white-
> box projected-gradient stress test on this metadata increases the corrector's error 8.1 times
> within the feature ranges used for training and evades the disagreement monitor on half of the
> worsened cases. Together, the results connect budget-aware evaluation, tail risk, and
> calibration integrity in near-term quantum learning pipelines.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

