# Reference Proof

## Proof Structure

Work at a fixed parameter value and fixed input locations. Transform both the process and observed gradients to scaled coordinates. The span of the target-centered differences contains every relevant pairwise difference. Derivative covariances then separate perpendicular gradient components from all function values and all parallel components. Joint Gaussianity turns this zero cross-covariance into independence. The directional statistic is a one-to-one encoding of each parallel component on the relevant subspace, not necessarily the orthogonal projection itself. Metric-matched noise becomes isotropic after scaling and preserves the same separation. Use conditional distributions throughout so that no nonsingularity assumption is needed.

## Complete Proof

### 1. Derivative model and scaled coordinates

All parameters and input locations are fixed, and all probabilities below are under the resulting model. If \(m=0\), both sides condition on empty vectors and equal the marginal law of \(y_*\). Hence assume \(m\geq1\).

The differentiable mean and twice continuously differentiable covariance give the stated mean-square derivatives. To see the relevant Gaussian and covariance facts directly, center the process and consider coordinate difference quotients. The covariance between two such quotients is a mixed finite difference of the kernel. As both increments tend to zero, it converges to the corresponding mixed input derivative of the kernel. At a single derivative location this also shows that the quotients are Cauchy in \(L^2\), since the variance of their difference tends to zero. Their means converge to the corresponding mean derivative. Finite collections of quotients and function values are jointly Gaussian; their \(L^2\) limits remain jointly Gaussian, as follows by passing to the limit in their Gaussian characteristic functions. Consequently the derivative-value and derivative-derivative covariances are respectively the first and mixed second input derivatives of the kernel. Adding the independent Gaussian observation errors preserves joint Gaussianity.

