# Problem

## Setup

Let \(X_t\in\mathbb R^d\), \(0\leq t\leq1\), solve, for a fixed \(\sigma>0\),
\[
dX_t=\nabla\phi(X_t)^\top(\eta_t-\sigma^2\theta_t)\,dt+\sqrt{2}\,\sigma\,dW_t,
\]
where \(W_t\) is a standard \(d\)-dimensional Brownian motion and \(\phi:\mathbb R^d\to\mathbb R^k\) is twice continuously differentiable. Write \(\Delta\phi\) for the componentwise Laplacian and take \(\nabla\phi(x)\in\mathbb R^{k\times d}\). Let \(m:[0,1]\to\mathbb R^k\) be continuously differentiable. For each \(t\), define
\[
G_t=\mathbb E[\nabla\phi(X_t)\nabla\phi(X_t)^\top],
\]
and suppose \(G_t\) is invertible and the measurable coefficient functions \(\eta,\theta:[0,1]\to\mathbb R^k\) satisfy the coupled equations
\[
G_t\eta_t=m'_t,\qquad G_t\theta_t=\mathbb E[\Delta\phi(X_t)].
\]
Assume a unique strong solution exists with smooth strictly positive densities \(p_t\). Let
\[
H(p)=-\int_{\mathbb R^d}p(x)\log p(x)\,dx.
\]
All expectations are with respect to the unconditional law of \(X_t\). Assume, for every \(t\in[0,1]\),
\[
\mathbb E|\phi(X_t)|<\infty,\qquad
\operatorname{tr}G_t<\infty,\qquad
\mathbb E|\Delta\phi(X_t)|<\infty,\qquad
\int_{\mathbb R^d}p_t(x)|\log p_t(x)|\,dx<\infty,
\]
and assume
\[
\int_0^1\left[
(1+|\eta_t-\sigma^2\theta_t|)\operatorname{tr}G_t
+\mathbb E|\Delta\phi(X_t)|
+|\theta_t^\top m'_t|
\right]dt<\infty.
\]
Here vector norms are Euclidean. Assume also that \(t\mapsto H(p_t)\) is absolutely continuous on \([0,1]\), that its derivative is obtained by differentiating its defining spatial integral, and that spatial integrations by parts involving \(1,p_t,\log p_t\), and the components of \(\phi\) are valid with absolutely integrable terms and vanishing boundary contributions for almost every \(t\). Finally, assume \(\mathbb E[\phi(X_0)]=m_0\).

## Task

Prove that
\[
\mathbb E[\phi(X_t)]=m_t\quad\text{for every }t\in[0,1],
\]
and that the terminal entropy satisfies the computable lower bound
\[
H(p_1)\geq H(p_0)+\int_0^1\theta_t^\top m'_t\,dt.
\]
