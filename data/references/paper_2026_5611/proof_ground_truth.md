# Reference Proof

## Proof Structure

Factor the two Gaussian likelihoods as one Gaussian density in the latent variable times a factor depending on the noisy state and observation. Differentiate the resulting conditional-density factorization, derive the Gaussian-smoothing identity directly, and identify the remaining normalized density with the conditional latent law. All conditioning uses the pointwise density-ratio convention in the task; no unconditional moment assumption on the prior is needed.

## Theorem-Critical Obligations

- **step_005 — Well-definedness and analytic justification:** Verify positive finite normalizers, positive definiteness of the covariance, finite conditional first moments, and the integral differentiations used below. These are established directly by Gaussian bounds.
- **step_001 — Gaussian factorization:** Expand and complete the joint likelihood quadratic to obtain the stated covariance and center.
- **step_002 — Conditional-score differentiation:** Differentiate the factorized conditional density, including the normalizer and the matrix chain rule.
- **step_003 — Smoothing-score conversion:** Derive the anisotropic Gaussian-smoothing identity from its defining integral and perform the cancellation.
- **step_004 — Posterior-mean identification:** Identify the two normalized conditional densities and hence their means.

Every obligation is closed in the proof below. No specialized external result is used as an unproved dependency.

## Complete Proof

Write \(\varphi_C(\cdot)\) for the centered Gaussian density with covariance \(C\). Fix \(t\), abbreviate \(a=a_t\), \(b=b_t\), and \(Z=Z_t\).

### Well-defined pointwise densities and smoothing means

For any \(h\in\mathbb R^d\),
\[
 h^\top Qh=\frac{a^2}{b^2}\|h\|^2+\tau^{-2}\|Hh\|^2\ge 0.
\]
If this expression vanishes, both nonnegative terms vanish and hence \(Qh=0\). Invertibility therefore implies strict positivity for every nonzero \(h\). Thus \(Q\) and \(S=Q^{-1}\) are symmetric positive definite.

Independence gives the joint density
\[
 f_{U,Z,R}(u,z,r)=p(u)\varphi_{b^2I_d}(z-au)\varphi_{\tau^2I_m}(r-Hu).
\]
Set
\[
 F(z,r)=\int_{\mathbb R^d}p(u)\varphi_{b^2I_d}(z-au)\varphi_{\tau^2I_m}(r-Hu)\,du,
\qquad
 G(r)=\int_{\mathbb R^d}p(u)\varphi_{\tau^2I_m}(r-Hu)\,du.
\]
Both functions are strictly positive and finite at every argument: the Gaussian factors are strictly positive and bounded, and \(p\) integrates to one. Integration first in \(z\) shows \(\int F(z,r)\,dz=G(r)\). Consequently, the conditional density in the task is
\[
 p_{Z\mid R}(z\mid r)=\frac{F(z,r)}{G(r)},
\]
and the pointwise conditional density of \(U\) given \((Z,R)=(z,r)\) is \(f_{U,Z,R}(u,z,r)/F(z,r)\).

For any symmetric positive-definite \(C\), the joint density of \((U,U+\xi)\) is \(p(u)\varphi_C(v-u)\). Thus \(0<p^C(v)<\infty\), and the conditional density defining \(M_C(v)\) is
\[
 \frac{p(u)\varphi_C(v-u)}{p^C(v)}.
\]
Its first absolute moment is finite for every \(v\). Indeed, if \(c>0\) is the smallest eigenvalue of \(C^{-1}\), then
\[
 \|u\|\varphi_C(v-u)
 \le K_C\bigl(\|v\|+\|u-v\|\bigr)
       \exp\!\left(-\frac c2\|u-v\|^2\right),
\]
where \(K_C=(2\pi)^{-d/2}(\det C)^{-1/2}\). For fixed \(v\), the right-hand side is bounded as a function of \(u\). Multiplication by \(p(u)\) and integration therefore prove absolute convergence. In particular,
\[
 M_C(v)=\frac{\int u\varphi_C(v-u)p(u)\,du}{p^C(v)}
\]
is a finite vector, without requiring \(\int\|u\|p(u)\,du<\infty\).

We also justify the needed differentiation. A continuously differentiable integrand whose first derivatives on a neighborhood are bounded by an integrable function can be differentiated under its integral; this follows by expressing difference quotients through the derivatives and applying dominated convergence. Here every first derivative of \(\varphi_C(v-u)\) is a linear polynomial in \(v-u\) times that Gaussian and is bounded uniformly in \(v-u\). Its product with \(p(u)\) is therefore dominated by a constant times the integrable function \(p(u)\). This verifies the hypotheses at every \(v\) and also gives continuity of the resulting derivatives.

