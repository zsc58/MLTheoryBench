# Reference Proof

## Proof obligations

1. Verify that the posterior and curation law are normalized and that the fiber-constant reweight can be canceled almost everywhere.
2. Verify the Gaussian conditional laws and strictly positive conditional variances, including the case with no resolved coordinates.
3. Derive the conditional coverage formula, the centered undercoverage criterion, and strict decrease with the absolute standardized mean gap.
4. Construct indistinguishable positive-definite Gaussian truths that actually change each claimed non-identifiable quantity, including coverage and the presence of undercoverage.
5. Transfer indistinguishability to statistics and fixed measurable deterministic archives.

## Standard background used

For a jointly Gaussian vector (R,T) with mean (mu_R,mu_T) and positive-definite covariance
\[
\begin{pmatrix}H&K^T\\K&J\end{pmatrix},
\]
the conditional law of T given R=r is Gaussian with mean mu_T+K H^{-1}(r-mu_R) and covariance J-K H^{-1}K^T. Both H and the Schur complement are positive definite. To see the formula, the residual E=T-mu_T-K H^{-1}(R-mu_R) has zero cross-covariance with R. Its joint Gaussian density with R therefore factors, giving independence and the displayed conditional law. Positivity follows by evaluating the joint covariance quadratic form on (-H^{-1}K^T t,t) for nonzero t. If R has dimension zero, conditioning is absent. This is the relevant standard independent result recorded in theory_019; no Woodbury or testing inequality is needed.

## Complete proof

### 1. Normalization and conditional invariance

Let k=rank(A). The matrix [U N] is orthogonal, so x=Ur+Nb is a change to orthonormal coordinates with unit absolute Jacobian. Since AN=0, p(y|Ur+Nb)=p(y|Ur).

The regularizer measurement marginal is
\[
Z_\rho(y)=\mathcal N(y;A\mu_\rho,A\Sigma_\rho A^T+\Gamma).
\]
Its covariance is positive definite because Gamma is positive definite. Consequently Z_rho(y) is finite and strictly positive for every y, and pi_rho(\cdot|y) is a normalized density. Tonelli's theorem gives
\[
\int q_\rho(x)\,dx
=\int p_*^Y(y)\left(\int\pi_\rho(x|y)\,dx\right)dy=1.
\]
Bayes' formula yields
\[
q_\rho(Ur+Nb)=\rho(Ur+Nb)g(r),\qquad
 g(r)=\int p_*^Y(y)\frac{p(y|Ur)}{Z_\rho(y)}\,dy.
\]
All integrands are nonnegative, and g(r)>0. Integrating in b gives q_rho^R(r)=rho^R(r)g(r). Since rho^R is strictly positive and q_rho^R integrates to one, g is finite for Lebesgue-almost every r. Hence, on this full-measure set,
\[
q_\rho(b|r)
=\frac{\rho(Ur+Nb)g(r)}{\rho^R(r)g(r)}
=\rho(b|r).
\]
The truth's resolved marginal also has a strictly positive Gaussian density, so this exceptional set is null under the truth as well. If k=0, R has only one value and the likelihood does not depend on x; directly Z_rho(y)=p(y|x), g=1, and q_rho=rho. Thus the same conclusion holds in the zero-dimensional resolved space.

### 2. Conditional Gaussian parameters

For j in {rho,*} and k>0, the vector (R,V) is jointly Gaussian. The rows of [U v]^T are linearly independent because v is a unit vector orthogonal to the columns of U. Therefore its covariance is positive definite: for every nonzero coefficient vector a, ([U v]a)^T Sigma_j([U v]a)>0. The conditioning result above applies and gives
\[
m_j(r)=v^T\mu_j+v^T\Sigma_jU(U^T\Sigma_jU)^{-1}(r-U^T\mu_j),
\]
\[
s_j^2=v^T\Sigma_jv-v^T\Sigma_jU(U^T\Sigma_jU)^{-1}U^T\Sigma_jv>0.
\]
In particular, the conditional standard deviations do not depend on r. If k=0, these formulas are replaced by m_j=v^T mu_j and s_j^2=v^T Sigma_j v>0.

Because v belongs to the span of N, V is a function of b alone in the split coordinates. The conditional invariance just proved therefore gives the curated conditional law V|R=r as N(m_rho(r),s_rho^2) almost everywhere.

### 3. Coverage and monotonicity

