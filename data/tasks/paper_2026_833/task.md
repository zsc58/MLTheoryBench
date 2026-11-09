# Problem

## Setup

Let $d\ge1$ be an integer, and let $X=\bigoplus_{i=1}^d X_i$ be a finite direct sum of real Hilbert spaces with norm $\|\cdot\|$. Let $G>0$, and let $f:X\to\mathbb R$ be convex and $G$-Lipschitz:
\[
|f(u)-f(v)|\le G\|u-v\|\quad(u,v\in X).
\]
Let $\Gamma_0(X)$ denote the proper, lower-semicontinuous, convex extended-real-valued functions on $X$. Let $g\in\Gamma_0(X)$, define $F=f+g$, and assume $\operatorname*{argmin}F\ne\varnothing$; write $F_\star=\min_XF$.

Fix $\eta,\varepsilon>0$. Choose $s^n\in\partial f(x^n)$ for $n\ge1$ and set $s^0=0$. For $n\ge1$, define
\[
w_i^n=\varepsilon+\sqrt{\sum_{k=1}^{n}\|s_i^k-s_i^{k-1}\|^2},\qquad
W_n=\bigoplus_{i=1}^d w_i^n I_{X_i}.
\]
Starting from $x^1\in X$, generate
\[
x^{n+1}=\operatorname*{argmin}_{y\in X}\left\{g(y)+\frac1{2\eta}\left\|y-\left(x^n-\eta W_n^{-1}s^n\right)\right\|_{W_n}^2\right\},
\]
where $\|z\|_{W_n}^2=\langle W_nz,z\rangle$. Assume $(x^n)$ is bounded. For $N\ge2$, let
\[
\bar x^N=\frac1{N-1}\sum_{k=2}^{N}x^k.
\]

## Task

Prove that there exist constants $A,B\ge0$, independent of $N$, such that for every $N\ge2$,
\[
0\le F(\bar x^N)-F_\star\le \frac{A}{N-1}+\frac{B}{\sqrt{N-1}}.
\]
In particular, $F(\bar x^N)-F_\star=O(N^{-1/2})$ as $N\to\infty$.
