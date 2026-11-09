# Reference Proof

## Proof Structure

Center the kernel feature map under the target law, identify empirical MMD risk with the expected squared norm of its stationary sample mean, and expand that norm into lag covariances. Regrouping pairs by lag gives the exact finite-sample identity and hence the finite-sample ESS formula. Absolute summability then permits dominated convergence in the lag expansion, yielding the long-run variance and both asymptotic ESS regimes.

## Complete Proof

Let \(\widehat\pi_n=n^{-1}\sum_{t=1}^n\delta_{X_t}\). By the definitions of the kernel mean and MMD,
\[
m_{\widehat\pi_n}-m_\pi=\frac1n\sum_{t=1}^n\bigl(k(X_t,\cdot)-m_\pi\bigr)=\frac1n\sum_{t=1}^n\phi(X_t),
\]
so
\[
R_n=\mathbb E\,\mathrm{MMD}_k^2(\widehat\pi_n,\pi)
=\frac1{n^2}\mathbb E\left\|\sum_{t=1}^n\phi(X_t)\right\|_H^2
=\frac1{n^2}\sum_{s,t=1}^n\mathbb E\langle\phi(X_s),\phi(X_t)\rangle_H.
\]
Stationarity implies that the summand depends only on \(t-s\), namely it equals \(\gamma_{t-s}\). Symmetry of the real Hilbert inner product and stationarity give \(\gamma_{-\ell}=\gamma_\ell\). There are \(n\) pairs with lag zero and, for each \(1\le\ell\le n-1\), exactly \(n-\ell\) pairs with lag \(\ell\) and the same number with lag \(-\ell\). Hence
\[
R_n=\frac1{n^2}\left[n\gamma_0+2\sum_{\ell=1}^{n-1}(n-\ell)\gamma_\ell\right].
\]
Substitution into the ESS definition gives the stated finite-sample formula whenever \(R_n>0\); when \(R_n=0\), ESS is \(+\infty\) by definition.

Rewrite the identity as
\[
nR_n=\gamma_0+2\sum_{\ell=1}^{n-1}\left(1-\frac{\ell}{n}\right)\gamma_\ell.
\]
For each fixed \(\ell\), the coefficient tends to one and has absolute value at most one. Extending the finite sum by zeros and using \(\sum_{\ell\ge1}|\gamma_\ell|<\infty\), dominated convergence for series yields
\[
nR_n\longrightarrow \sigma_k^2:=\gamma_0+2\sum_{\ell=1}^{\infty}\gamma_\ell.
\]
Because every \(nR_n\) is nonnegative, \(\sigma_k^2\ge0\). If \(\sigma_k^2>0\), then eventually \(R_n>0\) and
\[
\frac{\mathrm{ESS}^{(n)}_k}{n}=\frac{\gamma_0}{nR_n}\longrightarrow\frac{\gamma_0}{\sigma_k^2}
=\left(1+2\sum_{\ell=1}^{\infty}\frac{\gamma_\ell}{\gamma_0}\right)^{-1}.
\]
If \(\sigma_k^2=0\), then \(nR_n\to0\), so \(R_n=o(n^{-1})\). Along indices with \(R_n>0\), \(\mathrm{ESS}^{(n)}_k/n=\gamma_0/(nR_n)\to+\infty\), while indices with zero risk already have infinite ESS.
