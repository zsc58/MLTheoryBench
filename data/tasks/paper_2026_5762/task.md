# Problem

## Setup

Let \(n\ge2\), \(1\le k<n\), and \(0<R<\infty\). Define
\[
\mathcal E=\{\{a,b\}:1\le a<b\le n\},\qquad
\overrightarrow{\mathcal E}=\{(i,j):1\le i,j\le n,\ i\ne j\}.
\]
For each \(e=\{a,b\}\in\mathcal E\), fix the canonical orientation \(a(e)=a<b=b(e)\) and write \(x_e=e_a-e_b\), where \(e_i\) is the \(i\)-th standard basis vector. The unknown vector belongs to
\[
\mathcal K=\left\{v\in\mathbb R^n:\sum_i v_i=0,\ \|v\|_\infty\le R\right\}.
\]
For a nonempty finite set \(D\), let \(\Delta_D\) denote the probability simplex on \(D\).

Let \((P_z)_{z\in\mathbb R}\) be an exponential family on a measurable observation space with densities
\[
\frac{dP_z}{d\nu}(y)=\exp\{zT(y)-\psi(z)\}
\]
relative to a fixed measure \(\nu\), where \(T\) is a real-valued measurable sufficient statistic. The family is defined for every real \(z\). Assume \(\psi\in C^2(\mathbb R)\) and that, for finite constants \(\bar\sigma^2\) and \(\underline a>0\),
\[
0<\psi''(z)\le\bar\sigma^2\quad(z\in\mathbb R),
\qquad
\psi''(z)\ge\underline a\quad(|z|\le2R).
\]
Assume also that there is a finite \(\sigma_{\rm sg}>0\) such that
\[
\mathbb E_{P_z}\exp\{a(T(Y)-\psi'(z))\}
\le\exp(\sigma_{\rm sg}^2a^2/2)
\quad\text{for all }|z|\le2R\text{ and }a\in\mathbb R.
\]

Let \(\mathcal F_t\) be the complete algorithm history through round \(t\), including its auxiliary random draws. At round \(t\), the selected pair \(A_t\in\mathcal E\) is \(\mathcal F_{t-1}\)-measurable. Conditional on this history and \(A_t=e\), the observation \(Y_t\) has law \(P_{x_e^Tv}\). Each auxiliary draw specified below uses fresh randomization: conditional on the history available just before the draw, it has the specified distribution. These randomization kernels do not depend on the unknown parameter.

For every \(z\in\mathcal K\), order indices by decreasing \(z_i\), breaking ties by increasing index. Let \(S(z)\) be the first \(k\) indices and define
\[
\mathcal C(z)=\{(i,j):i\in S(z),\ j\notin S(z)\}\subseteq\overrightarrow{\mathcal E}.
\]
Fix \(v\) in the relative interior of \(\mathcal K\) in the subspace \(\{z:\sum_i z_i=0\}\), and suppose its \(k\)-th largest coordinate is strictly larger than its \((k+1)\)-st largest coordinate.

For every \(e=\{a,b\}\in\mathcal E\), with \(a<b\), and \(v,v'\in\mathcal K\), define
\[
d_e(v,v')=\operatorname{KL}(P_{v_a-v_b},P_{v'_a-v'_b}).
\]
For \((i,j)\in\mathcal C(v)\), let
\[
\mathcal K_{ij}=\{v'\in\mathcal K:v'_i\le v'_j\}.
\]
For \(w\in\Delta_{\mathcal E}\), set
\[
D_w(v,v')=\sum_{e\in\mathcal E}w_e d_e(v,v'),\qquad
 g_{ij}(w;v)=\inf_{v'\in\mathcal K_{ij}}D_w(v,v'),
\]
\[
F_v(w,q)=\sum_{(i,j)\in\mathcal C(v)}q_{ij}g_{ij}(w;v),
\qquad
\mathcal I^*(v)=\max_{w\in\Delta_{\mathcal E}}\min_{q\in\Delta_{\mathcal C(v)}}F_v(w,q).
\]

## Procedure

Fix \(\alpha,\gamma\in(0,1)\) and \(\lambda>0\), independently of the risk level \(\delta\). Define
\[
\ell_t(u)=\sum_{s=1}^t\{(u_{a(A_s)}-u_{b(A_s)})T(Y_s)-\psi(u_{a(A_s)}-u_{b(A_s)})\},
\]
\[
N_e(t)=\sum_{s=1}^t\mathbf1\{A_s=e\}.
\]
Let \(M_t=\arg\max_{u\in\mathcal K}\ell_t(u)\), and choose \(\widehat v_t\) as the lexicographically smallest element of \(M_t\). Initialize \(w_1\) uniformly on \(\mathcal E\), initialize \(r_1\) uniformly on \(\mathcal E\), and set \(\Psi^{(w)}_0=\Psi^{(q)}_0=0\) on \(\mathcal E\). Put \(N_e(0)=0\).

At round \(t\), set
\[
\eta_{t+1}=(t+1)^{-\alpha},\qquad \rho_t=t^{-\gamma},\qquad
\widetilde w_t=(1-\rho_t)w_t+\rho_t u,
\]
where \(u\) is uniform on \(\mathcal E\). Choose \(A_t\) among the pairs maximizing
\[
\sum_{s=1}^{t}\widetilde w_{s,e}-N_e(t-1),
\]
with deterministic tie-breaking, and observe \(Y_t\). Compute \(\widehat v_t\), put \(\widehat{\mathcal C}_t=\mathcal C(\widehat v_t)\), and for each \((i,j)\in\widehat{\mathcal C}_t\) define
\[
Z_{ij}(t)=\ell_t(\widehat v_t)-\sup_{z\in\mathcal K:z_i\le z_j}\ell_t(z).
\]
Let
\[
b(t,\delta)=\log(1/\delta)+\frac\lambda2\|\widehat v_t\|_2^2+
\frac12\log\det\!\left(I_n+\frac{\bar\sigma^2}{\lambda}L_t\right),
\qquad
L_t=\sum_{s=1}^t x_{A_s}x_{A_s}^{\mathsf T}.
\]
Stop at the first \(t\) for which
\[
Z_{ij}(t)\ge b(t,\delta)\quad\text{for every }(i,j)\in\widehat{\mathcal C}_t,
\]
and output \(S(\widehat v_t)\).

If the procedure has not stopped, define a distribution on the current oriented boundary by
\[
q_{t,ij}=\frac{r_{t,\{i,j\}}}{\displaystyle\sum_{(a,b)\in\widehat{\mathcal C}_t}r_{t,\{a,b\}}}
\quad((i,j)\in\widehat{\mathcal C}_t).
\]
Conditional on the complete history after \(Y_t\) and before this auxiliary draw, draw \(J_t\) uniformly from \(\widehat{\mathcal C}_t\). Write \(J_t=(J_t^+,J_t^-)\), and choose
\[
v_t^*\in\arg\min_{z\in\mathcal K:z_{J_t^+}\le z_{J_t^-}}D_{w_t}(\widehat v_t,z),
\qquad
h_t=D_{w_t}(\widehat v_t,v_t^*).
\]
With \(m=k(n-k)\), define scores on \(\mathcal E\) by
\[
g^{(w)}_{t,e}=m q_{t,J_t}d_e(\widehat v_t,v_t^*),
\qquad
g^{(q)}_{t,e}=m h_t\mathbf1\{e=\{J_t^+,J_t^-\}\}.
\]
Update
\[
\Psi^{(w)}_t=\Psi^{(w)}_{t-1}+g^{(w)}_t,
\qquad
\Psi^{(q)}_t=\Psi^{(q)}_{t-1}+g^{(q)}_t,
\]
\[
w_{t+1,e}=\frac{w_{1,e}\exp(\eta_{t+1}\Psi^{(w)}_{t,e})}
{\sum_{f\in\mathcal E}w_{1,f}\exp(\eta_{t+1}\Psi^{(w)}_{t,f})},
\qquad
r_{t+1,e}=r_{1,e}\exp(-\eta_{t+1}\Psi^{(q)}_{t,e}).
\]
The stopping time is denoted by \(\tau_\delta\).

## Task

Prove that, for every \(\delta\in(0,1)\),
\[
\Pr_v(\tau_\delta<\infty)=1,
\qquad
\Pr_v\bigl(\tau_\delta<\infty,\ S(\widehat v_{\tau_\delta})\ne S(v)\bigr)\le\delta.
\]
Moreover, prove
\[
\lim_{\delta\downarrow0}\frac{\mathbb E_v[\tau_\delta]}{\log(1/\delta)}
=\frac1{\mathcal I^*(v)}.
\]
