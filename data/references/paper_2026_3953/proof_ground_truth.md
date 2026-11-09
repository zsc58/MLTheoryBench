# Reference Proof

## Contract and Interpretation

The data are held fixed throughout. The object to be identified is the adjusted posterior defined in the problem, not a posterior obtained from genuine target training observations. The calculation uses the given Gaussian source posterior, the Gaussian conditional likelihood, and the exponential weight. No predictive representativeness assumption, calibration result, or external theorem is needed.

The conditional tilting interpretation can be made precise without asserting that a reweighted joint is already normalized. At fixed x and theta, the kernel
\[
k_\theta(x,u)=p_s(u\mid x,\theta)w(u)
\]
has label integral Z_theta(x). Once this integral is shown to be finite and positive, normalizing this kernel gives the conditional tilting model
\[
q_\theta(y\mid x)=\frac{p_s(y\mid x,\theta)w(y)}{Z_\theta(x)},
\qquad
\frac{q_\theta(y\mid x)}{p_s(y\mid x,\theta)}=\frac{w(y)}{Z_\theta(x)}.
\]
Here q_theta denotes the assumed conditional tilting model. This construction does not assert that population-level label shift alone implies a new invariance conditional on every parameter value. If the kernel is multiplied by a source covariate density p_s(x), its unnormalized covariate marginal is p_s(x)Z_theta(x), not necessarily a normalized probability density. A global joint normalizer, when finite, cancels from the conditional ratio. No global joint normalization is needed for the public target. The factors w(y_i) in a product of these conditional likelihood ratios are theta-independent and can be absorbed into posterior normalization. This explains the given adjustment, but deriving this interpretation is not an additional solver obligation.

## Proof Structure

1. Check positive definiteness of the source precision and interpret the correction using locally normalized conditional kernels.
2. Evaluate Z_theta(x) directly by completing the square in the label.
3. Apply the correction to the given source posterior and complete the square in theta.
4. Verify finite positive normalization and identify the full Gaussian distribution, including its covariance.

## Complete Proof

Let
\[
\phi_i=\phi(x_i),\qquad s=\sum_{i=1}^n\phi_i=n\bar\phi,
\qquad A=\Sigma_\theta^{-1}=\tau^{-2}I_d+\sigma^{-2}\Phi^\top\Phi.
\]
For every nonzero v in R^d,
\[
v^\top A v=\tau^{-2}\|v\|^2+\sigma^{-2}\|\Phi v\|^2>0.
\]
Thus A is positive definite and Sigma_theta is well defined and positive definite. This does not require Phi to have full rank.

For fixed x and theta, put m=theta^T phi(x). Completing the square gives
\[
-\frac{(u-m)^2}{2\sigma^2}+\beta u
=-\frac{(u-m-\beta\sigma^2)^2}{2\sigma^2}
+\beta m+\frac12\beta^2\sigma^2.
\]
Consequently,
\[
\begin{aligned}
Z_\theta(x)
&=\frac{1}{Z_w\sqrt{2\pi\sigma^2}}
\int_{\mathbb R}\exp\!\left(-\frac{(u-m)^2}{2\sigma^2}+\beta u\right)\,du\\
&=Z_w^{-1}\exp\!\left(\beta\theta^\top\phi(x)+\frac12\beta^2\sigma^2\right).
\end{aligned}
\]
The last integral is that of a normalized Gaussian density after extracting the displayed constant. In particular, Z_theta(x) is finite and strictly positive for every x and theta. It follows that
\[
\prod_{i=1}^n Z_\theta(x_i)^{-1}
=Z_w^n\exp\!\left(-\frac n2\beta^2\sigma^2\right)
\exp(-\beta\theta^\top s).
\]
The first two factors are finite, positive, and independent of theta.

Write a=theta_hat_s and define
\[
\mu=a-\beta\Sigma_\theta s.
\]
The exact quadratic identity is
\[
-\frac12(\theta-a)^\top A(\theta-a)-\beta\theta^\top s
=-\frac12(\theta-\mu)^\top A(\theta-\mu)
-\beta a^\top s+\frac12\beta^2s^\top\Sigma_\theta s.
\]
Therefore the unnormalized adjusted density is a finite positive constant times the density of N(mu,Sigma_theta). More explicitly, because the source Gaussian density has the same covariance normalization as that Gaussian,
\[
\int_{\mathbb R^d}\pi_s(\theta\mid D_{\rm tr})
\prod_{i=1}^nZ_\theta(x_i)^{-1}\,d\theta
=Z_w^n\exp\!\left(
-\frac n2\beta^2\sigma^2
-\beta a^\top s
+\frac12\beta^2s^\top\Sigma_\theta s
\right)\in(0,\infty).
\]
Normalizing hence gives
\[
\pi^\star(\theta\mid D_{\rm tr})
=\mathcal N\!\left(\hat\theta_s-\beta\Sigma_\theta s,\Sigma_\theta\right)
=\mathcal N\!\left(\hat\theta_s-\beta n\Sigma_\theta\bar\phi,\Sigma_\theta\right).
\]
This identifies the entire distribution, not merely its mode. Its covariance is exactly Sigma_theta. The same calculation includes beta=0 and s=0, in which cases the mean shift vanishes, and includes arbitrary rank-deficient designs.

## Proof-Obligation Audit

- Source precision invertibility: closed by the displayed positive quadratic form.
- Finiteness and positivity of every conditional normalizer: closed by the explicit Gaussian integral.
- Parameter dependence of the product correction: closed by direct multiplication.
- Adjusted posterior normalization: closed by the displayed finite positive integral.
- Full distribution, mean, and covariance: closed by the exact completed-square density identity.
- External or nonstandard proof dependencies: none.
