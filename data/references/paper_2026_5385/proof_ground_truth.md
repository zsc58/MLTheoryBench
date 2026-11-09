# Reference Proof

## Proof Structure

Expand the loss at the Dirichlet mean with a second-order Taylor formula and a cubic remainder controlled by the Lipschitz Hessian. The centered first moment removes the linear term. The quadratic expectation is expressed through the Dirichlet covariance, yielding the explicit trace correction. Bound the remainder using the simplex diameter and the covariance trace. Finally, bound the correction coefficient uniformly using the Hessian bound to establish the rate for the total discrepancy.

## Theorem-Critical Obligations

1. Verify that the loss and the terms whose expectations are taken are measurable and integrable.
2. Establish the cubic Taylor remainder using the Hessian Lipschitz condition only on the simplex.
3. Apply the Dirichlet mean and covariance identities under positive parameters, and remove the centered linear term.
4. Derive the exact Hessian-covariance correction.
5. Establish the required bound on the expected Taylor remainder.
6. Bound the correction coefficient independently of the Dirichlet parameter vector and conclude the rate for the total discrepancy.

## Complete Proof

### Step 1: Well-definedness and Taylor remainder

Fix the label and loss, with the stated constants \(M,G\), and let \(h=\pi-\bar p\). Because every parameter is positive, \(\alpha_0>0\), the Dirichlet distribution is well-defined, and \(\bar p\) belongs to the simplex. The simplex is compact, and the loss is continuous on its open neighborhood, so the loss is bounded and measurable on the simplex. Also, \(h\) is bounded. All expectations below therefore exist.

For a realization of \(\pi\), the entire segment \(\bar p+th\), \(0\le t\le1\), lies in the simplex. Applying the fundamental theorem of calculus twice to \(t\mapsto\ell(\bar p+th,y)\) gives
\[
\ell(\pi,y)=\ell(\bar p,y)+\nabla\ell(\bar p,y)^\top h+\frac12h^\top H_\ell(\bar p,y)h+r(h),
\]
where
\[
r(h)=\int_0^1(1-t)h^\top\bigl(H_\ell(\bar p+th,y)-H_\ell(\bar p,y)\bigr)h\,dt.
\]
Consequently,
\[
|r(h)|\le G\|h\|_2^3\int_0^1t(1-t)\,dt=\frac G6\|h\|_2^3.
\]
This verifies the needed segmentwise Taylor bound directly. In particular, it does not require a Hessian Lipschitz bound outside the simplex.

### Step 2: Centering and the quadratic expectation

The standard Dirichlet moment identities, valid for every vector of positive parameters, are
\[
\mathbb E[\pi]=\bar p,
\qquad
\operatorname{Cov}(\pi)=\frac{\operatorname{Diag}(\bar p)-\bar p\bar p^\top}{\alpha_0+1}.
\]
Their parameter hypotheses hold here. Hence \(\mathbb E[h]=0\) and \(\mathbb E[hh^\top]=\operatorname{Cov}(\pi)\). For the fixed symmetric matrix \(H=H_\ell(\bar p,y)\), the identity \(h^\top Hh=\operatorname{tr}(Hhh^\top)\) gives
\[
\mathbb E[h^\top Hh]=\operatorname{tr}\bigl(H\operatorname{Cov}(\pi)\bigr).
\]
Taking expectations in the Taylor expansion removes the linear term.

### Step 3: Exact correction

Substituting the covariance identity yields
\[
\mathbb E[\ell(\pi,y)]
=\ell(\bar p,y)+\frac{1}{\alpha_0+1}L_1(\bar p,y)+R(\alpha,y),
\]
where
\[
L_1(\bar p,y)=\frac12\operatorname{tr}\!\left(H_\ell(\bar p,y)\bigl(\operatorname{Diag}(\bar p)-\bar p\bar p^\top\bigr)\right),
\qquad
R(\alpha,y)=\mathbb E[r(h)].
\]
These are the asserted correction and remainder.

### Step 4: Expected remainder bound

Every simplex point has Euclidean norm at most one. Therefore \(\|h\|_2\le2\) and \(\|h\|_2^3\le2\|h\|_2^2\). It follows that
\[
|R(\alpha,y)|\le\frac G6\mathbb E\|h\|_2^3
\le\frac G3\mathbb E\|h\|_2^2
=\frac G3\operatorname{tr}\bigl(\operatorname{Cov}(\pi)\bigr).
\]
The covariance formula and \(\sum_i\bar p_i=1\) imply
\[
\operatorname{tr}\bigl(\operatorname{Cov}(\pi)\bigr)
=\frac{1-\|\bar p\|_2^2}{\alpha_0+1}.
\]
Thus
\[
|R(\alpha,y)|\le\frac G3\frac{1-\|\bar p\|_2^2}{\alpha_0+1}
\le\frac{G}{3(\alpha_0+1)}.
\]

### Step 5: Uniform correction bound and total discrepancy

Let \(S=\operatorname{Diag}(\bar p)-\bar p\bar p^\top\). Since \(S=(\alpha_0+1)\operatorname{Cov}(\pi)\), it is symmetric positive semidefinite, and \(\operatorname{tr}(S)=1-\|\bar p\|_2^2\). For any symmetric matrix \(H\) and positive semidefinite matrix \(S\), diagonalizing \(S\) with nonnegative eigenvalues \(\lambda_j\) and orthonormal eigenvectors \(v_j\) gives
\[
|\operatorname{tr}(HS)|
=\left|\sum_j\lambda_jv_j^\top Hv_j\right|
\le\|H\|_{\mathrm{op}}\sum_j\lambda_j
=\|H\|_{\mathrm{op}}\operatorname{tr}(S).
\]
Therefore
\[
|L_1(\bar p,y)|\le\frac M2\bigl(1-\|\bar p\|_2^2\bigr)\le\frac M2.
\]
Combining this with the expansion and the remainder estimate proves
\[
\left|\mathbb E[\ell(\pi,y)]-\ell(\bar p,y)\right|
\le\left(\frac M2+\frac G3\right)
\frac{1-\|\bar p\|_2^2}{\alpha_0+1}
\le\frac{M/2+G/3}{\alpha_0+1}.
\]
The constant is independent of \(\alpha\), so the asserted total-discrepancy rate holds as \(\alpha_0\to\infty\), without any additional restriction on the corresponding means. The argument also covers \(M=0\), \(G=0\), and arbitrarily small positive concentrations.
