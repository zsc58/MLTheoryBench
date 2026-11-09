# Problem

## Setup

Let \(K\ge 1\). For vectors, products and functions below are coordinatewise. Let \(\lambda_0\in(0,\infty)^K\) be baseline Poisson firing rates and let \(\delta\in(0,\infty)^K\) be a residual code. Define
\[
 p_P=\operatorname{Poisson}(\lambda_0),\qquad
 q_P=\operatorname{Poisson}(\lambda_0\odot\delta),
\]
with independent coordinates. The Poisson coding rate is \(R_P=D_{\rm KL}(q_P\Vert p_P)\), and set \(f(y)=y\log y-y+1\).

Also let \(q_G=N(\mu,\operatorname{diag}(\sigma^2))\) and \(p_G=N(\mu_0,\operatorname{diag}(\sigma_0^2))\) on \(\mathbb R^K\), where every \(\sigma_i,\sigma_{0i}>0\), with independent coordinates. Set \(R_G=D_{\rm KL}(q_G\Vert p_G)\), \(\Delta\mu=\mu-\mu_0\), \(\delta\sigma=\sigma\oslash\sigma_0\), and \(g(y)=y-1-\log y\).

## Task

Prove the integrated claim:

\[
R_P=\lambda_0^{\mathsf T}f(\delta),
\qquad
R_G=\frac12\sum_{i=1}^K\left[\frac{(\Delta\mu_i)^2}{\sigma_{0i}^2}+g\!\left((\delta\sigma_i)^2\right)\right].
\]
Moreover, show that for fixed residual code \(\delta\) and every \(c>0\), scaling baseline rates \(\lambda_0\mapsto c\lambda_0\) scales the Poisson coding rate by \(c\), so coding/information rate is directly coupled to absolute firing (metabolic) rate; in contrast, the Gaussian rate has no analogous dependence on an absolute activity level (translating \(\mu_0\) and \(\mu\) together while preserving their displacement and variances leaves it unchanged). Conclude that this metabolic-cost interpretation is specific to Poisson latent statistics rather than Gaussian latent statistics.
