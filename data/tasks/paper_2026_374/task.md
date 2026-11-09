# Problem

## Setup

Fix a horizon \(T>0\), discount rate \(\beta\geq0\), exploration weight \(\gamma>0\), and finite \(p\geq1\). States lie in \(\mathbb R^d\), and actions lie in a measurable set \(A\subseteq\mathbb R^m\), equipped with Lebesgue measure \(da\). Let \(W\) be a \(d\)-dimensional Brownian motion and let \(R\), independent of \(W\), be an irreducible continuous-time Markov chain on a finite set \(E\), with generator \(Q=(q_{ij})\).

Let \(b(t,x,i,a)\in\mathbb R^d\), \(\sigma(t,x,i,a)\in\mathbb R^{d\times d}\), and \(r(t,x,i,a),h(x)\in\mathbb R\) be continuous in their respective arguments. Uniformly in \((t,i,a)\), suppose \(b\) and \(\sigma\) are Lipschitz in \(x\), and
\[
 |b(t,x,i,a)|+\|\sigma(t,x,i,a)\|\leq C(1+|x|).
\]
For some \(C>0\) and \(c\geq1\), suppose
\[
 |r(t,x,i,a)|\leq C(1+|x|^c+|a|^c),\qquad
 |h(x)|\leq C(1+|x|^c).
\]

For a feedback probability density \(\rho(a\mid t,x,i)\), define
\[
 B^\rho(t,x,i)=\int_A b(t,x,i,a)\rho(a\mid t,x,i)\,da,\qquad
 C^\rho(t,x,i)=\int_A\sigma\sigma^{\mathsf T}(t,x,i,a)\rho(a\mid t,x,i)\,da.
\]
Write \(\overline\sigma^\rho=(C^\rho)^{1/2}\) for the nonnegative-definite matrix square root. Starting from \((X_t,R_t)=(x,i)\), the projected state equation is
\[
 dX_s=B^\rho(s,X_s,R_s)\,ds+\overline\sigma^\rho(s,X_s,R_s)\,dW_s.
\]

A policy \(\rho\) is **admissible** if it is a measurable, nonnegative feedback density of unit mass and full support in \(A\) at every \((t,x,i)\); its densities are continuous in \((t,x)\) in total variation for each \(i\), and, for a constant \(L_\rho\) independent of \((t,x,y,i)\),
\[
 \int_A|\rho(a\mid t,x,i)-\rho(a\mid t,y,i)|\,da\leq L_\rho|x-y|;
\]
the projected equation has a unique strong solution for every initial triple; and its action moments of every positive order and its integrated entropy are finite and have polynomial-growth bounds in \(x\), uniformly in \((t,i)\). Explicitly, for every \(n>0\) there are \(C_n,c_n>0\) with \(\int_A|a|^n\rho(a\mid t,x,i)\,da\leq C_n(1+|x|^{c_n})\), and there are \(C_\rho,c_\rho>0\) with \(|\int_A\rho\ell_p(\rho)\,da|\leq C_\rho(1+|x|^{c_\rho})\). Constants in these policy bounds may depend on the policy and moment order.

Set
\[
 \ell_p(z)=\begin{cases}(1-z^{p-1})/(p-1),&p>1,\\-\log z,&p=1.\end{cases}
\]
In integrals, \(z\ell_1(z)=-z\log z\) has its continuous value \(0\) at \(z=0\). For an admissible policy \(\rho\), define
\[
 J^\rho(t,x,i)=\mathbb E_{t,x,i}\!\left[\int_t^T e^{-\beta(s-t)}\int_A\bigl(r(s,X_s,R_s,a)+\gamma\ell_p(\rho(a\mid s,X_s,R_s))\bigr)\rho(a\mid s,X_s,R_s)\,da\,ds+e^{-\beta(T-t)}h(X_T)\right].
\]

Fix an admissible \(\pi\). Assume \(J^\pi(\cdot,\cdot,i)\in C^{1,2}([0,T)\times\mathbb R^d)\cap C([0,T]\times\mathbb R^d)\) for every \(i\), and that, for \(t<T\),
\[
\begin{aligned}
0={}&J_t^\pi(t,x,i)-\beta J^\pi(t,x,i)\\
&+\int_A\Bigl[b(t,x,i,a)\cdot\nabla J^\pi(t,x,i)
+\tfrac12\operatorname{Tr}\!\bigl(\sigma\sigma^{\mathsf T}(t,x,i,a)D^2J^\pi(t,x,i)\bigr)
+r(t,x,i,a)\\
&\hspace{43mm}+\sum_{j\in E}q_{ij}J^\pi(t,x,j)
+\gamma\ell_p(\pi(a\mid t,x,i))\Bigr]\pi(a\mid t,x,i)\,da,\\
&J^\pi(T,x,i)=h(x).
\end{aligned}\tag{1}
\]
Define, for \(t<T\),
\[
 G^\pi(t,x,i,a)=b(t,x,i,a)\cdot\nabla J^\pi(t,x,i)
+\tfrac12\operatorname{Tr}\!\bigl(\sigma\sigma^{\mathsf T}(t,x,i,a)D^2J^\pi(t,x,i)\bigr)
+r(t,x,i,a)+\sum_{j\in E}q_{ij}J^\pi(t,x,j).
\]

Define the improvement operator \(\mathcal T_p\) at preterminal times. For \(p>1\), suppose that at each \((t,x,i)\), \(t<T\), a real \(\lambda(t,x,i)\) exists for which
\[
 (\mathcal T_p\pi)(a\mid t,x,i)=\left(\frac{p-1}{p\gamma}\right)^{1/(p-1)}\bigl(G^\pi(t,x,i,a)+\lambda(t,x,i)\bigr)_+^{1/(p-1)}\tag{2}
\]
integrates to one. For \(p=1\), suppose \(0<Z(t,x,i):=\int_A\exp(G^\pi(t,x,i,u)/\gamma)\,du<\infty\), and set
\[
 (\mathcal T_1\pi)(a\mid t,x,i)=\frac{\exp(G^\pi(t,x,i,a)/\gamma)}{Z(t,x,i)}.\tag{3}
\]
Assume these preterminal densities extend to an admissible policy \(\pi'=\mathcal T_p\pi\) on \([0,T]\). The density assigned at \(T\) need not be defined by derivatives of \(J^\pi\); it does not affect the payoff.

## Task

Prove:

1. For every \((t,x,i)\in[0,T]\times\mathbb R^d\times E\), \(J^{\pi'}(t,x,i)\geq J^\pi(t,x,i)\).
2. Suppose an admissible \(\pi^*\) satisfies the same smooth-value and fixed-policy equation assumptions as \(\pi\), the appropriate preterminal normalizer exists, and \(\mathcal T_p\pi^*\) is admissible. If \(\pi^*(\cdot\mid t,x,i)=(\mathcal T_p\pi^*)(\cdot\mid t,x,i)\) for every \(t<T,x,i\), prove
\[
 J^{\pi^*}(t,x,i)=\sup_{\rho\ \mathrm{admissible}}J^\rho(t,x,i)
 \quad\text{for every }(t,x,i)\in[0,T]\times\mathbb R^d\times E.
\]
