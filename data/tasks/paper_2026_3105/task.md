# Problem

## Setup

Let $n,K$ be positive integers and let $[n]=\{1,\ldots,n\}$ be partitioned into $K$ nonempty clusters $C_1,\ldots,C_K$. Define the partition matrix $Z\in\mathbb{R}^{n\times n}$ by
\[
Z=\sum_{k=1}^K\frac{1}{|C_k|}\,\mathbf 1_{C_k}\mathbf 1_{C_k}^{\mathsf T}.
\]
Thus $Z_{ij}=1/|C_k|$ when $i,j\in C_k$ and $Z_{ij}=0$ otherwise.

Let $\mathcal G$ index protected groups. For each $g\in\mathcal G$, let $P_g\subseteq[n]$ be nonempty and let $e^g\in\{0,1\}^n$ be its indicator vector. Fix parameters $\alpha_g,\beta_g\in[0,1]$ and $\tau_g\in(0,1/K]$ for every $g$.

The clustering is called proportional-representation fair if
\[
\beta_g\le\frac{|C_k\cap P_g|}{|C_k|}\le\alpha_g
\quad\text{for all }g\in\mathcal G\text{ and }k=1,\ldots,K,
\]
and tau-ratio fair if
\[
\frac{|C_k\cap P_g|}{|P_g|}\ge\tau_g
\quad\text{for all }g\in\mathcal G\text{ and }k=1,\ldots,K.
\]

## Task

Prove that, for the partition matrix $Z$, proportional-representation fairness is equivalent to
\[
\beta_g\le\sum_{i=1}^n Z_{ij}e_i^g\le\alpha_g
\quad\text{for every }g\in\mathcal G,\ j\in[n],
\]
and tau-ratio fairness is equivalent to
\[
\sum_{i=1}^n Z_{ij}e_i^g
\ge \tau_g|P_g|\,Z_{jj}
\quad\text{for every }g\in\mathcal G,\ j\in[n].
\]
Consequently, both fairness notions have exact linear inequality characterizations in the partition-matrix variables.
