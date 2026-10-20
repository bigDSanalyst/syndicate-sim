---
aliases: ["Simulation-Based Quantum Forensics for QKD: Machine Learning Attack Detection and Signature Extraction"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2610.25203"
url: "http://arxiv.org/abs/2610.25203v1"
published: "2026-10-18T11:48:42Z"
ingested: "2026-10-20T10:53:29Z"
authors:
  - "Madhab Chandra Das"
  - "Sajid Ahmed"
  - "Uzair Hussain"
  - "Van Vung Pham"
---

# Simulation-Based Quantum Forensics for QKD: Machine Learning Attack Detection and Signature Extraction

## Abstract

> Quantum Key Distribution (QKD) supports secure key establishment under ideal protocol
> assumptions, but practical systems remain exposed to implementation-level attacks against
> optical channels, detectors, and controller behavior. This study presents Quantum Forensic Log
> (QF-LOG), a simulation-based forensic framework for analyzing aggregated QKD operational logs
> rather than raw quantum states. QF-LOG uses four observable features: quantum bit error rate
> (QBER), photon count, latency in milliseconds, and abort flag. The framework classifies normal
> operation and three simulated attack-related conditions: partial intercept-resend, detector-
> blind, and fiber-tap. A physics-inspired Generator-A dataset with 5 million balanced records was
> constructed using explicit mathematical generation models for all four features. A transparent
> threshold baseline, logistic regression, random forest, and XGBoost were evaluated on
> Generator-A. The full-feature learning models achieved macro F1-scores from 0.8211 to 0.8243 and
> outperformed the transparent two-feature comparator. Feature diagnostics showed that QBER
> contributed most, followed by latency in milliseconds and photon count, while no single feature
> reproduced the full feature set performance. Robustness was assessed on a separately generated
> Generator-B dataset of 5 million records that uses the same governing equations under shifted
> simulated operating parameters. Without retraining or tuning, their macro F1-scores decreased to
> values from 0.5645 to 0.5669. These findings show that QF-LOG can support interpretable forensic
> classification in a controlled synthetic setting, but stable internal evaluation does not
> establish reliability under changed simulated QKD operating conditions. The framework provides a
> documented basis for future evaluation across broader simulated settings and hardware-generated
> QKD logs.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

