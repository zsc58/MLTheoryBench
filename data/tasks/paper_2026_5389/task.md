# Problem

## Setup

Let \(F,S:\mathbb R^d\to\mathbb R\) be twice continuously differentiable, where \(F\) is a predictive loss and \(S\) is a representation-entropy surrogate. Fix \(\lambda>0\), and consider any global solution \(w:[0,\infty)\to\mathbb R^d\) of
\[
\dot w_t=-\nabla F(w_t)-\lambda\nabla S(w_t).
\]

Suppose there are constants \(\mu>0\), \(C\ge0\), and \(R>0\) such that, whenever \(\|w\|>R\),
\[
\left\langle \nabla S(w),\nabla^2S(w)\nabla S(w)\right\rangle
\ge \mu\|\nabla S(w)\|^2
\]
and
\[
\left|\left\langle \nabla S(w),\nabla^2S(w)\nabla F(w)\right\rangle\right|
\le C\|\nabla S(w)\|.
\]
Define
\[
G(t)=\|\nabla S(w_t)\|^2.
\]
All gradients, Hessians, inner products, and norms are Euclidean.

## Task

Prove that there exists a finite constant \(M\), independent of the chosen solution, such that every solution has a finite time \(T\) for which
\[
G(t)\le M\qquad\text{for all }t\ge T.
\]
Moreover, show that \([0,M]\) can be chosen forward invariant for \(G\): once \(G(t)\le M\), it remains at most \(M\) thereafter.
