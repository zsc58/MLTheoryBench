# Reference Proof

## Contract and proof obligations

The horizon, law, and covariance operator are fixed relative to the iid sample. The first conclusion uses a joint sample-and-sign expectation; the second uses a conditional sign expectation for each fixed sample. These expectations must not be interchanged.

The obligations are: establish the Q_s geometry and integrability; symmetrize the expected mean deviation; verify coordinate sensitivity and concentration with the source radius; and evaluate and bound the conditional empirical complexity. All are closed below.

## Complete proof

Write H=H_sig, Q=Q_s, R=R_s, X_i=S(tilde gamma_i), m=E X_i, and m_hat=n^{-1} sum_i X_i. All unlabelled norms and inner products below are in the Q geometry.

Because Omega_s is bounded, self-adjoint, and nonnegative, and lambda>0,
\[
\frac{1}{\|\Omega_s\|+\lambda}\|u\|_H^2
\le \langle u,Qu\rangle_H
\le \frac1\lambda\|u\|_H^2.
\]
Thus the Q inner product defines an equivalent Hilbert norm. Bochner integrability in H implies integrability in this norm. The Skorokhod path law gives full mass to its support, so ||X_i||<=R almost surely. In particular, all the expectations below are finite.

### Expected deviation

Let X'_1,...,X'_n be an independent copy of the signature sample. Conditional Jensen gives
\[
\mathbb E_X\|m-\widehat m\|
\le \mathbb E_{X,X'}\left\|\frac1n\sum_{i=1}^n(X'_i-X_i)\right\|.
\]
Independently swapping each pair (X_i,X'_i) leaves their joint law unchanged. Hence, for independent uniform signs sigma_i,
\[
\mathbb E_{X,X'}\left\|\frac1n\sum_i(X'_i-X_i)\right\|
=\mathbb E_{X,X',\sigma}\left\|\frac1n\sum_i\sigma_i(X'_i-X_i)\right\|.
\]
The triangle inequality and identical laws of the two samples yield
\[
\mathbb E_X\|m-\widehat m\|
\le \frac2n\mathbb E_{X,\sigma}\left\|\sum_i\sigma_iX_i\right\|.
\]
The expectation on the right includes the sample. This calculation does not give a conditional empirical-complexity bound.

### Concentration

Define Z(X_1,...,X_n)=||m-n^{-1} sum_i X_i||. If one coordinate is replaced by another support value, the reverse triangle inequality gives
\[
|Z(X_1,\ldots,X_i,\ldots,X_n)-Z(X_1,\ldots,X'_i,\ldots,X_n)|
\le \frac1n\|X_i-X'_i\|
\le \frac{2R}{n}.
\]
For completeness, the bounded-differences inequality used here states that a measurable function of independent inputs with coordinate oscillations at most c_i satisfies
\[
\mathbb P(Z-\mathbb EZ\ge t)
\le \exp\left(-\frac{2t^2}{\sum_i c_i^2}\right)
\quad(t>0).
\]
It follows from the Doob martingale of conditional expectations: its ith increment, conditionally on the previous inputs, has mean zero and lies in an interval of length at most c_i. For a centered variable Y in an interval of length c, let h(a)=log E exp(aY). Under exponential tilting, h''(a) is a variance, at most c^2/4: subtract the interval midpoint to bound the second moment by c^2/4. Since h(0)=h'(0)=0, integration gives h(a)<=a^2 c^2/8. Applying this estimate conditionally to the martingale increments yields E exp(a(Z-EZ))<=exp(a^2 sum_i c_i^2/8). Markov's inequality and minimization over a>0 give the displayed bound.

Here c_i=2R/n, independence is supplied by the sampling contract, and measurability follows from strong measurability of the signatures and continuity of the norm. If R>0, choosing
\[
t=2R\sqrt{\frac{\log(1/\delta)}{2n}}
\]
gives, with probability at least 1-delta,
\[
\|m-\widehat m\|
\le \mathbb E_X\|m-\widehat m\|
+2R\sqrt{\frac{\log(1/\delta)}{2n}}.
\]
Combining this with the expected-deviation bound proves the first conclusion. If R=0, X_i=m=0 almost surely and the conclusion holds directly.

### Conditional empirical complexity

Fix any realised sample and M>0. For each sign vector put v_sigma=sum_i sigma_i X_i. Cauchy-Schwarz gives
\[
\sup_{\|f\|\le M}\langle f,v_\sigma\rangle=M\|v_\sigma\|.
\]
When v_sigma is nonzero, equality is attained by f=M v_sigma/||v_sigma||; when it is zero, both sides vanish. Consequently,
\[
\widehat{\mathfrak R}_{n,s}(\mathcal F_{M,s})
=\frac Mn\mathbb E_\sigma\left\|\sum_i\sigma_iX_i\right\|
\le \frac Mn\left(\mathbb E_\sigma\left\|\sum_i\sigma_iX_i\right\|^2\right)^{1/2}.
\]
Expanding the finite sum and using E_sigma[sigma_i sigma_j]=0 for i!=j and 1 for i=j gives
\[
\mathbb E_\sigma\left\|\sum_i\sigma_iX_i\right\|^2
=\sum_i\|X_i\|^2.
\]
This proves the second conclusion for every fixed sample, including samples for which some signed sums vanish.

## Source correction

The source radius bounds individual signature norms, not pairwise distances. Its bounded-differences calculation therefore requires 2R_s/n and the corresponding factor-two concentration remainder. The joint expectation in the first conclusion is explicitly supported by the source symmetrization display. No conversion to a conditional empirical complexity has been assumed or proved.
