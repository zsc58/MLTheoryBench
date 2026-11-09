# Reference Proof

## Proof Structure

1. Rewrite the order-averaged autoregressive objective by sampling the position in the order uniformly.
2. Count uniform permutations to identify the law of the revealed prefix and of the next index conditional on that prefix.
3. Substitute this conditional average to obtain the random-mask objective and verify that its mask is independent of the data values.

## Complete Proof

Fix `theta` and `x`. All logarithms in the task are real and well-defined. There are finitely many relevant pairs `(S,j)`, so every expectation and rearrangement below is a finite sum of finite terms.

For a uniform permutation `Pi`, write `S_k(Pi)={Pi_1,...,Pi_k}`. By linearity of expectation,

\[
J_\theta(x)=\sum_{r=1}^d\mathbb E_\Pi\left[\log q_\theta(x_{\Pi_r}\mid x_{S_{r-1}(\Pi)})\right].
\]

Let `R` be uniform on `{1,...,d}` and independent of the permutation. By the definition of expectation for a finite uniform distribution,

\[
\mathbb E_R[a_R]=\frac1d\sum_{r=1}^d a_r.
\]

Applying this identity to the per-position expectations gives

\[
J_\theta(x)=d\,\mathbb E_R\mathbb E_\Pi\left[\log q_\theta(x_{\Pi_R}\mid x_{S_{R-1}(\Pi)})\right]. \tag{1}
\]

Put `K=R-1`. Fix `k\in\{0,...,d-1\}` and a set `S\subseteq[d]` of cardinality `k`. Exactly `k!(d-k)!` permutations have `S` as their first-`k` set: order the elements of `S` in the first `k` positions and order the complement thereafter. Hence

\[
\Pr(S_k(\Pi)=S)=\frac{k!(d-k)!}{d!}=\binom{d}{k}^{-1}.
\]

Thus `S_k(Pi)` is uniform among the `k`-element subsets. Moreover, for every `j\notin S`, exactly `k!(d-k-1)!` of these permutations have `Pi_{k+1}=j`, so

\[
\Pr(\Pi_{k+1}=j\mid S_k(\Pi)=S)=\frac1{d-k}. \tag{2}
\]

Conditioning the inner expectation in (1) on `R=r` and `S_{r-1}(Pi)=S`, then applying (2), yields

\[
\mathbb E_\Pi\left[\log q_\theta(x_{\Pi_r}\mid x_{S_{r-1}(\Pi)})\right]
=
\mathbb E_{S\sim\mathrm{Unif}\binom{[d]}{r-1}}
\left[\frac1{d-r+1}\sum_{j\notin S}\log q_\theta(x_j\mid x_S)\right].
\]

Substituting this identity into (1), and replacing `R-1` by `K`, proves

\[
J_\theta(x)
=
\mathbb E_K\mathbb E_{S\sim\mathrm{Unif}\binom{[d]}K}
\left[\frac{d}{d-K}\sum_{j\notin S}\log q_\theta(x_j\mid x_S)\right].
\]

The displayed random variable is therefore an unbiased single-iteration estimator of the order-averaged objective. Its sampled observed set is generated solely from `K` and auxiliary uniform randomness, whose sampling laws do not depend on the data values. More explicitly, for any proper subset `A` of `[d]`, this procedure selects `S=A` with probability

\[
\frac{1}{d}\binom{d}{|A|}^{-1},
\]

regardless of the supplied data vector. This is a statement about the complete mask law, not merely the one-coordinate masking probabilities. Thus the training update predicts the complementary, randomly masked entries from a value-independent observed subset, which is precisely the stated MCAR-style masking interpretation. It does not assert that mask coordinates are independent or that all subsets have equal unconditional probability.

The counting formulas also cover `k=0` and `k=d-1`, using `0!=1`. Since `K<=d-1`, every denominator `d-K` is positive. When `d=1`, the only context is empty and both sides equal `log q_theta(x_1|x_emptyset)`.

## Private Source Normalization Audit — step_005

The public task uses the correct expectation-based objective. Two source displays require explicit local repairs in the source records; neither repair changes the public theorem or its proof route.

First, in the source notation, the likelihood factorization and the expectation definition give

\[
\mathcal L(x,\theta)
=\mathbb E_{p(z)}[\log p_\theta(x\mid z)]
=\sum_z p(z)\sum_{i=1}^{L}\log p_\theta(x_{z_i}\mid x_{z_{<i}}).
\]

The expanded equality at L000036 instead places a one-step transition probability inside a sum over full permutations and places the parameter subscript on the wrong probability factors. The full-permutation weight must be `p(z)`, and the conditional likelihood must retain its `theta` subscript.

Second, define the actual per-position contribution by

\[
\mathcal L_i(x,\theta)
=\mathbb E_{p(z)}[\log p_\theta(x_{z_i}\mid x_{z_{<i}})].
\]

Using the source's convention that `z_<i` is a set, its unambiguous expanded form is

\[
\mathcal L_i(x,\theta)
=\sum_{\substack{S\subseteq[L]\\|S|=i-1}}
\Pr(z_{<i}=S)
\sum_{j\notin S}\Pr(z_i=j\mid z_{<i}=S)
\log p_\theta(x_j\mid x_S).
\]

Consequently,

\[
\mathcal L(x,\theta)=\sum_{i=1}^L\mathcal L_i(x,\theta),
\qquad
\mathcal L_i(x,\theta)=\mathbb E_{z_{<i}}[\widehat{\mathcal L}_i(x,\theta)].
\]

The expansion at L000055 omits the outer prefix probability. The factorization stated at L000062 and the context sampling specified at L000068 make its restoration explicit. With that probability restored, the estimators at L000063 and L000066 remain exactly as printed.

For a direct check of the original errors, take `L=2` and let both coordinates have Bernoulli(1/2) conditional models in every context. At any binary data vector, each conditional log-likelihood is `-log 2`. The correct objective is `-2 log 2`. In the full-permutation expansion at L000036, the two permutations each contribute `(1/2+1)(-log 2)`, producing `-3 log 2`. In the step expansion at L000055, the first step contributes `-log 2`, while the two possible one-element contexts each contribute `-log 2` without their required probability `1/2`, again producing `-3 log 2`. This example obeys the uniform prior, value-independence, and finite-likelihood requirements. It diagnoses the displayed normalization errors, not the frozen theorem.

## Audited Background and Proof Obligations — step_006

The attached finite form of LOTUS is the identity `E[a_R]=(1/d) sum_r a_r` explicitly derived from the uniform probability masses above. Its hypotheses hold because the position set is finite and the per-position values are finite.

The attached Jensen result is also valid in the source setup: for positive finite numbers `a_z` and probability weights `p(z)`, concavity of the logarithm gives

\[
\sum_z p(z)\log a_z\leq\log\!\left(\sum_z p(z)a_z\right).
\]

Here `a_z=p_theta(x|z)` is a finite product of positive finite conditional likelihoods, and the uniform permutation weights sum to one. This verifies the source's ELBO interpretation. The public equality itself does not require invoking Jensen or claiming that the averaged log-likelihood equals the log marginal likelihood.

All theorem-critical obligations are closed: finite objective evaluation, independent uniform position sampling, the complete prefix-subset law, the conditional next-index law, the exact estimator normalization, independence of the entire mask law from data values, and all included endpoints. No specialized external method or unresolved paper-specific dependency is used. The result concerns objective unbiasedness and the stated masking interpretation; it does not assert gradient interchange, recovery of every marginal-model conditional, or a statistical guarantee of imputation accuracy.
