# Problem

## Setup

Let \(d\geq 1\) and \(m\geq 0\) be integers. Fix a parameter value \(\theta\). Let \(f\sim\operatorname{GP}(\mu_\theta,k_\theta)\) on \(\mathcal D\subset\mathbb R^d\), with differentiable mean \(\mu_\theta\) and covariance kernel \(k_\theta\) twice continuously differentiable in its input arguments. Input derivatives are taken in ambient coordinates, and \(\nabla f\) denotes the mean-square gradient: its coordinate derivatives are the \(L^2\) limits of the corresponding input difference quotients. Assume
\[
k_\theta(x,x')=\kappa_\theta\!\left((x-x')^T\Lambda_\theta(x-x')\right),
\]
where \(\Lambda_\theta\) is positive diagonal. Equivalently, with \(\widetilde x=\Lambda_\theta^{1/2}x\), the kernel is a function of \(\|\widetilde x-\widetilde x'\|^2\).

Fix deterministic target and reference inputs \(x_*,x_1,\ldots,x_m\in\mathcal D\), with distinct observation labels \(*,1,\ldots,m\). Define
\[
y_a=f(x_a)+\varepsilon_a^y\quad(a\in\{*,1,\ldots,m\}),
\qquad
g_a=\nabla f(x_a)+\varepsilon_a^g\quad(a=1,\ldots,m).
\]
All observation-noise variables are mutually independent and independent of \(f\). For finite variances \(\sigma_y^2,\sigma_g^2\geq0\), let
\[
\varepsilon_a^y\sim N(0,\sigma_y^2),
\qquad
\varepsilon_a^g\sim N(0,\sigma_g^2\Lambda_\theta).
\]
Thus \(\sigma_g^2=0\) gives exact gradients, while positive \(\sigma_g^2\) gives metric-matched Gaussian gradient noise.

Let
\[
y_c=(y_1,\ldots,y_m)^T,\qquad
g_c=(g_1^T,\ldots,g_m^T)^T,
\]
and define
\[
D=[x_1-x_*\ \cdots\ x_m-x_*]\in\mathbb R^{d\times m},\qquad
q=(I_m\otimes D^T)g_c\in\mathbb R^{m^2}.
\]
Here \(I_m\) is the \(m\times m\) identity matrix and \(\otimes\) denotes the Kronecker product. Write \(\mathcal L_\theta(Y\mid Z)\) for the regular conditional distribution of \(Y\) given \(Z\) under this model.

## Task

Prove that, for every parameter value, target, and finite reference set satisfying the setup,
\[
\mathcal L_\theta(y_*\mid y_c,g_c)
=
\mathcal L_\theta(y_*\mid y_c,q)
\quad\text{almost surely}.
\]
Thus the full \(md\)-dimensional reference-gradient observation can be replaced, without changing the target function-value conditional distribution, by at most \(m^2\) target-centered directional-derivative observations. This assertion includes exact gradients and metric-matched Gaussian gradient noise; it is not asserted for general correlated or unscaled anisotropic gradient noise.
