# Problem

## Setup

Fix a positive integer \(d\) and \(\tau>0\). Write \(\mathcal P_1(\mathbb R^d)\) for the Borel probability measures \(\nu\) satisfying \(\int |x|\,d\nu(x)<\infty\). For \(\nu,\widetilde\nu\in\mathcal P_1(\mathbb R^d)\), define
\[
W_1(\nu,\widetilde\nu)=\inf_{\pi\in\Pi(\nu,\widetilde\nu)}\int |x-x'|\,d\pi(x,x'),
\]
where \(\Pi(\nu,\widetilde\nu)\) is the set of probability measures with marginals \(\nu\) and \(\widetilde\nu\). Continuity of probability-measure-valued curves below is with respect to \(W_1\).

Let \(P_0\in\mathcal P_1(\mathbb R^d)\), let \(\gamma_\tau=N(0,\tau I_d)\), and put \(f_0=\gamma_\tau*P_0\). For a Borel probability measure \(\nu\), define the Gaussian posterior-mean map
\[
m_\nu^\tau(y)=\frac{\int x\exp(-|y-x|^2/(2\tau))\,d\nu(x)}{\int \exp(-|y-x|^2/(2\tau))\,d\nu(x)}.
\]
For \(\beta>0\), let \(G_\beta=N(0,\beta^{-1}I_d)\), \(K_\beta(y,x)=\exp(-\beta|y-x|^2/2)\), and define
\[
F_{\beta,\nu}(y)=\frac{\int xK_\beta(y,x)\,d\nu(x)}{\int K_\beta(y,x)\,d\nu(x)},\qquad b_{\beta,\nu}(y)=F_{\beta,\nu}(y)-y.
\]

For \(T>0\), a finite-action weak flow on \([0,T]\) is a curve \(\mu\in C([0,T];\mathcal P_1(\mathbb R^d))\) such that
\[
\int_0^T\!\int |b_{\beta,\mu_s}(x)|\,d\mu_s(x)\,ds<\infty
\]
and, for every \(\varphi\in C_c^1(\mathbb R^d)\) and every \(t\in[0,T]\),
\[
\int\varphi\,d\mu_t-\int\varphi\,d\mu_0
=\int_0^t\!\int\nabla\varphi(x)\cdot b_{\beta,\mu_s}(x)\,d\mu_s(x)\,ds.
\]
Here \(C_c^1(\mathbb R^d)\) denotes the continuously differentiable real functions with compact support.

For \(R>0\), set \(B_R=\{x:|x|\le R\}\) and define the normalized restriction
\[
f_0^{[R]}(A)=\frac{f_0(A\cap B_R)}{f_0(B_R)}
\]
for Borel sets \(A\). Put \(T_\beta=\beta\tau/2\). Denote by \(\mu^{\beta,[R]}\) the compact-support flow on \([0,T_\beta]\) for the above weak equation, with initial law \(f_0^{[R]}\) and with every time marginal supported in \(B_R\).

Define \(\mathcal A_\tau\subseteq\mathcal P_1(\mathbb R^d)\) as follows. A prior \(P_0\) belongs to \(\mathcal A_\tau\) if there is a family \((\mu^\beta)_{\beta>0}\) such that, for every \(\beta>0\), \(\mu^\beta\) is a finite-action weak flow on \([0,T_\beta]\) with initial law \(f_0\),
\[
\lim_{R\to\infty}\sup_{0\le t\le T_\beta}W_1(\mu_t^{\beta,[R]},\mu_t^\beta)=0,
\]
and the same family satisfies
\[
\lim_{\beta\to\infty}W_1(\mu_{T_\beta}^\beta,P_0)=0.
\]

For each positive integer \(N\) and each \(R,\beta>0\), sample \(X_1(0),\ldots,X_N(0)\) independently with common law \(f_0^{[R]}\). Set \(\mu_t^{N,R}=N^{-1}\sum_{i=1}^N\delta_{X_i(t)}\), suppressing its dependence on \(\beta\), and evolve
\[
\dot X_i(t)=b_{\beta,\mu_t^{N,R}}(X_i(t)),\qquad i=1,\ldots,N,\quad 0\le t\le T_\beta.
\]
The initial sample is the only randomness in this construction.

## Task

Prove that for every \(P_0\in\mathcal A_\tau\) and every \(0\le M<\infty\),
\[
\lim_{\beta\to\infty}\limsup_{R\to\infty}\limsup_{N\to\infty}
\mathbb E\!\left[\sup_{|y|\le M}\left|m_{\mu_{T_\beta}^{N,R}}^\tau(y)-m_{P_0}^\tau(y)\right|\right]=0.
\]
Moreover, for every \(\varepsilon>0\), prove
\[
\lim_{\beta\to\infty}\limsup_{R\to\infty}\limsup_{N\to\infty}
\mathbb P\!\left(\sup_{|y|\le M}\left|m_{\mu_{T_\beta}^{N,R}}^\tau(y)-m_{P_0}^\tau(y)\right|>\varepsilon\right)=0.
\]
The order is \(N\to\infty\) at fixed \((\beta,R)\), then \(R\to\infty\) at fixed \(\beta\), and finally \(\beta\to\infty\). Here \(m_{P_0}^\tau(y)\) is the continuous version of \(\mathbb E[X\mid X+Z=y]\), for independent \(X\sim P_0\) and \(Z\sim N(0,\tau I_d)\).
