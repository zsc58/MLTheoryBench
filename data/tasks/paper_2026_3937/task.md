# Problem

## Setup

There are \(K\ge 2\) alternatives, indexed by \(\{1,\ldots,K\}\). Observations are drawn independently, and alternative \(i\) has density or mass function from the one-parameter exponential family
\[
f_i(y;\theta_i)=\exp\{y\theta_i-A_i(\theta_i)+c_i(y)\}.
\]
Let \(\Theta_i\subseteq\mathbb R\) be its natural-parameter domain. The true parameter \(\theta_i\) and all optimization parameters for alternative \(i\) lie in \(\operatorname{int}\Theta_i\), where \(A_i\) is twice continuously differentiable with \(A_i''>0\). Let \(\mu_i=A_i'(\theta_i)\), and assume that the true best alternative \(b\) is unique: \(\mu_b>\mu_j\) for every \(j\ne b\).

A static allocation is \(p\in\Delta^{K-1}=\{p\in[0,\infty)^K:\sum_i p_i=1\}\). For \(v\in\operatorname{int}\Theta_i\), define
\[
D_i(v;\theta_i)=A_i(\theta_i)-A_i(v)-A_i'(v)(\theta_i-v).
\]
For each allocation \(p\) and challenger \(j\ne b\), assume the constrained minimum
\[
\inf_{\substack{v\in\prod_{i=1}^K\operatorname{int}\Theta_i\\A_b'(v_b)\le A_j'(v_j)}}
\sum_{i=1}^K p_iD_i(v_i;\theta_i)
\]
is finite and attained, and let \(v^j\) denote any minimizer. Define its value by
\[
C_{b,j}(p)=\inf_{\substack{v\in\prod_{i=1}^K\operatorname{int}\Theta_i\\A_b'(v_b)\le A_j'(v_j)}}\sum_{i=1}^Kp_iD_i(v_i;\theta_i).
\]
Assume each \(C_{b,j}:\Delta^{K-1}\to\mathbb R\) is continuous, and that
\[
m(p)=\min_{j\ne b}C_{b,j}(p)
\]
has a unique maximizer \(p^\star\) on \(\Delta^{K-1}\). This \(p^\star\) is the large-deviation-optimal allocation.

For every \(t>0\), let \(\rho_{j,t}>0\) be independent of \(p\), define
\[
F_t(p)=-\frac1t\log\left(\sum_{j\ne b}\rho_{j,t}e^{-tC_{b,j}(p)}\right),
\]
and set \(L_t=\max_{j\ne b}|\log\rho_{j,t}|\). Assume \(L_t=o(t)\) as \(t\to\infty\).

## Task

Prove that
\[
\sup_{p\in\Delta^{K-1}}|F_t(p)-m(p)|\longrightarrow 0
\quad\text{as }t\to\infty,
\]
and that for every choice \(p_t\in\operatorname*{arg\,max}_{p\in\Delta^{K-1}}F_t(p)\), one has
\[
p_t\longrightarrow p^\star.
\]
