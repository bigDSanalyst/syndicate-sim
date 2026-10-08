---
aliases: ["ProtocolMatch: Protocol-Dependent Model Selection for Scientific Dynamics Forecasting"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.10239"
url: "http://arxiv.org/abs/2610.10239v1"
published: "2026-10-07T15:23:27Z"
ingested: "2026-10-08T12:45:22Z"
authors:
  - "Lu Wei"
  - "Yufeng Wang"
  - "Haibin Ling"
---

# ProtocolMatch: Protocol-Dependent Model Selection for Scientific Dynamics Forecasting

## Abstract

> Scientific dynamics forecasting is often framed as an architecture choice, although deployment
> is also determined by observed history, rollout feedback, compute budget, physical objective,
> and test distribution. We formulate protocol-dependent model selection and introduce
> ProtocolMatch, a compute-matched, validation-selected, and failure-preserving evaluation
> framework. On driven quantum-spin dynamics, we compare recurrent, patched-attention, causal-
> attention, and low-rank linear predictors across three independently generated datasets. The
> causal-attention--recurrence ordering reverses as the training set grows within a fixed two-spin
> task, while a linear predictor has the lowest mean error in the six-spin local-observable
> comparison. Restricting observed history worsens every refreshed-history view but improves every
> closed-loop view in the four-spin study. A latest-state MLP has lower error than persistence on
> every dataset under state refresh across all five cells, yet its closed-loop rank varies by
> system and includes finite explosive errors. Physical penalties improve targeted consistency
> without reliably improving prediction error, and in-distribution intervals lose most coverage
> after a driving-frequency shift. Thus scientific model selection should return a predictor with
> its protocol and report accuracy, physical validity, and shifted-distribution reliability
> separately.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

