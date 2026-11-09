# Problem

## Setup

Let \(\mu_0=e^{-V_0}\) and \(\pi=e^{-V_\pi}\) be strictly positive probability densities on \(\mathbb R^d\), where \(V_0,V_\pi\in C^1(\mathbb R^d)\), and assume both densities have finite second moments. Assume their density ratio has quadratic-exponential control: for some finite constants \(c_0,c_1\ge0\),
\[
\left|\log\frac{\mu_0(x)}{\pi(x)}\right|\le c_0+c_1\|x\|^2
\quad\text{for a.e. }x.
\]
Let \(\lambda:[0,\infty)\to[0,1]\) be fixed in advance, nondecreasing, and weakly differentiable, using its locally absolutely continuous representative. Define
\[
\pi_t(x)=\frac{\pi(x)^{\lambda_t}\mu_0(x)^{1-\lambda_t}}{\int \pi(y)^{\lambda_t}\mu_0(y)^{1-\lambda_t}\,dy}.
\]
For \(\alpha\in[0,1]\), set
\[
\rho_\alpha(x)=\frac{\mu_0(x)^{1-\alpha}\pi(x)^\alpha}{\int \mu_0(y)^{1-\alpha}\pi(y)^\alpha\,dy}.
\]
For probability densities \(p,q\), write
\[
D(p\|q)=\int p(x)\log\frac{p(x)}{q(x)}\,dx
\]
for their Kullback–Leibler divergence. For a density \(r\) and a function \(g\) with \(\int |g|r<\infty\), define
\[
\operatorname{Var}_r(g)=\int\left(g(x)-\int g(y)r(y)\,dy\right)^2r(x)\,dx\in[0,\infty].
\]

The normalized Fisher–Rao flow with target density \(q_t\) is the positive probability-density solution of
\[
\partial_t\rho_t(x)=\rho_t(x)\left(\log\frac{q_t(x)}{\rho_t(x)}-\int \rho_t(y)\log\frac{q_t(y)}{\rho_t(y)}\,dy\right),
\qquad \rho_{t=0}=\mu_0.
\]
The equation is understood for almost every time and spatial point, with \(t\mapsto\log\rho_t(x)\) locally absolutely continuous for almost every \(x\), and with
\[
t\mapsto\int\rho_t(x)\left|\log\frac{q_t(x)}{\rho_t(x)}\right|\,dx
\]
locally integrable in time. Let \(\mu_t^{\mathrm{T-FR}}\) denote this flow with \(q_t=\pi_t\), and let \(\mu_t^{\mathrm{FR}}\) denote the flow with the fixed target \(q_t=\pi\).

## Task

Prove that for every \(t\ge0\),
\[
D(\mu_t^{\mathrm{FR}}\|\pi)-D(\mu_t^{\mathrm{T-FR}}\|\pi)
= -\int_{\alpha_T(t)}^{\alpha_S(t)}(1-u)\,\operatorname{Var}_{\rho_u}\!\left(\log\frac{\mu_0}{\pi}\right)\,du\le0,
\]
where
\[
\alpha_T(t)=\int_0^t e^{-(t-s)}\lambda_s\,ds,
\qquad \alpha_S(t)=1-e^{-t}.
\]
The integral is a Lebesgue integral in \(u\), with value zero when its endpoints coincide.

In particular, the standard Fisher–Rao flow has KL divergence to \(\pi\) no larger than that of the geometrically tempered flow at every time.
