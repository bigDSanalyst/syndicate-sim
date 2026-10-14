---
aliases: ["Architectural Robustness to Label Noise Using Variational Quantum Circuits for Medical Image Classification"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.16153"
url: "http://arxiv.org/abs/2610.16153v1"
published: "2026-10-12T04:24:27Z"
ingested: "2026-10-14T11:06:59Z"
authors:
  - "Yasoda Lasiru Ariyarathna Epa"
  - "Yaseema Rusiru Ariyarathna Epa"
  - "Sandaru Liyanaarachchi"
  - "Kavindu Jayathissa"
  - "Kalana G. Abeywardena"
  - "Kithmin Wickremasinghe"
  - "Theshani Nuradha Piliththuwasam Gallage"
  - "Chamira U. S. Edussooriya"
---

# Architectural Robustness to Label Noise Using Variational Quantum Circuits for Medical Image Classification

## Abstract

> Label noise is prevalent in medical image datasets, arising from observer disagreement and
> ambiguous cases and deep networks memorize the mislabeled examples at the cost of
> generalization. Current solutions such as loss correction and sample selection add training
> complexity and generally assume the noise rate is known or estimable. This paper investigates
> whether robustness can be obtained architecturally, by routing a frozen backbone's features
> through a low-dimensional bounded bottleneck and classifying them with a head whose function
> class is intrinsically smooth. Variational quantum circuits with angle encoding and a linear
> cost function realise exactly such a class. Their use in medical imaging, however, has been
> limited by the small number of qubits available on noisy intermediate-scale devices, which
> typically restricts inputs to low-resolution grayscale images. We therefore couple a frozen
> ImageNet-pretrained ViT-B/16 backbone to a trainable linear bottleneck and an eight-qubit
> variational quantum circuit, allowing 224x224 RGB inputs to be processed. Under clean labels the
> model leads five of six MedMNISTv2 benchmarks against published hybrid quantum-classical models,
> with margins of 17.4 and 15.7 percentages on BloodMNIST and PathMNIST. The advantage emerges
> under corrupted labels. At symmetric noise rates of 30% and 50% the model outperforms many
> published quantum and noise-robust classical baselines on all six datasets without any explicit
> noise-handling component. Against a control that shares the backbone, bottleneck, parameter
> count and optimizer and replaces only the circuit with a ReLU layer, it retains 89.75% accuracy
> on PathMNIST at 50% noise where the control falls to 78.96%. Direct measurement of training
> dynamics shows that this advantage is not an inability to fit corrupted labels, which the
> circuit retains, but greater stability under prolonged training on them.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

