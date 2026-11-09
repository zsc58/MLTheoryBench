# Reference Proof

## Contract and scope

The initial parameter and step sizes are deterministic. The sigma-field \(\mathcal F_t\) contains the information before drawing the estimator used for update \(t\); \(\widehat g_t\) is \(\mathcal F_{t+1}\)-measurable. Smoothness holds on the whole deterministic parameter ball, which contains every update segment. The update is projection onto the linear subspace only: an additional radius projection is not part of the recursion being analyzed.

The executed action distribution uses the stated clipping convention. No unmodified-Gaussian score identity, Fisher identity, policy-gradient normalization, RL Hessian bound, or exponential-map estimate is needed: the objective's smoothness and the estimator's conditional properties are primitive hypotheses. The operator comparisons hold for the supplied SPD operators, including Fisher operators when these are well defined.

## 1. Conditional projected progress

Write \(g_t=\nabla J(\theta_t)\), \(d_t=P_{\mathfrak g}g_t\), and \(e_t=\widehat g_t-g_t\). Conditional unbiasedness gives \(\mathbb E[e_t\mid\mathcal F_t]=0\). Orthogonal projection is linear, self-adjoint, idempotent, and nonexpansive. Therefore
\[
\mathbb E[P_{\mathfrak g}\widehat g_t\mid\mathcal F_t]=d_t,
\qquad
\langle g_t,d_t\rangle_F=\|d_t\|_F^2,
\]
and
\[
\begin{aligned}
\mathbb E[\|P_{\mathfrak g}\widehat g_t\|_F^2\mid\mathcal F_t]
&=\|d_t\|_F^2+\mathbb E[\|P_{\mathfrak g}e_t\|_F^2\mid\mathcal F_t]\\
&\le \|d_t\|_F^2+\sigma_g^2.
\end{aligned}
\]
The cross term vanishes by conditional unbiasedness.

Integrating the gradient along the segment between successive iterates and using its Lipschitz bound gives
\[
J(\theta_{t+1})\ge J(\theta_t)+\langle g_t,\theta_{t+1}-\theta_t\rangle_F-\frac L2\|\theta_{t+1}-\theta_t\|_F^2.
\]
Consequently,
\[
\mathbb E[J(\theta_{t+1})\mid\mathcal F_t]
\ge J(\theta_t)+\eta_t\left(1-\frac{L\eta_t}{2}\right)\|d_t\|_F^2-\frac{L\eta_t^2\sigma_g^2}{2}.
\]
Since \(\eta_t\le1/L\),
\[
\mathbb E[J(\theta_{t+1})\mid\mathcal F_t]
\ge J(\theta_t)+\frac{\eta_t}{2}\|d_t\|_F^2-\frac{L\eta_t^2\sigma_g^2}{2}.\tag{1}
\]
All quantities needed here are integrable: bounded rewards bound the objective, and continuous gradients on the deterministic compact parameter ball are bounded. The conditional variance bound then gives finite estimator second moments.

## 2. Telescoping and weighted summability

Taking expectations in (1) and summing gives
\[
\frac12\sum_{t<N}\eta_t\mathbb E\|d_t\|_F^2
\le J^*-J(\theta_0)+\frac{L\sigma_g^2}{2}\sum_{t<N}\eta_t^2.\tag{2}
\]
For the infinite-horizon schedule, the right side is uniformly finite. Monotone convergence proves
\[
\sum_{t\ge0}\eta_t\mathbb E\|d_t\|_F^2<\infty.
\]
Tonelli then yields
\[
\mathbb E\left[\sum_{t\ge0}\eta_t\|d_t\|_F^2\right]<\infty,
\]
so the nonnegative random series is finite almost surely.

## 3. Almost-sure objective convergence

Set
\[
X_t=J^*-J(\theta_t),\qquad b_t=\frac{L\sigma_g^2\eta_t^2}{2},\qquad
Z_t=X_t+\sum_{k=t}^{\infty}b_k.
\]
The tail is finite and deterministic. By (1), \(Z_t\) is an integrable, nonnegative, adapted supermartingale:
\[
\mathbb E[Z_{t+1}\mid\mathcal F_t]\le Z_t-\frac{\eta_t}{2}\|d_t\|_F^2\le Z_t.
\]
We use the standard nonnegative-supermartingale convergence theorem: an integrable adapted process \(Z_t\ge0\) satisfying \(\mathbb E[Z_{t+1}\mid\mathcal F_t]\le Z_t\) converges almost surely to a finite random variable. Its hypotheses have just been verified; its expectations are bounded by \(\mathbb E Z_0<\infty\). Since the deterministic tail tends to zero, \(X_t\), and hence \(J(\theta_t)\), converges almost surely.

The source additionally states a liminf consequence, not an unweighted limit. Indeed, if \(\liminf_t\mathbb E\|d_t\|_F^2>0\), divergence of \(\sum_t\eta_t\) contradicts the weighted summability. This observation is not an additional target of the frozen task.

