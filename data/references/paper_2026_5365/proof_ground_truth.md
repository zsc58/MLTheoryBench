# Reference Proof

## Proof Structure

First verify integrability and decompose the same-group update bias into a coupling covariance and a marginal preconditioner bias. Independence of the numerator and denominator groups makes the corresponding cross-fitted covariance exactly zero. Next, use a quadratic Taylor expansion with a third-order remainder to identify the ordinary transform's order-\(m^{-1}\) bias. Derive unbiasedness and second-moment control of the microbatch-mean variance estimator, then show that the plug-in subtraction cancels the leading term with an order-\(m^{-3/2}\) remainder. Finally, lift the scalar estimates through the fixed aligned basis and use independence from the gradient estimate.

## Complete Proof

All expectations below are under the conditional law specified in the setup. The denominator-statistic law and the parameters \(d,a,\lambda\) are fixed in the sample-size asymptotics.

### Integrability, bias decomposition, and independence

For \(x\geq0\),

\[
0<T_a(x)\leq\lambda^{-a},\qquad
T_a''(x)=a(a+1)(x+\lambda)^{-a-2},
\]

and

\[
T_a'''(x)=-a(a+1)(a+2)(x+\lambda)^{-a-3}.
\]

Consequently, writing

\[
C_2=a(a+1)\lambda^{-a-2},\qquad
C_3=a(a+1)(a+2)\lambda^{-a-3},
\]

we have \(|T_a''(x)|\leq C_2\) and \(|T_a'''(x)|\leq C_3\) on the entire domain of every sample mean, not merely in a neighborhood of its population mean.

Both ordinary preconditioner estimators have operator norm at most \(\lambda^{-a}\). Their products with the integrable vector \(\widehat g_A\) are therefore integrable. To check the corrected estimator, use

\[
\sum_{j=1}^m(X_{j,k}-\bar X_k)^2
=\sum_{j=1}^m(X_{j,k}-\mu_k)^2-m(\bar X_k-\mu_k)^2
\leq\sum_{j=1}^m(X_{j,k}-\mu_k)^2.
\]

Thus \(\widehat V_k\geq0\) and

\[
\mathbb E\widehat V_k\leq\frac{\sigma_k^2}{m-1}<\infty.
\]

The definition of the correction gives

\[
\|\widetilde H_B\|_{\mathrm{op}}
\leq\lambda^{-a}+\frac{C_2}{2}\max_{1\leq k\leq d}\widehat V_k.
\]

Since \(d\) is finite, \(\mathbb E\|\widetilde H_B\|_{\mathrm{op}}<\infty\). The entire group \(B\) is independent of the entire group \(A\), so

\[
\mathbb E\|\widetilde H_B\widehat g_A\|
\leq\mathbb E\|\widetilde H_B\|_{\mathrm{op}}\,
\mathbb E\|\widehat g_A\|<\infty.
\]

All matrix-vector expectations and factorizations used below are therefore justified. No second moment of the numerator estimator is required.

Define

\[
\operatorname{Cov}(\widehat H_A,\widehat g_A)
=\mathbb E[\widehat H_A\widehat g_A]
-\mathbb E[\widehat H_A]\,\mathbb E[\widehat g_A].
\]

Using \(\mathbb E\widehat g_A=g\), adding and subtracting \(\mathbb E[\widehat H_A]g\) gives

\[
\mathbb E[\widehat H_A\widehat g_A]-Hg
=\operatorname{Cov}(\widehat H_A,\widehat g_A)
 +(\mathbb E\widehat H_A-H)g.
\]

Both \(\widehat H_B\) and \(\widetilde H_B\) are measurable functions of group \(B\) and the fixed parameters, including \(Q\). Independence therefore gives

\[
\mathbb E[\widehat H_B\widehat g_A]-Hg
=(\mathbb E\widehat H_B-H)g,
\qquad
\mathbb E[\widetilde H_B\widehat g_A]-Hg
=(\mathbb E\widetilde H_B-H)g.
\]

In particular, the cross-fitted coupling covariances vanish exactly.

### Sample-mean and variance-estimator moments

Fix a coordinate \(k\) and suppress its index. Set

\[
Y_j=X_{j,k}-\mu_k,\qquad
\delta=\frac1m\sum_{j=1}^mY_j,\qquad
\sigma^2=\mathbb EY_1^2,\qquad
\tau_4=\mathbb EY_1^4,\qquad V=\widehat V_k.
\]

The \(Y_j\) are independent and identically distributed, have mean zero, and satisfy \(\tau_4<\infty\). Independence yields

\[
\mathbb E\delta=0,\qquad
\mathbb E\delta^2=\frac{\sigma^2}{m}.
\]

In the expansion of \((\sum_jY_j)^4\), only fourth powers and products containing two pairs have nonzero expectations. Hence

\[
\mathbb E\delta^4
=\frac{m\tau_4+3m(m-1)\sigma^4}{m^4}
=\frac{\tau_4+3(m-1)\sigma^4}{m^3}
=O(m^{-2}).
\]

Hölder's inequality then gives

\[
\mathbb E|\delta|^3\leq(\mathbb E\delta^4)^{3/4}
=O(m^{-3/2}).
\]

For the variance estimator, the centered sum-of-squares identity gives

