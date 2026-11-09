# Reference Proof

## Proof Structure

1. Express each probability-limited or increment-limited monotonicity event as a fixed indicator function of a potential-outcome vector, so its probability is a linear form in the joint parameters.
2. Assemble the simplex, experimental and/or observational marginal, optional coordinatewise exogeneity, and monotonicity constraints into the feasible polytope.
3. Use finite-dimensional compactness and continuity to obtain the two extrema, and prove sharpness by realizing every feasible parameter vector as a finite joint distribution.

## Complete Proof

Let \(\mathcal Y=\{1,\ldots,d_Y\}^{d_X}\) and \(\mathcal X=\{1,\ldots,d_X\}\). The coordinates \(p_{y,x}\) are nonnegative and sum to one. For any law with these coordinates,
\[
\Pr(Y_k=j)=\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y:y_k=j}p_{y,x}.
\]
Consistency \(Y=Y_X\) gives
\[
\Pr(X=\ell,Y=m)=\sum_{y\in\mathcal Y:y_\ell=m}p_{y,\ell}.
\]
Thus the available experimental and observational marginal equations are necessary and sufficient to reproduce their respective data collections.

We next verify the optional exogeneity equations. Write
\[
r_{kj}(p)=\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y:y_k=j}p_{y,x},\qquad
s_\ell(p)=\sum_{y\in\mathcal Y}p_{y,\ell},\qquad
h_{kj\ell}(p)=\sum_{y\in\mathcal Y:y_k=j}p_{y,\ell}.
\]
These are respectively \(\Pr(Y_k=j)\), \(\Pr(X=\ell)\), and \(\Pr(Y_k=j,X=\ell)\). On finite state spaces, \(Y_k\) is independent of \(X\) exactly when
\[
h_{kj\ell}(p)=r_{kj}(p)s_\ell(p)
\]
for every \(j,\ell\).

If observational marginals are available, summing their equations over \(m\) gives \(s_\ell(p)=\sum_m b_{\ell m}=q_\ell\). The stated exogeneity equations are consequently exactly \(h_{kj\ell}(p)=q_\ell r_{kj}(p)\). If only experimental marginals are available, their equations give \(r_{kj}(p)=a_{kj}\), so the stated equations are exactly \(h_{kj\ell}(p)=a_{kj}s_\ell(p)\). In either regime these equations are linear and equivalent, subject to the data equations, to the required independence for every \(k\). No division by a treatment probability is used, and independence of the entire potential-outcome vector is not required.

For each \(w\), let
\[
E_w=\bigcap_{s>t}\{D^{(w),-}_{st}\le Y_s-Y_t\le D^{(w),+}_{st}\}.
\]
For every \(y\in\mathcal Y\), the product
\[
I_w(y)=\prod_{s>t}{\bf1}\{D^{(w),-}_{st}\le y_s-y_t\le D^{(w),+}_{st}\}
\]
is one exactly when all of its increment restrictions hold. Consequently \({\bf1}_{E_w}=I_w(Y_{1:d_X})\), and partitioning by the finite states \((Y_{1:d_X},X)=(y,x)\) yields
\[
\Pr(E_w)=\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y}I_w(y)p_{y,x}.
\]
The event-probability assumptions are therefore equivalent to the displayed lower and upper linear inequalities, for every \(w\). The coefficients \(I_w(y)\) are fixed numbers in \(\{0,1\}\). A single-pair restriction is included by choosing intervals covering every possible difference for all other pairs; global nondecreasing restrictions are likewise included by suitable intervals. When \(d_X=1\), the intersection is the entire sample space and the empty product is one, so the same calculation applies.

Let \(F\) denote the set satisfying the simplex, the applicable marginal equations, the optional exogeneity equations, and these event inequalities. The feasibility assumption gives \(F\ne\varnothing\). There are \(d_Xd_Y^{d_X}\) coordinates and finitely many closed affine constraints. Thus \(F\) is a closed subset of the probability simplex and is bounded. The standard finite-dimensional compactness fact states that a closed and bounded subset of \(\mathbb R^n\) is compact. It follows that \(F\) is compact. The standard extreme-value theorem states that a continuous real-valued function on a nonempty compact set attains both its minimum and maximum. Since
\[
\phi(p)=\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y}c_{y,x}p_{y,x}
\]
is a finite linear function with real coefficients, it is continuous. It therefore attains \(\underline\lambda\) and \(\overline\lambda\) on \(F\). These are precisely the optima of the stated linear programs. LP duality and slack-variable transformations are not needed.

Every admissible law induces a vector in \(F\), by the preceding calculations. Its target value therefore belongs to \([\underline\lambda,\overline\lambda]\).

Conversely, for any \(p\in F\), equip \(\mathcal Y\times\mathcal X\) with the probability measure assigning mass \(p_{y,x}\) to \((y,x)\). Define \(Y_k(y,x)=y_k\), \(X(y,x)=x\), and \(Y(y,x)=y_x\). These are measurable finite-valued random variables and satisfy consistency. The marginal calculations reproduce all available data. The event calculation verifies every probability restriction. When imposed, the exogeneity calculation proves \(Y_k\perp X\) for every \(k\). The target of this law is exactly \(\phi(p)\).

This construction also respects the source's unrestricted structural-causal semantics: take an exogenous state \(U=(v,z)\) with law \(p\), use structural equations \(X=z\) and \(Y=v_X\), and intervene by replacing the treatment equation with \(X=k\). The resulting potential outcome is \(v_k\). No additional causal-graph restrictions are part of the selected theorem.

In particular, minimizing and maximizing vectors produce admissible laws attaining both endpoints. The bounds are therefore sharp. The argument includes zero marginal cells, zero treatment probabilities, constant objectives, singleton feasible sets, and \(d_Y=1\); no strict positivity or full-dimensionality is needed.

## Proof-Obligation Audit

All theorem-critical obligations are closed: marginal equivalence, optional coordinatewise exogeneity equivalence, event-probability equivalence, nonempty compact feasibility, objective attainment, and both directions of the law/parameter correspondence. The only standard independent results used are the compactness and extreme-value statements given above, with their hypotheses verified. There are no unresolved private proof obligations.
