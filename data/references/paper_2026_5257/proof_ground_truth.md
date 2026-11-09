# Reference Proof

## Proof Structure

The obligations are to derive the conditional stopped-gradient covariance, compare full and stopped population gradients, separate the mixed-tangent gradient error into conditional bias and centered noise, and minimize its scalar-isotropic quadratic over the specified interval. All parameters and times are fixed during these calculations; the data law is independent of the parameters.

## Complete Proof

Write \(U=U_\theta(X_t,r,t)\). By the definition of the conditional mean,
\[
\mathbb E[\xi\mid X_t]=0,\qquad
\mathbb E[\xi\xi^\top\mid X_t]=\Sigma.
\]
All quantities \(U,H,K,R\), conditional on \(X_t\), are deterministic. The stated conditional second-moment hypothesis makes the conditional quadratic calculations below finite.

The forward value of the stopped residual is
\[
\begin{aligned}
&U+(t-r)\operatorname{sg}[\partial_xU\,V_c+\partial_tU]-V_c\\
&=R+\bigl((t-r)\partial_xU-I_d\bigr)\xi
=R+K\xi.
\end{aligned}
\]
Because the stop-gradient blocks differentiation through the bracketed term,
\[
\nabla_\theta\ell_{\rm sg}=2H^\top(R+K\xi).
\]
Its conditional mean is \(2H^\top R\), and its centered version is \(2H^\top K\xi\). Consequently,
\[
\operatorname{Cov}(\nabla_\theta\ell_{\rm sg}\mid X_t)
=4H^\top K\Sigma K^\top H.
\]
Taking the trace proves the trace assertion. Integrability of the stopped gradient and the tower property also give
\[
G_{\rm sg}=2\mathbb E[H^\top R].
\]

For the full-gradient comparison, let \(F\) denote the residual inside \(\ell_{\rm full}\), and put \(q=\partial_xU\,V+\partial_tU\). The same forward-value calculation gives \(F=R+K\xi\). Thus conditional centering establishes the loss decomposition
\[
\mathbb E[\|F\|^2\mid X_t]
=\|R\|^2+\operatorname{Tr}(K\Sigma K^\top),
\]
and hence
\[
L_{\rm full}=\mathbb E\bigl[\|R\|^2+\operatorname{Tr}(K\Sigma K^\top)\bigr].
\]
To obtain the gradient identity without requiring separate differentiation-under-expectation assumptions for these two summands, differentiate the original sample loss and then condition.

For a parameter coordinate \(j\), let \(H_j\) be column \(j\) of \(H\), \(Q_j=\partial_{\theta_j}q\), and \(K_j=\partial_{\theta_j}K\). Since the data law, \(V\), and \(\xi\) do not depend on \(\theta\),
\[
\partial_{\theta_j}F=H_j+(t-r)Q_j+K_j\xi.
\]
Differentiating \(\ell_{\rm full}=\|F\|^2\), multiplying out, and conditioning therefore gives
\[
\mathbb E[\partial_{\theta_j}\ell_{\rm full}\mid X_t]
=2\bigl(H_j+(t-r)Q_j\bigr)^\top R
+2\operatorname{Tr}(K_j\Sigma K^\top).
\]
The terms linear in \(\xi\) vanish by conditional centering. Moreover, symmetry of \(\Sigma\) and the product rule give
\[
\partial_{\theta_j}\operatorname{Tr}(K\Sigma K^\top)
=\operatorname{Tr}(K_j\Sigma K^\top+K\Sigma K_j^\top)
=2\operatorname{Tr}(K_j\Sigma K^\top).
\]
The public integrability assumptions make the resulting terms integrable. Taking expectations and using the stated interchange for \(L_{\rm full}\) yields
\[
\nabla_\theta L_{\rm full}
=2\mathbb E[H^\top R]
+2(t-r)\mathbb E[(\nabla_\theta q)^\top R]
+\mathbb E[\nabla_\theta\operatorname{Tr}(K\Sigma K^\top)].
\]
Subtracting \(G_{\rm sg}\) proves the claimed identity. If \(R=0\) almost surely, its mean-residual term vanishes. This is an exact statement at the parameter under consideration; no asymptotic convergence assertion is needed.

For the mixed tangent, set \(A=K+I_d\). Since \(V_c=V+\xi\) and \(\widehat V=V+b\),
\[
V_\beta=V+(1-\beta)\xi+\beta b.
\]
The forward residual of \(\ell_\beta\) is therefore
\[
\begin{aligned}
&U+(t-r)\operatorname{sg}[\partial_xU\,V_\beta+\partial_tU]-V_c\\
&=R+\bigl((1-\beta)K-\beta I_d\bigr)\xi+\beta(K+I_d)b\\
&=R+(K-\beta A)\xi+\beta Ab.
\end{aligned}
\]
Only \(U\) differentiates through this stopped residual, so
\[
h_\beta-2H^\top R
=2H^\top\bigl((K-\beta A)\xi+\beta Ab\bigr).
\]
The proxy bias is deterministic given \(X_t\); hence the cross term in the conditional squared norm is zero. It follows that
\[
M(\beta)=4\beta^2\|H^\top Ab\|^2
+4\operatorname{Tr}\bigl(H^\top(K-\beta A)\Sigma(K-\beta A)^\top H\bigr).
\]

Under the scalar-isotropic hypotheses, \(A=(\kappa+1)I_d\), \(K-\beta A=(\kappa-\beta(\kappa+1))I_d\), and \(HH^\top=\gamma I_d\). Thus
\[
M(\beta)=4\gamma\left[
\beta^2(\kappa+1)^2\|b\|^2
+\sigma^2d\bigl(\kappa-\beta(\kappa+1)\bigr)^2
\right].
\]
Let \(S=\sigma^2d\) and \(B=\|b\|^2\). The bracketed quadratic has coefficient \((\kappa+1)^2(S+B)>0\). Its derivative vanishes precisely when
\[
\beta(\kappa+1)^2(S+B)=S\kappa(\kappa+1),
\]
so its unique unconstrained minimizer is
\[
\beta^*=\frac{\kappa}{\kappa+1}\frac{S}{S+B}.
\]
Since \(S,B\ge0\), \(S+B>0\), and \(\kappa>0\),
\[
0\le\beta^*\le\frac{\kappa}{\kappa+1}<1.
\]
It is therefore also the unique minimizer on \([0,1]\). In particular, \(S=0\) gives the admissible endpoint minimizer \(\beta^*=0\); \(B=0\) gives \(\beta^*=\kappa/(\kappa+1)\). Substitution gives
\[
M(\beta^*)=4\gamma\frac{\kappa^2SB}{S+B},
\]
including both boundary cases, and proves the required optimum value.

## Source-Audit Note

The source index previously alleged that the two cross traces in the general matrix expansion might differ. This is false: for symmetric \(G\) and \(\Sigma\),
\[
\operatorname{Tr}(GK\Sigma A^\top)
=\operatorname{Tr}((GK\Sigma A^\top)^\top)
=\operatorname{Tr}(A\Sigma K^\top G)
=\operatorname{Tr}(GA\Sigma K^\top).
\]
No symmetrization repair is needed. The proof above retains the exact factor four throughout and does not depend on the source's auxiliary, differently normalized quadratic expansion. Every obligation in the public task has been explicitly derived.
