# Problem

## Setup

Let $d\geq1$ and $C\geq1$ be integers. Let $(\pi_1,\ldots,\pi_C)$ be strictly positive weights summing to one, let $\mu_1,\ldots,\mu_C\in\mathbb R^d$, and let $\Sigma\in\mathbb R^{d\times d}$ be a symmetric positive-definite covariance matrix. Write
\[
\phi_c(z)=\mathcal N(z;\mu_c,\Sigma)
\]
for the $d$-dimensional Gaussian density, and define the shared-covariance mixture
\[
p_\theta(z)=\sum_{c=1}^C\pi_c\phi_c(z).
\]
Let $p$ be any probability density on $\mathbb R^d$, with respect to Lebesgue measure. Use natural logarithms in
\[
\mathrm{KL}(p\|p_\theta)=\int_{\mathbb R^d}p(z)\log\frac{p(z)}{p_\theta(z)}\,dz\in[0,+\infty],
\]
where the integrand is zero when $p(z)=0$.

Define the intrinsic overlap (information potential) and the data-distribution overlap by
\[
C(p_\theta)=\int_{\mathbb R^d}p_\theta(z)^2\,dz,
\qquad
O(p,p_\theta)=\int_{\mathbb R^d}p(z)p_\theta(z)\,dz.
\]
The expected mixture-density penalty in a density-penalized LDA objective is proportional to $\lambda O(p,p_\theta)$ for a chosen $\lambda\geq0$.

For $u\in\mathbb R^d$, write $\|u\|_{\Sigma^{-1}}^2=u^\top\Sigma^{-1}u$ for the squared Mahalanobis norm. Interpret the comparison inequalities in the extended-real sense, using the convention $0\cdot(+\infty)=0$ for a zero penalty weight.

## Task

Prove the following integrated claim. First,
\[
C(p_\theta)=\sum_{i,j=1}^C\pi_i\pi_j\,\mathcal N(\mu_i-\mu_j;0,2\Sigma)
\]
and equivalently
\[
C(p_\theta)=\frac{1}{(4\pi)^{d/2}\sqrt{\det\Sigma}}
\sum_{i,j=1}^C\pi_i\pi_j
\exp\!\left[-\frac14(\mu_i-\mu_j)^\top\Sigma^{-1}(\mu_i-\mu_j)\right].
\]
Second, show that
\[
\bigl|O(p,p_\theta)-C(p_\theta)\bigr|
\leq (2\pi)^{-d/2}(\det\Sigma)^{-1/2}
\sqrt{2\,\mathrm{KL}(p\|p_\theta)}.
\]
The same inequality should be stated for the corresponding terms multiplied by any $\lambda\geq0$.

Finally, explain from these formulas that, with $d,C$ and the weights fixed, the unweighted comparison coefficient diverges as $\det\Sigma\downarrow0$, and the intrinsic overlap itself diverges through its diagonal contributions. Also explain that, for fixed $\Sigma$ and weights, each off-diagonal contribution is strictly decreasing as a function of the squared Mahalanobis separation of its pair of class means.
