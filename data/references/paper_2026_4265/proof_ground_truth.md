# Reference Proof

All directional limits below are taken separately on a feasible side. Fix a parameter \(\theta\), a direction \(r\), and such a side. No assertion about the opposite side is needed.

## Theorem-critical obligations

1. Establish bounded continuous recursively defined values and attainment of the one-step minima; verify the stated rectangular trajectory interpretation.
2. Obtain an integrable bound for policy-density difference quotients from the bounded score.
3. Justify the upgrade from pointwise value-quotient convergence to continuous uniform convergence.
4. Prove the signed envelope formulas over the original, possibly nonunique, worst-case-law set.
5. Close the backward induction by differentiating the policy integral, and then differentiate the fixed initial-law integral.

The proof below closes each obligation. It does not invoke the paper-specific directional-regularity proposition as a black box and does not require dual-quotient stability or optimizer uniqueness.

## Step 001: Continuity, attainment, and trajectory interpretation

Write \(\mathsf P(X)\) for the Borel probability laws on \(X\), and put
\[
H_t^\vartheta(x,a,y)=f(t,x,a,y)+V_{t+1}^\vartheta(y).
\]
On compact \(X\), the Wasserstein and weak topologies on probability laws agree. In particular, the assumed Wasserstein compactness and Hausdorff continuity can be used for continuous bounded integrands.

Let \(M_f=\max_{t<T}\|f(t,\cdot,\cdot,\cdot)\|_\infty\) and \(M_g=\|g\|_\infty\). Direct backward induction gives
\[
\|V_t^\vartheta\|_\infty\le (T-t)M_f+M_g,
\qquad
\|G_t^\vartheta\|_\infty\le (T-t)M_f+M_g,
\]
for all parameters and all applicable times.

We also prove joint continuity in the parameter and state variables by backward induction. The terminal case is immediate. If \(V_{t+1}^\vartheta(y)\) is jointly continuous, compactness makes the integrand uniformly continuous. Consequently
\[
(\vartheta,x,a,P)\longmapsto \int H_t^\vartheta(x,a,y)P(dy)
\]
is continuous: split an integral difference into the uniform change of the integrand and a weak-convergence term with a fixed continuous integrand.

For completeness, continuity of its minimum over \(\mathcal P_t(x,a)\) follows directly from Hausdorff continuity. Along a convergent sequence of parameters and state-action pairs, minimizers have subsequential limits in the limiting feasible set, giving the lower bound on the limiting values. Conversely, a fixed limiting minimizer can be approximated by feasible laws from the varying sets, giving the upper bound. Attainment follows from continuity on a nonempty compact feasible set. Thus \(G_t\) is continuous. Splitting the policy integral in the same fashion, and using weak continuity of the policy kernel, proves joint continuity of \(V_t\).

The worst-case set is the minimum level set of a continuous function on a compact feasible set. It is therefore nonempty and compact.

The standard measurable-minimum result used for the trajectory interpretation is the following: a weakly measurable nonempty compact-valued correspondence into a Polish space, together with an objective measurable in its parameter and continuous in its decision variable, has a measurable minimum and a measurable minimizing selector. This is the measurable maximum/minimum theorem stated in the supplied source, Appendix A. Here the parameter space is \(X\times A\), the decision space is the Polish space \(\mathsf P(X)\), the ambiguity correspondence is Hausdorff-continuous and hence weakly measurable, and the integral objective is continuous. Its hypotheses are therefore satisfied, giving Borel minimizing kernels at each time for a fixed policy parameter.

For any permitted sequence of transition kernels, conditional expectation and backward induction show that its remaining expected reward is at least the recursively defined \(V_t^\vartheta\). Choosing the minimizing kernels at every stage makes each inequality an equality. Rectangularity permits their simultaneous use. Hence the recursion indeed gives the infimum over the admissible trajectory laws. This verifies the interpretation without assuming an interchange theorem for an unspecified class of functions. It is supporting material, not an additional public target.

## Step 002: Policy-quotient domination

Choose \(\delta>0\) so that the whole segment on the selected side is feasible for \(|h|<\delta\). Set \(K=C_\pi\|r\|\), and, for fixed \(t,x,a\), write
\[
p_h=\pi_t^{\theta+hr}(a\mid x),\qquad p_0=\pi_t^\theta(a\mid x).
\]
Positivity and the score bound imply, by the mean value theorem along the feasible segment,
\[
|\log p_h-\log p_0|\le K|h|.
\]
Thus
\[
e^{-K|h|}\le p_h/p_0\le e^{K|h|},\qquad
\left|\frac{p_h-p_0}{h}\right|\le K e^{K\delta}p_0.
\]
Moreover,
\[
\frac{p_h-p_0}{h}\longrightarrow p_0S_t^\theta(x,a;r).
\]
The displayed bound is integrable with respect to the reference measure, since \(\int p_0\,d\nu=1\), and is uniform in \(t,x\). It also covers \(r=0\), when all these quotients vanish. No finiteness assumption on the reference measure is needed.

## Step 003: Equicontinuity and uniform convergence

We use an elementary compactness fact. Suppose a family \(Q_h\) on compact \(X\) is equicontinuous and converges pointwise to \(D\) as \(h\) tends to zero from a specified side. Passing to the limit in the common continuity estimate shows that \(D\) is continuous. To prove uniform convergence, cover \(X\) by finitely many balls on which both \(Q_h\) and \(D\) vary by less than a prescribed tolerance. Pointwise convergence at the finitely many centers then bounds \(\sup_x|Q_h(x)-D(x)|\). Thus convergence is uniform, and the quotients are uniformly bounded for sufficiently small \(|h|\).

