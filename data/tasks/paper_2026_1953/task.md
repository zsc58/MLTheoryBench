# Problem

## Setup

Let \(\Theta\subset\mathbb R^p\) be open, let \(N\ge1\) be the finite number of robust constraints, and let \(m,n\ge1\). For each \(\eta\in\Theta\), let \(C_{\eta,1}\subset\mathbb R^m\) be nonempty, convex, compact, and contain the origin in its interior. Let \(g_\eta\) be its gauge and define
\[
C_{\eta,r}=\{u:g_\eta(u)\le r\}=rC_{\eta,1},\qquad r>0.
\]
For a nonempty set \(C\), write \(\sigma_C(w)=\sup_{u\in C}\langle w,u\rangle\).

Let \(X\subset\mathbb R^n\) be closed and convex, let \(f:X\to\mathbb R\cup\{+\infty\}\) be convex, and let \(a_j:X\to\mathbb R\) be convex, with bounds \(b_j\in\mathbb R\) and fixed vectors \(w_j\in\mathbb R^m\), \(j=1,\ldots,N\). For \((\eta,r)\in\Theta\times(0,\infty)\), define
\[
W(\eta,r)=\inf_{x\in X}\left\{f(x):a_j(x)+\sigma_{C_{\eta,r}}(w_j)\le b_j\ \text{for }j=1,\ldots,N\right\},
\]
with value \(+\infty\) when infeasible. Assume \(\inf_{x\in X}f(x)>-\infty\). At every pair where \(W\) is finite, assume there is \(\bar x\in\operatorname{ri}(X)\), the relative interior of \(X\), such that \(f(\bar x)<\infty\) and
\[
a_j(\bar x)+\sigma_{C_{\eta,r}}(w_j)<b_j\qquad(j=1,\ldots,N).
\]
Assume each map \(\eta\mapsto\sigma_{C_{\eta,1}}(w_j)\) is continuously differentiable.

An optimal dual multiplier at \((\eta,r)\) means a maximizer over \(\lambda\in[0,\infty)^N\) of
\[
\inf_{x\in X}\left[f(x)+\sum_{j=1}^N\lambda_j\bigl(a_j(x)+\sigma_{C_{\eta,r}}(w_j)-b_j\bigr)\right].
\]
Assume this dual supremum is attained wherever \(W\) is finite.

For a locally Lipschitz real-valued function \(h\) on an open neighborhood, use the Clarke subdifferential convention
\[
h^\circ(z;d)=\limsup_{y\to z,\ t\downarrow0}\frac{h(y+td)-h(y)}{t},\qquad
\partial^C h(z)=\{v:\langle v,d\rangle\le h^\circ(z;d)\text{ for every }d\}.
\]
The notation \(\partial^C_\eta W(\eta,r)\) denotes the subdifferential of \(W(\cdot,r)\), and \(\partial^C_rW(\eta,r)\) denotes that of \(W(\eta,\cdot)\).

Let \(U\sim P\) be an \(\mathbb R^m\)-valued random vector such that \(g_\eta(U)\) is measurable. For fixed \(\tau\in(0,1)\), define
\[
F_\eta(t)=P(g_\eta(U)\le t),\qquad t\in\mathbb R,
\qquad
r_P(\eta)=\inf\{r>0:F_\eta(r)\ge\tau\}.
\]
For the profiled conclusion, consider points \(\eta\) at which \(0<r_P(\eta)<\infty\), the map \((\eta',t)\mapsto F_{\eta'}(t)\) is \(C^1\) on an open neighborhood of \((\eta,r_P(\eta))\), and
\[
f_\eta(r_P(\eta)):=\partial_tF_\eta(t)\big|_{t=r_P(\eta)}>0.
\]
Assume \(r_P\) is \(C^1\) near each such point, and \(W\) is finite and differentiable at \((\eta,r_P(\eta))\). Write \(L_P(\eta)=W(\eta,r_P(\eta))\) wherever this expression is defined.

## Task

Prove the following integrated theorem. For every \((\eta,r)\in\Theta\times(0,\infty)\) with finite \(W(\eta,r)\), the two sections used below are locally Lipschitz, and every optimal dual multiplier \(\lambda^*\) at that pair satisfies
\[
\sum_{j=1}^N\lambda_j^*\nabla_\eta\sigma_{C_{\eta,r}}(w_j)\in\partial^C_\eta W(\eta,r),
\qquad
\sum_{j=1}^N\lambda_j^*\sigma_{C_{\eta,1}}(w_j)\in\partial^C_rW(\eta,r).
\]
Moreover, at every profiled point satisfying the stated assumptions, for any optimal dual multiplier \(\lambda^*\) at \((\eta,r_P(\eta))\),
\[
\nabla_\eta L_P(\eta)=
\left.\sum_{j=1}^N\lambda_j^*\nabla_\eta\sigma_{C_{\eta,r}}(w_j)\right|_{r=r_P(\eta)}
+\left(\sum_{j=1}^N\lambda_j^*\sigma_{C_{\eta,1}}(w_j)\right)\nabla_\eta r_P(\eta),
\]
where
\[
\nabla_\eta r_P(\eta)=-\frac{\left.\nabla_\eta F_\eta(t)\right|_{t=r_P(\eta)}}{f_\eta(r_P(\eta))}.
\]
Here the derivatives of the support function and the CDF are partial derivatives with their scalar arguments held fixed, followed by the indicated evaluation. Thus the oracle gradient contains both direct shape and induced-radius effects.