\[
V=\frac{\sum_{j=1}^mY_j^2-m\delta^2}{m(m-1)}.
\]

Taking expectations proves the required normalization exactly:

\[
\mathbb EV
=\frac{m\sigma^2-m(\sigma^2/m)}{m(m-1)}
=\frac{\sigma^2}{m}
=\operatorname{Var}(\bar X_k).
\]

Moreover, nonnegativity and Cauchy-Schwarz imply

\[
V^2
\leq\frac{(\sum_{j=1}^mY_j^2)^2}{m^2(m-1)^2}
\leq\frac{\sum_{j=1}^mY_j^4}{m(m-1)^2}.
\]

Therefore, for every \(m\geq2\),

\[
\mathbb EV^2\leq\frac{\tau_4}{(m-1)^2}
\leq\frac{4\tau_4}{m^2}.
\]

This explicitly establishes the sample-variance second-moment bound under the given fourth-moment assumption.

### Ordinary transform bias

The whole segment between \(\mu_k\) and \(\bar X_k\) lies in \([0,\infty)\). Taylor's theorem and the support-wide bound on the third derivative therefore give

\[
T_a(\mu_k+\delta)
=T_a(\mu_k)+T_a'(\mu_k)\delta
 +\frac12T_a''(\mu_k)\delta^2+R,
\qquad |R|\leq\frac{C_3}{6}|\delta|^3.
\]

Taking expectations and using the moment estimates gives

\[
\mathbb ET_a(\bar X_k)
=T_a(\mu_k)
 +\frac{T_a''(\mu_k)\sigma_k^2}{2m}
 +O(m^{-3/2}).
\]

Thus the ordinary inverse or inverse-root bias is \(O(m^{-1})\). Its displayed leading coefficient is nonnegative and is positive whenever \(\sigma_k^2>0\), since \(T_a''(\mu_k)>0\).

### Plug-in correction and cancellation

The derivative bound makes \(T_a''\) Lipschitz on \([0,\infty)\), with Lipschitz constant \(C_3\). Without assuming independence between \(\delta\) and \(V\), Cauchy-Schwarz gives

\[
\begin{aligned}
\left|\mathbb E[(T_a''(\bar X_k)-T_a''(\mu_k))V]\right|
&\leq C_3\mathbb E[|\delta|V]\\
&\leq C_3(\mathbb E\delta^2)^{1/2}(\mathbb EV^2)^{1/2}\\
&\leq\frac{2C_3\sigma_k\sqrt{\tau_4}}{m^{3/2}}
=O(m^{-3/2}).
\end{aligned}
\]

Together with the exact identity for \(\mathbb EV\), this yields

\[
\mathbb E[T_a''(\bar X_k)\widehat V_k]
=T_a''(\mu_k)\frac{\sigma_k^2}{m}+O(m^{-3/2}).
\]

Subtracting half of this expression from the ordinary Taylor expansion cancels the entire order-\(m^{-1}\) term:

\[
\mathbb E\left[T_a(\bar X_k)-\frac12T_a''(\bar X_k)\widehat V_k\right]
=T_a(\mu_k)+O(m^{-3/2}).
\]

The bound is an expectation bound established by explicit moment estimates, not an inference from a stochastic-order statement alone.

### Matrix lifting and expected updates

Apply the scalar conclusions to every coordinate. The fourth-moment bound is uniform over the fixed finite set of coordinates. The orthogonal matrix \(Q\) is fixed under the conditional law, so it can be taken outside expectations. Orthogonal conjugation preserves operator norm, and the operator norm of a diagonal matrix is the largest absolute diagonal entry. Consequently,

\[
\mathbb E\widehat H_B-H
=\frac{1}{2m}Q\operatorname{diag}
\big(T_a''(\mu_k)\sigma_k^2\big)_{k=1}^dQ^\top
 +R_m,
\qquad \|R_m\|_{\mathrm{op}}=O(m^{-3/2}),
\]

and

\[
\|\mathbb E\widetilde H_B-H\|_{\mathrm{op}}=O(m^{-3/2}).
\]

These arguments require no independence between different coordinates of one observation.

Combining these matrix estimates with the independence factorizations gives

\[
\mathbb E[\widehat H_B\widehat g_A]-Hg
=\frac{1}{2m}Q\operatorname{diag}
\big(T_a''(\mu_k)\sigma_k^2\big)_{k=1}^dQ^\top g
 +R_mg,
\]

where

\[
\|R_mg\|\leq C m^{-3/2}\|g\|.
\]

Likewise,

\[
\|\mathbb E[\widetilde H_B\widehat g_A]-Hg\|
\leq\|\mathbb E\widetilde H_B-H\|_{\mathrm{op}}\|g\|
=O(m^{-3/2})\|g\|.
\]

The constants depend only on the fixed parameters and moment bounds, not on \(m\). The argument divides by neither \(\sigma_k\), \(\mu_k\), nor \(\|g\|\), so it includes zero variances, zero population entries, and \(g=0\); in the last case both cross-fitted update biases are exactly zero. Positive damping handles zero denominator entries. No eigengap assumption is needed, because the basis is fixed, including when population eigenvalues repeat.

This proves every asserted decomposition, coupling-removal identity, marginal bias expansion, and expected-update bound for the theoretical unclipped estimators. It makes no claim for a correction computed in a random empirical eigenbasis.
