---
aliases: ["Bounding Retraining Equivalence and the Deletion Floor in Materials Machine Unlearning"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.35635"
url: "http://arxiv.org/abs/2609.35635v1"
published: "2026-09-28T17:03:08Z"
ingested: "2026-09-29T12:04:08Z"
authors:
  - "Can Polat"
  - "Mustafa Kurban"
  - "Erchin Serpedin"
  - "Hasan Kurban"
---

# Bounding Retraining Equivalence and the Deletion Floor in Materials Machine Unlearning

## Abstract

> In materials machine learning, closely related retained structures can sustain accurate property
> predictions even after removing a specific record, rendering post-deletion prediction error an
> ambiguous metric for machine unlearning. To resolve this ambiguity, we define the deletion floor
> as the expected target loss under a specified retraining procedure at the deleted request.
> Standard indistinguishability constraints yield a sharp interval bounding an update's target
> loss around this baseline reference. Theoretically, a conditional neighbor bound links a low
> deletion floor directly to retained fit, prediction regularity, and local label agreement, while
> an exact ridge identity isolates residual fit from the prediction change induced by record
> deletion. Empirically, controlled redundancy sweeps show an $\approx 8\times$ drop in median
> normalized retraining loss when one retained relative remains after deletion. Across two
> distinct fitting regimes in a paired Materials Project study, the lower-floor regime also
> exhibits a larger prediction change on more than 50% of the shared requests. Systematic
> comparisons against approximate updates and the original model decouple deliberate target
> suppression from preserved overall model utility. Consequently, request-level unlearning
> evaluations should report reference loss, prediction change, and retained utility together,
> interpreting post-deletion accuracy against what retraining itself leaves behind.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

