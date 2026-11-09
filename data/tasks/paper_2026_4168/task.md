# Problem

## Setup

For each integer $T\geq2$, consider a Gaussian diffusion with timesteps $1,\ldots,T$, and let $I_T=\{2,\ldots,T\}$. Write $\nu_T$ for the law of its conditioning variables $(y_0,\ldots,y_T)$ and $\nu_{T,t}$ for the $(y_0,y_t)$-marginal. For each $t\in I_T$, conditional on $(y_0,y_t)$, the forward posterior and learned reverse kernel for $y_{t-1}$ are
\[
q_t(\cdot\mid y_0,y_t)=\mathcal N(\widetilde\mu_t,\Sigma_t),\qquad
p_t(\cdot\mid y_t)=\mathcal N(\mu_{\theta,t},\Sigma_t),
\]
where the means are measurable functions of the indicated conditioning variables, $\Sigma_t$ is positive definite, and the covariances match. The Gaussian parameterization satisfies
\[
m_t:=\tfrac12\|\Sigma_t^{-1/2}(\widetilde\mu_t-\mu_{\theta,t})\|^2
      =w_t\|\varepsilon(y_0,y_t)-\varepsilon_\theta(y_t,t)\|^2,
\]
where $\varepsilon$ and $\varepsilon_\theta$ are the prescribed measurable noise target and noise predictor, and $w_t$ are the prescribed finite deterministic nonnegative DDPM weights.

For probability measures $P\ll Q$, define
\[
D_G(P\|Q)=\mathbb E_Q\!\left[G\!\left(\frac{dP}{dQ}-1\right)\right],
\]
where $G:[-1,\infty)\to\mathbb R$ is a fixed convex function, $G(0)=0$, $G'(0)=0$, $G''(0)=1$, and $G$ is $C^3$ on a neighborhood of $0$.

Consider an auxiliary joint construction that retains the law $\nu_T$ of the conditioning variables and introduces additional local evaluation variables $v_t$ for $t\in I_T$. Require
\[
\mathcal L(v_t\mid y_0,y_t)=p_t(\cdot\mid y_t).
\]
These local evaluation variables are distinct from the coordinates of the forward trajectory. No independence across timesteps is assumed beyond the conditions below. Let
\[
r_t=\frac{q_t(v_t\mid y_0,y_t)}{p_t(v_t\mid y_t)},\quad
\delta_t=r_t-1,\quad R_T=\prod_{t\in I_T}(1+\delta_t),\quad
S_T=\sum_{t\in I_T}\delta_t,\quad B_T=R_T-1-S_T.
\]
Write $\mathbb E_{\mathrm{loc}}$ for expectation under this auxiliary construction. All unmarked expectations below use this same law; for functions of $(y_0,y_t)$ alone, they therefore equal expectation under $\nu_{T,t}$.

For $m\geq0$, let $U_m=\exp(\sqrt{2m}Z-m)$ for $Z\sim N(0,1)$, and define
\[
h_G(m)=\mathbb E_Z[G(U_m-1)],\qquad
L_G=\sum_{t\in I_T}\mathbb E_{\nu_{T,t}}[h_G(m_t)],\qquad
a_T=\sum_{t\in I_T}\mathbb E_{\nu_{T,t}}[m_t].
\]
The defining divergence and $h_G$ integrals are allowed to be extended-valued; the asymptotic assumptions below concern their indicated expectations.

Assume $0<a_T<\infty$ and $\delta_t\geq-1$ for $t\in I_T$. As $T\to\infty$, assume: $a_T\to0$; almost surely $\max_{t\in I_T}m_t\leq c_T$ for deterministic $c_T\to0$; $\sum_{t\in I_T}\mathbb E[m_t^2]=o(a_T)$ and $\sum_{t\in I_T}\mathbb E[m_t^{3/2}]=o(a_T)$; for distinct $s,t\in I_T$, $\mathbb E[\delta_s\delta_t]=0$; and
\[
\mathbb E|S_T|^3=o(a_T),\quad
\mathbb E|S_TB_T|=o(a_T),\quad
\mathbb E[B_T^2]=o(a_T),\quad
\mathbb E|B_T|^3=o(a_T).
\]
Finally, for every fixed $\eta>0$, require the tail conditions
\[
\mathbb E\!\left[|G(S_T+B_T)|\mathbf 1_{\{|S_T+B_T|>\eta\}}\right]=o(a_T),
\quad
\sum_{t\in I_T}\mathbb E\!\left[|G(\delta_t)|\mathbf 1_{\{|\delta_t|>\eta\}}\right]=o(a_T).
\]

## Task

Prove that
\[
\mathbb E_{\mathrm{loc}}\!\left[G(R_T-1)\right]
=\sum_{t\in I_T}\mathbb E_{\nu_{T,t}}[h_G(m_t)]+o(a_T)
=L_G+o(a_T)
\qquad (T\to\infty).
\]
