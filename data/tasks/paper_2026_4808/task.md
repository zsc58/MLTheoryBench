# Problem

## Setup

Let \(M\subset\mathbb R^d\) be a nonempty compact smooth embedded \(m\)-dimensional manifold, with \(m<d\), equipped with the induced Riemannian metric and Sobolev space \(H^1(M)\). Its intrinsic distance is the infimum of lengths of paths in \(M\) joining the two points, with value \(+\infty\) when no such path exists.

Let \(k:\mathbb R^d\times\mathbb R^d\to\mathbb R\) be a symmetric positive-definite kernel whose native space \(H_k(\mathbb R^d)\) equals \(H^s(\mathbb R^d)\) as a set, with equivalent norms. Let \(k_M=k|_{M\times M}\), and denote its native space by \(H_{k_M}(M)\). Set
\[
\widetilde s=s-\frac{d-m}{2},
\]
and assume \(\widetilde s>m/2\) and \(\lceil\widetilde s\rceil\ge1\).

Let \(f\in H_{k_M}(M)\cap H^1(M)\), and let \(\varepsilon,\delta>0\). For a finite nonempty node set \(X=\{x_i\}_{i=1}^n\subset M\), define the intrinsic fill distance
\[
h_{X,M}=\sup_{x\in M}\min_{1\le i\le n}\operatorname{dist}_M(x,x_i).
\]
Suppose a chosen finite restricted-kernel expansion, with real coefficients,
\[
g=\sum_{i=1}^n\alpha_i k_M(\cdot,x_i)
\]
satisfies \(\|g-f\|_{H^1(M)}<\varepsilon\).

Let \(T:H^1(M)\to H^1(M)\) be bounded and linear. Assume that, for every \(x\in M\), the section \(k_M(\cdot,x)\) belongs to \(H^1(M)\), the learned output \(\mathcal N_\theta[k_M(\cdot,x)]\) belongs to \(H^1(M)\), and
\[
\|\mathcal N_\theta[k_M(\cdot,x)]-T[k_M(\cdot,x)]\|_{H^1(M)}<\delta.
\]
For the chosen expansion define
\[
\mathcal N^e_\theta[g]=\sum_{i=1}^n\alpha_i\mathcal N_\theta[k_M(\cdot,x_i)].
\]

## Task

Prove that there are finite nonnegative constants \(C_1,C_2\), depending only on \(T\) and the chosen expansion, such that
\[
\|\mathcal N^e_\theta[g]-T[f]\|_{H^1(M)}\le C_1\varepsilon+C_2\delta.
\]
For a fixed \(T\) and expansion, the constants must be independent of the positive tolerances for which the assumptions hold; no uniformity over different expansions is required.

Explain how effective smoothness and intrinsic fill distance govern attainable reconstruction accuracy, and justify both error contributions from the stated assumptions.
