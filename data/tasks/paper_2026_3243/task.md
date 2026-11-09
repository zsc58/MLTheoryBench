# Problem

## Setup

Let \(n\ge1\) and let \(E\subseteq\mathbb R^n\) be a measurable finite-dimensional process space with prior density \(p(f)\) relative to Lebesgue measure restricted to \(E\). Let \(L:E\to[0,\infty)\) be measurable and assume
\[
0<Z:=\int_E L(f)p(f)\,df<\infty,
\qquad \pi(f\mid C):=\frac{L(f)p(f)}{Z}.
\]

Assume there are an integer \(d\ge1\), a measurable map \(T:\mathbb R^d\to E\), and the standard Gaussian density \(r\) on \(\mathbb R^d\) such that \(T_\#(r(\xi)\,d\xi)=p(f)\,df\). Define
\[
\Lambda(\xi):=L(T(\xi)),\qquad \rho_0(\xi):=\frac{\Lambda(\xi)r(\xi)}{Z}.
\]

Let \(\beta:[0,1)\to(0,\infty)\) be locally integrable. For \(0\le t<1\), set \(B(t)=\int_0^t\beta(s)\,ds\), \(\alpha(t)=e^{-B(t)/2}\), and \(\sigma(t)=\sqrt{1-\alpha(t)^2}\). Let \(\xi_0\sim\rho_0\) and let \(\varepsilon\sim N(0,I_d)\) be independent. For each \(0\le t<1\), set
\[
\xi_t:=\alpha(t)\xi_0+\sigma(t)\varepsilon,
\]
and denote its density by \(\rho_t\). For \(0<t<1\), define
\[
\psi(t,u):=\mathbb E_\varepsilon[\Lambda(\alpha(t)u+\sigma(t)\varepsilon)],
\qquad g(t,u):=\nabla_u\log\psi(t,u).
\]

On every compact interval \([a,b]\subset(0,1)\), assume \(\rho_t(u)>0\) for all \((t,u)\in[a,b]\times\mathbb R^d\) and that \((t,u)\mapsto\nabla_u\log\rho_t(u)\) is defined and jointly measurable. Assume the reverse SDE below, initialized with density \(\rho_b\), admits a continuous weak solution unique in law on \([0,b-a]\), and that its associated Fokker--Planck equation has a unique density-valued weak solution with that initial density.

## Task

Fix \(0<t_0<t_1<1\), write \(\tau_s=t_1-s\), and initialize \(\bar\xi_0\sim\rho_{t_1}\) independently of a standard \(d\)-dimensional Brownian motion \(\bar W\). Prove that the solution of
\[
 d\bar\xi_s=\left[\beta(\tau_s)g(\tau_s,\bar\xi_s)-\tfrac12\beta(\tau_s)\bar\xi_s\right]ds
 +\sqrt{\beta(\tau_s)}\,d\bar W_s
\]
has law \(\bar\xi_s\sim\rho_{\tau_s}\) for every \(s\in[0,t_1-t_0]\). If the SDE is well posed with continuous paths through \(s=t_1\), with its coefficients interpreted for \(s<t_1\), prove that \(\bar\xi_{t_1}\sim\rho_0\) and that \(T(\bar\xi_{t_1})\) has density \(\pi(\cdot\mid C)\) on \(E\).
