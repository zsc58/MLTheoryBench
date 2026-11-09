# Reference Proof

## Proof Structure and Closure

1. Check the loss and its integrability. The nearest-center partition reduction is supporting context, not an additional required public conclusion.
2. Derive the empirical transport-budget dual explicitly and justify restricting its infimum to gamma greater than one, including the boundary case.
3. State and check the applicable standard minimax result, evaluate the quadratic supremum, and establish the correct saddle-point assertion.
4. Differentiate only the unconstrained center coordinates and the interior robustness parameter, treating empty clusters and zero residuals correctly.

All theorem-critical obligations below are closed. The source's nonstandard Wasserstein-duality citation is retained as provenance, but its required empirical specialization is derived rather than assumed. The only named minimax result used is the standard independent result stated in Step 3.

## Step 1: Loss, Integrability, and Partition Context

Fix M and write
\[
f(x)=\min_{1\le k\le K}\|x-\mu_k\|^2.
\]
This function is continuous, nonnegative, and bounded above by \(2\|x\|^2+2\|\mu_1\|^2\). Hence it is integrable under every measure in \(\mathcal P_2\). The partition loss is also integrable, since it is bounded by \(2\|x\|^2+2\max_k\|\mu_k\|^2\).

For context, every partition loss is pointwise at least f. Assigning each point to a nearest center, resolving ties by the smallest index, gives a measurable partition attaining equality. This applies even with repeated centers, in which case some cells may be empty. It explains the reduced robust objective, which the public task already defines directly.

## Step 2: Empirical Transport Dual and Its Parameter Domain

### Explicit duality derivation

For \(t\ge0\), consider tuples \(q=(q_1,\ldots,q_N)\) of probability measures in \(\mathcal P_2(\mathbb R^d)\). Define
\[
c(q)=\frac1N\sum_n\int\|z-x_n\|^2\,dq_n(z),
\qquad
b(q)=\frac1N\sum_n\int f(z)\,dq_n(z),
\]
and
\[
V(t)=\sup\{b(q):c(q)\le t\}.
\]
The choice \(q_n=\delta_{x_n}\) is feasible. If
\[
A=\frac1N\sum_n\|x_n-\mu_1\|^2,
\]
then \(f(z)\le2\|z-x_n\|^2+2\|x_n-\mu_1\|^2\), so
\[
0\le V(t)\le2t+2A<\infty.
\]
Componentwise mixtures of feasible tuples show that V is concave: mix arbitrarily near-optimal tuples at two budgets and then let the approximation errors tend to zero. It is also nondecreasing.

We give the supporting-line argument explicitly. Fix \(t>0\). Concavity implies, whenever \(0\le s<t<u\),
\[
\frac{V(t)-V(s)}{t-s}\ge\frac{V(u)-V(t)}{u-t}.
\]
Consequently
\[
a=\sup_{u>t}\frac{V(u)-V(t)}{u-t}
\]
is nonnegative and finite, since every slope in this supremum is bounded above by the finite slope from \(t/2\) to t. The same inequality and the definition of a give
\[
V(s)\le V(t)+a(s-t)\qquad(s\ge0).
\]
In particular, \(V(t+\varepsilon)\to V(t)\) as \(\varepsilon\downarrow0\).

We next identify \(V(r^2)\) with \(\operatorname{WC}(M)\). A tuple q induces the coupling
\[
\frac1N\sum_n\delta_{x_n}\otimes q_n
\]
between \(\widehat P_N\) and \(P=N^{-1}\sum_nq_n\), with cost c(q). Thus \(V(r^2)\le\operatorname{WC}(M)\).

Conversely, let \(P\in\mathcal B_r(\widehat P_N)\). For every \(\varepsilon>0\), the definition of Wasserstein distance supplies a coupling of \(\widehat P_N\) and P with cost at most \(r^2+\varepsilon\). Conditioning on the finitely many atoms of the empirical marginal gives measures q_n with \(N^{-1}\sum_nq_n=P\), the same reward, and that cost. If an empirical atom is repeated, use its conditional law for each copy of that atom. Each q_n has finite second moment because P does and every empirical atom has positive mass. Therefore
\[
\mathbb E_Pf\le V(r^2+\varepsilon).
\]
Right continuity at the positive budget \(r^2\) gives \(\operatorname{WC}(M)\le V(r^2)\), proving equality without assuming attainment of an optimal transport coupling or a worst-case distribution.

