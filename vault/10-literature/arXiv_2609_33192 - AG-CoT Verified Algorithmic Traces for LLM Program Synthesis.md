---
aliases: ["AG-CoT: Verified Algorithmic Traces for LLM Program Synthesis on Clifford Circuits"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.33192"
url: "http://arxiv.org/abs/2609.33192v1"
published: "2026-09-27T04:19:00Z"
ingested: "2026-09-29T12:04:08Z"
authors:
  - "Lu Wei"
  - "Yufeng Wang"
  - "Chenfeng Cao"
  - "Lu Pang"
  - "Haibin Ling"
---

# AG-CoT: Verified Algorithmic Traces for LLM Program Synthesis on Clifford Circuits

## Abstract

> Scientific code generation can produce executable programs that fail to compute the intended
> scientific object. We study this problem in language-model synthesis of Clifford circuits, which
> prepare the stabilizer states used in quantum error correction and admit exact classical
> verification. In our target-conditioned framework, each target is given as compact signed
> stabilizer generators, and an exact verifier checks the generated OpenQASM circuits. We
> supervise models with Aaronson-Gottesman chain-of-thought (AG-CoT) traces checked by the
> verifier, and continue training on model generations that the verifier accepts. Across two
> independently trained model families (3B and 7B), AG-CoT supervision multiplies greedy-decode
> state-equivalence accuracy by four to six times over circuit-only baselines, and verifier-
> filtered continuation training adds a further consistent gain atop both. A complementary 32B
> study shows that supervised models achieve near-perfect syntax and Clifford validity while the
> strongest direct model reaches 6.14% state equivalence per target, rising to over 10% under
> verifier-guided selection with multiple candidates. These results show that algorithmic trace
> supervision gives a large, statistically significant gain in both model families and that
> verifier-filtered continuation adds a further repeated gain. The persistent gap between Clifford
> validity and state equivalence confirms that exact verification is necessary: a circuit can be
> syntactically and physically valid yet prepare the wrong quantum state.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

