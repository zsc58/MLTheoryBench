# Problem

## Setup

Fix positive integers \(p,k\), constants \(B>0\) and \(\lambda^*\ge0\), and a nonempty compact set \(\mathcal X\subset\mathbb R^p\). Let \((X_i,R_i)_{i\ge1}\) be iid pairs, where \(X_i\in\mathcal X\) is sub-Gaussian and \(R_i\in\{0,1\}^p\) indicates observed coordinates: \(R_{ij}=1\) means that \(X_{ij}\) is observed. For each \(n\), conditionally on \(X_1,\ldots,X_n\), the indicators \(R_{ij}\), \(1\le i\le n\), \(1\le j\le p\), are independent and satisfy
\[
\Pr(R_{ij}=1\mid X_1,\ldots,X_n)=1-\exp(-\lambda^*X_{ij}^2).
\]
The constants and the joint distribution of the pairs do not vary with \(n\).

Fix \(\lambda\ge0\). For a matrix \(M\in\mathbb R^{k\times p}\) with rows \(\mu_1,\ldots,\mu_k\), define
\[
\ell_\lambda(M;X_i,R_i)=\min_{1\le l\le k}\sum_{j=1}^p\left[R_{ij}(X_{ij}-\mu_{lj})^2+(1-R_{ij})\lambda\mu_{lj}^2\right].
\]
Let
\[
\widehat L_n^\lambda(M)=\frac1n\sum_{i=1}^n\ell_\lambda(M;X_i,R_i),
\qquad L^\lambda(M)=\mathbb E\,\ell_\lambda(M;X,R),
\]
where \((X,R)\) has the common distribution of the pairs, and the expectation is over both variables.

The parameter space is
\[
\mathcal M=\{M\in\mathbb R^{k\times p}:\mu_l\in\mathcal X,\ \|\mu_l\|_2\le B\text{ for every }l\},
\]
which is assumed nonempty. Assume that \(L^\lambda\) has a unique minimizer \(M^{*,\lambda}\) on \(\mathcal M\), and that, for every \(n\), \(\widehat L_n^\lambda\) has an almost surely unique minimizer \(\widehat M_n^\lambda\) on \(\mathcal M\). Uniqueness is as an ordered matrix. Write \(\operatorname{vec}(M)\) for the vector obtained by stacking the rows of \(M\) in their given order.

## Task

Prove that, for every fixed \(\lambda\ge0\) satisfying these assumptions and every \(\varepsilon>0\),
\[
\Pr\!\left(\left\|\operatorname{vec}(\widehat M_n^\lambda)-\operatorname{vec}(M^{*,\lambda})\right\|_2>\varepsilon\right)\longrightarrow0
\qquad(n\to\infty).
\]