This argument establishes uniform convergence only after pointwise convergence has been proved. Equicontinuity alone is not used to assert existence of a directional derivative.

## Step 004: The compact primal envelope

Fix \(t,x,a\). Suppose the downstream quotients converge uniformly on the selected side to a continuous function \(H\). Put
\[
\Phi_h(P)=\int_X[f(t,x,a,y)+V_{t+1}^{\theta+hr}(y)]P(dy),
\quad m_h=\min_{P\in\mathcal P_t(x,a)}\Phi_h(P),
\quad B^*=\operatorname*{argmin}_{P\in\mathcal P_t(x,a)}\Phi_0(P).
\]
There is \(\rho(h)\to0\) such that, uniformly over all feasible \(P\),
\[
|\Phi_h(P)-\Phi_0(P)-h\!\int H\,dP|\le |h|\rho(h).
\]
Also
\[
|m_h-m_0|\le\|V_{t+1}^{\theta+hr}-V_{t+1}^\theta\|_\infty,
\]
so \(m_h\to m_0\), and its directional quotients are bounded.

For \(h>0\), comparison with any \(P^*\in B^*\) gives
\[
\frac{m_h-m_0}{h}\le\int H\,dP^*+\rho(h).
\]
Consequently the upper limit is at most \(\min_{B^*}\int H\,dP\). This minimum is attained because \(H\) is continuous and \(B^*\) is compact.

Choose a minimizing law \(P_h\) for \(\Phi_h\). Since \(\Phi_0(P_h)\ge m_0\),
\[
\frac{m_h-m_0}{h}\ge\int H\,dP_h-\rho(h).
\]
Choose a sequence realizing the lower limit and then a subsequence along which \(P_h\) converges weakly to \(\bar P\). The uniform expansion gives
\[
\Phi_0(P_h)=m_h+O(|h|)\longrightarrow m_0.
\]
Continuity implies \(\Phi_0(\bar P)=m_0\), so \(\bar P\in B^*\). Continuity of \(H\) then gives the reverse lower bound \(\min_{B^*}\int H\,dP\). This proves the right derivative and its minimum formula.

For \(h<0\), the same comparisons, with division by a negative number, give
\[
\frac{m_h-m_0}{h}\ge\int H\,dP^*-\rho(h)
\quad(P^*\in B^*),
\qquad
\frac{m_h-m_0}{h}\le\int H\,dP_h+\rho(h).
\]
The first inequality bounds the lower limit by the maximum over \(B^*\). Taking a sequence realizing the upper limit and using the identical cluster-point argument bounds that upper limit by the same maximum. This proves the left formula. Optimizers need not be unique or vary continuously with the parameter.

For later use, directly from the two minimization problems,
\[
\sup_{x,a}\left|\frac{G_t^{\theta+hr}(x,a)-G_t^\theta(x,a)}h\right|
\le\left\|\frac{V_{t+1}^{\theta+hr}-V_{t+1}^\theta}h\right\|_\infty.
\]
The pointwise derivative of \(G_t\) is Borel measurable as a pointwise limit of continuous quotients. Its continuity in \((x,a)\) is not needed or asserted.

## Step 005: Backward induction and policy differentiation

At \(t=T\), all value quotients are zero, so the desired derivative exists and convergence is uniform to the continuous zero function.

Suppose the value quotients at \(t+1\) converge uniformly to the continuous derivative for the selected side. Step 004 gives the corresponding derivative of \(G_t\) and the required minimum or maximum formula. It also gives a bound on all sufficiently small \(G_t\) quotients, uniform in \((x,a)\), and uniform convergence \(G_t^{\theta+hr}\to G_t^\theta\).

For each \(x\), use the exact decomposition
\[
\frac{V_t^{\theta+hr}(x)-V_t^\theta(x)}h
=\int_A\frac{G_t^{\theta+hr}(x,a)-G_t^\theta(x,a)}h\,p_0\,d\nu
+\int_A G_t^{\theta+hr}(x,a)\frac{p_h-p_0}{h}\,d\nu.
\]
The first integrand is dominated by a constant times \(p_0\), by Step 004. The second is dominated by a constant times \(p_0\), by Step 002 and the uniform reward bound. Dominated convergence therefore proves pointwise existence and
\[
D_r^\sigma V_t^\theta(x)
=\int_A\left[D_r^\sigma G_t^\theta(x,a)+G_t^\theta(x,a)S_t^\theta(x,a;r)\right]\pi_t^\theta(da\mid x).
\]
The assumed equicontinuity of the value quotients, together with Step 003, now makes this derivative continuous in \(x\) and upgrades convergence to uniform convergence. This closes the induction. In particular, no separate equicontinuity assumption for the minimized one-step quotients and no dual stability assumption was used.

Finally, \(\mu_0\) is a fixed probability law. Uniform convergence at time zero gives
\[
\frac{J(\theta+hr)-J(\theta)}h
=\int_X\frac{V_0^{\theta+hr}-V_0^\theta}h\,d\mu_0
\longrightarrow\int_XD_r^\sigma V_0^\theta\,d\mu_0.
\]
All statements have been proved separately for each feasible side. At an interior parameter both sides are feasible for every direction; at a boundary parameter only the corresponding feasible-side conclusions are asserted.
