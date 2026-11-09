# Problem

## Setup

Let `Theta` be an open subset of `R^d`. There are `M` items. Item `i` has a fixed, parameter-independent bounded reward `r_i` and a probability `p_i(theta)`, where each `p_i` is continuously differentiable, `p_i(theta)>0`, and `sum_{i=1}^M p_i(theta)=1`.

Fix integers `1 <= K <= n < M`. Define a sequential without-replacement draw by choosing, at each step, among the remaining items with probability proportional to `p_i(theta)`. For a set `S` of size `K`, let `P_theta(S)` be the probability that the unordered set of the first `K` choices is `S`. Equivalently,

`P_theta(S) = sum_{(i_1,...,i_K): {i_1,...,i_K}=S} product_{ell=1}^K p_{i_ell}(theta)/(1-sum_{u<ell}p_{i_u}(theta))`.

The objective is

`L_K(theta)=sum_{|S|=K}P_theta(S) max_{i in S}r_i`.

Independently sample standard Gumbel variables `xi_1,...,xi_M` and set `Y_i=log p_i(theta)+xi_i`. Let `A` be the set of indices of the `n` largest scores, let `m` be the index of the next-largest score, and let `kappa=Y_m`. Put `tau=exp(-kappa)` and

`q_i(kappa)=1-exp(-p_i(theta)tau)`.

Let `Z=(A,m,kappa)` and let `f_theta` denote its joint density with respect to counting measure on `(A,m)` and Lebesgue measure on `kappa`. Define

`widehat L(Z;theta)=sum_{S subset A, |S|=K} P_theta(S) max_{i in S}r_i / product_{i in S}q_i(kappa)`.

All derivatives below hold the realized `A,m,kappa` fixed. If `sg` denotes stop-gradient, define

`widehat g(Z;theta)=grad_theta widehat L(Z;theta)+sg(widehat L(Z;theta)) grad_theta log f_theta(Z)`.

For the computational statement, order the retained items as `a_1,...,a_n` so that `r_{a_1} >= ... >= r_{a_n}`, breaking ties arbitrarily. For `x>0`, define

`h_i(x)=(exp(p_i(theta)x)-1)/q_i(kappa)`,

`c_i(x)=p_i(theta)/(exp(p_i(theta)x)-1)`.

At a fixed `x`, initialize `E_0=1`, `G_0=0`, `E_s=G_s=0` for `1<=s<=K-1`, and `F(x)=0`. Traverse `j=n,n-1,...,1`. Before updating the arrays, add

`r_{a_j}h_{a_j}(x)(c_{a_j}(x)E_{K-1}+G_{K-1})`

to `F(x)` whenever `j<=n-K+1`. Then, for `s=K-1,K-2,...,1`, update

`G_s <- G_s+h_{a_j}(x)(G_{s-1}+c_{a_j}(x)E_{s-1})`,

`E_s <- E_s+h_{a_j}(x)E_{s-1}`.

For `K=1`, the array-update loop is empty.

## Task

Prove the following integrated theorem:

1. The estimator and its full score-function surrogate are unbiased:

`E_theta[widehat L]=L_K(theta)` and `E_theta[widehat g]=grad_theta L_K(theta)`.

The second identity must include a valid justification for differentiating under the expectation.

2. The same estimator has the exact one-dimensional representation

`widehat L=integral_0^infinity exp(-x)F(x) dx`,

where the reward-sorted recurrence in the setup computes `F(x)` exactly without enumerating `K`-subsets. Consequently, after one `O(n log n)` reward sort, evaluating the corresponding `Q`-node Gauss-Laguerre approximation takes `O(nKQ)` additional arithmetic, for total cost `O(n log n+nKQ)`. The integral identity and nodewise recurrence are exact; no assertion is made that finite-`Q` quadrature has zero error.
