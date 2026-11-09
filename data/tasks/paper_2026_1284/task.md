# Problem

## Setup

Let \(S=\mathbb R^d\). Let \(\pi\) be a target probability distribution with Lebesgue density \(\rho\), and let \(q:S\times S\to(0,\infty)\) be a continuous transition density for the prescribed transition kernel. Assume detailed balance:
\[
\rho(x)q(x,y)=\rho(y)q(y,x)\quad\text{for all }x,y\in S.
\]
For each parameter \(\theta\), the generator induces a probability law \(\nu_\theta\) having Lebesgue density \(f_\theta\). Its forward transition-pair law is
\[
\mu_\theta(dx,dy)=\nu_\theta(dx)q(x,y)\,dy,
\]
and its reverse law \(\mu_\theta^\leftarrow\) is the image of \(\mu_\theta\) under \((x,y)\mapsto(y,x)\). Let \(\kappa\) be a continuous integrally strictly positive definite kernel on \(S^2\) whose RKHS is contained in \(C_0(S^2)\), and define
\[
L(\theta)=\operatorname{MMD}_\kappa^2(\mu_\theta,\mu_\theta^\leftarrow).
\]
Consider a sequence \(\theta_l\) such that the generated laws \(\nu_l:=\nu_{\theta_l}\) form a tight family and \(L(\theta_l)\to0\).

## Task

Prove that \(\nu_l\) converges weakly to \(\pi\); equivalently, for every bounded continuous \(u:S\to\mathbb R\),
\[
\int_S u\,d\nu_l\longrightarrow\int_S u\,d\pi.
\]
