---
aliases: ["Fast Quantum Algorithms for Learning Linear Threshold Functions"]
tags: [literature/arxiv, status/triage]
arxiv_id: "2609.40331"
url: "http://arxiv.org/abs/2609.40331v1"
published: "2026-09-30T17:56:41Z"
ingested: "2026-10-01T12:22:27Z"
authors:
  - "Aleksandrs Krivcenko"
  - "Tuyen Nguyen"
  - "Ronald de Wolf"
---

# Fast Quantum Algorithms for Learning Linear Threshold Functions

## Abstract

> Linear threshold functions are $f_{w,θ}(x)=\text{sign}(\langle x,w \rangle -θ)$, where the
> weight vector $w\in\mathbb{R}^n$ is a unit vector, $θ\in\mathbb R$ is a threshold, and typically
> $x\in\mathbb{R}^n$ or $x\in\{-1,1\}^n$. When $θ=0$, the LTF is called homogeneous, and we write
> $f_w:=f_{w,0}$. Such functions are among the most important objects in machine learning, since
> they serve to linearly discriminate positive and negative examples. We give three positive
> results about learning LTFs: 1. Suppose we can make real-domain queries, meaning we can compute
> $f_{w,θ}(x)$ at any $x\in\mathbb{R}^n$ of our choice. We give a quantum algorithm that learns
> $f_{w,θ}$ up to Euclidean error~$ε$ using $O(\log(n/ε))$ membership queries and
> $\widetilde{O}(n)$ other gates. Then we have also learned $f_{w,θ}$ up to error $O(ε)$ when $x$
> is Gaussian. Classical algorithms need $Ω(n\log(1/ε))$ queries. 2. A homogeneous LTF $f_w$ on
> domain $\{-1,1\}^n$ where $w$ has only $k$ nonzero entries of the same value, is the Majority
> function on the support of $w$. Belovs gave a bounded-error quantum algorithm that identifies
> the hidden support exactly (and hence learns $f_w$) using $O(k^{1/4})$ queries. We give an
> exponential improvement, using $O(\log k)$ queries. 3. Suppose we have a unitary $U$ that can
> produce (discretized) \emph{quantum examples} under Gaussian measure, corresponding to $\int_x
> \sqrt{γ_n(x)}|x\rangle |f_w(x)\rangle dx$. This is a weaker access model than membership
> queries. We give a quantum algorithm based on the efficient \emph{Hermite transform} of Jain et
> al.\ to learn homogeneous LTFs~$f_w$ with error~$ε$ under the Gaussian distribution, using
> $O(n^{1/4}/\sqrtε)$ applications of $U$ and $U^\dagger$ and $\widetilde{O}(n^2/ε^4)$ other
> gates.

---
## Reading Notes
*Annotations below. Update the status tag as you triage; the arxiv_id frontmatter must survive edits - it is the dedup key.*

