# Reference Proof

## Proof Structure

Condition on the prompt batch. First compute the conditional mean and variance of a general leave-one-out linear estimator. Unbiasedness becomes a linear constraint, under which conditional mean-squared error reduces to a strictly convex quadratic form. Solve the resulting constrained quadratic program and verify uniqueness.

## Complete Proof

Fix a target index \(i\) and condition throughout on \(X\). Since the coefficients \(a_{ij}\) are deterministic after conditioning and \(\mathbb E[R_j\mid X]=\mu_j\),
\[
\mathbb E[\widehat\mu_i\mid X]
 =\sum_{j\ne i}a_{ij}\mu_j.
\]
Thus \(\widehat\mu_i\) is conditionally unbiased for \(\mu_i\) exactly when
\[
\sum_{j\ne i}a_{ij}\mu_j=\mu_i. \tag{1}
\]
Conditional independence implies that distinct \(R_j\)'s have zero conditional covariance. Consequently,
\[
\operatorname{Var}(\widehat\mu_i\mid X)
 =\sum_{j\ne i}a_{ij}^2\tau_j^2.
\]
The conditional bias-variance decomposition gives
\[
\mathbb E[(\widehat\mu_i-\mu_i)^2\mid X]
 =\left(\sum_{j\ne i}a_{ij}\mu_j-\mu_i\right)^2
  +\sum_{j\ne i}a_{ij}^2\tau_j^2.
\]
Under (1), the squared-bias term vanishes. It therefore remains to minimize
\[
q(a)=\sum_{j\ne i}\tau_j^2a_{ij}^2
\]
subject to (1).

Introduce a multiplier \(\lambda\) and the Lagrangian
\[
L(a,\lambda)=\sum_{j\ne i}\tau_j^2a_{ij}^2
 +\lambda\left(\sum_{j\ne i}a_{ij}\mu_j-\mu_i\right).
\]
Its stationarity equations are
\[
2\tau_j^2a_{ij}+\lambda\mu_j=0,
\qquad j\ne i,
\]
so
\[
a_{ij}=-\frac{\lambda\mu_j}{2\tau_j^2}. \tag{2}
\]
Substitution into (1) yields
\[
-\frac{\lambda}{2}\sum_{k\ne i}\frac{\mu_k^2}{\tau_k^2}=\mu_i.
\]
Because \(Q_i>0\), this gives \(\lambda=-2\mu_i/Q_i\). Equation (2) therefore becomes
\[
a_{ij}^{\star}
 =\frac{\mu_i\mu_j/\tau_j^2}{Q_i}
 =\frac{\mu_i\mu_j/\tau_j^2}
 {\sum_{k\ne i}\mu_k^2/\tau_k^2}.
\]
These coefficients are feasible because
\[
\sum_{j\ne i}a_{ij}^{\star}\mu_j
 =\frac{\mu_i}{Q_i}\sum_{j\ne i}\frac{\mu_j^2}{\tau_j^2}
 =\mu_i.
\]
Finally, every \(\tau_j^2\) is positive, so the Hessian of \(q\) is the positive-definite diagonal matrix with entries \(2\tau_j^2\). Hence \(q\) is strictly convex. Its restriction to the nonempty affine constraint set (1) is strictly convex as well, and the feasible stationary point above is its unique global minimizer. Since conditional MSE equals \(q\) on that constraint set, the displayed estimator is the unique conditionally unbiased leave-one-out linear estimator of minimum conditional MSE.
