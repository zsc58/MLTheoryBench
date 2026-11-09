# Problem

## Setup

Let E be a finite state space and let \(p^{\mathrm{base}}\) be the law of a nonexplosive continuous-time Markov chain \((X_t)_{0\le t\le1}\) with prescribed initial law \(\mu\). Use a specified Markov family of nonexplosive càdlàg processes with transition kernels \(p^{\mathrm{base}}_{s|t}(z\mid x)\) for every starting state x and every \(0\le t\le s\le1\), including states not reached under \(\mu\). At equal times the kernel is the identity.

The base rates are finite, measurable, and locally integrable in time on [0,1). For \(t<1\), they are the infinitesimal transition rates
\[
u_t^{\mathrm{base}}(y,x)=\lim_{\varepsilon\downarrow0}
\frac{p^{\mathrm{base}}_{t+\varepsilon|t}(y\mid x)-\mathbf1_{\{y=x\}}}{\varepsilon},
\]
with nonnegative off-diagonal entries and
\[
u_t^{\mathrm{base}}(x,x)=-\sum_{y\ne x}u_t^{\mathrm{base}}(y,x).
\]
These rates describe all jumps before time 1 as ordinary jump intensities. Precisely, under the law starting from any pair (a,x), for every \(a<b<1\) and every pair of distinct states v,w, let \(N_s^{v,w}\) count jumps from w to v in (a,s]. Then
\[
N_s^{v,w}-\int_a^s\mathbf1_{\{X_{r-}=w\}}u_r^{\mathrm{base}}(v,w)\,dr,
\qquad a\le s\le b,
\]
is a martingale for the natural filtration of X. Under every starting law (a,x) with a<1, also require \(X_{1-}=X_1\) almost surely, where \(X_{1-}=\lim_{s\uparrow1}X_s\).

Assume that under the base law the terminal state is independent of the initial state. Let \(g:E\to\mathbb R\) be a terminal cost. Among path laws p with initial law \(\mu\), consider
\[
J(p)=\mathbb E_p[g(X_1)]+\operatorname{KL}(p\,\|\,p^{\mathrm{base}}).
\]
Define
\[
V_t(x)=-\log\!\sum_z p^{\mathrm{base}}_{1|t}(z\mid x)e^{-g(z)},\qquad V_1(x)=g(x).
\]
Let \(p_\star\) denote the optimizer and \(u_t^\star(y,x)\) its canonical infinitesimal CTMC rates for \(t<1\).

For a trajectory X with terminal state \(X_1\), define its adjoint vector by the backward terminal-value system
\[
\widetilde a_1(y;X)=e^{-g(y)+g(X_1)},\qquad
\frac d{dt}\widetilde a_t(y;X)=-\sum_z u_t^{\mathrm{base}}(z,y)\widetilde a_t(z;X).
\]
This definition is understood in the well-posed terminal-value sense: for each fixed terminal state \(w\in E\), the system with terminal vector \((e^{-g(y)+g(w)})_{y\in E}\) has a unique absolutely continuous solution on [0,1]. The differential equation holds almost everywhere, and the terminal value is attained.

## Task

Prove that for every \(0\le t<1\), every \(y\ne x\), and every state x satisfying \(\mathbb P_{p_\star}(X_t=x)>0\),
\[
u_t^\star(y,x)=u_t^{\mathrm{base}}(y,x)e^{-V_t(y)+V_t(x)}
=u_t^{\mathrm{base}}(y,x)\,\mathbb E_{p_\star}\!\left[\widetilde a_t(y;X)\mid X_t=x\right].
\]
At t=1, prove the same rate identities for every \(y\ne x\) with \(\mathbb P_{p_\star}(X_1=x)>0\) whenever the base rate in question has a finite left limit, interpreting \(u_1^{\mathrm{base}}(y,x)\) and \(u_1^\star(y,x)\) as the respective left limits. No forward rate beyond time 1 is asserted.

Moreover, prove that for every \(t\in[0,1]\) and every state y, whether or not it is reachable under \(p_\star\),
\[
\widetilde a_t(y;X)=\sum_z p^{\mathrm{base}}_{1|t}(z\mid y)e^{-g(z)+g(X_1)}.
\]
