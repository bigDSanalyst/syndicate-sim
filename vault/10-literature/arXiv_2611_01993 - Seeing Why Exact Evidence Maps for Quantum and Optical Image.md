---
aliases: ["Seeing Why: Exact Evidence Maps for Quantum and Optical Image Classifiers"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.01993"
url: "http://arxiv.org/abs/2611.01993v1"
published: "2026-11-01T15:27:02Z"
ingested: "2026-11-03T13:34:16Z"
authors:
  - "Teerawat Tongloy"
  - "Rangsan Jomtarak"
---

# Seeing Why: Exact Evidence Maps for Quantum and Optical Image Classifiers

## Abstract

> When an image classifier decides, we can usually only estimate why. For quantum and all-optical
> classifiers that act linearly on amplitude-encoded pictures up to the measurement, with no
> trained classical network before or after them, the decomposition needs no approximation: each
> class's probability above its no-information share splits exactly into contributions of the
> encoded amplitudes, shown as Born evidence maps (BEM) over the picture and measurable on the
> hardware that classifies. For the quadratic form behind each class probability it equals
> Integrated Gradients from a zero baseline, in closed form. Deleting the 5 % of pixels with the
> highest evidence drops accuracy from 73 % to 9 %, as occlusion does with 1,024 extra runs per
> picture, whereas gradient saliency removes much less. One architecture serves both: a Fourier-
> plane mask followed by a brickwall circuit on qubits or by phase plates on a lens bench, read by
> a Born headroom readout with no trained parameter; centring each picture on its own mean lets
> dark features count as much as bright ones. In simulation, four phase plates at a single
> wavelength reach 72.3 % on Caltech-10 colour photographs (96.8 % on MNIST, 86.7 % on Fashion-
> MNIST, 47.9 % on colour CIFAR-10). On IBM's ibm_kingston, with the mask applied before
> approximate loading, 300 Caltech-10 test pictures were classified at 37.7 % against 10 % by
> chance (56.3 % in exact simulation), and 2x2 maps of ten correctly and confidently classified
> pictures, estimated on the chip, agreed with the exact ones (r = 0.77). The maps also revealed a
> shortcut in the data.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

