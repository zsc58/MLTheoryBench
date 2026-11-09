# Reference Proof

## Proof Structure

Use the spectral calculus of the symmetric positive-definite matrix \(\Sigma\) to conjugate the generalized eigenproblem. This yields an ordinary eigenproblem for \(\Sigma^{1-\beta}\), from which the generalized eigenpairs and condition number follow directly. Monotonicity and endpoint values then follow from elementary properties of positive powers.

## Complete Proof

Write the spectral decomposition
\[
\Sigma=\sum_{i=1}^p\lambda_i v_i v_i^\top,
\qquad \lambda_1\ge\cdots\ge\lambda_p>0,
\]
with \(\{v_i\}\) orthonormal. For \(\beta\in[0,1]\), define powers by
\(\Sigma^\alpha=\sum_i\lambda_i^\alpha v_i v_i^\top\). In particular, \(M(\beta)=\Sigma^\beta\) is positive definite and invertible.

The generalized eigenproblem is
\[
\Sigma w=\lambda\,\Sigma^\beta w.
\]
Set \(u=\Sigma^{\beta/2}w\), so \(w=\Sigma^{-\beta/2}u\). Left-multiplying by \(\Sigma^{-\beta/2}\), and using commutativity of all spectral powers of \(\Sigma\), gives
\[
\Sigma^{-\beta/2}\Sigma\Sigma^{-\beta/2}u
 =\lambda\,\Sigma^{-\beta/2}\Sigma^\beta\Sigma^{-\beta/2}u,
\]
hence
\[
\Sigma^{1-\beta}u=\lambda u.
\]
Thus the effective ordinary operator is \(\Sigma^{1-\beta}\). Since \(\Sigma^{1-\beta}v_i=\lambda_i^{1-\beta}v_i\), choose \(u_i=v_i\). The corresponding generalized eigenvector is
\[
w_i=\Sigma^{-\beta/2}v_i,
\]
and its generalized eigenvalue is
\[
\lambda_i(\beta)=\lambda_i^{1-\beta}.
\]

The eigenvalues of the effective operator remain ordered, so its condition number is
\[
\kappa(\beta)=\frac{\lambda_1^{1-\beta}}{\lambda_p^{1-\beta}}
 =\left(\frac{\lambda_1}{\lambda_p}\right)^{1-\beta}.
\]
Let \(r=\lambda_1/\lambda_p\ge1\). For \(0\le\beta\le1\), \(r^{1-\beta}\) is continuous and nonincreasing in \(\beta\), and is strictly decreasing when \(r>1\). At the endpoints,
\[
\kappa(0)=r=\lambda_1/\lambda_p,
\qquad \kappa(1)=1.
\]
When \(\beta=0\), the effective operator is \(\Sigma\); when \(\beta=1\), it is the identity, completing the claim.
