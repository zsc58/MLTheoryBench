# Problem

## Setup

Let \(S\) and \(A\) be finite nonempty state and action sets, and let \(\mathcal Q\) be a set of action distributions containing every point mass on \(A\). Controller policies may depend on the observed state-action history and must choose distributions in \(\mathcal Q\). Let \(\mathcal P\) be a nonempty, possibly non-rectangular set of stationary transition kernels \(p(\cdot\mid x,a)\); the adversary chooses one \(p\in\mathcal P\) for the entire horizon. For reward \(r:S\times A\to[0,1]\), a policy \(\pi\), and initial distribution \(\mu\), write
\[
G_T(\pi,p,\mu)=\mathbb E_\mu^{\pi,p}\!\left[\sum_{t=0}^{T-1}r(X_t,A_t)\right].
\]
Assume every \(p\in\mathcal P\) is weakly communicating: there is a set \(C_p\subseteq S\) such that any two states of \(C_p\) can reach each other with positive probability under suitable stationary controller policies, and every state outside \(C_p\) is transient under every stationary controller policy. Let \(\alpha_p\) be the state-independent classical optimal average reward for the fixed reward \(r\). Assume there is a unique worst kernel \(p^*\in\mathcal P\), with \(\alpha_{p^*}=\inf_{p\in\mathcal P}\alpha_p=:\alpha^*\).

Assume a reference history-dependent policy \(\pi_{\rm RL}\), taking distributions in \(\mathcal Q\), satisfies the following all-rewards property. For each \(u:S\times A\to[0,1]\), denote by \(\alpha_p(u)\) the classical optimal gain for reward \(u\) and kernel \(p\). For every \(p\in\mathcal P\), initial distribution \(\mu\), and such \(u\),
\[
\limsup_{T\to\infty}\frac1T\mathbb E_\mu^{\pi_{\rm RL},p}\!\left[\sum_{t=0}^{T-1}\bigl(\alpha_p(u)-u(X_t,A_t)\bigr)\right]=0.
\]
Choose an admissible stationary policy \(\Delta^*\), possibly randomized, that is optimal for \(p^*\) and whose induced matrix
\[
P_0(x'\mid x)=\sum_{a\in A}\Delta^*(a\mid x)p^*(x'\mid x,a)
\]
is unichain, with unique closed class \(C_0\). Let \(v^*:S\to\mathbb R\) solve
\[
\alpha^*+v^*(x)=\sum_a\Delta^*(a\mid x)r(x,a)+\sum_{x'}P_0(x'\mid x)v^*(x'),
\]
and define \(|v^*|_{\rm span}=\max_xv^*(x)-\min_xv^*(x)\).

Let \(\nu\) be a product Dirichlet prior on transition matrices \(Q\), with strictly positive parameters for every row entry. While \(\Delta^*\) is run from time \(m\), compute, for \(m<n\) and as long as all observed \(P_0\)-transition probabilities are positive,
\[
\Lambda_{m,n}=\int\prod_{t=m}^{n-1}\frac{Q(X_{t+1}\mid X_t)}{P_0(X_{t+1}\mid X_t)}\,\nu(dQ).
\]
An observed transition with zero \(P_0\)-probability causes immediate rejection. For \(\rho\in(0,1)\), set
\[
\tau_{m,\rho}=\inf\{n\ge m+1:P_0(X_n\mid X_{n-1})=0\ \text{or}\ \Lambda_{m,n}\ge1/\rho\}.
\]
Write \(P_p(x'\mid x)=\sum_a\Delta^*(a\mid x)p(x'\mid x,a)\). Assume either (i) \(P_p|_{C_0}\ne P_0|_{C_0}\) for every \(p\in\mathcal P\setminus\{p^*\}\), or (ii) \(P_0\) is irreducible.

Define transient value by
\[
\operatorname{TV}(\mu,\pi;p)=\liminf_{T\to\infty}\mathbb E_\mu^{\pi,p}\!\left[\sum_{t=0}^{T-1}(r(X_t,A_t)-\alpha^*)\right],\qquad
\operatorname{TV}(\mu,\pi)=\inf_{p\in\mathcal P}\operatorname{TV}(\mu,\pi;p).
\]

## Task

Fix \(\zeta>1\). Let \(L_j=2^j\), \(\rho_j=2^{-\zeta j}\), \(t_1=0\), and \(t_j=t_{j-1}+L_{j-1}\) for \(j\ge2\). Construct the epoch policy \(\pi^*\) which, in epoch \(j\), runs \(\Delta^*\) from time \(t_j\) until \(\tau_{t_j,\rho_j}\) or time \(t_j+L_j\), whichever comes first. If rejection occurs before the epoch ends, restart \(\pi_{\rm RL}\) at the rejection time using that time's state as its initial state and the subsequent within-epoch history as its history; run it until the epoch ends. At the next epoch, restart the test-and-learn rule. Prove that for every initial distribution \(\mu\), \(\pi^*\) is robust-optimal, i.e.
\[
\inf_{p\in\mathcal P}\liminf_{T\to\infty}T^{-1}G_T(\pi^*,p,\mu)=\alpha^*,
\]
and that
\[
\operatorname{TV}(\mu,\pi^*)\ge -\frac{2^\zeta}{2^\zeta-1}|v^*|_{\rm span}-\frac1{2^{\zeta-1}-1}.
\]
