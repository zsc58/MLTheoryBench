# Problem

## Setup

Let \(d\ge1\), \(T>0\), and let \(\beta:[0,T]\to[0,\infty)\) be nondecreasing and integrable. Fix \(\alpha\ge0\). Let \(B\) be a standard \(d\)-dimensional Brownian motion, independent of \(X_0\), and let
\[
dX_t=-\alpha\beta_tX_t\,dt+\sqrt{2\beta_t}\,dB_t.
\]
Assume that \(X_0\) has a strictly positive \(C^2\) density \(p_0\). Write \(p_t\) for the density of \(X_t\), \(\pi_0\) for its initial law, and \(S_t=\nabla\log p_t\). Put \(\bar\beta_u=\beta_{T-u}\). Let \(Q_{t|s}\), \(0\le s\le t\le T\), be the transition kernels of the reverse diffusion with drift
\[
\alpha\bar\beta_u x+2\bar\beta_u S_{T-u}(x)
\]
and diffusion coefficient \(\sqrt{2\bar\beta_u}I_d\). This reverse process is initialized at reverse time zero with law \(p_T\). Thus its law at reverse time \(T\) is \(\pi_0\); denote this law by \(\pi_{\mathrm{data}}=p_TQ_{T|0}=\pi_0\).

Choose a finite grid \(0=t_0<\cdots<t_N=T\), with \(N\ge1\), satisfying
\[
\Delta_k:=\int_{t_{k-1}}^{t_k}\bar\beta_u\,du>0
\qquad(k=1,\ldots,N),
\]
and put \(I_T=\int_0^T\beta_u\,du\). For \(\ell\ge2\), let \(V_\ell(x)=\|x\|^\ell\). For probability measures \(\mu,\nu\) on \(\mathbb R^d\), define the possibly extended-valued distance
\[
\rho_b(\mu,\nu)=\int_{\mathbb R^d}(1+bV_2(x))\,|\mu-\nu|(dx),\qquad b>0,
\]
where \(|\mu-\nu|\) is the total variation measure of the signed measure \(\mu-\nu\).

Assume there are \(\gamma_0>\alpha/2\), \(\kappa_0\ge0\), \(C_0>0\), and \(p\ge1\) such that, for every \(x\in\mathbb R^d\),
\[
\langle S_0(x),x\rangle\le-\gamma_0\|x\|^2+\kappa_0,
\qquad
\|\nabla S_0(x)\|_F\le C_0(1+\|x\|^p).
\]

Define
\[
\pi_\infty=
\begin{cases}
N(0,2I_T I_d),&\alpha=0,\\
N(0,\alpha^{-1}I_d),&\alpha>0.
\end{cases}
\]
Let \(s_\theta:\mathbb R^d\times(0,T]\to\mathbb R^d\) be a fixed Borel measurable learned score. Let \(\xi_1,\ldots,\xi_N\) be independent standard Gaussian vectors, independent of \(\bar X_{t_0}\sim\pi_\infty\). Define
\[
\bar X_{t_k}=\bar X_{t_{k-1}}+
\Delta_k\bigl(\alpha\bar X_{t_{k-1}}+
2s_\theta(\bar X_{t_{k-1}},T-t_{k-1})\bigr)
+\sqrt{2\Delta_k}\,\xi_k.
\]
Let \(Q_k^\theta\) be its one-step transition kernel. Set \(Q_{0:0}^\theta\) equal to the identity kernel and let \(Q_{0:k}^\theta\) apply \(Q_1^\theta,\ldots,Q_k^\theta\) successively in that order. Write
\[
\hat\pi_k^\theta=\pi_\infty Q_{0:k}^\theta,
\qquad
E_j(x)=S_{T-t_j}(x)-s_\theta(x,T-t_j),
\quad j=0,\ldots,N-1.
\]
For a vector-valued measurable function \(f\), use
\(\|f\|_{L^2(\mu)}=(\int\|f(x)\|^2\mu(dx))^{1/2}\), and write
\(\|X_0\|_{L^2}=(\mathbb E\|X_0\|^2)^{1/2}\).

Assume
\[
M:=\sup_{0\le k\le N}\mathbb E[V_{4p+4}(\bar X_{t_k})]<\infty.
\]
In the case \(\alpha>0\), also assume \(\mathrm{KL}(\pi_0\|\pi_\infty)<\infty\), where
\(\mathrm{KL}(\mu\|\nu)=\int\log(d\mu/d\nu)\,d\mu\) when \(\mu\ll\nu\), and is \(+\infty\) otherwise. Let \(X_\infty\sim\pi_\infty\).

## Task

Prove that there exist \(b>0\), \(\bar\alpha\in(0,1)\), and finite nonnegative constants \(C_{k-1}^{\mathrm{discr}},C_{k-1}^{\mathrm{net}}\), \(k=1,\ldots,N\), such that
\[
\rho_b(\pi_{\mathrm{data}},\hat\pi_N^\theta)
\le \bar\alpha^N\Lambda(T)C^{\mathrm{mix}}
+\sum_{k=1}^N\bar\alpha^{N-k}
\left[
\Delta_k C_{k-1}^{\mathrm{discr}}
+\sqrt{\Delta_k}\,C_{k-1}^{\mathrm{net}}
\|E_{k-1}\|_{L^2(\hat\pi_{k-1}^\theta)}
\right],
\]
where
\[
C^{\mathrm{mix}}=
\sqrt2+b\sqrt{2\left(
\mathbb E[V_2(X_T)^2]+\mathbb E[V_2(X_\infty)^2]
\right)},
\]
and
\[
\Lambda(T)=
\begin{cases}
\displaystyle\frac{\|X_0\|_{L^2}}{2\sqrt{I_T}},&\alpha=0,\\[6pt]
\displaystyle\sqrt{\mathrm{KL}(\pi_0\|\pi_\infty)}\,e^{-\alpha I_T},&\alpha>0.
\end{cases}
\]
The constants \(b,\bar\alpha\) may depend on \(d,T,\alpha,\beta,\gamma_0,\kappa_0\) and the fixed grid, but not on the learned score. The discretization and network coefficients may additionally depend on \(C_0,p,M\), and may depend on the learned score only through the displayed moment bound \(M\).

Prove also that the same \(b,\bar\alpha\) satisfy, for every grid step and every pair of probability measures,
\[
\rho_b(\mu Q_{t_k|t_{k-1}},\nu Q_{t_k|t_{k-1}})
\le\bar\alpha\rho_b(\mu,\nu),
\]
and that each exact grid kernel has a positive minorization on every bounded ball: for each \(k\) and \(r>0\), there are \(\varepsilon_{k,r}>0\) and a probability measure \(\nu_{k,r}\) such that
\[
Q_{t_k|t_{k-1}}(x,A)\ge\varepsilon_{k,r}\nu_{k,r}(A)
\]
for every \(\|x\|\le r\) and every Borel set \(A\).

The consequences
\[
\|\mu-\nu\|_{\mathrm{TV}}\le\rho_b(\mu,\nu)/2,
\qquad
W_2^2(\mu,\nu)\le2\rho_b(\mu,\nu)/b
\]
may be stated for probability measures with finite second moments. Here \(\|\mu-\nu\|_{\mathrm{TV}}=\tfrac12|\mu-\nu|(\mathbb R^d)\), and \(W_2^2\) is the infimum of \(\int\|x-y\|^2\,d\eta(x,y)\) over couplings \(\eta\) of \(\mu,\nu\).
