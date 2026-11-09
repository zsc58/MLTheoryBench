# Reference Proof

## Proof Structure

Standardize the clean and observed covariates, compute conditional expectations of normalized Hermite modes coordinatewise, extend the resulting diagonal action to the full L2 expansion, and use orthogonal projection to compare Bayes and affine risks.

The theorem-critical obligations are: identify the joint Gaussian structure; verify that label noise contributes zero conditional mean; justify the conditional Hermite identity and its product form; pass from finite sums to the L2 expansion; identify affine predictors with the degree-at-most-one subspace; and obtain the risk difference by conditional-expectation orthogonality and the squared norm of the omitted modes. Each obligation is closed below.

## Complete Proof

### Integrability and noise independence

The assumptions give \(Y\in L^2\). Moreover, \(\epsilon=Y-f(X)\) is measurable with respect to \((X,Y)\), so independence of \(\eta\) from \((X,Y)\) implies independence of \(\eta\) from \((X,\epsilon)\). Combining this with independence of \(\epsilon\) and \(X\), the joint law of \((\epsilon,X,\eta)\) factors into the three marginal laws. Thus \(\epsilon\) is independent of \((X,\eta)\), hence of \(\widetilde X\), and
\[
\mathbb E[\epsilon\mid\widetilde X]=0.
\]

### Gaussian standardization

Let
\[
U=\Lambda^{-1/2}(X-\mu),\qquad
V=(\Lambda+\Sigma_\eta)^{-1/2}(\widetilde X-\mu).
\]
Both vectors have independent standard normal coordinates. Their cross-covariances are
\[
\mathbb E[U_jV_k]=\begin{cases}\sqrt{\rho_j},&j=k,\\0,&j\ne k.\end{cases}
\]
The joint vector \((U,V)\) is Gaussian. Its covariance matrix, ordered by coordinate pairs, is block diagonal, so its Gaussian characteristic function factors by those pairs. Consequently the pairs \((U_j,V_j)\) are independent.

Put \(r_j=\sqrt{\rho_j}\in(0,1)\). For each \(j\), the residual
\[
W_j=\frac{U_j-r_jV_j}{\sqrt{1-r_j^2}}
\]
is standard normal and has zero covariance with \(V_j\). Their joint Gaussian characteristic function therefore factors, proving independence. In particular,
\[
U_j\mid V_j=v\sim N(r_jv,1-r_j^2).
\]
Independence of the coordinate pairs also implies that the conditional law of \(U\) given \(V\) is the product of these coordinatewise conditional laws.

### Conditional Hermite identity

The generating function of the probabilists' Hermite polynomials is
\[
e^{tu-t^2/2}=\sum_{n=0}^{\infty}\operatorname{He}_n(u)\frac{t^n}{n!}.
\]
Using the conditional Gaussian moment-generating function gives
\[
\mathbb E[e^{tU_j-t^2/2}\mid V_j=v]
=e^{tr_jv-t^2r_j^2/2}.
\]
For each fixed \(v\), this identity may be differentiated any finite number of times at \(t=0\) under the conditional integral: on a bounded interval of \(t\), the derivatives are bounded by a constant times a polynomial in \(|U_j|\) times \(e^{T|U_j|}\), which is integrable under the conditional Gaussian law. Differentiating \(n\) times and applying the same generating function to the right-hand side yields
\[
\mathbb E\left[\frac{\operatorname{He}_n(U_j)}{\sqrt{n!}}\,\middle|\,V_j\right]
=\rho_j^{n/2}\frac{\operatorname{He}_n(V_j)}{\sqrt{n!}}.
\]
The product conditional law now gives, for every \(\alpha\in\mathbb N_0^d\),
\[
\mathbb E[h_\alpha(U)\mid V]
=m_\alpha h_\alpha(V),\qquad
m_\alpha:=\prod_{j=1}^d\rho_j^{\alpha_j/2}.
\]
Thus the conditional identity indexed by theory_003 is derived rather than taken as an unexplained specialized method.

### Orthonormality and the L2 limit

For a standard Gaussian vector \(Z\) and \(s,t\in\mathbb R^d\), its moment-generating function gives
\[
\mathbb E\left[e^{t^\top Z-\|t\|^2/2}e^{s^\top Z-\|s\|^2/2}\right]=e^{t^\top s}.
\]
Differentiating in the coordinates of \(s,t\) at zero, justified by Gaussian exponential integrability as above, proves
\[
\mathbb E[h_\alpha(Z)h_\beta(Z)]=\mathbf 1_{\{\alpha=\beta\}}.
\]
For a finite sum of these modes, its squared L2 norm is therefore the sum of its squared coefficients. Passing to an L2 limit gives the same norm identity for any convergent expansion. This is the orthonormal/Parseval calculation indexed by theory_004. The task already supplies the L2-convergent expansion of \(f\), so no additional completeness assertion is needed to pass to that expansion.

