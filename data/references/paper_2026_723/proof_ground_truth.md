# Reference Proof

## Proof Structure

1. Express the population accuracy difference through the two disagreement probabilities.
2. Condition on the observed number of disagreements and derive the binomial law for baseline-only wins.
3. Reduce the equal-accuracy null to a fair-binomial null, define the exact upper-tail test, and prove its type-I control, including the zero-disagreement case.

## Complete Proof

Let the paired outcomes on one draw be `(Y,Z)`, where `Y` is the baseline score and `Z` is the optimized score. Write
\[
P_b=\Pr(Y=1,Z=0),\qquad P_c=\Pr(Y=0,Z=1),
\]
and let `p_flip=P_b+P_c`. The population accuracies satisfy
\[
\gamma=\Pr(Y=1),\qquad \beta=\Pr(Z=1),
\]
so the agreement cells cancel and
\[
\gamma-\beta=P_b-P_c.
\]
If `p_flip>0`, define `q_downarrow=P_b/p_flip`. Then
\[
\gamma-\beta=p_{flip}(2q_{\downarrow}-1).
\]
Consequently, `beta<gamma` exactly when `q_downarrow>1/2`, and equality holds exactly when `q_downarrow=1/2`. If `p_flip=0`, both disagreement probabilities vanish, hence `beta=gamma`, while `q_downarrow` is undefined.

For the `N` iid paired examples, write their outcomes as `(Y_i,Z_i)` and define
\[
I_i=\mathbf 1\{Y_i\ne Z_i\},\qquad
B_i=\mathbf 1\{(Y_i,Z_i)=(1,0)\}.
\]
Thus `n_flips=sum_i I_i`, `b=sum_i B_i`, and `c=n_flips-b`. Suppose first that `p_flip>0`. For any disagreement-indicator vector `s=(s_1,...,s_N)` with positive probability, conditioning on `I_i=s_i` for every `i` preserves independence across the pairs. Indeed, if `A_i` is any event determined by pair `i` and `E_i={I_i=s_i}`, independence gives
\[
\Pr\!\left(\bigcap_i A_i\,\middle|\,\bigcap_i E_i\right)
=\frac{\prod_i\Pr(A_i\cap E_i)}{\prod_i\Pr(E_i)}
=\prod_i\Pr(A_i\mid E_i).
\]
The denominator is positive for the indicator vectors under consideration. Whenever `s_i=1`,
\[
\Pr(B_i=1\mid I_i=1)=\frac{P_b}{P_b+P_c}=q_{\downarrow};
\]
whenever `s_i=0`, `B_i=0`. Therefore, conditional on any such vector with exactly `n` ones, `b` is the sum of `n` independent Bernoulli variables with parameter `q_downarrow`, and has distribution `Binomial(n,q_downarrow)`. Conditioning only on `n_flips=n` mixes these identical distributions over the possible indicator vectors, so
\[
b\mid n_{flips}=n\sim\operatorname{Binomial}(n,q_{\downarrow})
\]
for every `n` with `Pr(n_flips=n)>0`. This also covers `n=0`, when `b=0`, and the endpoint cases `p_flip=1` and `q_downarrow` equal to zero or one. No conditional distribution on a probability-zero count event is required.

Under the equal-accuracy null `H_0: beta=gamma` with `p_flip>0`, the first part gives `q_downarrow=1/2`. Degradation corresponds to an excess of baseline-only wins, so for an observed `n_flips=n>0` and count `b`, the exact one-sided conditional p-value is
\[
p=\Pr\{\operatorname{Binomial}(n,1/2)\ge b\}
=\sum_{k=b}^{n}\binom nk2^{-n}.
\]
Reject when this value is at most `alpha`; otherwise fail to reject. This is the exact one-sided conditional McNemar/binomial test.

To establish its level directly, fix `n>0` and put
\[
T_n(j)=\sum_{k=j}^{n}\binom nk2^{-n},\qquad j=0,\ldots,n.
\]
These tails decrease with `j`. If there is no `j` with `T_n(j)<=alpha`, the rejection probability conditional on `n_flips=n` is zero. Otherwise, let `r` be the smallest such `j`. The rejection event is exactly `b>=r`, and under the conditional null its probability is
\[
\Pr_{H_0}(b\ge r\mid n_{flips}=n)=T_n(r)\le\alpha.
\]
The inequality may be strict because the distribution is discrete.

When `n_flips=0`, the observed counts satisfy `b=c=0`. The prescribed decision is to report no disagreements and fail to reject. This sample event does not imply that the population probabilities `P_b` and `P_c` are zero. Its rejection probability is zero whenever the event has positive probability.

For any null population with `p_flip>0`, let `R` denote the rejection event. Averaging over count events of positive probability gives
\[
\Pr_{H_0}(R)
=\sum_{\substack{0\le n\le N\\\Pr(n_{flips}=n)>0}}
\Pr_{H_0}(R\mid n_{flips}=n)\Pr(n_{flips}=n)
\le\alpha\Pr(n_{flips}>0)\le\alpha.
\]
Finally, if `p_flip=0`, then every pair agrees almost surely, `n_flips=0` almost surely, and the procedure never rejects. Its type-I error is therefore zero in that case. Thus the complete decision rule controls type-I error at most `alpha` for every equal-accuracy population in the stated paired iid experiment.
