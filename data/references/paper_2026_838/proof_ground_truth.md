# Reference Proof

## Proof Structure

Compute the posterior-to-prior KL coordinatewise for the Poisson residual model and factor it into baseline-rate weights. Compute the analogous diagonal-Gaussian KL and show that translating both means by the same vector does not change it. Finally interpret the defined coding rate relative to baseline spike activity, restricting the conclusion to the specified Poisson-versus-Gaussian comparison.

## Complete Proof

For one Poisson coordinate, let the posterior and prior masses be
\[
q(z)=e^{-\lambda}\lambda^z/z!,\qquad p(z)=e^{-\lambda_0}\lambda_0^z/z!,\qquad z\in\{0,1,2,\ldots\},
\]
with \(\lambda=\lambda_0\delta\), \(\lambda_0>0\), and \(\delta>0\). Both masses are positive on this support, and
\[
\log\frac{q(z)}{p(z)}=-(\lambda-\lambda_0)+z\log(\lambda/\lambda_0).
\]
This log ratio is integrable under \(q\), because it is affine in \(z\) and \(\mathbb E_q z=\lambda<\infty\). Taking its expectation gives
\[
D_{\rm KL}(q\Vert p)=\lambda\log(\lambda/\lambda_0)-\lambda+\lambda_0
=\lambda_0(\delta\log\delta-\delta+1).
\]
For independent coordinates, the joint mass ratio is the product of the coordinate mass ratios. Its logarithm is therefore their sum. Since there are finitely many integrable summands, taking expectation gives
\[
R_P=D_{\rm KL}(q_P\Vert p_P)
=\sum_{i=1}^K\lambda_{0i}f(\delta_i)
=\lambda_0^{\mathsf T}f(\delta).
\]

The public task requires only positive rates. For clarity, the optional zero-rate extensions have specific meanings. If \(\lambda_0>0\) is fixed and \(\lambda\downarrow0\), then \(\lambda\log(\lambda/\lambda_0)\to0\), so the KL tends to \(\lambda_0\); this also follows directly from the posterior being a point mass at zero and corresponds to defining \(f(0)=1\). If a finite residual \(\delta\) is held fixed and \(\lambda_0\downarrow0\), then \(\lambda=\lambda_0\delta\) and \(\lambda_0 f(\delta)\to0\); at the endpoint both distributions are the same point mass. These statements do not assert unrestricted joint continuity as two independently varying rates approach zero.

For one Gaussian coordinate, write \(q=N(\mu,\sigma^2)\) and \(p=N(\mu_0,\sigma_0^2)\), with positive standard deviations. Their densities are positive on \(\mathbb R\), and
\[
\log\frac{q(z)}{p(z)}
=\log\frac{\sigma_0}{\sigma}
-\frac{(z-\mu)^2}{2\sigma^2}
+\frac{(z-\mu_0)^2}{2\sigma_0^2}.
\]
The log ratio is integrable because Gaussian second moments are finite. Using
\[
\mathbb E_q[(Z-\mu)^2]=\sigma^2,\qquad
\mathbb E_q[(Z-\mu_0)^2]=\sigma^2+(\mu-\mu_0)^2,
\]
we obtain
\[
\begin{aligned}
D_{\rm KL}(q\Vert p)
&=\log\frac{\sigma_0}{\sigma}-\frac12
+\frac{\sigma^2+(\mu-\mu_0)^2}{2\sigma_0^2}\\
&=\frac12\left[\frac{(\mu-\mu_0)^2}{\sigma_0^2}
+\frac{\sigma^2}{\sigma_0^2}-1-\log\frac{\sigma^2}{\sigma_0^2}\right].
\end{aligned}
\]
The same product-log-ratio argument applies to the independent Gaussian coordinates. Hence, with \(\Delta\mu=\mu-\mu_0\), \(\delta\sigma_i=\sigma_i/\sigma_{0i}\), and \(g(y)=y-1-\log y\),
\[
R_G=D_{\rm KL}(q_G\Vert p_G)
=\frac12\sum_{i=1}^K\left[\frac{(\Delta\mu_i)^2}{\sigma_{0i}^2}
+g\!\left((\delta\sigma_i)^2\right)\right].
\]

Now fix \(\delta\) and let \(c>0\). The scaled prior and posterior rates remain positive, and
\[
D_{\rm KL}\!\left(\operatorname{Poisson}(c\lambda_0\odot\delta)
\Vert\operatorname{Poisson}(c\lambda_0)\right)
=(c\lambda_0)^{\mathsf T}f(\delta)=cR_P.
\]
Here the posterior rates scale together with the baseline rates; the residual is unchanged. Also, \(f'(y)=\log y\), so \(f\) has its unique minimum \(f(1)=0\) on \((0,\infty)\). Thus the coefficient of \(c\) is nonnegative and is positive unless every residual coordinate is one. If \(\delta\) is the identity residual, \(R_P=0\) for every baseline; the scaling claim remains valid and does not imply a strictly positive penalty for activity when posterior and prior coincide.

For any \(a\in\mathbb R^K\), replace the Gaussian means by \(\mu+a\) and \(\mu_0+a\), keeping \(\sigma\) and \(\sigma_0\) fixed. The displacement remains \(\Delta\mu\), and all variance ratios remain unchanged. The displayed expression for \(R_G\) is consequently unchanged. Its mean-shift cost depends on prior precision and the displacement, not on the common absolute mean level.

Finally, coding rate in this problem is the posterior-to-prior KL already defined in the setup. Its information-cost meaning is the expected log ratio \(\mathbb E_q[\log(q/p)]\), with the expectation taken under the posterior. This interpretation does not assert equality with a stimulus-latent mutual information or require an unspecified distribution of stimuli. With natural logarithms the units are nats; conversion to bits multiplies both rates by the same constant and does not affect the comparison.

For the Poisson model, baseline rates are expected baseline spike counts in a fixed observation interval. Their sum measures total expected baseline activity, and it scales by \(c\); posterior expected activity also scales by \(c\) when the residual is fixed. The exact Poisson identity therefore weights the defined information cost by baseline activity, supporting the stated metabolic-cost interpretation when spike activity is used as the metabolic proxy. In the Gaussian model, changing the common mean level alone has no effect on the coding rate. This establishes the claimed baseline-activity coupling for the Poisson model and its absence under the specified Gaussian translation comparison. It is not a universal identification of KL with physical energy, a strict activity penalty at the identity residual, or an exclusivity claim over all other distribution families.

All theorem-critical obligations have been derived directly. The source's axiomatic information-gain characterization and information-geometric explanation are not needed as additional theorems for this exact calculation and comparison.
