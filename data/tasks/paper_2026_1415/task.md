# Problem

## Setup

Let \((X,A,Y)\) be jointly distributed. There are \(J\ge2\) experts and advice actions \([K]_0=\{0,1,\ldots,K\}\), where action \(0\) means no advice. A sequential policy consists of a measurable router \(r:X\to[J]\) and query map \(q:X\times[J]\to[K]_0\); its executed pair is \((r(x),q(x,r(x)))\). Costs satisfy \(0\le c_{j,k}(x,a,y)\le C\), and the incurred loss is the cost of the executed pair.

An H-consistency bound means \(\mathcal E_\ell+\mathcal M_\ell\le\Gamma(\mathcal E_\psi+\mathcal M_\psi)\) for a nondecreasing \(\Gamma\) with \(\Gamma(0)=0\), where \(\mathcal E\) is excess risk and \(\mathcal M=R_{\mathcal H}^*-R^*\) is the minimizability gap. For the notation used below, if \(L\) is a loss evaluated through a score \(s\in\mathcal H_\Pi\), define
\[
R_L(s)=\mathbb E[L(s;X,A,Y)],\quad R_L^B(\mathcal H_\Pi)=\inf_{s\in\mathcal H_\Pi}R_L(s),
\]
\[
R_L^*(\mathcal H_\Pi)=\mathbb E\left[\inf_{s\in\mathcal H_\Pi}\mathbb E[L(s;X,A,Y)\mid X]\right],
\]
\[
\mathcal E_L(s)=R_L(s)-R_L^B(\mathcal H_\Pi),\qquad
\mathcal M_L(\mathcal H_\Pi)=R_L^B(\mathcal H_\Pi)-R_L^*(\mathcal H_\Pi).
\]

## Separated binary construction

For the separated binary construction \((J=2,K=1)\), interpret the displayed table as a conditional expected cost table at a fixed input; equivalently, it is realized by a one-point input distribution. Let the router score be \(s\in\mathbb R\) and the two query scores be \(t_1,t_2\in\mathbb R\). Let
\[
\Phi_0(t)=\log(1+e^{-t}),\qquad \Phi_1(t)=\log(1+e^t).
\]
The separated pointwise surrogate is
\[
\begin{aligned}
\ell_{\rm sep}(s,t_1,t_2;c)
={}&\Psi_1(s)G(t_1)\big[\nu(c_{1,0})\Phi_0(U(t_1))+\nu(c_{1,1})\Phi_1(U(t_1))\big]\\
&+\Psi_2(s)G(t_2)\big[\nu(c_{2,0})\Phi_0(U(t_2))+\nu(c_{2,1})\Phi_1(U(t_2))\big].
\end{aligned}
\]
Assume \(\nu:[0,C]\to[0,\infty)\) is continuous with \(\nu'(u)>0\) on \((0,C)\); \(G:\mathbb R\to(0,\infty)\) is continuous; \(U:\mathbb R\to\mathbb R\) is continuous, strictly increasing, and onto; and, for every \((u,v)\in(0,C]^2\), the corresponding query objective is coercive and strictly convex with a unique minimizer \(t^*(u,v)\) varying continuously in \((u,v)\). Assume \(\Psi_1,\Psi_2\) are positive \(C^2\) functions with \(\Psi_1'<0\), \(\Psi_2'>0\), and \(\Psi_1'',\Psi_2''>0\); and \(\rho=-\Psi_1'/\Psi_2'\) is a strictly decreasing bijection \(\mathbb R\to(0,\infty)\) with \(\rho(0)=1\). Decode expert 1 when \(s<0\) and expert 2 when \(s>0\); either label may be assigned at \(s=0\).

For a row \((u,v)\), define \(F(u,v)\) by the displayed query infimum in the proof. The table's Bayes expert is the row with the smaller row minimum.

## Augmented construction

Let \(\Pi=[J]\times[K]_0\), identify each \(i=(j,k)\in\Pi\) with \(c_i=c_{j,k}(x,a,y)\), and let \(\mathcal H_\Pi\) be a measurable composite score class. Each \(s\in\mathcal H_\Pi\) decodes as \(\pi_s(x)=\arg\max_{i\in\Pi}s(x,i)\) with fixed finite tie-breaking. Assume this score class satisfies the symmetry and completeness hypotheses of the standard comp-sum multiclass H-consistency theorem for the standard comp-sum loss \(\Phi_{01}^\tau\) on the finite label set \(\Pi\), with transfer function \(\Gamma_\tau\) for \(\tau\ge0\), and \(\Gamma_1(u)=\sqrt{2u}\).

Set, pointwise,
\[
M=\max_{i\in\Pi}c_i,\qquad w_i=M-c_i,\qquad D=\sum_i c_i-(|\Pi|-1)M,
\]
and define
\[
\ell_{\rm aug}(s;x,a,y)=\sum_{i\in\Pi}w_i(x,a,y)\Phi_{01}^\tau(s(x),i).
\]
Let \(L_{\rm def}(s;x,a,y)=c_{\pi_s(x)}(x,a,y)\), let \(L_{\rm aug}=\ell_{\rm aug}\), and use the preceding definitions of \(\mathcal E\) and \(\mathcal M\) for these two losses. Prove:

(i) for every \(b\in(0,C)\) and \(\varepsilon\in(0,C-b)\) there is \(\delta\in(0,b)\) such that the table
\[
\begin{pmatrix}b-\delta&C\\ b&b+\varepsilon\end{pmatrix}
\]
has Bayes policy selecting expert 1, while the unique separated-surrogate minimizer has positive router score and therefore decodes expert 2; hence the separated family is not Bayes consistent.

(ii) With
\[
\alpha=\mathbb E\sum_i\mathbb E[w_i\mid X],
\]
prove the H-consistency bound
\[
\mathcal E_{\rm def}+\mathcal M_{\rm def}\le\widetilde\Gamma_\tau(\mathcal E_{\rm aug}+\mathcal M_{\rm aug}),
\qquad
\widetilde\Gamma_\tau(u)=\alpha\Gamma_\tau(u/\alpha),
\]
with the assertion immediate when \(\alpha=0\).
