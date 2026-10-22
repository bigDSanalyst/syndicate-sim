---
aliases: ["Can Quantum Layers offer Performance and Security Advantages in Vision-Language Models?"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.28964"
url: "http://arxiv.org/abs/2610.28964v1"
published: "2026-10-20T22:28:17Z"
ingested: "2026-10-22T11:06:12Z"
authors:
  - "Md Khalid Syfullah"
  - "Alvi Ataur Khalil"
---

# Can Quantum Layers offer Performance and Security Advantages in Vision-Language Models?

## Abstract

> As quantum computing moves from the noisy intermediate-scale quantum (NISQ) era toward early
> fault-tolerant quantum computing (EFTQC), quantum-enhanced AI is shifting from a conceptual idea
> to experimental research. Quantum components are expected to extend the capabilities of existing
> AI systems, yet it remains unclear how such components will help within large multimodal models.
> In this study, we try to answer that question for vision-language models (VLMs) using
> classically simulated quantum layers. With LLaVA-OneVision as the backbone, we evaluate 4- and
> 8-qubit basic-ring and strongly entangling circuits at four insertion and four replacement
> locations. Insertion adds quantum layers to the classical model, while replacement substitutes
> them for classical components. Using the same setup, we compare performance and computational
> cost between classical and quantum-classical hybrid models. On the Visual Spatial Reasoning
> dataset, inserting a quantum layer after the visual projector reaches 80.7% development
> accuracy, 2.28 percentage-points above classical full fine-tuning. Replacing the final decoder
> feed-forward sublayer retains 79.22% accuracy with 13.07 million fewer trainable parameters.
> Quantum insertion can thus improve accuracy, and selective replacement can reduce parameters.
> These benefits depend strongly on where the quantum layer is inserted or which classical
> component it replaces: earlier replacements lower accuracy, and fewer parameters do not reliably
> shorten training or reduce computation. To assess potential security benefits, we evaluated the
> robustness of quantum-classical hybrid models under six attack settings. Overall, our study maps
> where quantum layers help and hurt within VLMs, offering a starting point for hybrid VLM design;
> whether these gains generalize remains open. The code is available at https://github.com/TITANS-
> Lab-Artifacts/QuantumVLM.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