## 4. Fixed-horizon rate

For a separately run horizon \(T\ge1\), take \(\eta_t=\eta/\sqrt T\), where \(0<\eta\le1/L\). This ensures the step bound, while
\[
\sum_{t<T}\eta_t=\eta\sqrt T,\qquad \sum_{t<T}\eta_t^2=\eta^2.
\]
Divide (2) by \(\eta\sqrt T/2\) to obtain
\[
\frac1T\sum_{t<T}\mathbb E\|d_t\|_F^2
\le\frac{2(J^*-J(\theta_0))}{\eta\sqrt T}+\frac{L\eta\sigma_g^2}{\sqrt T}.
\]
The infinite-horizon summability conditions are not imposed on this finite constant schedule.

## 5. Natural-gradient quadratic forms and expectation scope

For each realization, the inverse of an SPD operator has eigenvalues between \(1/\lambda_{\max,t}\) and \(1/\lambda_{\min,t}\). Expanding \(d_t\) in an orthonormal eigenbasis gives
\[
\frac{\|d_t\|_F^2}{\lambda_{\max,t}}
\le \langle d_t,F_t^{-1}d_t\rangle_F
\le \frac{\|d_t\|_F^2}{\lambda_{\min,t}}.
\]
Taking nonnegative expectations and averaging proves
\[
\frac1T\sum_{t<T}\mathbb E\langle d_t,F_t^{-1}d_t\rangle_F
\le\frac1T\sum_{t<T}\mathbb E\left[\frac{\|d_t\|_F^2}{\lambda_{\min,t}}\right].
\]
These expectations are well defined as extended nonnegative integrals. Positive definiteness at every realization alone does not ensure a finite expected inverse quadratic form.

Let \(m_T=\operatorname{ess\,inf}_\omega\min_{t<T}\lambda_{\min,t}(\omega)\). If \(m_T>0\), then \(\lambda_{\min,t}\ge m_T\) almost surely for every \(t<T\), and therefore
\[
\frac1T\sum_{t<T}\mathbb E\langle d_t,F_t^{-1}d_t\rangle_F
\le\frac1{m_T}\frac1T\sum_{t<T}\mathbb E\|d_t\|_F^2.
\]
In particular the displayed finite-horizon rate transfers with the factor \(1/m_T\). If the eigenvalues are deterministic, \(m_T=\min_{t<T}\lambda_{\min,t}>0\). No independence between \(F_t\) and \(d_t\) was assumed or used. If \(m_T=0\), only the expectation-within-the-weight statement is asserted.

## 6. Alignment, including a derivation of Kantorovich

For an SPD operator \(A\) with eigenvalues \(\lambda_i\in[m,M]\), \(0<m\le M\), and nonzero vector \(x\), let \(w_i\) be the normalized squared coordinates of \(x\) in an orthonormal eigenbasis. Thus \(w_i\ge0\) and \(\sum_iw_i=1\). Because \((\lambda_i-m)(\lambda_i-M)\le0\),
\[
\frac1{\lambda_i}\le\frac{m+M-\lambda_i}{mM}.
\]
Writing \(a=\sum_iw_i\lambda_i\), we obtain
\[
\frac{\langle x,Ax\rangle\langle x,A^{-1}x\rangle}{\|x\|^4}
\le\frac{a(m+M-a)}{mM}
\le\frac{(m+M)^2}{4mM}.
\]
This also covers \(m=M\). In the endpoint-weight description, the product is \(1+t(1-t)(M-m)^2/(mM)\), maximized at \(t=1/2\) for distinct endpoints, correcting the source's local arithmetic error.

Now fix an iterate with \(d_t\ne0\) and put \(h=F_t^{-1/2}d_t\ne0\). Then
\[
\langle d_t,F_t^{-1}d_t\rangle_F=\|h\|_F^2,
\quad \|d_t\|_F^2=\langle h,F_th\rangle_F,
\quad \|F_t^{-1}d_t\|_F^2=\langle h,F_t^{-1}h\rangle_F.
\]
Apply the proved inequality with \(A=F_t\), \(m=\lambda_{\min,t}\), and \(M=\lambda_{\max,t}\). It follows that
\[
\alpha_t^2\ge\frac{4\lambda_{\min,t}\lambda_{\max,t}}{(\lambda_{\min,t}+\lambda_{\max,t})^2}
=\frac{4\kappa_t}{(\kappa_t+1)^2}.
\]
Positive definiteness makes the cosine strictly positive, so
\[
\alpha_t\ge\frac{2\sqrt{\kappa_t}}{\kappa_t+1}.
\]
When \(d_t=0\), the quadratic forms vanish and no cosine is asserted. When \(\kappa_t=1\), the bound is exactly 1.
