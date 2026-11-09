# Reference Proof

## Proof Structure and Audit Notes

Identify the union-DAG sources from their variance-one characterization. Recursively condition identified sources to zero and then recover the coefficients and variance parameters from conditional means and variances. Next establish population identification, uniform convergence, and consistency. Analyze the true-support restricted estimator, control only those inactive coordinates whose addition preserves acyclicity, and use feasibility to eliminate the others. Finally compare objectives using local strong convexity.

The loss formula is a genuine negative log-likelihood on the DAG-feasible set. Its ambient extension is useful for differentiation and Taylor expansion, but its gradient need not have mean zero in cycle-creating directions. The source's overbroad sentence asserting mean-zero contributions for every gradient coordinate is repaired by centering the ambient empirical gradient at its population gradient and using feasible-direction optimality where needed.

The public normalization is half the source's displayed loss. Correspondingly halving the source penalty sequences makes the objectives proportional. This does not change the estimator or any stated assumption.

## 1. Finite moments and distributional identifiability

Write \(W=A_0+Z\) for one cluster. In a topological order of the true union DAG, \(W^p=0\), so the structural equations imply
\[
Y=E(I-W)^{-1}=E\sum_{q=0}^{p-1}W^q.
\]
Every observation is therefore a finite polynomial in finitely many Gaussian noises and random effects. All its moments are finite. Conditional on \(Z\), each observation row has mean zero and a positive definite Gaussian covariance, since \(I-W\) is invertible. Consequently the unconditional row covariance and every parent covariance are positive definite.

Consider one observation row \(y\). If \(k\) is a source of the union DAG, then \(y_k=e_k\) and \(\operatorname{Var}(y_k)=1\). Otherwise let \(P_k\) be its union-parent set and \(c_k=(A_{0,jk}+Z_{jk})_{j\in P_k}\). The vector \(c_k\) is independent of \(y_{P_k}\), and \(e_k\) is independent of both. Since all variables have mean zero,
\[
\operatorname{Var}(y_k)=1+\mathbb E[(y_{P_k}^{\mathsf T}c_k)^2].
\]
Let \(\Sigma_{P_k}=\mathbb E[y_{P_k}y_{P_k}^{\mathsf T}]\succ0\). At least one component of \(c_k\) has a nonzero fixed coefficient or positive variance, so \(\mathbb E\|c_k\|_2^2>0\). Thus
\[
\mathbb E[c_k^{\mathsf T}\Sigma_{P_k}c_k]
\ge\lambda_{\min}(\Sigma_{P_k})\mathbb E\|c_k\|_2^2>0.
\]
The source set is therefore exactly the set of coordinates with variance one.

For any topological order, integrating the independent incoming random effects gives the sequential row conditionals
\[
y_k\mid(y_j)_{j<k}\sim N\left(\sum_{j<k}A_{0,jk}y_j,
1+\sum_{j<k}R_{0,jk}y_j^2\right).
\]
Their product is a continuous strictly positive joint density. The same holds for every initial segment of this order.

Choose an identified source using a fixed tie-breaking rule and relabel it first. Its value is its noise and is independent of all remaining primitive noises and random effects. Conditional on that source being zero, its outgoing terms vanish, leaving a mixed-effects SEM on the remaining vertices with the same remaining parameters and independent primitive variables. This conditional law has a continuous version determined by the observed density; it is not an arbitrary choice of a conditional distribution on a null event. Repeating the source characterization in these reduced conditional laws determines a common topological order for any two parameter pairs producing the same observed distribution.

In that order, equality of the observed laws gives equality almost everywhere of the displayed conditional means and variances. Predecessor densities are strictly positive, and the mean and variance functions are continuous, so equality holds everywhere. Equality of the linear mean polynomials identifies each \(A_{0,jk}\); equality of the quadratic variance polynomials identifies each \(R_{0,jk}\). All coordinates inconsistent with the order are zero. This proves identification of the parameter pair and both component graphs and their union. A row marginal suffices, so the argument covers every fixed \(n\ge1\).

