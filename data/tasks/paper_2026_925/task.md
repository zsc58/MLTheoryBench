# Problem

## Setup

Fix a dimension \(d\ge1\), times \(0<t_0<T<\infty\), and \(\alpha\in(0,1]\). Let \(p_{\mathrm{data}}\) be a probability density on \(\mathbb R^d\). At generation \(i\ge0\), let
\[
q_i=\alpha p_{\mathrm{data}}+(1-\alpha)\widehat p^i,
\qquad \widehat p^0=p_{\mathrm{data}},
\]
where each \(\widehat p^i\) is a probability density absolutely continuous with respect to \(p_{\mathrm{data}}\).

The following continuous-time sampling model uses a common initialization for the ideal and learned processes. Write \(L=T-t_0\). The sampling clock is \(u\in[0,L]\); the physical-time coordinate is \(Y_t=X_{T-t}\). For each generation, the ideal process has law \(P_i\) and solves
\[
dX_u=\left[\tfrac12X_u+s_i(X_u,T-u)\right]du-dB_u,
\qquad X_0\sim\mathcal N(0,I_d),
\]
where \(B\) is a standard \(d\)-dimensional Brownian motion in the sampling filtration, independent of \(X_0\). Denote the ideal density of \(Y_t\) by \(q_{i,t}\), and let
\[
s_i(x,t)=\nabla_x\log q_{i,t}(x),
\qquad q_{i,t_0}=q_i.
\]
The densities are positive and differentiable wherever this score is used. Thus the ideal sampling terminal marginal is \(X_L=Y_{t_0}\sim q_i\), and its initialization density is \(q_{i,T}=\mathcal N(0,I_d)\).

The learned process has law \(\widehat P_i\) and solves
\[
dX_u=\left[\tfrac12X_u+\widehat s_i(X_u,T-u)\right]du-d\widehat B_u,
\qquad X_0\sim\mathcal N(0,I_d),
\]
with a standard Brownian motion \(\widehat B\) independent of its initial state. Its terminal density is \(\widehat p^{i+1}\). Assume these SDEs are well-posed in law with nonexplosive continuous solutions. The score fields are measurable, and their evaluations along the processes are predictable in sampling time. Expectations below concern these path laws for the specified score fields.

Set
\[
e_{i,t}(x)=\widehat s_i(x,t)-s_i(x,t),
\]
\[
a_i^2=\mathbb E_{P_i}\!\left[\int_{t_0}^T\|e_{i,t}(Y_t)\|^2dt\right],
\qquad
b_i^2=\mathbb E_{\widehat P_i}\!\left[\int_{t_0}^T\|e_{i,t}(Y_t)\|^2dt\right].
\]
For the generations considered below, define under \(P_i\), in sampling time,
\[
N_i(u)=-\int_0^u e_{i,T-v}(X_v)\cdot dB_v,
\qquad A_i(u)=\langle N_i\rangle_u,
\qquad 0\le u\le L,
\]
and write
\[
N_i=N_i(L),\qquad A_i=A_i(L),\qquad W_i=N_i-\tfrac12A_i.
\]
Define
\[
\rho_i=
\begin{cases}
\operatorname{Var}_{P_i}\!\bigl(\mathbb E_{P_i}[N_i\mid Y_{t_0}]\bigr)/a_i^2,&a_i^2>0,\\
0,&a_i^2=0.
\end{cases}
\]

Assume there are an integer \(i_0\ge0\), \(\delta>1\), \(0<C_\delta<\infty\), \(\gamma>\max\{2,4/(\delta-1)\}\), and \(0<K_\gamma<\infty\) such that, for every \(i\ge i_0\),
\[
a_i^2<\infty,\qquad b_i^2<\infty,
\]
the process
\[
\mathcal E_i(u)=\exp\bigl(N_i(u)-\tfrac12A_i(u)\bigr),\qquad 0\le u\le L,
\]
is a true \(P_i\)-martingale in the sampling filtration, and
\[
\mathbb E_{P_i}[e^{(1+\delta)W_i}]\le C_\delta,
\qquad
\mathbb E_{P_i}[A_i^{2+\gamma}]\le K_\gamma(a_i^2)^{2+\gamma}.
\]
The last inequality is stated without division so that it also applies when \(a_i=0\).

For probability densities \(p,q\), define
\[
\chi^2(p\|q)=\int_{\mathbb R^d}\left(\frac{p(x)}{q(x)}-1\right)^2q(x)\,dx
\]
when \(p\ll q\), with the ratio interpreted \(q\)-almost everywhere; set the divergence to \(+\infty\) otherwise.

## Task

Prove that there are constants \(c,C>0\), depending only on \(\delta,C_\delta,\gamma,K_\gamma\), such that for every \(i\ge i_0\) satisfying
\[
a_i^2\le\min\{1,\rho_i/(8C)\},
\]
one has the integrated two-sided bound
\[
\frac14\rho_i a_i^2-Ca_i^4
\;\le\;
\chi^2(\widehat p^{i+1}\|q_i)
\;\le\;
4a_i^2+ca_i^4.
\]
Consequently,
\[
\chi^2(\widehat p^{i+1}\|q_i)\ge\frac18\rho_i a_i^2.
\]
Further, show that if \(\rho_i\ge\underline\rho>0\) and \(a_i^2\) is sufficiently small, uniformly over the generations under consideration, then
\[
\chi^2(\widehat p^{i+1}\|q_i)\asymp a_i^2.
\]
Here \(\asymp\) means upper and lower bounds by finite positive constant multiples, with constants independent of \(i\); these comparison constants may additionally depend on \(\underline\rho\).
