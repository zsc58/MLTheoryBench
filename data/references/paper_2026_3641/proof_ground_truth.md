# Reference Proof

## Proof Structure

For any fixed recalibration, the estimator is a sampled residual mean plus $\lambda$ times a fixed population surrogate mean. Simple-random-sampling variance and quadratic minimization give the oracle variance as a constant times one minus squared finite-population correlation. The conditional-regression residual is orthogonal to every function of the proxy, so covariance with a recalibration depends only on the conditional regression. Cauchy-Schwarz identifies its maximal squared correlation with the nonparametric regression R-squared, attained by the regression itself. A separate constant-regression case and the nondegenerate equality condition yield the affine/non-affine characterization.

## Complete Proof

Write $E_N[Z]=N^{-1}\sum_{i=1}^N Z_i$, $\operatorname{Var}_N(Z)=E_N[(Z-E_NZ)^2]$, and $\operatorname{Cov}_N(Z,W)=E_N[(Z-E_NZ)(W-E_NW)]$. Fix a measurable $\phi$ and put $s_i=\phi(\hat Y_i)$. For fixed $\lambda\in\mathbb R$,
\[
\hat\theta_\lambda(\phi)=\lambda E_N[s]+\frac1n\sum_{i\in L}(Y_i-\lambda s_i),
\]
so it is unbiased for $\theta_\star$. With variance normalized by $N$, the exact simple-random-sampling-without-replacement formula is
\[
\operatorname{Var}(\hat\theta_\lambda(\phi))=D\operatorname{Var}_N(Y-\lambda s),\qquad D=\frac{N-n}{n(N-1)}>0.
\]
If $\operatorname{Var}_N(s)>0$, minimizing this quadratic yields
\[
\lambda^*(\phi)=\frac{\operatorname{Cov}_N(Y,s)}{\operatorname{Var}_N(s)},\qquad V^*(\phi)=DS_Y^2[1-\rho_N^2(Y,s)].
\]
If $\operatorname{Var}_N(s)=0$, the estimator is the labeled mean for every $\lambda$; choosing $\lambda^*(\phi)=0$ gives the same variance formula under the stipulated zero-correlation convention.

Let $m(z)=E_N[Y\mid\hat Y=z]$. The residual $R_i=Y_i-m(\hat Y_i)$ has zero sum in every fiber of equal proxy value. Since $\phi(\hat Y_i)-E_N[\phi(\hat Y)]$ is constant on each fiber, $\operatorname{Cov}_N(R,\phi(\hat Y))=0$. Hence
\[
\operatorname{Cov}_N(Y,\phi(\hat Y))=\operatorname{Cov}_N(m(\hat Y),\phi(\hat Y)).
\]
When $\operatorname{Var}_N(\phi(\hat Y))>0$, Cauchy-Schwarz gives
\[
\rho_N^2(Y,\phi(\hat Y))\le \frac{\operatorname{Var}_N(m(\hat Y))}{S_Y^2}=R^2_{Y\sim\hat Y}.
\]
For a constant recalibration the correlation is zero, so the inequality still holds. If $\operatorname{Var}_N(m(\hat Y))>0$, choosing $\phi=m$ makes $\operatorname{Cov}_N(Y,m(\hat Y))=\operatorname{Var}_N(m(\hat Y))$ and attains equality. If $m(\hat Y)$ is constant, every recalibration has zero covariance with $Y$, and $\phi=m$ also attains the bound under the convention. Consequently,
\[
\inf_\phi V^*(\phi)=DS_Y^2(1-R^2_{Y\sim\hat Y}).
\]
For $\phi_{\rm id}(z)=z$, $V^*(\phi_{\rm id})=DS_Y^2[1-\rho_N^2(Y,\hat Y)]$, and subtraction gives the stated gain.

It remains to characterize equality for the identity, whose proxy variance is positive. If $m(\hat Y)$ is constant, both $R^2_{Y\sim\hat Y}$ and $\rho_N^2(Y,\hat Y)$ are zero; $m$ is affine and there is no strict improvement. If $m(\hat Y)$ is nonconstant, equality in the correlation bound for the identity holds precisely when its centered vector is proportional to the centered proxy vector. Equivalently, $m(\hat Y_i)=a+b\hat Y_i$ for every $i$, with $b\ne0$. Thus in all cases equality holds exactly when $m$ is affine on the finite proxy support. Since $D S_Y^2>0$, strict improvement occurs exactly when $m$ is non-affine.