Set
\[
A=\Lambda_\theta^{1/2},\qquad z_a=Ax_a,\qquad F(z)=f(A^{-1}z).
\]
The mean-square chain rule, or the same difference-quotient calculation, gives
\[
\nabla_zF(z_a)=A^{-1}\nabla_xf(x_a).
\]
Define
\[
\widetilde g_a=A^{-1}g_a,\qquad
\widetilde g_c=(I_m\otimes A^{-1})g_c,\qquad
\Delta=AD.
\]
The covariance of \(F\) is \(\kappa_\theta(\|z-z'\|^2)\). Since \(A\) is invertible, \(g_c\) and \(\widetilde g_c\) generate the same sigma-algebra. Blockwise,
\[
\Delta^T\widetilde g_a=D^Tg_a,
\qquad
q=(I_m\otimes\Delta^T)\widetilde g_c.
\]
These identities have dimensions \(m\) per reference block and \(m^2\) after stacking.

### 2. Geometry and derivative covariances

Let
\[
S=\operatorname{col}(\Delta),
\]
and let \(P\) be the Euclidean orthogonal projection onto \(S\). Every difference \(z_a-z_b\), for \(a,b\in\{*,1,\ldots,m\}\), belongs to \(S\): target-reference differences are columns of \(\Delta\), and reference-reference differences are differences of those columns.

Write \(h(r)=\kappa_\theta(\|r\|^2)\), so the scaled covariance is \(h(z-z')\). For a nonzero difference \(r\), put \(t=\|r\|^2\). Twice continuous differentiability of the input kernel gives the radial-profile derivatives locally at this positive \(t\): one may restrict the input difference to \(\sqrt{s}\,r/\|r\|\) for \(s\) near \(t\). The chain rule gives
\[
\nabla h(r)=2\kappa_\theta'(t)r,
\qquad
\nabla^2h(r)=2\kappa_\theta'(t)I_d+4\kappa_\theta''(t)rr^T.
\]
At \(r=0\), no assumption that \(\kappa_\theta''(0)\) exists is needed. The twice continuously differentiable function \(h\) is even, so \(\nabla h(0)=0\). Its invariance under orthogonal transformations implies that \(\nabla^2h(0)\) is a scalar multiple of \(I_d\): coordinate reflections make its off-diagonal entries zero, and coordinate permutations make its diagonal entries equal. These are statements about the actual input derivatives of the covariance at zero.

For \(u\in S^\perp\), \(v\in S\), and \(r=z_a-z_b\in S\), the derivative covariance identities therefore imply
\[
\operatorname{Cov}\bigl(u^T\nabla F(z_a),F(z_b)\bigr)
=u^T\nabla h(r)=0,
\]
and
\[
\operatorname{Cov}\bigl(u^T\nabla F(z_a),v^T\nabla F(z_b)\bigr)
=-u^T\nabla^2h(r)v=0.
\]
For nonzero \(r\), the terms vanish because \(u^Tr=0\) and \(u^Tv=0\). At zero they vanish by the just-established gradient and Hessian forms. Independent function-observation noise does not change the first zero covariance when \(F(z_b)\) is replaced by \(y_b\).

### 3. Gaussian independence removes perpendicular components

First take exact gradients. Define the stacked vectors
\[
U=(I_m\otimes P)\widetilde g_c,
\qquad
W=(I_m\otimes(I_d-P))\widetilde g_c.
\]
Thus \(\widetilde g_c=U+W\), and the full scaled-gradient vector and the pair \((U,W)\) determine each other. Applying the preceding covariance identities to bases of \(S\) and \(S^\perp\) gives
\[
\operatorname{Cov}\bigl(W,(y_*,y_c,U)\bigr)=0.
\]

The standard Gaussian independence fact used here includes singular Gaussian vectors: two jointly Gaussian vectors with zero cross-covariance are independent. Indeed, their joint Gaussian characteristic function factors into the two marginal characteristic functions when the cross-covariance block is zero, irrespective of rank or mean. Its hypotheses hold here by Step 1 and the displayed cross-covariance calculation. Hence \(W\) is independent of \((y_*,y_c,U)\).

This independence implies
\[
\mathcal L_\theta(y_*\mid y_c,U,W)
=\mathcal L_\theta(y_*\mid y_c,U)
\quad\text{almost surely}.
\]
For completeness, for any bounded Borel function \(\phi\), let \(M=E_\theta[\phi(y_*)\mid y_c,U]\). Independence verifies that \(M\) has the defining conditional-expectation identity when tested against products of indicators measurable with respect to \((y_c,U)\) and to \(W\). Extending from these products proves \(E_\theta[\phi(y_*)\mid y_c,U,W]=M\). Applying this to a countable determining class of Borel subsets of \(\mathbb R\) gives equality of the regular conditional laws. No density or covariance inverse is used.

### 4. The reduced statistic and parallel components carry identical information

Since \(\Delta^T(I_d-P)=0\), each reference block satisfies
\[
\Delta^T\widetilde g_a=\Delta^TP\widetilde g_a.
\]
The map \(v\mapsto\Delta^Tv\) is injective on \(S\). If \(v\in S\) and \(\Delta^Tv=0\), then \(v\) is orthogonal to every column of \(\Delta\), and hence to \(S\); therefore \(v=0\). This reasoning does not require independent columns of \(\Delta\).

An injective linear map between finite-dimensional spaces has a linear, and therefore measurable, inverse on its image. Applying this inverse separately to the reference blocks of \(q\) recovers \(U\). Conversely, \(q=(I_m\otimes\Delta^T)U\). Thus
\[
\sigma(q)=\sigma(U).
\]
Combining this fact with the invertible scaling and Step 3 yields
\[
\begin{aligned}
\mathcal L_\theta(y_*\mid y_c,g_c)
&=\mathcal L_\theta(y_*\mid y_c,U,W)\\
&=\mathcal L_\theta(y_*\mid y_c,U)\\
&=\mathcal L_\theta(y_*\mid y_c,q)
\end{aligned}
\]
almost surely for exact gradients.

### 5. Metric-matched noise and boundary cases

For the stated noisy-gradient model,
\[
\eta_a=A^{-1}\varepsilon_a^g\sim N(0,\sigma_g^2I_d),
\qquad
\widetilde g_a=\nabla F(z_a)+\eta_a.
\]
The vectors \(\eta_a\) are independent across observation labels and independent of the process and all function-observation errors. For \(u\in S^\perp\) and \(v\in S\),
\[
\operatorname{Cov}(u^T\eta_a,v^T\eta_b)
=\mathbf 1\{a=b\}\sigma_g^2u^Tv=0.
\]
The process-noise cross-covariances and noise-function-value cross-covariances are also zero. Consequently, when \(U,W\) are formed from the noisy observed gradients, the same identity
\[
\operatorname{Cov}\bigl(W,(y_*,y_c,U)\bigr)=0
\]
holds. The observed vectors remain jointly Gaussian. Steps 3 and 4 therefore apply without change and prove the claimed conditional-law equality for metric-matched noise, including \(\sigma_g^2=0\).

The statistic has \(m\) scalar entries for each of \(m\) reference observations, hence \(m^2\) entries. Empty reference sets were addressed at the start. Rank-deficient difference matrices, \(S=\{0\}\), coincident input locations, arbitrary differentiable means, zero function noise, and singular Gaussian conditional distributions are all covered by the same argument. In particular, no condition such as \(m\leq d\), full column rank, or strictly positive conditional variance was used. Where conditional densities exist, the established equality of conditional laws gives equality of density versions almost everywhere. No equality for a general correlated or unscaled anisotropic gradient-noise model is claimed.

## Obligation Audit

1. Derivative existence, finite-dimensional joint Gaussianity, and the covariance identities are obtained from the stated mean and kernel regularity by the difference-quotient argument in Step 1.
2. The geometric inclusion and all required zero covariances, including zero separation, are derived in Step 2.
3. The singular-compatible Gaussian independence statement is stated, justified, and applied with its hypotheses verified in Step 3; the conditional-law implication is also justified there.
4. Measurable equivalence of the retained statistic and the parallel gradients is proved without a rank assumption in Step 4.
5. The noisy experiment, information transformations, coordinate count, and degenerate cases are covered in Step 5.

All theorem-critical obligations are closed. There is no unresolved specialized dependency or private reference-proof gap.
