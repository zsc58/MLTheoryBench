# Reference Proof

## Proof Structure

Derive the Gaussian product-of-experts covariance and the variance-preserving diffusion covariance map. Compute the covariance for each operation order. Prove the required harmonic-mean super-additivity and its equality case explicitly, and conclude by comparing centered Gaussian laws.

## Complete Proof

### 1. Gaussian product of experts

For centered Gaussian densities with positive-definite covariances \(\Sigma_k\), their geometric mean is a positive constant times
\[
\exp\!\left(-\frac12 x^\top Qx\right),\qquad Q=\frac1K\sum_{k=1}^K\Sigma_k^{-1}.
\]
The matrix \(Q\) is positive definite, so this function has a finite, strictly positive integral. Normalization therefore gives a centered Gaussian with covariance \(Q^{-1}\).

For \(\Sigma_k=\alpha_k I_d\), define
\[
H(\alpha_1,\ldots,\alpha_K)=\frac{K}{\sum_{k=1}^K\alpha_k^{-1}}.
\]
The initial product of experts consequently has covariance \(H(\alpha)I_d\).

### 2. Diffusion covariance map

Put
\[
b(t)=\int_0^t\beta_s\,ds,\qquad \gamma_t=e^{-2b(t)}.
\]
The schedule assumptions imply \(0<b(t)<\infty\), and hence \(0<\gamma_t<1\), for every finite \(t>0\).

The integrating-factor solution of the stated SDE is
\[
z_t=e^{-b(t)}z_0+\int_0^t e^{-(b(t)-b(s))}\sqrt{2\beta_s}\,dw_s.
\]
The deterministic integrand is square integrable on every finite interval. Its stochastic integral is a centered Gaussian vector independent of \(z_0\), with covariance
\[
\left(\int_0^t 2\beta_s e^{-2(b(t)-b(s))}\,ds\right)I_d
=(1-e^{-2b(t)})I_d.
\]
The last equality follows by integrating the almost-everywhere derivative of \(e^{-2(b(t)-b(s))}\) with respect to \(s\). Thus, if \(z_0\sim\mathcal N(0,cI_d)\), then
\[
z_t\sim\mathcal N\!\left(0,\bigl(\gamma_t c+1-\gamma_t\bigr)I_d\right).
\]

Applying this to the initial product of experts shows that \(A_t\) is centered Gaussian with scalar covariance
\[
c_{\mathrm{diff}}=\gamma_tH(\alpha)+(1-\gamma_t).
\]
Applying it separately to each initial component gives scalar covariances \(\gamma_t\alpha_k+1-\gamma_t>0\). The Gaussian product formula then shows that \(B_t\) is centered Gaussian with scalar covariance
\[
c_{\mathrm{step}}=H\bigl(\gamma_t\alpha_1+1-\gamma_t,\ldots,\gamma_t\alpha_K+1-\gamma_t\bigr).
\]
In particular, every product of experts used here is well-defined.

### 3. Harmonic-mean comparison, including equality

We prove the required finite positive-vector inequality rather than leave it as an invocation of an internal lemma. Let \(x_k,y_k>0\), and set
\[
S=\sum_k\frac1{x_k+y_k},\qquad U=\sum_k\frac1{x_k},\qquad V=\sum_k\frac1{y_k}.
\]
Expanding a sum of squares gives
\[
0\leq\sum_k\left(\frac{\sqrt{x_k}}{x_k+y_k}-\frac{S/U}{\sqrt{x_k}}\right)^2
=\sum_k\frac{x_k}{(x_k+y_k)^2}-\frac{S^2}{U}.
\]
Interchanging \(x\) and \(y\) similarly gives
\[
\sum_k\frac{y_k}{(x_k+y_k)^2}\geq\frac{S^2}{V}.
\]
Adding yields
\[
S\geq S^2\left(\frac1U+\frac1V\right).
\]
All quantities are finite and positive, so division by \(S^2\) and multiplication by \(K\) give
\[
H(x+y)\geq H(x)+H(y).
\]

Equality holds precisely when both sums of squares vanish. Vanishing of the first implies
\[
\frac{x_k}{x_k+y_k}=\frac SU\quad\text{for every }k.
\]
The common value lies strictly between zero and one, so \(x_k/y_k\) is constant across \(k\). Conversely, if \(x=\lambda y\) for some \(\lambda>0\), homogeneity of \(H\) immediately gives equality. Thus equality holds exactly when \(x\) and \(y\) are proportional.

Apply this result to
\[
x_k=\gamma_t\alpha_k,\qquad y_k=1-\gamma_t.
\]
Both vectors are strictly positive. Since \(H(\lambda x)=\lambda H(x)\) and \(H(1,\ldots,1)=1\),
\[
c_{\mathrm{step}}\geq\gamma_tH(\alpha)+(1-\gamma_t)=c_{\mathrm{diff}}.
\]
Equality holds exactly when \((\gamma_t\alpha_k)_k\) is proportional to the constant vector \((1-\gamma_t)_k\). Since \(0<\gamma_t<1\), this is equivalent to \(\alpha_1=\cdots=\alpha_K\).

### 4. Equality of laws

Both \(A_t\) and \(B_t\) are centered isotropic Gaussian laws with positive scalar covariances. Equal laws have equal covariances, and equal covariances give the same centered Gaussian law. Therefore
\[
A_t=B_t\quad\Longleftrightarrow\quad\alpha_1=\cdots=\alpha_K.
\]
The argument applies to each finite \(t>0\). If the variances are not all equal, it also proves \(c_{\mathrm{step}}>c_{\mathrm{diff}}\) at every such time.

## Proof-Closure Notes

The finite sum-of-squares argument supplies the negative-exponent reverse-Minkowski instance needed by the source's harmonic-mean comparison. It completes the previously recorded local sign-convention repair without requiring an unaudited specialized theorem. The attenuation \(\gamma_t\) is the covariance attenuation; its coefficient in the SDE solution is \(\sqrt{\gamma_t}\), consistently with the previously recorded notation repair. There are no unresolved theorem-critical obligations.
