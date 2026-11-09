# Problem

## Setup

Let \(d,p\) be positive integers. Let \(X_0\) be an \(\mathbb R^d\)-valued random variable and let \(X_1\sim\mathcal N(0,I_d)\) be independent of \(X_0\). Their joint law does not depend on the model parameter \(\theta\). Fix \(0\le r\le t\le1\), and define
\[
X_t=(1-t)X_0+tX_1,\qquad V_c=X_1-X_0.
\]
Assume \(\mathbb E\|X_0\|<\infty\) and \(\mathbb E[\|V_c\|^2\mid X_t]<\infty\) almost surely. Define the induced conditional-mean velocity and its fluctuation by
\[
V(x,t)=\mathbb E[V_c\mid X_t=x],\qquad
\xi=V_c-V(X_t,t),\qquad
\Sigma=\operatorname{Cov}(\xi\mid X_t).
\]
Thus \(\mathbb E[\xi\mid X_t]=0\). Conditional quantities are understood up to almost-sure equality, and expectations are over the endpoint sampling with \(r,t\) fixed.

Let \(\theta\) range over an open subset of \(\mathbb R^p\), and let \(U_\theta(x,r,t)\in\mathbb R^d\) be deterministic and differentiable in \(x,t,\theta\), with mixed derivatives \(\nabla_\theta\partial_xU_\theta\) and \(\nabla_\theta\partial_tU_\theta\). Time derivatives at endpoints are understood one-sided. The functions and derivatives used here are measurable and finite-valued. At \((X_t,r,t)\), write
\[
H=\nabla_\theta U_\theta\in\mathbb R^{d\times p},\qquad
K=(t-r)\partial_xU_\theta-I_d,
\]
and define the forward mean residual
\[
R=U_\theta+(t-r)(\partial_xU_\theta\,V+\partial_tU_\theta)-V,
\]
where \(V=V(X_t,t)\). The operator \(\operatorname{sg}[\cdot]\) has the same forward value as its argument and zero derivative with respect to \(\theta\).

Define the stopped sample loss and the unstopped sample and population losses by
\[
\ell_{\rm sg}=\left\|U_\theta+(t-r)\operatorname{sg}[\partial_xU_\theta\,V_c+\partial_tU_\theta]-V_c\right\|^2,
\]
\[
\ell_{\rm full}=\left\|U_\theta+(t-r)(\partial_xU_\theta\,V_c+\partial_tU_\theta)-V_c\right\|^2,
\qquad L_{\rm full}=\mathbb E[\ell_{\rm full}],
\]
and let \(G_{\rm sg}=\mathbb E[\nabla_\theta\ell_{\rm sg}]\), where the derivative respects the stop-gradient.

For the population assertions, assume
\[
\mathbb E[\ell_{\rm full}]<\infty,\qquad
\mathbb E\|\nabla_\theta\ell_{\rm full}\|<\infty,\qquad
\mathbb E\|\nabla_\theta\ell_{\rm sg}\|<\infty,
\]
\[
\mathbb E\left\|\bigl(\nabla_\theta(\partial_xU_\theta\,V+\partial_tU_\theta)\bigr)^\top R\right\|<\infty,
\qquad
\mathbb E\left\|\nabla_\theta\operatorname{Tr}(K\Sigma K^\top)\right\|<\infty.
\]
Assume also that \(L_{\rm full}\) is differentiable at the parameter under consideration and differentiation may be passed through its expectation:
\[
\nabla_\theta L_{\rm full}=\mathbb E[\nabla_\theta\ell_{\rm full}].
\]

For a finite-valued deterministic measurable proxy \(\widehat V(x,t)\), set \(b=\widehat V(X_t,t)-V\). For a scalar \(\beta\in[0,1]\), held fixed when taking parameter derivatives, define
\[
V_\beta=(1-\beta)V_c+\beta\widehat V(X_t,t),
\]
\[
\ell_\beta=\left\|U_\theta+(t-r)\operatorname{sg}[\partial_xU_\theta\,V_\beta+\partial_tU_\theta]-V_c\right\|^2,
\]
and
\[
h_\beta=\nabla_\theta\ell_\beta,\qquad
M(\beta)=\mathbb E\left[\left\|h_\beta-2H^\top R\right\|^2\mid X_t\right].
\]

## Task

Prove the following integrated claim.

1. The stopped sample-gradient has conditional covariance
\[
\operatorname{Cov}(\nabla_\theta\ell_{\rm sg}\mid X_t)=4H^\top K\Sigma K^\top H,
\]
and therefore
\[
\operatorname{Tr}\operatorname{Cov}(\nabla_\theta\ell_{\rm sg}\mid X_t)
=4\operatorname{Tr}(H^\top K\Sigma K^\top H).
\]
Moreover,
\[
\begin{aligned}
\nabla_\theta L_{\rm full}-G_{\rm sg}
={}&2(t-r)\mathbb E\left[\bigl(\nabla_\theta(\partial_xU_\theta\,V+\partial_tU_\theta)\bigr)^\top R\right]\\
&+\mathbb E\left[\nabla_\theta\operatorname{Tr}(K\Sigma K^\top)\right].
\end{aligned}
\]
In particular, if \(R=0\) almost surely, the difference is precisely the expected parameter derivative of the conditional-velocity variance term.

2. Let \(A=K+I_d\). Show that, for every \(\beta\in[0,1]\),
\[
M(\beta)=4\beta^2\|H^\top Ab\|^2
+4\operatorname{Tr}\left(H^\top(K-\beta A)\Sigma(K-\beta A)^\top H\right).
\]
At a conditioned state, suppose additionally that
\[
K=\kappa I_d,\qquad \Sigma=\sigma^2I_d,\qquad HH^\top=\gamma I_d,
\]
where \(\kappa>0\), \(\gamma>0\), \(\sigma\ge0\), and \(\sigma^2d+\|b\|^2>0\). Prove that \(M\), minimized over \(\beta\in[0,1]\), has the unique minimizer
\[
\beta^*=\frac{\kappa}{\kappa+1}\frac{\sigma^2d}{\sigma^2d+\|b\|^2},
\]
and that
\[
M(\beta^*)=4\gamma\frac{\sigma^2d\,\kappa^2\|b\|^2}{\sigma^2d+\|b\|^2}.
\]
