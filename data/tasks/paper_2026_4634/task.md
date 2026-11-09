# Problem

## Setup

Let \(K\geq 2\) be an integer. Consider i.i.d. tasks with covariates \(Z\in\mathbb R^d\), real prices \(p_1,\ldots,p_K\), real demands \(D_1,\ldots,D_K\), and \(P_k=(1,p_k)^T\). The structural model is
\[
D_k=P_k^T\Theta+\varepsilon_k,\qquad \Theta=g(Z)+\Omega,
\]
where \(g:\mathbb R^d\to\mathbb R^2\) is measurable. Demand shocks have mean zero and finite second moments and are independent across tasks and observations. The heterogeneity satisfies
\[
E[\Omega\mid Z]=0,\qquad E\|\Omega\|^2<\infty,
\]
and the collection of task covariates and heterogeneity variables is independent of the collection of demand shocks. Prices may depend arbitrarily on \(\Omega\) conditional on \(Z\).

Let \(A=\{a,b\}\subseteq\{1,\ldots,K\}\) be selected by a fixed measurable rule depending on \((Z,p_1,\ldots,p_K)\), with \(p_a\ne p_b\) almost surely. Write \(D^{-k}\) for the indexed vector of outcomes other than \(D_k\). For every index \(k\), assume local exogeneity on the event that it is selected:
\[
E[\varepsilon_k\mid Z,p_1,\ldots,p_K,D^{-k}]=0
\quad\text{almost surely on }\{k\in A\}.
\]

Draw \(\kappa\) uniformly from \(A\), independently across tasks and independently of \((Z,p_1,\ldots,p_K,\Theta,\varepsilon_1,\ldots,\varepsilon_K)\) conditional on \(A\). Mask both selected outcomes and define
\[
X=(Z,p_1,\ldots,p_K,D^{-A}),
\]
where \(D^{-A}\) retains the indexed outcomes outside \(A\); it is the empty vector when \(K=2\).

A refinement is an input \(W=(X,R)\), where
\[
R=r(\kappa,D_a,D_b)
\]
for a fixed measurable rule \(r\). The rule takes values in a measurable space \(\mathsf S\) whose singletons are measurable. When discussing the rule at a specified covariate/price support point, those covariate and price values are held fixed.

For a process with \(E\|\Theta\|<\infty\), define its causal target by the ordinary vector conditional expectation
\[
m(W)=E[\Theta\mid W].
\]
For every measurable \(\mathbb R^2\)-valued function \(h\) of \(W\), define its population prediction risk by
\[
\mathcal R(h)=E\big[(D_\kappa-P_\kappa^T h(W))^2\big],
\]
allowing the nonnegative expectation to equal \(+\infty\). The refined information identifies the causal target if \(m(W)\) is the unique population risk minimizer over these functions, up to almost-sure equality.

## Task

Prove the following theorem.

Fix any covariate/price support point \((\bar z,\bar p_1,\ldots,\bar p_K)\) at which the selection rule chooses \(\{a,b\}\) with \(\bar p_a\ne\bar p_b\). For every fixed measurable refinement rule whose restriction at this point to \(\{a,b\}\times\mathbb R^2\) is nonconstant, there exists a data-generating process satisfying all the setup assumptions, with \(E\|\Theta\|<\infty\), and satisfying the stronger local-exogeneity condition
\[
E[\varepsilon_k\mid Z,p_1,\ldots,p_K,D^{-k}]=0
\qquad\text{for every }k\in\{1,\ldots,K\},
\]
such that the refined risk \(\mathcal R\) does not identify \(E[\Theta\mid W]\).
