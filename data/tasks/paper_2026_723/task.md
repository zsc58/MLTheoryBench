# Problem

## Setup

Let `X` be drawn iid from a distribution `P_X`. On each example, two models are evaluated on the same input using a binary score: let `Y=L(M(X))` be the baseline outcome and `Z=L(M_opt(X))` be the optimized outcome, with values in `{0,1}`. Define the population accuracies
\[
\gamma=\mathbb E[Y],\qquad \beta=\mathbb E[Z].
\]
For one paired draw, define
\[
P_b=\Pr(Y=1,Z=0),\qquad P_c=\Pr(Y=0,Z=1),\qquad p_{flip}=P_b+P_c.
\]
When `p_flip>0`, define `q_downarrow=P_b/p_flip`. For `N` iid paired examples, let `b` and `c` be the observed counts of `(Y,Z)=(1,0)` and `(Y,Z)=(0,1)`, and let `n_flips=b+c`. Fix a significance level `alpha` with `0<alpha<1`.

## Task

Prove the following integrated theorem. If `p_flip>0`, then `beta<gamma` if and only if `q_downarrow>1/2`, with equality `beta=gamma` if and only if `q_downarrow=1/2`. Moreover, conditional on the observed disagreement count,\[
b\mid n_flips\sim\operatorname{Binomial}(n_flips,q_downarrow).
\]
Consequently, to test `H_0: beta=gamma` against degradation `H_1: beta<gamma`, for `n_flips=n>0` the exact one-sided p-value is
\[
\sum_{k=b}^{n}\binom{n}{k}2^{-n},
\]
corresponding to the null `q_downarrow=1/2`; rejecting when this value is at most `alpha` has type-I error at most `alpha`. Specify the prescribed decision for `n_flips=0` and include it in the type-I-error argument.