Since 0<alpha<1, z=Phi^{-1}(1-alpha/2) is finite and strictly positive. Under the truth, conditional on R=r, standardizing V gives
\[
C_*(r)=\Pr_*\{|V-m_\rho(r)|\le z s_\rho\mid R=r\}
=\Phi(\delta(r)+z s_\rho/s_*)-\Phi(\delta(r)-z s_\rho/s_*),
\]
where delta(r)=(m_rho(r)-m_*(r))/s_*.

At delta(r)=0 this becomes 2Phi(z s_rho/s_*)-1. Strict increase of Phi, together with z>0, shows that this is less than 1-alpha=2Phi(z)-1 exactly when s_rho<s_*.

For the mean-gap claim, fix a=z s_rho/s_*>0 and write f(delta)=Phi(delta+a)-Phi(delta-a). Normal symmetry gives f(-delta)=f(delta). Writing phi for the standard normal density, for delta>0,
\[
f'(\delta)=\phi(\delta+a)-\phi(\delta-a)<0,
\]
because (delta+a)^2-(delta-a)^2=4delta a>0 and phi(t)=(2pi)^{-1/2}exp(-t^2/2). Thus coverage strictly decreases as |delta| increases at fixed width ratio and alpha. This also shows that every nonzero mean gap lowers coverage relative to the centered case of the same width.

### 4. Actual changes in the non-identifiable quantities

Integrating the linear Gaussian observation model gives
\[
p_*^Y=\mathcal N(A\mu_*,A\Sigma_*A^T+\Gamma).
\]
For example, this follows by representing Y=AX+epsilon with epsilon independent of X and distributed as N(0,Gamma); the Gaussian means and covariances then add.

For any fixed Gaussian truth and any real h, replacing mu_* by mu_*+hv leaves A mu_* unchanged. For any t>0, replacing Sigma_* by Sigma_*+t vv^T preserves positive definiteness and leaves A Sigma_* A^T unchanged. Since U^T v=0, the first change adds h to m_*(r) without changing s_*, and the second adds t to s_*^2 without changing m_*(r). These assertions follow directly from the conditional formulas, also in the k=0 case. Thus the scalar spread and standardized mean gap cannot be determined by the measurement marginal.

To verify explicitly that coverage itself changes, hold the prescribed regularizer fixed and take the following candidate truths:
\[
p_0=\mathcal N(\mu_\rho,\Sigma_\rho),\qquad
p_t=\mathcal N(\mu_\rho,\Sigma_\rho+t vv^T),\quad t>0.
\]
They are positive-definite Gaussian laws with the same measurement marginal. Under p_0, m_0=m_rho and s_0=s_rho, so C_0(r)=1-alpha. Under p_t, m_t=m_rho and s_t^2=s_rho^2+t, so
\[
C_t(r)=2\Phi\!\left(\frac{z s_\rho}{\sqrt{s_\rho^2+t}}\right)-1<1-\alpha.
\]
Thus both coverage and its deficit differ, at every resolved readout, despite identical measurement laws. This pair also distinguishes absence from presence of inherited blind undercoverage.

For an equally explicit mean-gap witness, take
\[
p_h=\mathcal N(\mu_\rho+h v,\Sigma_\rho),\quad h\ne0.
\]
It has the same measurement law as p_0, but delta_h=-h/s_rho rather than zero. Its coverage is strictly smaller than that of p_0 by the monotonicity proved above. All these comparisons keep A, Gamma, rho, U, N, v, and alpha fixed. Since q_rho is determined by the measurement law and rho, the curated law is also identical within each pair.

These pairs prove non-identifiability in the stated parameter class: equality of measurement laws does not force equality of s_*(r), delta(r), C_*(r), or (1-alpha)-C_*(r).

### 5. Statistics and deterministic archives

For any positive integer n, independent measurements from two candidate truths with the same p_*^Y have identical product laws. Applying any one fixed measurable statistic, or any one fixed measurable deterministic archive map, produces identical pushforward laws under the two truths. The map may use the known model and regularizer, but is the same map under both truths and has no access to the unknown truth parameters.

In particular, under the nominal-versus-undercovering pair p_0,p_t, any event that a measurement-based procedure flags as undercoverage has the same probability under both truths. Such a procedure cannot distinguish these two cases; equivalently, its power against this pair equals its false-positive probability. This is the asserted impossibility of detecting inherited blind overconfidence in general, not a claim that an arbitrary diagnostic can never flag a particular data realization.

All five proof obligations are closed.
