# Reference Proof

## Proof Structure

Express the weighted least-squares estimator as a weighted average of the taskwise OLS estimators. Its conditional mean gives the task-mismatch bias, while independence and centering of the Gaussian noises give its conditional covariance. The standard inverse-Wishart mean identity evaluates the expected covariance contribution and establishes integrability. Independent test noise then gives the exact risk. Compute the zero-weight baseline directly, and compare the two risks without dividing by a possibly zero or negative mismatch/noise coefficient.

## Complete Proof

### step_001: Existence, measurability, and normal equations

Let \(A=X^\top X\) and \(\Lambda=\sum_{k=1}^K\lambda_k\). Write \(X=G\Sigma_x^{1/2}\), where \(G\) has independent standard Gaussian entries. Because \(N\geq d\), the first \(d\) rows of \(G\) form a square matrix whose determinant is a nonzero polynomial in continuously distributed entries. That determinant vanishes with probability zero. Since \(\Sigma_x\) is positive definite, \(X\) consequently has full column rank almost surely.

The objective has positive-definite Hessian \(2(1+\Lambda)A\) on this event, so its unique minimizer satisfies
\[
\widehat w=\frac{1}{1+\Lambda}A^{-1}X^\top\left(Y_m+\sum_{k=1}^K\lambda_kY_k\right).
\]
This is a measurable function on the full-rank event and can be assigned any fixed value on its null complement without changing any expectation.

### step_002: Conditional mean and mismatch bias

