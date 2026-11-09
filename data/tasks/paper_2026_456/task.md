# Problem

## Setup

Fix integers \(p\ge1\) and \(0\le t\le p\). For each positive integer \(n\), let \(X\) consist of \(n\) observations with joint density
\[
p(X\mid\nu)=\exp\{n\,\eta(\nu)^\top y(X)-n\,\psi(\eta(\nu))\}\,g(X)
\]
from a regular minimal exponential family. The natural parameter domain \(\mathcal H\), the map \(\eta(\nu)\), and \(\psi\) are the same for every \(n\); the data, statistic, and parameter-independent factor \(g\) may depend on \(n\), with that dependence suppressed in the notation. The natural parameter \(\eta\in\mathcal H\) and parameter \(\nu\) in its corresponding domain \(\mathcal M\subseteq\mathbb R^p\) are in one-to-one correspondence. The coordinates of the sufficient-statistic average \(y\in\mathbb R^p\) are linearly independent.

Write \(\mu(\nu)=\mathbb E_{\eta(\nu)}[y]\), and assume the parameter-to-mean identity \(\mu(\nu)=\nu\) throughout the parameter domain. Work at a fixed interior true parameter where \(\psi\) is twice continuously differentiable and \(V:=\nabla^2\psi(\eta)\) is positive definite. Partition
\[
\nu=(\nu_E,\nu_K),\qquad y=(y_E,y_K),
\]
with \(\nu_E\in\mathbb R^t\) unknown and \(\nu_K\in\mathbb R^{p-t}\) known and fixed. The dimensions and true parameter remain fixed as \(n\to\infty\).

Let \(\Theta_K=\{\theta\in\mathbb R^t:(\theta,\nu_K)\in\mathcal M\}\). Denote by \(\widehat\nu_E\) a measurable choice of global maximizer of the likelihood over \(\Theta_K\) whenever a maximizer exists. On samples where no maximizer exists, assign a fixed admissible value selected from \(\Theta_K\) independently of the data and of the unknown true parameter.

For a fixed \(\alpha\in\mathbb R^t\), consider the scalar target \(\alpha^\top\nu_E\) and the control-variate estimators
\[
T_c=\alpha^\top y_E+c^\top(y_K-\nu_K),\qquad c\in\mathbb R^{p-t}.
\]
The variance is minimized over deterministic coefficients at the fixed true parameter. Thus a population-optimal coefficient may depend on that parameter, but it is not estimated from the observations in this comparison.

For empty coordinate blocks, use \(\mathbb R^0=\{0\}\), interpret empty products and quadratic forms in the usual zero-dimensional sense, and take the inverse of the unique linear map on \(\mathbb R^0\) to be that map.

## Task

Prove that, for every fixed \(\alpha\in\mathbb R^t\), the asymptotic variance of the MLE of \(\alpha^\top\nu_E\) equals the variance of the optimally weighted control-variate estimator, with the normalization specified below. Here asymptotic variance refers to the variance of the limiting normal distribution of the centered estimator multiplied by \(\sqrt n\).

More precisely, if
\[
V=\begin{pmatrix}A&B\\B^\top&D\end{pmatrix}
\]
conformably with the \((E,K)\) partition, prove that the optimal coefficient is \(c^*=-D^{-1}B^\top\alpha\), that
\[
\sqrt n\bigl(\widehat\nu_E-\nu_E\bigr)\Rightarrow N\!\left(0,[(V^{-1})_{EE}]^{-1}\right),
\]
and that
\[
n\,\operatorname{Var}(T_{c^*})
=\alpha^\top(A-BD^{-1}B^\top)\alpha
=\alpha^\top[(V^{-1})_{EE}]^{-1}\alpha.
\]
