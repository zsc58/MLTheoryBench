# Reference Proof

## Theorem-critical obligations

1. Establish support scaling and attained strong duality under the stated convex assumptions, allowing an extended-real objective.
2. Derive a uniform local multiplier bound and local Lipschitz continuity of the value.
3. Obtain both partial Clarke inclusions for every active multiplier, and identify its derivatives with ordinary derivatives when the value is differentiable.
4. Establish the quantile identity and differentiate it.
5. Apply the chain rule with the multiplier evaluated at the profiled pair.

All five obligations are closed below.

## 1. Scaling and strong duality

From the definition of support functions and the equality \(C_{\eta,r}=rC_{\eta,1}\),
\[
\sigma_{C_{\eta,r}}(w)=\sup_{v\in C_{\eta,1}}\langle w,rv\rangle=r\sigma_{C_{\eta,1}}(w).
\]
Set \(z=(\eta,r)\) and \(s_j(z)=\sigma_{C_{\eta,r}}(w_j)\). These functions are jointly \(C^1\), since \(s_j(\eta,r)=r\sigma_{C_{\eta,1}}(w_j)\).

Fix \(z\) with finite value \(v=W(z)\), and put \(G_j(x)=a_j(x)+s_j(z)-b_j\). The Lagrange dual function is
\[
q(\lambda;z)=\inf_{x\in X}\left[f(x)+\sum_j\lambda_jG_j(x)\right],\qquad \lambda\ge0.
\]
Weak duality gives \(q(\lambda;z)\le v\).

For completeness, strong duality follows from finite-dimensional separation even though \(f\) may take the value \(+\infty\). The elementary separation fact used here is: a point outside a nonempty open convex subset of a finite-dimensional Euclidean space can be separated from that set by a nonzero linear functional, with the functional on the set at least its value at the point.

Apply this fact to
\[
A=\{(y,t):\text{there is }x\in X\text{ with }f(x)<\infty,\ G_j(x)<y_j\ (1\le j\le N),\ f(x)<t\}.
\]
This set is open, nonempty, and convex. Convexity follows by taking convex combinations of its witnessing decision points and using convexity of \(f\) and all \(a_j\). The point \((0,v)\) is not in \(A\), since membership would exhibit a feasible point of objective strictly below \(v\). Thus there is a nonzero pair \((\alpha,\beta)\) such that
\[
\alpha\cdot y+\beta t\ge\beta v\qquad((y,t)\in A).
\]
Since \(A\) is upward closed in every coordinate, \(\alpha\ge0\) and \(\beta\ge0\). If \(\beta=0\), then \(\alpha\ne0\). A strictly feasible point \(\bar x\) permits a componentwise negative vector \(y\) with \(G(\bar x)<y<0\), contradicting \(\alpha\cdot y\ge0\). Hence \(\beta>0\).

For \(\lambda=\alpha/\beta\), taking \(y\downarrow G(x)\) and \(t\downarrow f(x)\) gives
\[
f(x)+\lambda\cdot G(x)\ge v
\]
for every finite-objective \(x\in X\). For infinite-objective points this inequality holds automatically. Therefore \(q(\lambda;z)\ge v\); weak duality gives equality. Consequently
\[
W(z)=\max_{\lambda\ge0}q(\lambda;z).
\]
No primal attainment or additional lower-semicontinuity assumption has been used.

## 2. Uniform multiplier bound and local Lipschitz continuity

Fix a finite-value point \(z_0\). Choose the stated Slater point \(\bar x\), and define
\[
\delta=\min_j\{b_j-a_j(\bar x)-s_j(z_0)\}>0,
\qquad \ell=\inf_{x\in X}f(x)>-\infty.
\]
Because \(f(\bar x)<\infty\), \(\ell\) is a finite real number. Continuity of the finitely many support terms supplies a neighborhood \(B\) of \(z_0\) on which \(\bar x\) has every slack at least \(\delta/2\). Shrink \(B\) to a convex neighborhood contained in \(\Theta\times(0,\infty)\). Every point in \(B\) has finite value, since
\[
\ell\le W(z)\le f(\bar x).
\]
For \(\lambda\ge0\), evaluation at \(\bar x\) yields
\[
q(\lambda;z)\le f(\bar x)-\frac{\delta}{2}\|\lambda\|_1.
\]
If \(\lambda_z\) is optimal at \(z\), then \(q(\lambda_z;z)=W(z)\ge\ell\), so
\[
\|\lambda_z\|_1\le M:=\frac{2(f(\bar x)-\ell)}{\delta}
\qquad(z\in B).
\]
This argument also covers \(M=0\).

Write
\[
c(\lambda)=\inf_{x\in X}\left[f(x)+\sum_j\lambda_j(a_j(x)-b_j)\right],
\qquad q(\lambda;z)=c(\lambda)+\sum_j\lambda_js_j(z).
\]
An active multiplier has finite \(c(\lambda)\), because its dual value is finite. Other multipliers can have \(c(\lambda)=-\infty\); such sections are never differentiated.

