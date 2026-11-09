# Problem

## Setup

Consider a finite-horizon controlled Markov process with stages \(t=1,\ldots,H\), state space \(\mathcal S\), action space \(\mathcal A\), initial law \(S_1\sim\rho_1\), and rewards \(R_t\in[-1,1]\). Use measurable versions of the controlled and regular conditional probability kernels below. Conditional expectations at specified state-action pairs mean integration against these kernels.

The behavior policy is \(\mu_t(da\mid s)\). A target policy is a measurable probability kernel \(\pi_t(da\mid s,o_-)\). Both policies have the same initial law and controlled dynamics. Conditional on the decision history and current action, the reward/next-state law of \((R_t,S_{t+1})\) depends only on \((S_t,A_t)\). The conditional law of \((S_{t+1},O_t)\) also depends only on \((S_t,A_t)\) and is shared by the two policies. Set \(O_0=0\) and \(\widetilde S_t=(S_t,O_{t-1})\); in particular, the augmented process is Markov.

The observation indicator \(O_t\in\{0,1\}\) records whether the reward is available. The behavior observation law is the population law of
\[
\bigl(S_t,A_t,O_t,O_tR_t,S_{t+1}\bigr)_{t=1}^H.
\]
Thus all states, including \(S_{H+1}\), actions, and observation indicators are observed. The propensity
\[
e_t(s,a,r)=P_\mu(O_t=1\mid S_t=s,A_t=a,R_t=r)
\]
is not assumed known. For every stage and state-action-reward triple in the specified conditional laws, assume \(0<e_t(s,a,r)<1\). Under the behavior law assume
\[
O_t\perp(S_{t+1:H},R_{t+1:H})\mid(S_t,A_t,R_t),\qquad t<H,
\]
and, at every stage including \(H\), assume
\[
S_{t+1}\perp O_t\mid(R_t,S_t,A_t),
\qquad
S_{t+1}\not\perp R_t\mid(S_t,S_t\text{'s action }A_t,O_t=1).
\]
In the second expression the conditioning variables are simply \((S_t,A_t,O_t=1)\); equivalently, the conditional next-state and reward variables are not independent on the observed-reward subset at a fixed state-action pair.

Fix any target policy for which there are finite constants \(\kappa_t\), allowed to depend on that policy, such that, for every measurable action set \(B\),
\[
\pi_t(B\mid s,o_-)\leq\kappa_t\mu_t(B\mid s)
\]
for every \((s,o_-)\). For discrete actions this is \(\pi_t(a\mid s,o_-)\leq\kappa_t\mu_t(a\mid s)\), including the requirement that the target assign zero probability to behavior-null actions.

For each \((t,s,a)\), let \(\nu_{t,s,a}\) and \(\eta_{t,s,a}\) be the controlled conditional laws of \(S_{t+1}\) and \(R_t\), respectively, at \((s,a)\). Assume the following completeness properties:

- If \(f\in L^2(\eta_{t,s,a})\) and \(E[f(R_t)\mid S_{t+1},s,a]=0\), then \(f=0\) \(\eta_{t,s,a}\)-almost surely.
- If \(h\in L^2(\nu_{t,s,a})\) and \(E[h(S_{t+1})\mid R_t,s,a]=0\), then \(h=0\) \(\nu_{t,s,a}\)-almost surely.

Define
\[
T_{t,s,a}:L^2(\nu_{t,s,a})\longrightarrow L^2(\eta_{t,s,a}),
\qquad
(T_{t,s,a}h)(r)=E[h(S_{t+1})\mid R_t=r,s,a].
\]
Assume this operator is Hilbert--Schmidt. Write a singular system as \((\sigma_j,u_j,v_j)_{j\in J}\), where \(J\) may be finite or countable, \(\sigma_j>0\), \(u_j\in L^2(\eta_{t,s,a})\), \(v_j\in L^2(\nu_{t,s,a})\),
\[
T_{t,s,a}v_j=\sigma_j u_j,
\qquad T_{t,s,a}^*u_j=\sigma_j v_j.
\]
For \(g(r)=r\), assume
\[
\sum_{j\in J}\frac{|\langle g,u_j\rangle_{L^2(\eta_{t,s,a})}|^2}{\sigma_j^2}<\infty.
\]

A bridge is a measurable function \(b_t:\mathcal S\times\mathcal A\times\mathcal S\to\mathbb R\) whose section \(b_t(s,a,\cdot)\) belongs to \(L^2(\nu_{t,s,a})\) and satisfies
\[
E[b_t(s,a,S_{t+1})\mid R_t=r,s,a]=r
\]
for \(\eta_{t,s,a}\)-almost every \(r\). Square integrability here refers to these conditional laws; no unconditional bound on the bridge's squared norm over state-action pairs is imposed.

Define the target value by
\[
V(\pi)=E_\pi\left[\sum_{t=1}^H R_t\right].
\]
A quantity is identified if any two models satisfying the assumptions and inducing the same behavior observation law give it the same value. For functions, identification and uniqueness are understood up to the relevant probability-null sets; observational identification is required only on behavior support and on state-action pairs visited by the target.

## Task

Prove that bridges exist and that each section is unique up to \(\nu_{t,s,a}\)-null sets. Prove that the bridges on behavior support and the value of every target policy satisfying the stated action-domination condition are identified by the behavior observation law.

In particular, define, on behavior-supported augmented state-action pairs,
\[
\bar r_t(\tilde s,a)
=E_\mu[b_t(S_t,a,S_{t+1})\mid\widetilde S_t=\tilde s,A_t=a].
\]
Show that the recursion
\[
\widetilde V_{H+1}^\pi=0,
\]
\[
\widetilde Q_t^\pi(\tilde s,a)
=\bar r_t(\tilde s,a)
+E_\mu[\widetilde V_{t+1}^\pi(\widetilde S_{t+1})\mid\widetilde S_t=\tilde s,A_t=a],
\]
\[
\widetilde V_t^\pi(\tilde s)
=\int_{\mathcal A}\widetilde Q_t^\pi(\tilde s,a)\,\pi_t(da\mid\tilde s)
\]
identifies the true target conditional return functions on target support and satisfies
\[
V(\pi)=\int\widetilde V_1^\pi(s,0)\,\rho_1(ds).
\]
For discrete actions, the action integral is the corresponding sum.

Also prove that, at each behavior-supported state-action pair, the full bridge equation is equivalent to the conditional weighted equation
\[
E_\mu\left[
\frac{O_t}{e_t(s,a,R_t)}
\bigl(b_t(s,a,S_{t+1})-R_t\bigr)
\,\middle|\,R_t,S_t=s,A_t=a
\right]=0.
\]
The weighted residual is defined to be zero when \(O_t=0\). Establish this equivalence without assuming that the propensity is known.
