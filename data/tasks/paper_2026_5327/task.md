# Problem

## Setup

Let $m,n$ be positive integers, let $A\in\mathbb R^{m\times n}$ and $b\in\mathbb R^m$, and assume that

$$
C=\{y\in\mathbb R^n:Ay\leq b\}
$$

is nonempty. Define the Euclidean projection map

$$
g(z)=\mathop{\rm argmin}_{y\in C}\frac12\|y-z\|_2^2,
\qquad z\in\mathbb R^n.
$$

For $I\subseteq[m]$, let $A_I$ and $b_I$ denote the corresponding rows and coordinates. Write $(\cdot)^+$ for the Moore-Penrose pseudoinverse and set

$$
P_I=I_n-A_I^T(A_IA_I^T)^+A_I,
\qquad
c_I=A_I^T(A_IA_I^T)^+b_I.
$$

For $I=\varnothing$, use $P_I=I_n$ and $c_I=0$.

## Task

Prove the following theorem.

There are an exceptional set $E\subseteq\mathbb R^n$, contained in a finite union of proper affine hyperplanes, and finitely many pairwise disjoint open polyhedral cells $R_1,\ldots,R_N$ whose union is $\mathbb R^n\setminus E$, such that for every $k$ there is an index set $I_k\subseteq[m]$ satisfying

$$
A_{I_k}g(z)=b_{I_k}
\quad\text{and}\quad
g(z)=P_{I_k}z+c_{I_k}
\qquad(z\in R_k).
$$

Moreover, at every point $z$ where $g$ is differentiable, including any such point in $E$, one can choose a cell $R_k$ whose closure contains $z$ so that $A_{I_k}g(z)=b_{I_k}$ and

$$
Dg(z)=P_{I_k}=I_n-A_{I_k}^T(A_{I_k}A_{I_k}^T)^+A_{I_k}.
$$

Consequently, every eigenvalue of $Dg(z)$ belongs to $\{0,1\}$, and for all $v\in\mathbb R^n$ and $u\in\mathbb R^{|I_k|}$,

$$
A_{I_k}Dg(z)v=0,
\qquad
Dg(z)A_{I_k}^Tu=0.
$$

Thus infinitesimal output changes lie tangent to the active constraints, while differentiation annihilates their normal directions.