Set \(t=r^2\) and choose its supporting slope a. For every tuple q,
\[
b(q)-a c(q)\le V(t)-at.
\]
Conversely, tuples with \(c(q)\le t\) and \(b(q)\to V(t)\) show
\[
\sup_q[b(q)-a c(q)]=V(t)-at.
\]
For any \(\gamma\ge0\), weak duality gives
\[
V(t)\le\gamma t+\sup_q[b(q)-\gamma c(q)].
\]
The equality at a therefore proves
\[
V(t)=\inf_{\gamma\ge0}\left\{\gamma t+\sup_q[b(q)-\gamma c(q)]\right\}.
\]
The supremum over q separates over the N coordinates. For each coordinate its value is the supremum of the integrand over z: every integral is at most that supremum, and Dirac measures approximate it, including when the supremum is infinite. Thus
\[
\operatorname{WC}(M)=\inf_{\gamma\ge0}\left\{\gamma r^2+\frac1N\sum_n\sup_x[f(x)-\gamma\|x-x_n\|^2]\right\}.
\]
This closes the required instance of the source's nonstandard external dependency.

### Restricting to gamma greater than one

Temporarily define e_n by the inner supremum also for \(0\le\gamma\le1\). Along any fixed unit direction, \(f(tv)=t^2+O(t)\). Hence for \(\gamma<1\) the inner expression has leading term \((1-\gamma)t^2\), and \(e_n(\gamma,M)=+\infty\).

For \(\gamma>1\), the inner expression is continuous and bounded above by \(\|x-\mu_1\|^2-\gamma\|x-x_n\|^2\), which tends to minus infinity as \(\|x\|\to\infty\). Thus its supremum is finite and attained.

As \(\gamma\downarrow1\), the functions \(f(x)-\gamma\|x-x_n\|^2\) increase pointwise to their value at one. Consequently
\[
\lim_{\gamma\downarrow1}e_n(\gamma,M)=e_n(1,M)
\]
in the extended-real sense: the limit is at most the right-hand side, whereas testing any fixed x gives the opposite inequality after taking its supremum. No exchange of a limit with a minimizing assignment is assumed here.

For completeness, \(e_n(1,M)\) is finite exactly when \(x_n\) belongs to the convex hull H of the centers. If \(M\pi=x_n\), averaging the squared distances with pi bounds the inner expression above by \(\sum_k\pi_k\|\mu_k\|^2-\|x_n\|^2\). If \(x_n\notin H\), let z be a closest point in the compact convex set H and put \(v=x_n-z\ne0\). Minimizing squared distance along segments in H gives \(v^\top(\mu_k-z)\le0\). Therefore \(v^\top(x_n-\mu_k)\ge\|v\|^2\) for every k. Substituting \(x=sv\) in
\[
f(x)-\|x-x_n\|^2=\min_k\{2x^\top(x_n-\mu_k)+\|\mu_k\|^2-\|x_n\|^2\}
\]
and letting s tend to infinity proves divergence.

Writing \(D(\gamma)=\gamma r^2+N^{-1}\sum_ne_n(\gamma,M)\), the finite number of summands and the established limits give \(D(1)=\lim_{\gamma\downarrow1}D(\gamma)\). Therefore including or excluding one does not change the infimum, while all parameters below one have infinite value. This proves the first public identity. It does not assert that the infimum is always attained in \((1,\infty)\).

## Step 3: Simplex Formula and Correct Saddle Assertion

The standard independent minimax result used here is the following continuous convex-concave form: if A is a nonempty compact convex subset of a finite-dimensional vector space, B is a nonempty convex set, and a real-valued continuous function F(b,a) is convex in a and concave in b, then
\[
\min_{a\in A}\sup_{b\in B}F(b,a)=\sup_{b\in B}\min_{a\in A}F(b,a).
\]
Attainment of the supremum on the noncompact set B must be verified separately.

Fix n and \(\gamma>1\). Because the simplex is closed and contains its vertices,
\[
\min_k\|x-\mu_k\|^2=\min_{\pi\in\Delta_K}\sum_k\pi_k\|x-\mu_k\|^2.
\]
Set
\[
F_n(x,\pi)=\sum_k\pi_k\|x-\mu_k\|^2-\gamma\|x-x_n\|^2.
\]
It is continuous, affine in pi, and strictly concave in x with Hessian \(-2(\gamma-1)I\). The simplex is nonempty, compact, and convex, and \(\mathbb R^d\) is convex. The stated minimax theorem therefore gives
\[
e_n(\gamma,M)=\min_{\pi\in\Delta_K}\sup_x F_n(x,\pi).
\]
For \(y=x-x_n\), completion of the square starts from
\[
F_n(x,\pi)=\sum_k\pi_k\|x_n-\mu_k\|^2+2y^\top(x_n-M\pi)-(\gamma-1)\|y\|^2.
\]
Its unique maximizer is
\[
x(\pi)=x_n+\frac{x_n-M\pi}{\gamma-1},
\]
and its maximum is
\[
H_n(\pi)=\sum_k\pi_k\|x_n-\mu_k\|^2+\frac{\|x_n-M\pi\|^2}{\gamma-1}.
\]
This continuous function attains its minimum on the closed simplex, proving the second public identity, including attainment.

