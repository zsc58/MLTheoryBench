# Problem

## Setup

Let $(\Omega,\mathcal F,P)$ be a probability space, let $E$ be a real Banach space, and let $X\subset E$ be nonempty, open, and convex. Let $\phi:\Omega\times X\to\mathbb R$ satisfy $\phi(\cdot,x)\in L^2(P)$ for every $x\in X$, so in particular each such section is measurable. Assume there is $F\in L^2(P)$, $F\ge0$, such that, for $P$-almost every $\omega$ and all $x,y\in X$,
\[
|\phi(\omega,x)-\phi(\omega,y)|\le F(\omega)\,\|x-y\|_E.
\]
Assume also that for every $x\in X$, the map $\phi(\omega,\cdot)$ is Frechet differentiable at $x$ for $P$-almost every $\omega$. The exceptional null set may depend on $x$. Set $D\phi(\omega,x)=0$ wherever this derivative does not exist, and assume that for every $x\in X$ and $z\in E$, the map $\omega\mapsto D\phi(\omega,x)[z]$ is measurable.

Define the integral kernel
\[
k(x,y)=\int_\Omega \phi(\omega,x)\phi(\omega,y)\,dP(\omega),
\]
let $H_k$ be its RKHS, and let $\Phi:X\to H_k$ be the canonical feature map $\Phi(x)=k(x,\cdot)$. For a map $G:X\to H_k$, write
\[
\operatorname{Lip}(G)=\sup_{x\ne y}\frac{\|G(x)-G(y)\|_{H_k}}{\|x-y\|_E},
\]
where the supremum is taken in $[0,\infty]$ and is zero if there are no distinct points in $X$.

For $x\in X$ and $z\in E$, denote by $D_1D_2k(x,x)[z,z]$ the iterated mixed Frechet derivative at $(x,x)$, first in the second argument and then in the first, evaluated on $(z,z)$. The second differentiation is taken in the norm of the space of bounded linear functionals on $E$. Existence of this mixed derivative is part of the conclusion.

## Task

Prove that $\Phi$ is Frechet differentiable on $X$ and that
\[
\operatorname{Lip}(\Phi)
=\sup_{x\in X,\ \|z\|_E\le1}
\left(\int_\Omega |D\phi(\omega,x)[z]|^2\,dP(\omega)\right)^{1/2}
=\sup_{x\in X,\ \|z\|_E\le1}
\sqrt{D_1D_2k(x,x)[z,z]}.
\]