## 2. Population identification and uniform convergence

For a feasible candidate, choose a topological order of its union graph. Conditional on all preceding node columns, the incoming random effects for node \(k\) are independent of those columns. Integrating them gives the Gaussian conditional covariance \(V_k(r_k)\) and mean \(Ya_k\). The product of these sequential conditional densities is a normalized cluster density \(p_{A,R}\). Hence
\[
Q(A,R)-Q(A_0,R_0)
=\mathbb E_0\log\frac{p_{A_0,R_0}(Y)}{p_{A,R}(Y)}
=D_{\mathrm{KL}}(p_{A_0,R_0}\Vert p_{A,R})\ge0.
\]
The finite-moment bounds below ensure finiteness. Equality holds exactly when the cluster laws agree, which by Section 1 identifies the parameter pair. Thus \(Q\) has a unique minimum at the truth on \(\mathcal A\).

The feasible set is compact: it is the finite union over topological orders of closed bounded sets defined by setting forbidden coordinates to zero and imposing the box and nonnegativity constraints. Both full and true-support restricted objectives attain their minima.

Here is a direct justification of the uniform convergence used below. Let \(g(Y,\theta)\) be one cluster's contribution to \(Q_m\). On a fixed bounded convex box in the ambient zero-diagonal parameter space with \(R\ge0\),
\[
V_k\succeq I_n,\qquad \|V_k^{-1}\|_{\mathrm{op}}\le1,
\qquad 0\le\log\det V_k\le\operatorname{tr}(V_k-I_n).
\]
The residual \(Y_k-Ya_k\) is bounded by a constant times \(\|Y\|_F\). Differentiating an inverse uses
\(d(V^{-1})=-V^{-1}(dV)V^{-1}\), and a variance-coordinate derivative of \(V\) is \(Y_jY_j^{\mathsf T}\). These facts bound the loss and all its parameter derivatives through order three by
\[
C(1+\|Y\|_F^8)
\]
for a finite constant depending on the box, \(n\), and \(p\). The bound has finite moments of every finite order by Section 1. It also gives integrable Lipschitz envelopes for the loss and each Hessian entry on that box. One-sided derivatives are used at the nonnegative boundary.

For completeness, take a finite \(\delta\)-net of any compact parameter set \(K\) in the box. For the loss or one Hessian entry \(f\), with Lipschitz envelope \(L(Y)\),
\[
\sup_{\theta\in K}|(P_m-P)f_\theta|
\le\max_{\theta\text{ in the net}}|(P_m-P)f_\theta|
+\delta\{P_mL+PL\}.
\]
The maximum tends to zero in probability by Chebyshev's inequality for finitely many iid averages, and \(P_mL\to_p PL<\infty\). Letting \(\delta\downarrow0\) proves uniform convergence. Polynomial domination also justifies differentiating the expectation, including one-sided limits, and proves continuity of the population Hessian. Since its dimension is fixed,
\[
\sup_K|Q_m-Q|\to_p0,
\qquad
\sup_K\|\nabla^2Q_m-\nabla^2Q\|_{\mathrm{op}}\to_p0.
\]
The same polynomial bounds give the centered score estimate
\[
\nabla Q_m(\theta_0)-\nabla Q(\theta_0)=O_p(m^{-1/2}).
\]
This is a centered statement; it does not assert that every population score coordinate is zero.

## 3. Local strong convexity and consistency

Positive definiteness of \(H\) and continuity of the population Hessian give \(c>0\) and a small closed ball about \(\theta_0\) on which the population minimum eigenvalue is at least \(2c\), relative to the ambient nonnegative-variance domain. Intersect this ball with that domain and the zero-diagonal coordinate space to obtain a convex compact set \(K_0\). Uniform Hessian convergence implies that, with probability tending to one, the empirical Hessian has minimum eigenvalue at least \(c\) throughout \(K_0\).

