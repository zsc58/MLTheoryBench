# Problem

## Setup

Let $n\ge1$ be an integer, set $I=\{1,\ldots,n\}$, and let $H$ be a real Hilbert space with inner product $\langle\cdot,\cdot\rangle$ and norm $\|\cdot\|$. Let
\[
S=\{(u_i,y_i):i\in I\},\qquad u_i\in H,\quad y_i\in\{-1,1\},
\]
be a finite sample indexed by $I$. Assume the hard-margin constraints are feasible: there exists $f\in H$ such that $y_i\langle f,u_i\rangle\ge1$ for every $i\in I$.

For each $T\subseteq I$, let $f_T$ denote the minimum-norm element of $H$ satisfying $y_j\langle f,u_j\rangle\ge1$ for all $j\in T$. Write $f_S=f_I$. For $i\in I$, write $S\setminus i$ for the sample with the $i$th pair removed and $f_{S\setminus i}=f_{I\setminus\{i\}}$. Define
\[
R=\max_{1\le i\le n}\|u_i\|.
\]

## Task

Prove the deterministic leave-one-out hinge-margin bound
\[
\frac1n\sum_{i=1}^n\max\!\left\{1-y_i\left\langle f_{S\setminus i},u_i\right\rangle,0\right\}
\;\le\;
\frac{R^2\|f_S\|^2}{n}.
\]
