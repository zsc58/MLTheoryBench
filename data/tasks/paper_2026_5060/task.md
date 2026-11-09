# Problem

## Setup

Let \(\Sigma\in\mathbb R^{p\times p}\) be symmetric positive definite with eigendecomposition
\[
\Sigma=\sum_{i=1}^p\lambda_i v_i v_i^\top,
\qquad \lambda_1\ge\lambda_2\ge\cdots\ge\lambda_p>0,
\]
where \(\{v_i\}_{i=1}^p\) is an orthonormal basis. For any real \(\alpha\), define
\[
\Sigma^\alpha:=\sum_{i=1}^p\lambda_i^\alpha v_i v_i^\top.
\]
For \(\beta\in[0,1]\), let the metric be \(M(\beta)=\Sigma^\beta\). The associated generalized eigenproblem is
\[
\Sigma w=\lambda\,M(\beta)w.
\]
For the effective ordinary operator obtained from this problem, let \(\kappa(\beta)\) denote its largest eigenvalue divided by its smallest eigenvalue.

## Task

Prove that, for every \(\beta\in[0,1]\), the generalized eigenproblem is equivalent under a congruence/change of variables to the ordinary eigenproblem
\[
\Sigma^{1-\beta}u=\lambda u.
\]
Consequently, its eigenvalues are \(\lambda_i^{1-\beta}\) and one may take corresponding generalized eigenvectors \(w_i=\Sigma^{-\beta/2}v_i\). Moreover,
\[
\kappa(\beta)=\left(\frac{\lambda_1}{\lambda_p}\right)^{1-\beta},
\]
which is continuous and nonincreasing in \(\beta\) (strictly decreasing if \(\lambda_1>\lambda_p\)), with \(\kappa(0)=\lambda_1/\lambda_p\) and \(\kappa(1)=1\).