Integrating the Hessian along a segment in \(K_0\) gives
\[
Q_m(\theta')\ge Q_m(\theta)+\nabla Q_m(\theta)^{\mathsf T}(\theta'-\theta)
+\frac c2\|\theta'-\theta\|_2^2.
\]
The segment need not be acyclic: the ambient formula remains defined and differentiable there because all variances are nonnegative.

The penalties vanish uniformly on \(\mathcal A\), so
\[
z_m:=\sup_{\mathcal A}|F_m-Q|\to_p0.
\]
For any \(\epsilon>0\), the subset of \(\mathcal A\) at distance at least \(\epsilon\) from the truth is either empty or compact with a strictly positive population gap \(d_\epsilon\). Every global minimizer obeys
\[
Q(\widehat\theta)\le F_m(\widehat\theta)+z_m
\le F_m(\theta_0)+z_m\le Q(\theta_0)+2z_m.
\]
On \(2z_m<d_\epsilon\), all global minimizers are within \(\epsilon\) of the truth. This proves consistency simultaneously for all global minimizers.

Because the true supports are fixed, finite, and nonempty,
\[
c_A=\min_{T_A}|A_{0,jk}|>0,
\qquad c_R=\min_{T_R}R_{0,jk}>0.
\]
Consistency therefore ensures that every global minimizer retains all true edges with probability tending to one.

## 4. Restricted minimizer and active expansion

Let \(\widetilde\theta\) minimize \(F_m\) over the true-support restriction, with all inactive coordinates zero. Its graphs are subgraphs of the true union DAG, so acyclicity is automatic. The preceding compactness and separation argument gives consistency of every restricted minimizer. With probability tending to one, its active coordinates are interior to their box bounds, active random variances are positive, and active fixed coefficients have signs \(s_A\).

Put
\[
r_m=\lambda_{2m}/\lambda_{1m},\qquad q_m=(s_A,r_m\mathbf1)^{\mathsf T}.
\]
The restricted first-order equations are
\[
\nabla_TQ_m(\widetilde\theta)+\lambda_{1m}q_m=0.
\]
At the truth, each active coordinate admits sufficiently small feasible perturbations of either sign. Population optimality therefore implies \(\nabla_TQ(\theta_0)=0\). The centered score bound from Section 2 gives
\[
\nabla_TQ_m(\theta_0)=O_p(m^{-1/2})=o_p(\lambda_{1m}).
\]
With \(d_T=\widetilde\theta_T-\theta_{0,T}\), integrate the active Hessian along the segment from the truth to the restricted estimator:
\[
\overline H_{TT,m}d_T=-\nabla_TQ_m(\theta_0)-\lambda_{1m}q_m.
\]
Consistency, uniform Hessian convergence, and population Hessian continuity imply \(\overline H_{TT,m}\to_p H_{TT}\). Since \(H_{TT}\) is positive definite, inversion yields
\[
d_T=-\lambda_{1m}H_{TT}^{-1}q_m+o_p(\lambda_{1m}).
\]

## 5. Strict inequalities on feasible inactive directions

Let \(G_0=\mathcal G(A_0)\cup\mathcal G(R_0)\), and define privately
\[
J_A=\{(j,k)\in\mathcal I\setminus T_A:G_0\cup\{j\to k\}\text{ is a DAG}\},
\]
\[
J_R=\{(j,k)\in\mathcal I\setminus T_R:G_0\cup\{j\to k\}\text{ is a DAG}\}.
\]
For \(a\in J_A\), both signs of a sufficiently small fixed-coordinate perturbation are feasible. Thus \(\partial_{A_a}Q(\theta_0)=0\), and the centered score bound gives \(\partial_{A_a}Q_m(\theta_0)=o_p(\lambda_{1m})\). Taylor expansion using the active displacement yields
\[
\partial_{A_a}Q_m(\widetilde\theta)
=-\lambda_{1m}h^{(A)}_{a,T}H_{TT}^{-1}q_m+o_p(\lambda_{1m}).
\]
The fixed-effect irrepresentability assumption, \(q_m\to(s_A,\kappa\mathbf1)^{\mathsf T}\), and finiteness of \(J_A\) imply, simultaneously,
\[
|\partial_{A_a}Q_m(\widetilde\theta)|\le(1-\eta/2)\lambda_{1m}
\quad(a\in J_A)
\]
with probability tending to one.

