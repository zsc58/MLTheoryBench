# Problem

## Setup

Let n>=2 be an integer. Let Lambda~N(0,1) and G~N(0,I_n) be independent, and let Q be the law of X=Lambda G. Two laws on R^n match moments through degree k if every monomial of total degree at most k has a finite absolute expectation under both laws and the two expectations agree.

For positive integers k,m and laws P,Q with finite moments through degree 2k, define
\[
\operatorname{LDA}_{\le k}^{(m)}(P,Q)
=\sup_{\substack{f:(\mathbb R^n)^m\to\mathbb R\ \text{polynomial}\,;\ \deg f\le k\\
\operatorname{Var}_{Q^{\otimes m}}(f)=1}}
\left|\mathbb E_{P^{\otimes m}}f-\mathbb E_{Q^{\otimes m}}f\right|.
\]
Here the product laws mean m independent samples, and degree means total degree over all sample coordinates. Write delta_0 for the point mass at the origin.

In the relative-perturbation observation model, fix a law D on R^n, p in [0,1), and epsilon>=0. Draw m independent latent samples from D. Independently for each sample, with probability p replace it by an independent draw from Q, and otherwise retain it. Write x_i for the resulting samples. After observing these samples, an adversary may choose arbitrarily correlated measurable perturbations z_i satisfying ||z_i||<=epsilon||x_i||. The observations are y_i=x_i+z_i.

For m>=2 define the following test. Set a_i=y_i/||y_i|| when y_i!=0 and set a_i=0 when y_i=0. Enumerate all unordered pairs {i,j}, and accept the planted hypothesis if and only if some n-by-2 matrix (a_i,a_j) has smallest singular value at most 1/2.

## Task

Prove the following integrated theorem, with universal constants a_0,B,C,c>0.

For every positive integer k there are a law P_k, a one-dimensional linear subspace S_k, and alpha_k in (0,1) such that
\[
P_k(S_k)\ge\alpha_k\ge a_0(k+1)^{-B k^2},
\]
and P_k matches the moments of Q through degree k. This lower bound is the endpoint-explicit interpretation of alpha_k>=k^{-O(k^2)}.

Moreover, for every alpha in (0,1), every positive integer m, and R_alpha=(1-alpha)Q+alpha delta_0,
\[
\operatorname{LDA}_{\le k}^{(m)}(R_\alpha,Q)
\le\sqrt{(1+C^2\alpha^2 k)^m-1}.
\]
In particular, the advantage is bounded by an absolute constant when k=O(1/(alpha^2 m)), with a fixed absolute implied constant.

Finally, let alpha in (0,1), p in [0,1), 0<=epsilon<=1/16, and m>=C/[alpha(1-p)]. In the relative-perturbation observation model, the pair test has the following guarantees, uniformly over all allowed adversaries:

- Under D=Q, it rejects with probability at least 1-m^2 exp(-c n).
- Under every law D with D(S)>=alpha for some fixed one-dimensional linear subspace S, it accepts with probability at least 1-exp(-c m alpha(1-p)).

Thus its probability of a correct answer under either hypothesis is at least
\[
1-m^2e^{-cn}-e^{-c m\alpha(1-p)}.
\]
The test uses O(m^2) pair checks and can be implemented in O(nm^2) arithmetic operations.
