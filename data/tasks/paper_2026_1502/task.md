# Problem

## Setup

Fix integers $d,n\ge1$ and nonzero data vectors $x^1,\ldots,x^n\in\mathbb R^d$. Let $S^{d-1}$ be the unit sphere, and let $\mathcal M(S^{d-1})$ be the finite signed Radon measures on the sphere, with total-variation norm $\|\cdot\|_{\rm TV}$. All vector norms and orthogonal projections below are Euclidean. For $\sigma(t)=\max\{t,0\}$ define
\[
(K\mu)_j=\int_{S^{d-1}}\sigma(\langle w,x^j\rangle)\,d\mu(w),\qquad j=1,\ldots,n,
\]
and
\[
K_*p(w)=\sum_{j=1}^n p_j\sigma(\langle w,x^j\rangle),\qquad p\in\mathbb R^n.
\]
Given $y_0,y_\zeta\in\mathbb R^n$ and $\lambda>0$, consider the primal problems
\[
\min_{\mu\in\mathcal M(S^{d-1})}\ \|\mu\|_{\rm TV}\quad\text{subject to }K\mu=y_0,
\]
\[
\min_{\mu\in\mathcal M(S^{d-1})}\ \frac12\|K\mu-y_\zeta\|_2^2+\lambda\|\mu\|_{\rm TV}.
\]
Their corresponding dual optimization problems are
\[
\sup_{p\in\mathbb R^n:\,\|K_*p\|_\infty\le1}\langle y_0,p\rangle,
\qquad
\sup_{p\in\mathbb R^n:\,\|K_*p\|_\infty\le1}\left(\langle y_\zeta,p\rangle-\frac\lambda2\|p\|_2^2\right),
\]
where $\|K_*p\|_\infty=\sup_{w\in S^{d-1}}|K_*p(w)|$.

Write $[n]=\{1,\ldots,n\}$ and $H_i=\{w\in\mathbb R^d:\langle w,x^i\rangle=0\}$. For $J\subseteq[n]$, define
\[
L_J=\{v\in\mathbb R^d:\langle v,x^i\rangle=0\text{ for every }i\notin J\}.
\]
For a binary vector $\pi\in\{0,1\}^{J}$, define the spherical stratum
\[
S_{J,\pi}=\left\{w\in L_J\cap S^{d-1}:
\begin{array}{ll}
\langle w,x^i\rangle>0&\text{if }i\in J,\ \pi_i=1,\\
\langle w,x^i\rangle<0&\text{if }i\in J,\ \pi_i=0
\end{array}\right\}.
\]

For integers $m,r\ge1$, let $\Xi(m,r)$ be the maximal number of regions, meaning connected components of the complement, formed by $m$ hyperplanes through the origin in $\mathbb R^r$. Set $\Xi(0,r)=1$ for $r\ge0$, $\Xi(m,0)=0$ for $m\ge1$, and $\Xi(m,r)=0$ for $r<0$. Define
\[
B(n,d)=\max_{0\le k\le n}\binom nk\,\Xi(n-k,d-k).
\]

## Task

Prove that, for every minimizer $\mu$ of either primal problem, there exists an optimizer $p$ of its corresponding dual problem and a representation
\[
\mu=\sum_{q=1}^{N}c_q\,\delta_{w_q},\qquad 0\le N\le B(n,d),
\]
with distinct $w_q\in S^{d-1}$ and nonzero real coefficients $c_q$. The empty sum represents the zero measure. The same $p$ must apply to every atom in this representation.

For every atom, prove that there exist $J\subseteq[n]$, $\pi\in\{0,1\}^{J}$, and $s_q\in\{-1,1\}$ such that $w_q\in S_{J,\pi}$, the following denominator is nonzero, and
\[
w_q=s_q\,\frac{\operatorname{Proj}_{L_J}\left(\sum_{i\in J}p_i\pi_i x^i\right)}{\left\|\operatorname{Proj}_{L_J}\left(\sum_{i\in J}p_i\pi_i x^i\right)\right\|_2}.
\]

Also prove $B(n,d)\le3^n$ and, for fixed $d$ and $n>d$, $B(n,d)=O(n^d)$ with an implied constant depending only on $d$. Thus the same bounds hold for $N$. The interpolation and regularized assertions hold independently, with their respective dual optimizers and atom representations.
