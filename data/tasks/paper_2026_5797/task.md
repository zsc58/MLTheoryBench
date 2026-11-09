# Problem

## Setup

Let $d\ge 2$ and let $S=(S_1,\ldots,S_d)$ have mutually independent components. Assume each component is centered, has variance one, and has a smooth strictly positive density; assume that at most one component has a Gaussian distribution. Let $G=\mathcal N(0,1)$. For any real-valued random variable $U$ with finite second moment, define
\[
C(U)=W_2^2(\mathcal L(U),G),
\]
where $W_2^2(\mu,\nu)$ is the infimum of $\mathbb E|U'-V'|^2$ over all couplings $(U',V')$ with marginals $\mu,\nu$. Let $O(d)$ be the set of real orthogonal $d\times d$ matrices.

## Task

Prove the following integrated theorem.

1. For every $u\in\mathbb R^d$ with $\|u\|_2=1$ and at least two nonzero coordinates,
\[
C\!\left(\sum_{j=1}^d u_jS_j\right)
<\sum_{j=1}^d u_j^2 C(S_j).
\]

2. For every $Q=(Q_{ij})\in O(d)$,
\[
\sum_{i=1}^d C\!\left(\sum_{j=1}^d Q_{ij}S_j\right)
\leq\sum_{j=1}^d C(S_j),
\]
and equality holds if and only if $Q$ is a signed permutation matrix (each row and each column has exactly one nonzero entry, equal to $1$ or $-1$).
