# Reference Proof

## Proof Structure

1. Handle an empty safe set and a zero-row safe-set representation directly.
2. Characterize the exact learned-QP optimizer by its affine-constraint KKT system, using the attained optimizer and positive definiteness of the objective.
3. Rewrite componentwise invariance as a worst-row violation problem using the probability simplex, and identify the QCQP value with the negative supremum of violations.
4. Conclude safety from a nonnegative QCQP value, and then from a nonnegative certified SOS/SDP lower bound.

## Complete Proof

All optimal values below use the extended-real infimum convention in the public task.

If $X_0=\varnothing$, persistent safety is vacuous. The QCQP is infeasible because it requires $x_0\in X_0$, so $z^*=+\infty$ is consistent with this conclusion. If $r=0$, the inequality $Gx\le c$ has no components and $X_0=\mathbb R^n$. Every next state belongs to $X_0$, so persistent safety holds automatically. In this case $v\in\mathbb R^0$ cannot satisfy $\mathbf1^\top v=1$, and the QCQP again has value $+\infty$. Thus both requested implications hold in these cases. Assume henceforth that $X_0$ is nonempty and $r\ge1$.

### The learned-QP optimizer and KKT conditions

Fix a state $x_0$ and a reference $\hat u$, and set
\[
f(y)=\frac12y^\top Py-(E^\top\hat u)^\top y,
\qquad h(y)=Hy+Wx_0+b.
\]
The task assumes that the QP is feasible and its optimum is attained. Its feasible set is a nonempty polyhedron. Since $P\succ0$, $f$ is differentiable and strictly convex, and the attained optimizer $y^*$ is unique.

The standard affine-constraint KKT result used here is the following: for a differentiable convex function $f$ and a nonempty polyhedron $C=\{y:Hy+d\ge0\}$, a feasible point $y^*$ minimizes $f$ on $C$ if and only if there exists $\mu\ge0$ such that
\[
\nabla f(y^*)-H^\top\mu=0,
\qquad \mu^\top(Hy^*+d)=0.
\]
For affine constraints this result does not require a strictly feasible point. Its hypotheses hold here with $d=Wx_0+b$ and $\nabla f(y)=Py-E^\top\hat u$. Therefore the optimizer has a multiplier satisfying
\[
Py^*-E^\top\hat u-H^\top\mu=0,
\qquad h(y^*)\ge0,
\qquad \mu\ge0,
\qquad \mu^\top h(y^*)=0.
\]
This remains valid when $s=0$: the multiplier and constraint vectors are empty, and stationarity is the unconstrained optimality condition.

For completeness, KKT sufficiency and uniqueness can also be checked directly. Suppose $(y,\mu)$ satisfies the displayed conditions and let $\widetilde y$ be any feasible point. Expanding the quadratic gives
\[
f(\widetilde y)-f(y)
=\nabla f(y)^\top(\widetilde y-y)
+\frac12(\widetilde y-y)^\top P(\widetilde y-y).
\]
Stationarity and complementarity imply
\[
\nabla f(y)^\top(\widetilde y-y)
=\mu^\top H(\widetilde y-y)
=\mu^\top h(\widetilde y)-\mu^\top h(y)
=\mu^\top h(\widetilde y)\ge0.
\]
The quadratic term is nonnegative and is strictly positive when $\widetilde y\ne y$. Thus $y$ is the unique optimizer. In particular, every KKT-feasible tuple has $Ey=\pi(x_0,\hat u)$, and every state/reference optimizer can be extended to such a tuple.

### Worst-row violations and the QCQP value

For a safe state and any reference define
\[
\rho(x_0,\hat u)=G(Ax_0+B\pi(x_0,\hat u))-c\in\mathbb R^r.
\]
Persistent safety means $\rho(x_0,\hat u)\le0$ componentwise for every $x_0\in X_0$ and every $\hat u\in\mathbb R^m$.

Let $\Delta_r=\{v\in\mathbb R^r:v\ge0,\mathbf1^\top v=1\}$. For any $a\in\mathbb R^r$,
\[
\max_{v\in\Delta_r}v^\top a=\max_{1\le i\le r}a_i.
\]
Indeed, a convex combination of the components is at most their maximum, and a unit vector corresponding to a maximizing component achieves that maximum. No additional LP duality hypothesis is needed.

By the KKT characterization above, the possible QCQP objective values are precisely
\[
-v^\top\rho(x_0,\hat u),
\qquad x_0\in X_0,\quad \hat u\in\mathbb R^m,\quad v\in\Delta_r.
\]
Both directions hold: every QCQP-feasible $y$ is the optimizer for its state and reference, and every such optimizer has multipliers making it QCQP-feasible for any chosen $v\in\Delta_r$. Consequently,
\[
z^*
=\inf_{x_0\in X_0,\,\hat u\in\mathbb R^m,\,v\in\Delta_r}
\bigl[-v^\top\rho(x_0,\hat u)\bigr]
=-\sup_{x_0\in X_0,\,\hat u\in\mathbb R^m}
\max_{1\le i\le r}\rho_i(x_0,\hat u).
\]
The equality uses extended-real optimal values and does not require a maximizing state/reference or a minimizing QCQP tuple.

If $z^*\ge0$, every feasible tuple has objective at least $z^*$ and hence at least zero. Fix any safe state, any reference, and any row $i$. Extend their optimizer to a KKT tuple and choose $v=e_i$. Its objective is $-\rho_i(x_0,\hat u)$, so $\rho_i(x_0,\hat u)\le0$. Since the state, reference, and row were arbitrary,
\[
G(Ax_0+B\pi(x_0,\hat u))\le c
\]
for every safe state and every reference. This is persistent safety. An unbounded-below QCQP has $z^*=-\infty$ and does not satisfy the certificate premise.

### Certified relaxation bound

By definition, the certified relaxation bound satisfies $z_{\mathrm{SDP}}\le z^*$. Therefore $z_{\mathrm{SDP}}\ge0$ implies $z^*\ge0$, and the preceding argument proves persistent safety. The task requires only this certified lower-bound property, not construction, attainment, tightness, or convergence of a relaxation hierarchy.
