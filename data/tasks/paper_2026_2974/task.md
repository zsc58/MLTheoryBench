# Problem

## Setup

Fix integers \(d\ge1\) and \(T\ge1\). Let \(f:\mathbb R^d\to\mathbb R\) be differentiable, nonconvex in general, and satisfy \(f_*:=\inf_x f(x)>-\infty\). Let \(\ell\in(0,\infty)^d\) and assume that, for all \(x,y\in\mathbb R^d\),
\[
|f(x)-f(y)-\langle\nabla f(y),x-y\rangle|\le \tfrac12\|x-y\|_{\ell}^2,
\qquad \|u\|_{\ell}^2:=\sum_{i=1}^d\ell_i u_i^2.
\]
Fix \(p\in(4/3,2]\), set \(\bar p=p/(p-1)\), and fix a deterministic initial point \(x_1\in\mathbb R^d\). Let \(z_t\) be the stochastic vector queried at \(x_t\), and let \(\mathcal F_t=\sigma(z_1,\ldots,z_t)\), with \(\mathcal F_0\) trivial. Write \(\mathbb E_{t-1}[\cdot]=\mathbb E[\cdot\mid\mathcal F_{t-1}]\). For each \(t\), assume almost surely that
\[
\mathbb E_{t-1}[z_t]=\nabla f(x_t),
\qquad \mathbb E_{t-1}|z_{t,i}-\nabla_i f(x_t)|^p\le s_i^p
\]
for every coordinate \(i\), where \(s\in[0,\infty)^d\) is fixed. For fixed parameters \(\eta>0\) and \(\rho>0\), standard AdaGrad is
\[
v_0=0,\qquad v_t=v_{t-1}+z_t^2,\qquad
x_{t+1,i}=x_{t,i}-\frac{\eta z_{t,i}}{\rho+\sqrt{v_{t,i}}},
\]
with all vector operations coordinatewise. In particular, \(x_t\) is \(\mathcal F_{t-1}\)-measurable. Write \(\Delta=f(x_1)-f_*\), \(\|s\|_1=\sum_i s_i\), \(\|s\|_\infty=\max_i s_i\), and analogously for \(\ell\). Define
\[
K_T:=1+\frac{\sqrt2\|s\|_\infty T^{1/p}+2\|\nabla f(x_1)\|_\infty T^{1/2}+2\eta\sqrt{\|\ell\|_1\|\ell\|_\infty}\,T^{3/2}}{\rho}.
\]

## Task

Prove that there is a constant \(C_p\), depending only on \(p\), such that
\[
\mathbb E\!\left[\frac1T\sum_{t=1}^T\|\nabla f(x_t)\|_1\right]
\le C_p\Bigg(
\frac{d\rho+\Delta/\eta+\eta\|\ell\|_1\ln K_T}{\sqrt T}
+\frac{\|s\|_1\ln^{1/\bar p+1/2}(K_T)}{T^{(p-1)/p}}
+\frac{\sqrt{(\Delta/\eta+\eta\|\ell\|_1\ln K_T)\|s\|_1}}{T^{(p-1)/(2p)}}
+\frac{\|s\|_1\ln^{1/(2\bar p)+1/4}(K_T)}{T^{(3p-4)/(4p)}}
\Bigg).
\]