The precise saddle assertion is as follows. Let pi* minimize H_n, and let \(\bar x\) maximize \(\min_\pi F_n(x,\pi)\); existence of the latter was established by the coercive upper bound in Step 2. Equality of the minimax values gives
\[
e_n\le F_n(\bar x,\pi^*)\le H_n(\pi^*)=e_n.
\]
It follows that \(\bar x=x(\pi^*)\), and
\[
F_n(x,\pi^*)\le F_n(\bar x,\pi^*)\le F_n(\bar x,\pi)
\]
for all x and pi. In particular, pi* minimizes the assignment loss at \(\bar x\). The converse assertion that any assignment minimizing the loss at \(\bar x\) is a saddle assignment is not valid without the maximizing condition in x; it is not used.

To complete the source's endpoint calculation privately, suppose \(x_n\in H\). Put
\[
a_n(\pi)=\sum_k\pi_k\|x_n-\mu_k\|^2,
\qquad
b_n(\pi)=\|x_n-M\pi\|^2,
\qquad
c_n=\min_{\pi\in\Delta_K:\,b_n(\pi)=0}a_n(\pi).
\]
The last minimum exists by compactness. For a minimizer \(\pi_\gamma\) of H_n,
\[
a_n(\pi_\gamma)+\frac{b_n(\pi_\gamma)}{\gamma-1}\le c_n,
\qquad
b_n(\pi_\gamma)\le(\gamma-1)c_n.
\]
Every accumulation point as \(\gamma\downarrow1\) therefore has b_n equal to zero. Continuity and nonnegativity of the penalty give \(\liminf_{\gamma\downarrow1}e_n(\gamma,M)\ge c_n\), while evaluating at a minimizing feasible barycentric representation gives the reverse bound. Together with Step 2, this proves \(e_n(1,M)=c_n\). An arbitrary barycentric representation need not give this limiting value.

## Step 4: Necessary Conditions

Let \((M^*,\Pi^*,\gamma^*)\) satisfy the public assumptions. The centers are unconstrained, and \(\gamma^*>1\) is interior in its one-dimensional domain. Hence partial derivatives in those coordinates vanish while the other coordinates are held fixed. No positivity assumption on the assignment coordinates and no differentiability of an assignment-selection map are needed.

For each k,
\[
0=\nabla_{\mu_k}J(M^*,\Pi^*,\gamma^*)
=\frac2N\sum_n\pi_{kn}^*\left[(\mu_k^*-x_n)+\frac{M^*\pi_n^*-x_n}{\gamma^*-1}\right]
=\frac2N\sum_n\pi_{kn}^*(\mu_k^*-x_n^*).
\]
When \(s_k^*=\sum_n\pi_{kn}^*>0\), division by s_k* gives the stated weighted centroid. When s_k* is zero, nonnegativity implies every weight for that cluster is zero, so the gradient identity is vacuous and no division is made.

The derivative with respect to gamma is
\[
0=\partial_\gamma J(M^*,\Pi^*,\gamma^*)
=r^2-\frac{1}{N(\gamma^*-1)^2}\sum_n\|x_n-M^*\pi_n^*\|^2.
\]
Since \(r>0\) and \(\gamma^*-1>0\), the residual sum is strictly positive at any such local minimizer. Taking the positive square root yields
\[
\gamma^*=1+\frac1r\sqrt{\frac1N\sum_n\|x_n-M^*\pi_n^*\|^2}.
\]
If the residual sum is zero at a feasible triple, its gamma derivative equals \(r^2>0\), so that triple cannot satisfy the assumed interior local minimality. No false existence claim is made in this degenerate case.

### Private clarification of shifted distributions

At an arbitrary fixed gamma greater than one, the shifted points supplied by Step 3 maximize penalized inner problems; their empirical measure need not be feasible or optimal for the specified Wasserstein ball. If their labeled mean transport cost equals \(r^2\), however, the measure \(P^*=N^{-1}\sum_n\delta_{x_n^*}\) is feasible. The saddle identities then give
\[
\mathbb E_{P^*}f=\gamma r^2+\frac1N\sum_ne_n(\gamma,M)=D(\gamma).
\]
Weak duality proves it attains the worst-case risk. At the local minimizer in Step 4, the gamma stationarity equation gives exactly this labeled cost equality. This clarification repairs the source-map reconstruction; it is not an additional public target or scoring requirement.
