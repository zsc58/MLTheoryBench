# Reference Proof

## Source Contract and Obligations

The source model permits arbitrary real prices and structural parameters, zero-variance shocks, and independent finite-variance shocks without requiring identical distributions across observations. The constructed witness must satisfy local exogeneity for every index, and query randomization must be independent of all structural variables conditional on the selected pair. The refinement rule is fixed before constructing the witness. The finite-support constructions below also ensure that the target, comparison predictors, and their risks are finite.

The obligations are: realize a distinguishing outcome configuration when query identity can be revealed; otherwise obtain a coordinate on which the common outcome refinement varies; construct admissible centered shocks; prove a nonzero observable event moment without unjustified cancellation claims; and establish nonuniqueness or strict population-risk improvement. Each obligation is derived below. No external theorem or unproved paper-specific dependency is used.

## 1. Common Admissible Setup

Fix the stipulated support point and concentrate the covariates and all prices there:
\[
Z\equiv\bar z,\qquad p_{1:K}\equiv\bar p_{1:K}.
\]
Then the selected pair is deterministically \(A=\{a,b\}\). Write \(P_j=(1,\bar p_j)^T\). The matrix with rows \(P_a^T,P_b^T\) has determinant \(\bar p_b-\bar p_a\ne0\), so either pair of desired mean outcomes determines a unique constant parameter.

In each case choose that parameter \(\theta_0\), set \(g\equiv\theta_0\) and \(\Omega\equiv0\), and define
\[
\Theta\equiv\theta_0,\qquad D_j=P_j^T\theta_0+\varepsilon_j.
\]
Draw \(\kappa\) independently of all task variables with probabilities \(1/2,1/2\) on \(a,b\). Independent copies of this construction supply i.i.d. tasks. The target is always \(m(W)=\theta_0\). The parameter is chosen separately in the two cases; it cannot in general be fixed at zero.

## 2. A Distinguishing Query Configuration

Suppose some \((d_a,d_b)\) satisfies
\[
r(a,d_a,d_b)\ne r(b,d_a,d_b).
\]
Choose \(\theta_0\) as the unique solution of
\[
P_a^T\theta_0=d_a,\qquad P_b^T\theta_0=d_b,
\]
and set every shock to zero. All independence and moment requirements hold, and local exogeneity holds for every index. The selected outcomes are exactly \((d_a,d_b)\), not necessarily \((0,0)\).

The input \(X\) is deterministic. The two possible values of \(R\) distinguish \(\kappa=a\) from \(\kappa=b\); their singleton events are measurable. Consequently the following predictors are measurable functions of \(W\):
\[
h_0(W)=\theta_0,\qquad
h_1(W)=\theta_0+v_\kappa,\qquad
v_j=(\bar p_j,-1)^T\quad(j=a,b).
\]
They may be defined arbitrarily outside the realized input support. Each \(v_j\ne0\) and \(P_j^Tv_j=0\). Therefore
\[
P_\kappa^Th_1(W)=P_\kappa^T\theta_0=D_\kappa,
\]
so both predictors have zero risk, while they differ almost surely. Nonnegative squared loss makes both population minimizers. Thus the target is not uniquely identified.

## 3. An Outcome-Dependent Refinement

If the preceding case does not occur, then
\[
r(a,u,v)=r(b,u,v)=F(u,v)
\quad\text{for all }(u,v)\in\mathbb R^2.
\]
The function \(F\) is nonconstant. It must vary in at least one coordinate: otherwise moving between any two points one coordinate at a time would leave its value unchanged.

First suppose there exist \(u_0<u_1\) and \(c\) such that
\[
F(u_0,c)\ne F(u_1,c).
\]
Choose \(\mu\in(u_0,u_1)\), and define
\[
x_0=u_0-\mu<0,\qquad x_1=u_1-\mu>0,\qquad
\lambda=\frac{x_1}{-x_0}>0,
\]
\[
s=1+\lambda,\qquad B=\max\{|x_0|,x_1\}.
\]
Choose a positive number satisfying
\[
0<\rho<\min\left\{\frac{1}{2s},\frac{x_1}{4Bs^2}\right\}.
\]
Let every \(\varepsilon_j\) be an independent draw from the same distribution
\[
\Pr(\varepsilon_j=x_0)=\rho\lambda,\qquad
\Pr(\varepsilon_j=x_1)=\rho,\qquad
\Pr(\varepsilon_j=0)=1-\rho s.
\]
These are positive probabilities summing to one. Moreover,
\[
E[\varepsilon_j]=\rho\lambda x_0+\rho x_1=0,
\]
and the shocks have finite second moments. The small parameter changes the atom probabilities; it does not shrink the distinguishing outcome values.

