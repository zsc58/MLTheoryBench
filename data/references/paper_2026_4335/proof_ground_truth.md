# Reference Proof

## Proof Structure and Obligations

The proof must preserve two different conditioning operations: minibatch averaging at a fixed full training state, followed by stationary-state averaging at a fixed radius. Its obligations are: (1) justify pointwise evaluation under the specified conditional laws and derive the task second-moment decomposition; (2) incorporate the actual post-task decay contribution; (3) justify the outer stationarity identity without identifying it with pointwise zero drift; (4) evaluate at the selected zero-drift radius; (5) solve the quadratic and handle feasible zero-heat cases; and (6) establish the three precise limiting regimes. Each obligation is derived below. The final optional interpretation is not needed for any of them.

## Complete Proof

Suppress the fixed input. At a fixed state \(s\), let \(z=f(x;\theta(s))\), \(r=\|z\|>0\), \(\hat z=z/r\), and \(\delta=\Delta z_{\rm task}(s,B)\). Write \(\mathbb E_B\) for integration over the prescribed fresh-minibatch law with the update functions evaluated at \(s\). The public definitions specify
\[
\mu(s)=\mathbb E_B[r\delta],\qquad C(s)=\operatorname{Cov}_B(r\delta).
\]
These are the actual minibatch moments, not independently chosen versions on exceptional states. Whenever \(\mathbb E_B\|\delta\|^2<\infty\), write \(r\delta=\mu(s)+\xi\), where \(\mathbb E_B\xi=0\). Expanding the square gives
\[
\mathbb E_B\|r\delta\|^2=\|\mu(s)\|^2+\operatorname{tr}C(s).
\]
Consequently,
\[
\mathbb E_B[\|z+\delta\|^2-\|z\|^2]
=2\hat z^\top\mu(s)+\frac{\|\mu(s)\|^2+\operatorname{tr}C(s)}{r^2}.
\]
This holds pointwise at each state having the stated finite minibatch second moment.

Fix a radius \(R\) used in the task, and let \(Q_R\) be its specified conditional state law. By the public domain requirement, \(r=R\) for \(Q_R\)-almost every state. Moreover, under the joint experiment that first draws \(s\) from \(Q_R\) and then a fresh minibatch, both \(\mathbb E\|\delta\|^2\) and \(\mathbb E R_{t+1}^2\) are finite. Thus the preceding local identity holds for \(Q_R\)-almost every state and can be integrated. In particular,
\[
\mathbb E[\|z_t^+\|^2-R^2\mid R_t=R]
=2\widetilde D_R+\frac{M_R^2+\widetilde V_R^2}{R^2}
=2\widetilde D_R+\frac{\Sigma_R^2}{R^2}.
\]
Here the radius-conditioned expectation means precisely the specified joint experiment. The same integration shows
\[
\Sigma_R^2=\mathbb E[\|R_t\delta\|^2\mid R_t=R].
\]
No almost-everywhere conditional identity has been extended to a selected exceptional radius without justification: the argument was performed directly under \(Q_R\), using its fiber support and the pointwise minibatch definitions. This also explains why a fixed regular conditional-distribution version alone would not have sufficed.

The direction cannot be pulled outside a radius-conditioned expectation, because it generally varies across states on the same radius fiber. Likewise, \(M_R^2\) is an average of squared local means, not the squared mean after radius averaging. The conditional task increment is integrable: on this fiber, \(\mathbb E\|z_t^+\|^2\leq 2R^2+2\mathbb E\|\delta\|^2<\infty\). The conditional next-state second moment also makes the decay increment integrable.

The embedding increment splits exactly into its task and post-task decay increments. By the definition of effective damping,
\[
\mathbb E[\|z_{t+1}\|^2-\|z_t^+\|^2\mid R_t=R]
=-2\eta\bar\lambda_{\rm rad}(R)R^2.
\]
This includes all interactions with the task step. Therefore, defining the radius-conditioned squared-norm drift by \(g(R)=\mathbb E[R_{t+1}^2-R_t^2\mid R_t=R]\), we obtain at every evaluation radius
\[
g(R)=2\widetilde D_R+\frac{\Sigma_R^2}{R^2}-2\eta\bar\lambda_{\rm rad}(R)R^2.
\]

For the outer stationary identity, the global second-moment assumptions imply
\[
\mathbb E\|z_t^+\|^2\leq 2\mathbb E R_t^2+2\mathbb E\|\delta\|^2<\infty.
\]
Stationarity gives \(\mathbb E R_{t+1}^2=\mathbb E R_t^2<\infty\). Both substep squared-norm differences are therefore globally integrable. The task cross term is integrable by Cauchy–Schwarz, and the task energy term is integrable by the assumption on \(\delta\). The conditional-law construction agrees almost everywhere with stationary conditional expectation. Hence the tower property gives
\[
\mathbb E[g(R_t)]=\mathbb E[R_{t+1}^2-R_t^2]=0.
\]
The fiber-support and conditional-integrability properties used above hold almost everywhere under the stationary radius law; the public task additionally ensures them at every radius it explicitly evaluates. This averaged identity does not imply \(g(R)=0\) at an arbitrary radius. The task instead selects \(R_{\rm eq}>0\) with zero conditional drift, so \(g(R_{\rm eq})=0\) is part of its equilibrium definition. No quantitative concentration argument is being asserted.

