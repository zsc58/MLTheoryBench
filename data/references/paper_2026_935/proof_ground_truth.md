# Reference Proof

## Proof Structure

1. Apply Itô's formula to the feature vector \(\phi(X_t)\); justify taking expectations, and use the two Gram equations to obtain exact tracking of \(m_t\).
2. Derive the Fokker--Planck equation for the smooth density \(p_t\), differentiate its differential entropy, and integrate by parts.
3. Substitute the second Gram equation and complete the square in the score and feature gradients, obtaining the entropy identity and then the lower bound.

## Complete Proof

Write \(J_t=\nabla\phi(X_t)\in\mathbb R^{k\times d}\), with rows given by the gradients of the components of \(\phi\), and write
\[
b(t,x)=\nabla\phi(x)^\top(\eta_t-\sigma^2\theta_t).
\]
The coefficient functions are deterministic: the expectations defining \(G_t\) and \(\mathbb E[\Delta\phi(X_t)]\) are unconditional, and the invertible Gram equations determine \(\eta_t\) and \(\theta_t\).

Itô's formula, componentwise and in integrated form, gives
\[
\phi(X_t)-\phi(X_0)
=\int_0^t\left[J_sJ_s^\top(\eta_s-\sigma^2\theta_s)+\sigma^2\Delta\phi(X_s)\right]ds
+\sqrt{2}\sigma\int_0^t J_s\,dW_s.
\]
Here
\[
\mathbb E\int_0^1\|J_s\|_F^2ds
=\int_0^1\operatorname{tr}G_s\,ds<\infty,
\]
so the stochastic integral is a square-integrable martingale and has expectation zero. Moreover,
\[
|J_sJ_s^\top(\eta_s-\sigma^2\theta_s)|
\leq |\eta_s-\sigma^2\theta_s|\,\|J_s\|_F^2.
\]
The stated time-integrability condition therefore justifies Fubini's theorem for the drift and Laplacian terms. Taking expectations yields
\[
\mathbb E[\phi(X_t)]-\mathbb E[\phi(X_0)]
=\int_0^t\left[G_s(\eta_s-\sigma^2\theta_s)+\sigma^2\mathbb E[\Delta\phi(X_s)]\right]ds.
\]
The second Gram equation cancels the two terms multiplied by \(\sigma^2\), and the first Gram equation then gives
\[
\mathbb E[\phi(X_t)]-\mathbb E[\phi(X_0)]
=\int_0^t m'_s\,ds=m_t-m_0.
\]
The initial moment match proves
\[
\mathbb E[\phi(X_t)]=m_t\qquad(0\leq t\leq1).
\]

For completeness, the Fokker--Planck equation follows by applying Itô's formula to a compactly supported smooth scalar test function \(f\):
\[
\frac{d}{dt}\int f(x)p_t(x)\,dx
=\int\left[b(t,x)\cdot\nabla f(x)+\sigma^2\Delta f(x)\right]p_t(x)\,dx.
\]
Integration by parts against the compactly supported test function gives the distributional equation, and the assumed density regularity gives its classical interpretation:
\[
\partial_t p_t=-\nabla\!\cdot\!\bigl(p_t\nabla\phi^\top(\eta_t-\sigma^2\theta_t)\bigr)+\sigma^2\Delta p_t.
\]

Set \(q_t(x)=\nabla\log p_t(x)\). The assumed entropy differentiation and spatial integrations by parts imply, for almost every \(t\),
\[
\frac{d}{dt}H(p_t)
=-\int (1+\log p_t)\partial_t p_t\,dx
=-\mathbb E[b(t,X_t)\cdot q_t(X_t)]+\sigma^2\mathbb E|q_t(X_t)|^2.
\]
The mass derivative is zero because \(p_t\) is a probability density and the Fokker--Planck flux has no boundary contribution. Absolute integrability in the granted integration-by-parts hypothesis justifies the displayed terms. In particular, the diffusion integration by parts has integrand \(|\nabla p_t|^2/p_t\), so the Fisher term is finite at the times at which this calculation is used.

Another componentwise integration by parts gives
\[
\mathbb E[\nabla\phi(X_t)q_t(X_t)]
=-\mathbb E[\Delta\phi(X_t)]=-G_t\theta_t.
\]
Consequently,
\[
\frac{d}{dt}H(p_t)
=\eta_t^\top G_t\theta_t-\sigma^2\theta_t^\top G_t\theta_t+\sigma^2\mathbb E|q_t(X_t)|^2.
\]
The matrix \(G_t\) is symmetric, so \(G_t\eta_t=m'_t\) makes the first term \(\theta_t^\top m'_t\). Expanding the square and using the preceding integration-by-parts identity gives
\[
\begin{aligned}
\mathbb E\left|q_t(X_t)+\nabla\phi(X_t)^\top\theta_t\right|^2
&=\mathbb E|q_t(X_t)|^2
+2\theta_t^\top\mathbb E[\nabla\phi(X_t)q_t(X_t)]
+\theta_t^\top G_t\theta_t\\
&=\mathbb E|q_t(X_t)|^2-\theta_t^\top G_t\theta_t.
\end{aligned}
\]
Thus, for almost every \(t\),
\[
\frac{d}{dt}H(p_t)
=\theta_t^\top m'_t
+\sigma^2\mathbb E\left|\nabla\log p_t(X_t)+\nabla\phi(X_t)^\top\theta_t\right|^2.
\]
The residual is nonnegative. Since \(t\mapsto H(p_t)\) is absolutely continuous and \(t\mapsto\theta_t^\top m'_t\) is integrable, the identity also shows that the residual is integrable in time. Integrating the resulting inequality on \([0,1]\) gives
\[
H(p_1)\geq H(p_0)+\int_0^1\theta_t^\top m'_t\,dt.
\]
This proves both clauses of the target.