Substituting the label model yields
\[
\widehat w=\frac{w_m^*+\sum_k\lambda_kw_k^*}{1+\Lambda}
+\frac{1}{1+\Lambda}A^{-1}X^\top\eta,
\qquad
\eta=\varepsilon_m+\sum_k\lambda_k\varepsilon_k.
\]
All weights are deterministic. The centered training noises are independent of \(X\), so \(\mathbb E[\eta\mid X]=0\). Thus
\[
\mu:=\mathbb E[\widehat w\mid X]
=\frac{w_m^*+\sum_k\lambda_kw_k^*}{1+\Lambda}
\]
is deterministic. For \(\Lambda>0\), the definitions of \(\lambda'_k\) and \(w_a^*\) give
\[
b:=\mu-w_m^*=\frac{\Lambda}{1+\Lambda}(w_a^*-w_m^*).
\]
In particular,
\[
b^\top\Sigma_xb=\left(\frac{\Lambda}{1+\Lambda}\right)^2
\|\Sigma_x^{1/2}(w_a^*-w_m^*)\|^2.
\]

### step_003: Conditional covariance

Let \(v=\sigma_m^2+\sum_k\lambda_k^2\sigma_k^2\). Independence across tasks and entries, centering, and independence from \(X\) imply
\[
\mathbb E[\eta\eta^\top\mid X]=vI_N.
\]
Consequently,
\[
\operatorname{Cov}(\widehat w\mid X)
=\frac{1}{(1+\Lambda)^2}A^{-1}X^\top(vI_N)XA^{-1}
=\frac{v}{(1+\Lambda)^2}A^{-1}.
\]
This calculation remains valid when some or all noise variances vanish.

### step_004: Exact design moment and integrability

Use the following standard independent result, recorded as theory_020: if \(z_1,\ldots,z_N\) are independent \(\mathcal N(0,\Sigma)\) vectors in \(\mathbb R^d\), \(\Sigma\) is positive definite, and \(N>d+1\), then for their Wishart Gram matrix \(A=\sum_{i=1}^Nz_iz_i^\top\),
\[
\mathbb E[A^{-1}]=\frac{\Sigma^{-1}}{N-d-1}.
\]
Here the rows of \(X\) are exactly these Gaussian vectors with scale \(\Sigma_x\), and all hypotheses are part of the setup. Hence
\[
\mathbb E[A^{-1}]=\frac{\Sigma_x^{-1}}{N-d-1},
\qquad
\operatorname{tr}\bigl(\Sigma_x\mathbb E[A^{-1}]\bigr)=\frac{d}{N-d-1}.
\]
For the centered estimator part \(\nu=\widehat w-\mu\), conditional second moments and nonnegativity give
\[
\mathbb E\|\nu\|^2
=\frac{v}{(1+\Lambda)^2}\frac{\operatorname{tr}(\Sigma_x^{-1})}{N-d-1}<\infty.
\]
Thus \(\widehat w\) is square integrable, and the expectations and bias-variance decomposition below are justified.

### step_005: Test risk and the zero-weight baseline

The test feature and test noise are independent of the estimator and of each other, with zero means, feature covariance \(\Sigma_x\), and noise variance \(\sigma_m^2\). Therefore
\[
\mathbb E[(x^\top\widehat w-y_m)^2\mid\widehat w]
=\sigma_m^2+(\widehat w-w_m^*)^\top\Sigma_x(\widehat w-w_m^*).
\]
Since \(\mu\) is deterministic and \(\mathbb E[\nu\mid X]=0\), taking expectations gives
\[
E_K=\sigma_m^2+b^\top\Sigma_xb+
\operatorname{tr}\!\left(\Sigma_x\mathbb E[\operatorname{Cov}(\widehat w\mid X)]\right).
\]
For \(\Lambda>0\), inserting the preceding calculations proves
\[
E_K=\frac{\sigma_m^2+\sum_k\lambda_k^2\sigma_k^2}{(1+\Lambda)^2}\frac{d}{N-d-1}
+\left(\frac{\Lambda}{1+\Lambda}\right)^2\|\Sigma_x^{1/2}(w_a^*-w_m^*)\|^2+\sigma_m^2.
\]

For the baseline, set every auxiliary weight to zero directly in the normal equations; do not evaluate \(w_a^*\) or \(\lambda'_k\) at zero total weight. Then
\[
\widehat w_0=w_m^*+A^{-1}X^\top\varepsilon_m,
\qquad
\mathbb E[\widehat w_0\mid X]=w_m^*,
\qquad
\operatorname{Cov}(\widehat w_0\mid X)=\sigma_m^2A^{-1}.
\]
The same test-risk calculation gives
\[
E_0=\sigma_m^2\frac{d}{N-d-1}+\sigma_m^2.
\]
Nonnegativity of the auxiliary weights ensures that \(\Lambda=0\) is exactly the case in which all auxiliary weights vanish.

### step_006: Necessary-and-sufficient comparison

For \(\Lambda>0\), put
\[
c=\frac{d}{N-d-1}>0,\qquad
S=\sum_k(\lambda'_k)^2\sigma_k^2,\qquad
M=\|\Sigma_x^{1/2}(w_a^*-w_m^*)\|^2.
\]
Using \(\sum_k\lambda_k^2\sigma_k^2=\Lambda^2S\), the exact risk difference is
\[
E_K-E_0
=\frac{\Lambda^2\bigl[(S-\sigma_m^2)c+M\bigr]-2\sigma_m^2c\Lambda}{(1+\Lambda)^2}.
\]
The denominator and \(\Lambda\) are strictly positive, so
\[
E_K<E_0
\iff
\Lambda\bigl[(S-\sigma_m^2)c+M\bigr]<2\sigma_m^2c,
\]
which is the claimed equivalence. No division by \(\sigma_m^2\), \(S\), \(M\), or the bracketed coefficient occurs. Thus this proof covers zero individual weights, zero variances, identical or cancelling auxiliary parameters, and every sign of the bracketed coefficient. In particular, if \(\sigma_m^2=0\), then \(E_0=0\) and the displayed strict inequality is impossible because its left side is \(\Lambda(Sc+M)\geq0\), as required.

## Private Source-Audit Notes

The source explicitly centers every training-noise entry at L000069; specifying variances alone in the original public task did not reproduce that model. The source's conditional expectations and cross-task cancellation at L000232-L000252 confirm the independence semantics used here. Its weights are fixed parameters in these exact expectation calculations, not weights estimated from the same training sample.

The previously applied theory_005 source repair is retained: L000239-L000240 must contain the squared numerator \(\Lambda^2\), as determined by L000238 and the stated error formula at L000107. Two additional local notation slips in that proof are also recorded: L000233 requires \(X^\top\) before each conditional noise mean, and the vector second moments at L000249-L000252 must be written using outer products and \(\sigma_t^2I_N\). The proof above uses the dimensionally correct forms throughout.

The informal task-count regime at L000068 supplies no numerical threshold. The selected finite-sample OLS derivation uses only finite sums over tasks and does not require a task-count-versus-dimension inequality; no arbitrary replacement for that informal comparison is assumed. The stronger sample-size requirement for the separate network branch is not inherited by this chain. All theorem-critical obligations are closed; the sole external probabilistic identity used is the explicitly stated standard independent inverse-Wishart mean result with verified hypotheses.