Set \(a=\eta\bar\lambda_{\rm rad}(R_{\rm eq})>0\). The conditional finiteness assumptions make \(a\) finite. Evaluating the drift at the selected radius gives
\[
0=2\widetilde D_{R_{\rm eq}}+\frac{\Sigma_{R_{\rm eq}}^2}{R_{\rm eq}^2}-2aR_{\rm eq}^2.
\]
Multiply by \(R_{\rm eq}^2/a\) and use the definitions of \(D_*\) and \(V_*^2\) to obtain
\[
2R_{\rm eq}^4-2D_*R_{\rm eq}^2-V_*^2=0.
\]

### Root and boundary cases

First check which zero-heat cases are compatible with these definitions. If \(V_*^2=0\), then \(\Sigma_{R_{\rm eq}}^2=0\). Its two summands \(M_{R_{\rm eq}}^2\) and \(\widetilde V_{R_{\rm eq}}^2\) are nonnegative, so \(\mathbb E[\|\mu_t\|^2\mid R_t=R_{\rm eq}]=0\). Hence \(\mu_t=0\) almost surely under that conditional law, and \(\widetilde D_{R_{\rm eq}}=0\). The zero-drift equation would then say \(0=-2aR_{\rm eq}^2\), contradicting \(a>0\) and \(R_{\rm eq}>0\). Thus a selected positive equilibrium necessarily has \(V_*^2>0\), even though no separate positive-heat assumption was imposed.

Freeze the evaluated coefficients and write \(y=R_{\rm eq}^2\). The two roots of \(2y^2-2D_*y-V_*^2=0\) are
\[
y_\pm=\frac{D_*\pm\sqrt{D_*^2+2V_*^2}}{2}.
\]
Since \(V_*^2>0\), the square root is strictly larger than \(|D_*|\), so \(y_-<0<y_+\). This proves the displayed formula, positivity, and uniqueness among nonnegative solutions for these evaluated coefficients.

For clarity, if arbitrary unrelated coefficients were allowed, \(V_*^2=0,D_*>0\) would give two nonnegative roots, \(0\) and \(D_*\). That case is not a counterexample under the task's moment definitions. Nor does algebraic uniqueness for evaluated coefficients imply that the original radius-dependent function \(g\) has only one zero.

### Limiting regimes

Let \(V_*=\sqrt{V_*^2}\). Along any family of admissible equilibria with \(V_*\to\infty\) and bounded \(D_*\),
\[
\frac{R_{\rm eq}^2}{V_*}
=\frac{D_*/V_*+\sqrt{(D_*/V_*)^2+2}}{2}
\longrightarrow\frac1{\sqrt2}.
\]
Thus \(R_{\rm eq}^2\sim V_*/\sqrt2\).

When \(D_*>0\), rationalizing the difference gives
\[
R_{\rm eq}^2-D_*
=\frac{V_*^2}{\sqrt{D_*^2+2V_*^2}+D_*}.
\]
It lies between zero and \(V_*^2/(2D_*)\). In particular, when \(V_*^2/D_*^2\to0\),
\[
R_{\rm eq}^2=D_*+O(V_*^2/D_*),
\]
with a numerical implied constant independent of the family.

When \(D_*<0\), put \(b=|D_*|\). Rationalization gives
\[
R_{\rm eq}^2=\frac{V_*^2}{\sqrt{b^2+2V_*^2}+b}.
\]
Because positive equilibria have \(V_*^2>0\), the ratio defining the asserted asymptotic is meaningful. If \(V_*^2/b^2\to0\), then
\[
\frac{R_{\rm eq}^2}{V_*^2/(2b)}
=\frac{2}{\sqrt{1+2V_*^2/b^2}+1}\longrightarrow1.
\]
This proves the inward-drift limit.

## Optional Interpretation, Not Used in the Proof

At a fixed differentiable model state, suppose additionally that the task update is SGD-style and that first-order parameter linearization is an appropriate approximation. Write \(J_z(x)\) for the parameter Jacobian and \(K(x,X)=J_z(x)J_z(X)^\top\). The chain rule gives
\[
\Delta z_{\rm task}(x)\approx-\eta\sum_kK(x,X_k)\nabla_{z(X_k)}L
=-\eta\sum_kK(x,X_k)\frac{s_k}{\|z(X_k)\|},
\qquad s_k=\|z(X_k)\|\nabla_{z(X_k)}L.
\]
These are gradients of the full averaged minibatch loss; no extra averaging factor is inserted. Multiplying by \(R=\|z(x)\|\) retains factors \(R/\|z(X_k)\|\). Replacing these factors by one additionally uses the source's comparable-neighbor-norm approximation; the resulting expression is for \(R\Delta z_{\rm task}\), not for \(\Delta z_{\rm task}\).

Differentiating scale invariance with respect to the scale of a nonzero source embedding gives \(z(X_k)^\top\nabla_{z(X_k)}L=0\). Hence \(s_k\) is tangent. With \(P_u^\perp=I-uu^\top\),
\[
\hat z(x)^\top K(x,X_k)s_k
=\bigl(P_{\hat z(X_k)}^\perp K(x,X_k)^\top\hat z(x)\bigr)^\top s_k.
\]
This explains the radial projection in the moment definitions. It makes no unconditional NTK approximation claim for arbitrary optimizers and supplies no additional hypothesis to the exact equilibrium proof.
