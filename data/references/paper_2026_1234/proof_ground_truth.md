# Reference Proof

## Proof Structure

For a fixed covariate, first use generalized-quantile inequalities and a union bound to show that the retained posterior parameter set has mass at least `1-gamma`. Every retained model places at least `1-alpha_0` conditional probability in the trimmed envelope, so posterior integration gives the predictive lower bound. For the calibrated set, condition on the training fit; exchangeability makes the calibration and test scores exchangeable, and the split-conformal order-statistic argument gives the stated marginal coverage.

## Complete Proof

Fix `x`. Write
\[
a_\theta=q_L(\theta,x)=F_\theta^{-1}(\alpha_0/2\mid x),\qquad
b_\theta=q_U(\theta,x)=F_\theta^{-1}(1-\alpha_0/2\mid x).
\]
Let `c_L` be the posterior `gamma/2` quantile of `a_theta`, and `c_U` the posterior `1-gamma/2` quantile of `b_theta`. By the generalized-inverse quantile inequalities, \(\pi(a_\theta<c_L\mid D_{tr})\le\gamma/2\) and \(\pi(b_\theta>c_U\mid D_{tr})\le\gamma/2\) (with the usual harmless boundary convention for atoms). Hence, for
\[
R(x)=\{\theta:a_\theta\ge c_L,\ b_\theta\le c_U\},
\]
the union bound gives \(\pi(R(x)\mid D_{tr})\ge1-\gamma\).

If \(\theta\in R(x)\), then \([a_\theta,b_\theta]\subseteq[c_L,c_U]\). The quantile-sandwich inequality for a random variable with CDF `F_theta(.|x)` gives
\[
F_\theta([a_\theta,b_\theta]\mid x)\ge1-\alpha_0,
\]
so also \(F_\theta([c_L,c_U]\mid x)\ge1-\alpha_0\). Therefore, for the posterior-predictive mixture,
\[
\int F_\theta([c_L,c_U]\mid x)\,\pi(d\theta\mid D_{tr})
\ge\int_{R(x)}(1-\alpha_0)\,\pi(d\theta\mid D_{tr})
\ge(1-\gamma)(1-\alpha_0).
\]
Since the trimmed envelope is \([L(x),U(x)]=[c_L,c_U]\), this proves the first claim.

For the conformal claim, condition on the training sample `D_tr`, which fixes the functions `L` and `U`. For each calibration observation and the test observation define
\[
S_i=r(X_i,Y_i)=\max\{L(X_i)-Y_i,\,Y_i-U(X_i)\}.
\]
The observations are exchangeable and the same training-fitted score function is used for all of them; consequently \(S_1,\ldots,S_m,S_{m+1}\) are exchangeable conditional on `D_tr`. Let \(k=\lceil(m+1)(1-\alpha)\rceil\) and let \(\hat t\) be the `k`th calibration order statistic (with the standard `+infinity` convention if `k>m`). The split-conformal order-statistic lemma then yields
\[
\Pr(S_{m+1}\le\hat t\mid D_{tr})\ge1-\alpha,
\]
and hence the same unconditional inequality. Finally,
\[
S_{m+1}\le\hat t
\iff L(X_{m+1})-\hat t\le Y_{m+1}\le U(X_{m+1})+\hat t,
\]
which is exactly \(Y_{m+1}\in\mathcal C(X_{m+1})\). Thus \(\Pr\{Y_{m+1}\in\mathcal C(X_{m+1})\}\ge1-\alpha\).
