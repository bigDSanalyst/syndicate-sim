---
aliases: ["QCap: a physics-corrected graph neural network for the capacitance matrix of any planar superconducting device layout"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2611.22057"
url: "http://arxiv.org/abs/2611.22057v1"
published: "2026-11-17T01:34:18Z"
ingested: "2026-11-18T15:01:54Z"
authors:
  - "Sadman Ahmed Shanto"
  - "Saikat Das"
  - "Eli M. Levenson-Falk"
---

# QCap: a physics-corrected graph neural network for the capacitance matrix of any planar superconducting device layout

## Abstract

> Electromagnetic simulations of device layouts to extract capacitance are computationally
> intensive, a major obstacle to accurate design of circuit devices. Machine learning models can
> bypass these simulations, but previous approaches have been restricted to layouts using only
> particular components, and require thousands of simulations of those same components as training
> data. We present QCap, a model that accurately predicts the Maxwell capacitance matrix of an
> arbitrary superconducting device layout in seconds, compared to minutes to hours of Ansys Q3D
> simulations. We develop a novel design-embedding algorithm that converts the layout into a
> universal graph format, allowing the model to work with any layout created with any tool. To
> achieve high accuracy, we obtain a coarse physics prior from a fast method of moments simulation
> of capacitance, then train the model to correct this prior. On 4,009 test designs withheld from
> training data the model outputs agree with Q3D simulations to a median error of 0.177%, and on
> never-seen component families it stays below 1% error. We demonstrate the model's scaling by
> obtaining the capacitance matrix of a 9-superconducting-qubit device in 12 seconds on a laptop
> (compared to 19.9 h and 228 GB of memory in Ansys) with sub-percent error, and capacitance of a
> (too large to simulate) 100-qubit, 781-conductor device in 3.4 min on a laptop. We provide the
> open-source models and data on SQuADDS and Hugging Face. Our results provide a powerful tool for
> large-scale accurate circuit design and guide the development of models to bypass other physical
> simulations.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