Choose \(\theta_0\) to solve
\[
P_a^T\theta_0=\mu,\qquad P_b^T\theta_0=c.
\]
Use the common setup above with these shocks. For every index \(k\), \((Z,p_{1:K},D^{-k})\) depends only on deterministic quantities and shocks other than \(\varepsilon_k\). Hence independence and centering imply
\[
E[\varepsilon_k\mid Z,p_{1:K},D^{-k}]=0.
\]
Thus the all-index condition, not merely its selected-index version, holds. Constant \(Z,\Omega,\Theta\) verify the remaining structural and heterogeneity conditions.

Set
\[
r_0=F(u_0,c),\qquad E_0=\{R=r_0\},\qquad
c_a=E[\varepsilon_a\mathbf1_{E_0}],\qquad
c_b=E[\varepsilon_b\mathbf1_{E_0}].
\]
The event is measurable. Whenever \(\varepsilon_a=x_0\) and \(\varepsilon_b=0\), the selected outcomes are \((u_0,c)\), so
\[
\Pr(E_0)\geq\rho\lambda(1-\rho s)>0.
\]
When \(\varepsilon_b=0\), the term with \(\varepsilon_a=x_1\) does not belong to \(E_0\), and the term with \(\varepsilon_a=0\) contributes zero to \(c_a\). Consequently
\[
c_a=\rho\lambda x_0(1-\rho s)+\delta_\rho
=-\rho x_1(1-\rho s)+\delta_\rho,
\]
where the remaining contribution requires both selected shocks to be nonzero. Thus
\[
|\delta_\rho|
\leq B\Pr(\varepsilon_a\ne0,\varepsilon_b\ne0)
=B\rho^2s^2.
\]
The chosen bound on \(\rho\) gives
\[
c_a<-\frac{\rho x_1}{2}+\frac{\rho x_1}{4}
=-\frac{\rho x_1}{4}<0.
\]

In this case \(R=F(D_a,D_b)\) does not depend on \(\kappa\). By independent uniform query selection,
\[
M:=E[P_\kappa\varepsilon_\kappa\mathbf1_{E_0}]
=\frac12(P_a c_a+P_b c_b).
\]
Because \(P_a,P_b\) are linearly independent and \(c_a\ne0\), we have \(M\ne0\). No smallness claim about \(c_b\) is needed: other-query contributions may be first order and still cannot cancel the nonzero coefficient in the \(P_a\) direction.

## 4. Failure of Population Minimization and Completion

Under the outcome-dependent construction, \(X\) depends only on the shocks outside \(A\). Those shocks are independent of \((\kappa,\varepsilon_a,\varepsilon_b)\), which determine \((R,P_\kappa\varepsilon_\kappa)\). Therefore
\[
E[P_\kappa\varepsilon_\kappa\mid W]
=E[P_\kappa\varepsilon_\kappa\mid R].
\]
On the positive-probability event \(E_0\), this conditional vector is
\[
\frac{M}{\Pr(E_0)}\ne0.
\]
This violates the conditional first-order condition at the target \(\theta_0\). To verify directly that it also yields a strictly better measurable population predictor, define
\[
C=E[(P_\kappa^TM)^2\mathbf1_{E_0}]<\infty,\qquad
 t=\frac{\|M\|^2}{C+1}>0,
\]
and
\[
h_t(W)=\theta_0+tM\mathbf1_{E_0}.
\]
This is a bounded measurable predictor. Since \(D_\kappa-P_\kappa^T\theta_0=\varepsilon_\kappa\), expanding the finite expectations gives
\[
\mathcal R(h_t)-\mathcal R(\theta_0)
=t^2C-2tM^TE[P_\kappa\varepsilon_\kappa\mathbf1_{E_0}]
=t^2C-2t\|M\|^2<0,
\]
because \(tC<\|M\|^2\). Thus the causal target is not a population minimizer.

If \(F\) instead varies in its second coordinate, interchange \(a\) and \(b\): solve for selected means \((c,\mu)\), use the same centered shock construction, and obtain a nonzero coefficient in the \(P_b\) direction. Every calculation and all-index exogeneity verification remain valid.

The two query cases are exhaustive. In each case the rule and support point were fixed before selecting the witnessing law. The constructions work also when \(K=2\), where the unselected outcome vector is empty. All comparison risks are finite, all required means exist, and no positivity restriction on noise variance or further price separation is used. Therefore every stipulated nonconstant refinement admits a process satisfying the complete source contract under which the causal target is not uniquely identified.
