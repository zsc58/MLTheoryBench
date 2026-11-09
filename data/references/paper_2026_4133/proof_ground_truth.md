# Reference Proof

## Source Contract and Proof Obligations

The pre-decision history, past controls, model parameters, policy, and actual state are held fixed. Only the final available observation is replaced. The observation induces a posterior state draw, followed by an action drawn from the policy conditional on that draw. The actual state is not replaced. Fixing that state for this identity does not assert that it is revealed to an attacker.

The selected local RL setup uses the Bellman relations stated in the problem and a discount factor in \([0,1)\). The final available observation is not assumed to terminate the future return. The Gaussian predictive law explains the given likelihood ellipsoid; no filtering, smoothing, or likelihood-region derivation is a target of this problem.

The theorem-critical obligations are: (1) change the real-state transition measure to the attacked-state measure; (2) separate the three action-level terms using integrable algebra; (3) average under the policy and posterior in the stated order; and (4) preserve the optimization problem on the same feasible set. All four are proved below.

## Complete Proof

Fix \(o\in\mathcal E_\rho\), and fix \(x\) and \(a\). Write
\[
p_0(y)=p(y\mid x^0,a),\qquad p_x(y)=p(y\mid x,a),\qquad
 g_x(y)=r(x,a,y)+\gamma V^\pi(y).
\]
Absolute continuity implies that \(p_0=0\) almost everywhere on \(\{p_x=0\}\). With the stated version of \(w\), therefore,
\[
p_x(y)w(y,a;x^0,x)=p_0(y)
\]
almost everywhere with respect to the common reference measure. Consequently, for every integrable function \(f\) under the real-state transition law,
\[
\int p_0(y)f(y)\,dy=\int p_x(y)w(y,a;x^0,x)f(y)\,dy.
\]
In particular, the real-state Bellman relation gives
\[
Q^\pi(x^0,a)=\int p_x(y)w(y,a;x^0,x)
 [r(x^0,a,y)+\gamma V^\pi(y)]\,dy.
\]
The following equality holds pointwise wherever the densities and ratio are defined:
\[
w[r(x^0,a,y)+\gamma V^\pi(y)]
=g_x(y)+(w-1)g_x(y)+w[r(x^0,a,y)-r(x,a,y)].
\]
The three terms on the right are integrable by the assumptions on the defining Bellman and correction integrals. Integrating and using their definitions yields
\[
Q^\pi(x^0,a)=Q^\pi(x,a)+\Delta_{\mathrm{tr}}(x,a)+\Delta_{\mathrm{rw}}(x,a).
\]
This closes the change-of-measure and action-level decomposition obligations, including denominator-null sets.

For each \(x\), integrate this identity under \(\pi(da\mid x)\). The assumed absolute integrability of the policy integrals justifies linearity. Thus
\[
\int Q^\pi(x^0,a)\pi(da\mid x)
=V^\pi(x)+\Delta_{\mathrm{tr}}(x)+\Delta_{\mathrm{rw}}(x).
\]
By the definition of the joint sampling law \(\mu_o(dx)\pi(da\mid x)\), and the absolute integrability in the definition of \(J(o)\),
\[
\begin{aligned}
J(o)
&=\int\mu_o(dx)\int Q^\pi(x^0,a)\pi(da\mid x)\\
&=\mathbb E_{X\sim\mu_o}
 [V^\pi(X)+\Delta_{\mathrm{tr}}(X)+\Delta_{\mathrm{rw}}(X)].
\end{aligned}
\]
The sum inside the last expectation is integrable because it equals the conditional integral of the integrable random variable \(Q^\pi(x^0,A)\). Separate posterior integrability of each of its three summands is not needed. This proves the requested identity for every feasible observation.

The original and decomposed objectives agree at every point of the same feasible set. They therefore specify identical minimization problems, have equal infima, and have identical minimizers whenever a minimizer exists. No continuity or attainment assertion is needed. For \(\rho=0\), the feasible set is the singleton \(\{\bar o\}\); the proof still applies. It also applies without change when \(\gamma=0\) or the policy is deterministic.