### Gaussian factorization

Let
\[
 q=\frac{a}{b^2}z+\tau^{-2}H^\top r.
\]
Expanding the two Gaussian exponents as functions of \(u\) gives
\[
 -\frac{\|z-au\|^2}{2b^2}-\frac{\|r-Hu\|^2}{2\tau^2}
 =-\frac12u^\top Q u+q^\top u-
 \frac{\|z\|^2}{2b^2}-\frac{\|r\|^2}{2\tau^2}.
\]
With \(S=Q^{-1}\) and \(w=S q\), completing the square yields
\[
 -\frac12u^\top Qu+q^\top u
 =-\frac12(u-w)^\top S^{-1}(u-w)+\frac12q^\top Sq.
\]
Hence there is a positive smooth factor \(C(z,r)\), independent of \(u\), such that
\[
 \varphi_{b^2I_d}(z-au)\varphi_{\tau^2I_m}(r-Hu)
 = C(z,r)\varphi_S(u-w).
\]
The Gaussian normalization constants depend only on the fixed parameters, so
\[
 \log C(z,r)=\text{constant}-\frac{\|z\|^2}{2b^2}
 -\frac{\|r\|^2}{2\tau^2}+\frac12q^\top Sq.
\]
Using \(\varphi_S(u-w)=\varphi_S(w-u)\), integration against the prior gives
\[
 F(z,r)=C(z,r)p^S(w),\qquad
 p_{Z\mid R}(z\mid r)=\frac{C(z,r)}{G(r)}p^S(w).
\]
This also proves that the conditional density is positive and continuously differentiable in \(z\) for every \(r\), so its score exists everywhere.

### Conditional-score differentiation

Since \(S\) is symmetric and independent of \(z\),
\[
 \nabla_z\log C(z,r)=-\frac{z}{b^2}+\frac{a}{b^2}w,
 \qquad
 J_z w=\frac{a}{b^2}S,
\]
where \(J_z w\) is the Jacobian matrix of \(w\) with respect to \(z\). The marginal normalizer \(G(r)\) is independent of \(z\). The chain rule therefore gives
\[
 \nabla_z\log p_{Z\mid R}(z\mid r)
 =-\frac{z}{b^2}+\frac{a}{b^2}w
   +\frac{a}{b^2}S\nabla_v\log p^S(v)\big|_{v=w}. \tag{1}
\]

### Gaussian-smoothing identity and cancellation

By the integral differentiation already justified,
\[
 \nabla_v p^S(v)
 =\int \varphi_S(v-u)S^{-1}(u-v)p(u)\,du.
\]
Divide by the positive quantity \(p^S(v)\). The normalized integral uses exactly the conditional density defining \(M_S(v)\), with finite first absolute moment. It follows that
\[
 S\nabla_v\log p^S(v)=M_S(v)-v. \tag{2}
\]
Substituting (2) with \(v=w\) into (1) cancels the two terms involving \(w\), yielding
\[
 \nabla_z\log p_{Z\mid R}(z\mid r)
 =\frac{1}{b^2}\bigl(aM_S(w)-z\bigr).
\]
This proves the score formula at every \((z,r)\).

### Posterior-mean identity

The factorization and its integrated form give the pointwise conditional latent density
\[
 \frac{f_{U,Z,R}(u,z,r)}{F(z,r)}
 =\frac{\varphi_S(u-w)p(u)}{p^S(w)}.
\]
This is exactly the density of \(U\) conditional on \(U+\xi=w\), for independent \(\xi\sim\mathcal N(0,S)\). Its first absolute moment is finite by the bound established above with \(C=S\) and \(v=w\). Taking its mean proves
\[
 \mathbb E[U\mid Z=z,R=r]=M_S(w(z,r))
\]
for every \(z,r\), under the specified density-ratio convention.

No step divides by \(a\). In particular, when \(a=0\), invertibility requires \(H\) to have full column rank, and the same proof gives the score \(-z/b^2\) and the stated posterior-mean identity. Rank-deficient \(H\), including \(H=0\), is allowed whenever \(Q\) is invertible. Times with \(b=0\) or singular \(Q\) remain outside the stated domain.