Define finite partial sums
\[
F_m(U)=\sum_{|\alpha|\leq m}c_\alpha h_\alpha(U).
\]
They converge to \(f(X)\) in L2. Conditional Jensen gives
\[
\|\mathbb E[F_m(U)-f(X)\mid V]\|_2^2
\leq\mathbb E[(F_m(U)-f(X))^2]\longrightarrow0.
\]
For each finite sum the conditional Hermite identity gives
\[
\mathbb E[F_m(U)\mid V]
=\sum_{|\alpha|\leq m}c_\alpha m_\alpha h_\alpha(V).
\]
Because the transformation between \(V\) and \(\widetilde X\) is invertible, they generate the same sigma-field. The preceding limit and the zero conditional mean of \(\epsilon\) prove
\[
g^*(\widetilde X)=\mathbb E[f(X)\mid\widetilde X]
=\sum_{\alpha\in\mathbb N_0^d}c_\alpha m_\alpha h_\alpha(V)
\]
in L2. Substituting the definition of \(V\) proves the first target. In particular, this is an equality of L2 classes, not an assertion of pointwise convergence at every observed value.

The series is square-summable: orthonormality and the supplied clean expansion give \(\sum_\alpha c_\alpha^2=\mathbb E[f(X)^2]<\infty\), and \(0<m_\alpha\leq1\).

### Bayes risk and the affine subspace

For any admissible \(q\), the product \((Y-g^*(\widetilde X))(g^*(\widetilde X)-q(\widetilde X))\) is integrable by Cauchy–Schwarz. Conditioning on \(\widetilde X\) shows its expectation is zero. Hence
\[
\mathbb E[(Y-q(\widetilde X))^2]
=\mathbb E[(Y-g^*(\widetilde X))^2]
+\mathbb E[(g^*(\widetilde X)-q(\widetilde X))^2].
\]
Conditional Jensen ensures \(g^*\) is admissible, so
\[
R_{\rm Bayes}=\mathbb E[(Y-g^*(\widetilde X))^2].
\]
All these risks are finite for admissible predictors, and both infima in the task are finite since the zero predictor is admissible.

Let \(\mathcal A\) be the linear subspace of L2 consisting of random variables \(a+b^\top\widetilde X\). Write \(0\) for the zero multi-index and \(e_j\) for the \(j\)-th coordinate unit multi-index. Since \(h_0(V)=1\), \(h_{e_j}(V)=V_j\), and
\[
\widetilde X=\mu+(\Lambda+\Sigma_\eta)^{1/2}V,
\]
we have
\[
\mathcal A=\operatorname{span}\{h_0(V),h_{e_1}(V),\ldots,h_{e_d}(V)\}.
\]
Thus \(\mathcal A\) is precisely the span of the degree-at-most-one modes and is finite-dimensional and closed.

Set
\[
P=\sum_{|\alpha|\leq1}c_\alpha m_\alpha h_\alpha(V),\qquad H=g^*(\widetilde X)-P.
\]
The L2 expansion and orthonormality show that \(H\) is orthogonal to \(\mathcal A\). Consequently, for every \(\ell\in\mathcal A\),
\[
\|g^*(\widetilde X)-\ell\|_2^2=\|H\|_2^2+\|P-\ell\|_2^2.
\]
Its minimum is attained at \(\ell=P\). Combining this with the risk decomposition yields
\[
R_{\rm lin}^*-R_{\rm Bayes}=\|H\|_2^2.
\]
Finally, applying the finite-sum norm identity and then taking the L2 limit gives
\[
\|H\|_2^2
=\sum_{|\alpha|\geq2}(c_\alpha m_\alpha)^2
=\sum_{|\alpha|\geq2}c_\alpha^2\prod_{j=1}^d\rho_j^{\alpha_j}.
\]
This proves the second target. Constant or affine \(f\), vanishing nonlinear coefficients, and zero label noise require no separate assumptions: the same calculation applies, with nonlinear energy zero when appropriate. Zero measurement variance is outside the explicitly stated source range restored in the task, and no noise-limit assertion is required.
