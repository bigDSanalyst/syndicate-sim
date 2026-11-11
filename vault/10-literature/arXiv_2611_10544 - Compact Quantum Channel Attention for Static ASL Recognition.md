---
aliases: ["Compact Quantum Channel Attention for Static ASL Recognition: A Controlled Study with Parameter-Matched Baselines"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.10544"
url: "http://arxiv.org/abs/2611.10544v1"
published: "2026-11-07T07:20:37Z"
ingested: "2026-11-11T13:29:45Z"
authors:
  - "Ronak Bhalgami"
  - "Deep Kothadiya"
  - "Nikita Bhatt"
---

# Compact Quantum Channel Attention for Static ASL Recognition: A Controlled Study with Parameter-Matched Baselines

## Abstract

> Hybrid quantum-classical models often report good accuracy on image tasks, but it is rarely
> clear whether the quantum part is responsible. This paper proposes QCA-DenseNet, a static
> American Sign Language (ASL) recognition pipeline in which an eight-qubit variational circuit
> acts as a channel-attention gate on DenseNet121 features. The quantum channel attention (QCA)
> gate has 17,464 parameters, 7.51 times fewer than a squeeze-and-excitation (SE) block. The
> pipeline is tested on 1,815 MU HandImages images by holding out one of five signers at a time,
> and a frozen-backbone ablation uses small parts of the Kaggle ASL Alphabet data. On unseen
> signers, QCA-DenseNet reaches 94.50% mean accuracy, above SE (93.72%) and within 0.28 points of
> the best model. A matched classical MLP and a model without attention perform about the same,
> and no difference is significant. QCA gives a much smaller attention gate without a detectable
> loss in accuracy, but no quantum advantage.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