For \(a\in J_R\), a sufficiently small positive variance perturbation is feasible. Population optimality gives
\[
g_a:=\partial_{R_a}Q(\theta_0)\ge0.
\]
Consequently,
\[
\partial_{R_a}Q_m(\widetilde\theta)
=g_a-\lambda_{1m}h^{(R)}_{a,T}H_{TT}^{-1}q_m+o_p(\lambda_{1m}).
\]
Dividing by \(\lambda_{2m}=r_m\lambda_{1m}\), the second term converges to a number no smaller than \(-(1-\eta)\), while \(g_a/\lambda_{2m}\ge0\). The random-effect irrepresentability assumption therefore gives, simultaneously,
\[
\partial_{R_a}Q_m(\widetilde\theta)>-(1-\eta/2)\lambda_{2m}
\quad(a\in J_R)
\]
with probability tending to one. Empty sets require no inequalities.

No such score claim is made for cycle-creating inactive coordinates. On the no-false-negative event, every feasible global minimizer contains \(G_0\), so any additional coordinate outside \(J_A\) or \(J_R\), respectively, must be zero: otherwise its graph would contain a directed cycle.

## 6. Objective comparison and exact recovery

Work on the intersection of the preceding events, whose probability tends to one. Let \(\widehat\theta\) be any global minimizer. Both \(\widehat\theta\) and \(\widetilde\theta\) lie in \(K_0\). Put \(\Delta=\widehat\theta-\widetilde\theta\), and let \(P_m\) denote the sum of the two penalties. Strong convexity gives
\[
F_m(\widehat\theta)-F_m(\widetilde\theta)
\ge\nabla Q_m(\widetilde\theta)^{\mathsf T}\Delta
+P_m(\widehat\theta)-P_m(\widetilde\theta)
+\frac c2\|\Delta\|_2^2.
\]
For active fixed coordinates,
\[
|\widehat A_a|-|\widetilde A_a|\ge s_{A,a}(\widehat A_a-\widetilde A_a).
\]
For active random coordinates the penalty difference is exactly linear. The active first-order equations consequently make the sum of active score and penalty contributions nonnegative.

For \(a\in J_A\), the inactive contribution is bounded below by
\[
\bigl(\lambda_{1m}-|\partial_{A_a}Q_m(\widetilde\theta)|\bigr)|\widehat A_a|
\ge\frac\eta2\lambda_{1m}|\widehat A_a|.
\]
For \(a\in J_R\), nonnegativity of \(\widehat R_a\) gives the lower bound
\[
\bigl(\lambda_{2m}+\partial_{R_a}Q_m(\widetilde\theta)\bigr)\widehat R_a
\ge\frac\eta2\lambda_{2m}\widehat R_a.
\]
All other inactive contributions are zero by the feasibility argument in Section 5. Thus
\[
F_m(\widehat\theta)-F_m(\widetilde\theta)
\ge\frac c2\|\widehat\theta-\widetilde\theta\|_2^2
+\frac\eta2\lambda_{1m}\sum_{a\in J_A}|\widehat A_a|
+\frac\eta2\lambda_{2m}\sum_{a\in J_R}\widehat R_a\ge0.
\]
Global optimality and feasibility of \(\widetilde\theta\) give the reverse inequality. Every nonnegative term vanishes. In particular, \(\widehat\theta=\widetilde\theta\), and every inactive coordinate is zero. Together with retention of all true edges, this proves simultaneous exact recovery of the fixed and random graphs. All events used control every global minimizer, so both conclusions hold for any measurable choice and, in fact, simultaneously over all global minimizers with probability tending to one.

All theorem-critical obligations are closed; no specialized external support-recovery result is used as an unproved step.