The \(C^1\) support terms have a common finite Lipschitz constant \(K\) after shrinking \(B\). For \(z,z'\in B\), choose an optimizer \(\lambda_z\). Weak duality at \(z'\) gives
\[
W(z)-W(z')\le q(\lambda_z;z)-q(\lambda_z;z')
=\sum_j(\lambda_z)_j\bigl(s_j(z)-s_j(z')\bigr)
\le MK\|z-z'\|.
\]
Interchanging the points proves local Lipschitz continuity of \(W\), hence also of both coordinate sections.

## 3. Sensitivities from any active multiplier

Fix any optimal multiplier \(\lambda^*\) at \(z_0\). The real-valued function \(\phi(z)=q(\lambda^*;z)\) is \(C^1\), satisfies \(\phi(z)\le W(z)\), and touches \(W\) at \(z_0\).

Here is the required elementary Clarke-envelope argument. If a locally Lipschitz function \(h\) has a \(C^1\) lower support \(\psi\) touching at \(x\), then for every direction \(d\),
\[
h^\circ(x;d)\ge\limsup_{t\downarrow0}\frac{h(x+td)-h(x)}{t}
\ge\nabla\psi(x)\cdot d.
\]
The defining inequalities for the Clarke subdifferential therefore give \(\nabla\psi(x)\in\partial^C h(x)\). Apply this argument directly to each fixed-coordinate section of \(W\) and \(\phi\). Since
\[
\nabla_\eta\phi(\eta,r)=\sum_j\lambda_j^*\nabla_\eta\sigma_{C_{\eta,r}}(w_j),
\qquad
\partial_r\phi(\eta,r)=\sum_j\lambda_j^*\sigma_{C_{\eta,1}}(w_j),
\]
both claimed partial Clarke inclusions follow. This avoids confusing the partial Clarke subdifferentials with projections of a joint subdifferential.

If \(W\) is differentiable at \(z_0\), the differentiable function \(W-\phi\) has a local minimum there. Thus \(\nabla W(z_0)=\nabla\phi(z_0)\). This holds for every optimal multiplier, with no uniqueness assumption. In particular, the ordinary partial derivatives at a differentiable point equal the displayed multiplier expressions. Ordinary differentiability alone is not used to assert that an arbitrary locally Lipschitz function has a singleton Clarke subdifferential.

## 4. Quantile identity and derivative

The gauge is finite on \(\mathbb R^m\): the unit set contains a ball about the origin. Hence \(g_\eta(U)\) is finite almost surely and \(F_\eta(r)\to1\) as \(r\to\infty\). Because \(\tau<1\), the set defining \(r_P(\eta)\) is nonempty.

At a profiled point under consideration, put \(r_0=r_P(\eta)>0\). There are feasible radii converging to this infimum. Continuity at \(r_0\) therefore gives \(F_\eta(r_0)\ge\tau\). If the inequality were strict, continuity and \(r_0>0\) would give a smaller positive feasible radius. Thus
\[
F_\eta(r_P(\eta))=\tau.
\]
The identity also holds for nearby shapes: choose positive radii on either side of \(r_0\) sufficiently close that their CDF values bracket \(\tau\), using the positive radial derivative. Joint continuity preserves this bracketing nearby, and joint \(C^1\) regularity with positive radial derivative identifies the quantile with the unique local root.

The standard implicit function theorem applies to \(H(\eta,r)=F_\eta(r)-\tau\): it is \(C^1\), vanishes at the point, and has nonzero radial derivative. It gives a local \(C^1\) root and derivative \(-\nabla_\eta H/\partial_rH\). Equivalently, using the publicly assumed \(C^1\) regularity of \(r_P\), differentiate the established identity directly:
\[
\nabla_\eta F_\eta(r_P(\eta))+f_\eta(r_P(\eta))\nabla_\eta r_P(\eta)=0.
\]
The positive denominator gives the required quantile derivative.

## 5. Profiled gradient

At \(z_0=(\eta,r_P(\eta))\), let \(\lambda^*\) be any optimal dual multiplier. The assumed differentiability of \(W\), the \(C^1\) profile, and the ordinary chain rule give
\[
\nabla_\eta L_P(\eta)=\nabla_\eta W(\eta,r_P(\eta))+
\partial_rW(\eta,r_P(\eta))\nabla_\eta r_P(\eta).
\]
Substituting the ordinary derivatives identified in Section 3 yields
\[
\nabla_\eta L_P(\eta)=
\left.\sum_{j=1}^N\lambda_j^*\nabla_\eta\sigma_{C_{\eta,r}}(w_j)\right|_{r=r_P(\eta)}
+\left(\sum_{j=1}^N\lambda_j^*\sigma_{C_{\eta,1}}(w_j)\right)\nabla_\eta r_P(\eta).
\]
The first term is a fixed-radius partial derivative evaluated at the profiled radius, not a derivative of the support function already composed with that radius. Together with Section 4, this proves the integrated theorem.
