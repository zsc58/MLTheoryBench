# Problem

## Setup

Let \(d\geq1\), let \(\mathcal P_2(\mathbb R^d)\) be the probability measures with finite second moment, and let \(\rho_0\in\mathcal P_2(\mathbb R^d)\) be absolutely continuous. For probability measures \(\mu,\nu\), write \(\Pi(\mu,\nu)\) for their couplings and
\[
W_2(\mu,\nu)^2=\min_{\pi\in\Pi(\mu,\nu)}\int |x-y|^2\,d\pi(x,y).
\]
Write \(\Pi_o(\mu,\nu)\) for the minimizing couplings. Throughout, convergence in \(\mathcal P_2\) means narrow convergence, that is, convergence against bounded continuous functions, together with convergence of second moments; equivalently, it means convergence in \(W_2\). Lower semicontinuity on \(\mathcal P_2\) refers to this topology.

Set \(H=L^2_{\rho_0}(\mathbb R^d;\mathbb R^d)\), with its usual inner product, and let
\[
\mathcal K=\{\nabla\varphi:\ \varphi\text{ is a convex potential and }\nabla\varphi\in H\}.
\]
Potentials are understood in the usual convex optimal-transport sense on their effective domains, with gradients defined \(\rho_0\)-almost everywhere. The Sobolev requirement is homogeneous and weighted: the gradient must belong to \(H\), but the potential itself need not be square-integrable. Maps are identified up to \(\rho_0\)-null sets. Let \(\operatorname{Tan}_T\mathcal K\) denote the closed tangent cone at \(T\), and let \(\operatorname{proj}\) denote Hilbert-space metric projection. For \(\mu\in\mathcal P_2\), denote by \(B_\mu\in\mathcal K\) the unique gradient-of-convex map transporting \(\rho_0\) to \(\mu\), and set \(\mathrm{id}=B_{\rho_0}\).

Let \(\mathcal D:\mathcal P_2\to\mathbb R\) be bounded below, lower semicontinuous, and Wasserstein differentiable at every \(\mu\in\mathcal P_2\). Specifically, its gradient \(g_\mu\) belongs to
\[
\overline{\{\nabla\psi:\psi\in C_c^\infty(\mathbb R^d)\}}^{L^2_\mu},
\]
and, as \(W_2(\mu,\nu)\to0\),
\[
\mathcal D(\nu)-\mathcal D(\mu)
=\int\langle g_\mu(x),y-x\rangle\,d\pi_\nu(x,y)
+o(W_2(\mu,\nu))
\]
for every selection \(\pi_\nu\in\Pi_o(\mu,\nu)\). Thus this differentiability assumption is a finite-valued expansion at every measure, including \(\rho_0\).

Assume that for some \(\lambda\in\mathbb R\), every \(S,T\in\mathcal K\), and every \(s\in[0,1]\),
\[
\mathcal D(((1-s)T+sS)_\#\rho_0)
\leq(1-s)\mathcal D(T_\#\rho_0)+s\mathcal D(S_\#\rho_0)
-\frac\lambda2s(1-s)\|T-S\|_H^2.
\]

A constrained flow on \([0,t_{\max}]\) is an \(H^1\) curve \(T:[0,t_{\max}]\to\mathcal K\), initialized by \(T_0=\mathrm{id}\), satisfying
\[
\dot T_t=\operatorname{proj}_{\operatorname{Tan}_{T_t}\mathcal K}
\bigl(-g_{T_{t\#}\rho_0}\circ T_t\bigr)
\quad\text{for almost every }t.
\]
A global constrained flow is a curve on \([0,\infty)\) whose restriction to every finite interval is a constrained flow. Long-time conclusions below concern such global flows. Write \(\mu_t=T_{t\#}\rho_0\).

For the convergence bounds, assume additionally that \(\mathcal D\) has a unique minimizer \(\mu_*\), set \(T_*=B_{\mu_*}\), and assume endpoint convexity: for some \(\kappa\geq0\), the segment inequality above holds for every \(T\in\mathcal K\) with \(S=T_*\) and with parameter \(\kappa\).

The following two additional conditions are used only for the conclusions that explicitly invoke them:

- \(\mathcal D\) metrizes convergence to its minimizer if, for every sequence \((\nu_n)\subset\mathcal P_2\),
\[
\mathcal D(\nu_n)-\mathcal D(\mu_*)\longrightarrow0
\quad\Longleftrightarrow\quad
W_2(\nu_n,\mu_*)\longrightarrow0.
\]
- A given global flow satisfies power growth if there are constants \(c>0\) and \(\alpha>0\), independent of time, such that
\[
\|B_{\mu_t}-B_{\mu_*}\|_H^2
\leq c\,[\mathcal D(\mu_t)-\mathcal D(\mu_*)]^\alpha
\quad\text{for almost every }t\geq0.
\]
No power-growth inequality away from the selected flow is assumed.

## Task

Prove the following integrated theorem.

1. For every \(t_{\max}>0\), a constrained flow with the stated initial condition exists on \([0,t_{\max}]\). The finite-horizon flows can be chosen consistently to give a global constrained flow.

2. Along any constrained flow, \(\mathcal D(\mu_t)\) is nonincreasing. Under the additional convergence hypotheses, prove the following bounds on the interval of the flow, and the stated long-time conclusions for global flows.

If \(\kappa=0\), then for every \(t>0\),
\[
0\leq\mathcal D(\mu_t)-\mathcal D(\mu_*)
\leq\frac{W_2(\rho_0,\mu_*)^2}{2t}.
\]
If \(\mathcal D\) metrizes convergence to its minimizer as defined above, then \(T_t\to T_*\) strongly in \(H\) as \(t\to\infty\). If the flow satisfies power growth with constants \(c,\alpha\), prove, for every \(t>0\),
\[
\|T_t-T_*\|_H^2
\leq c\,2^{-\alpha}t^{-\alpha}W_2(\rho_0,\mu_*)^{2\alpha}.
\]

If \(\kappa>0\), then for every \(t\geq0\),
\[
\mathcal D(\mu_t)-\mathcal D(\mu_*)
\leq e^{-2\kappa t}\bigl[\mathcal D(\rho_0)-\mathcal D(\mu_*)\bigr],
\]
and
\[
\|T_t-T_*\|_H^2
\leq\frac4\kappa e^{-2\kappa t}
\bigl[\mathcal D(\rho_0)-\mathcal D(\mu_*)\bigr].
\]
