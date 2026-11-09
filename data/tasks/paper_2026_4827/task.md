# Problem

## Setup

Let `d_s,d_a` be positive integers. Define the state space `\mathcal X=[0,1]^{d_s}` and the action space `\mathcal A=[0,1]^{d_a}`. Let `M\in[0,\infty)^{d_a\times d_s}` have every row summing to one, and let `d\in\mathbb R^{d_s}` be fixed. For a fixed action `a\in\mathcal A`, set
\[
c=aM+d\in\mathbb R^{d_s}
\]
and define `F_a:\mathcal X\to\mathcal X` coordinatewise by
\[
(F_a(x))_i=\phi(x_i+c_i),\qquad i=1,\ldots,d_s,
\]
where
\[
\phi(t)=\frac1\pi\arccos(\cos(2\pi t)).
\]
Let `S` be uniformly distributed on `\mathcal X` (Lebesgue probability measure).

## Task

Prove that for every fixed action `a` and every Borel set `B\subseteq[0,1]^{d_s}`,
\[
\Pr\{F_a(S)\in B\}=\operatorname{Leb}(B).
\]
Equivalently, the transition output has exactly the uniform distribution on `[0,1]^{d_s}` for every fixed action-dependent shift.
