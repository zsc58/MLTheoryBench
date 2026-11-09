# Reference Proof

## Proof Structure

Establish that the posterior scale matrix remains positive definite because it is the positive-definite prior scale plus positive-semidefinite scatter and mean-correction terms. Then verify positivity of the predictive scalar and degrees of freedom, and use the multivariate Student-t density formula to conclude propriety and finiteness of its log-density everywhere.

## Complete Proof

Fix an arbitrary embedding parameter \(\theta\), an integer \(K\ge 1\), and support embeddings \(z_1,\ldots,z_K\in\mathbb R^d\). Write
\[
\bar z=K^{-1}\sum_{i=1}^K z_i,\qquad S_z=\sum_{i=1}^K(z_i-\bar z)(z_i-\bar z)^\top.
\]
By construction, \(S_z\succeq0\). The matrix
\[
(\bar z-\mu_0)(\bar z-\mu_0)^\top
\]
is also positive semidefinite. Since \(\Lambda_0\succ0\) and \(\kappa_0,K>0\), the posterior scale
\[
\Lambda_n=\Lambda_0+S_z+\frac{\kappa_0K}{\kappa_n}(\bar z-\mu_0)(\bar z-\mu_0)^\top,
\qquad \kappa_n=\kappa_0+K,
\]
satisfies \(\Lambda_n\succeq\Lambda_0\succ0\), hence \(\Lambda_n\succ0\). Also \(\nu_n=\nu_0+K\), so
\[
\nu_n-d+1=\nu_0+K-d+1>0
\]
because \(\nu_0>d-1\) and \(K\ge1\). Therefore
\[
a_n=\frac{\kappa_n+1}{\kappa_n(\nu_n-d+1)}>0.
\]
Consequently the predictive scale \(\Sigma_n=a_n\Lambda_n\) is strictly positive definite.

Let \(v_n=\nu_n-d+1\). The resulting predictive law is the multivariate Student-t distribution with location \(\mu_n\), scale \(\Sigma_n\), and degrees of freedom \(v_n\), where
\[
\mu_n=\frac{\kappa_0\mu_0+K\bar z}{\kappa_n}.
\]
For \(v_n>0\) and \(\Sigma_n\succ0\), its density on \(\mathbb R^d\) is
\[
f(x)=\frac{\Gamma((v_n+d)/2)}{\Gamma(v_n/2)(v_n\pi)^{d/2}|\Sigma_n|^{1/2}}
\left(1+\frac{(x-\mu_n)^\top\Sigma_n^{-1}(x-\mu_n)}{v_n}\right)^{-(v_n+d)/2}.
\]
This is a proper density. For every \(x\in\mathbb R^d\), positive definiteness gives a finite nonnegative quadratic form, so the parenthesized factor is finite and at least one; all normalizing factors are finite and strictly positive. Hence \(0<f(x)<\infty\) and \(\log f(x)\in\mathbb R\) for every \(x\). The argument does not use invertibility of \(S_z\), so it remains valid when \(K<d\).
