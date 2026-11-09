# Problem

## Setup

Let \(u_{0,1},u_{0,2}\) be probability measures on \(\mathbb R^d\) with finite nonempty supports \(A_i=\operatorname{supp}(u_{0,i})\). Assume that for each \(i\) there are constants \(c_i>0\), \(\alpha_i\ge0\), and \(r_i>0\) such that
\[
\inf_{a\in A_i}u_{0,i}(B(a,r))\ge c_i r^{\alpha_i}\qquad(0<r\le r_i).
\]
For \(t>0\), let \(u_i(\cdot,t)\) be the Gaussian heat convolution of \(u_{0,i}\) with kernel \((4\pi t)^{-d/2}e^{-\|x-y\|^2/(4t)}\). Define
\[
d_i(x)=\operatorname{dist}(x,A_i),\qquad
\Phi_\lambda(x)=\lambda d_1(x)^2+(1-\lambda)d_2(x)^2,\quad \lambda\ge0.
\]
For a locally Lipschitz function \(f\), let \(\partial^C f(x)\) denote its Clarke subdifferential and set
\[
\widehat\partial\Phi_\lambda(x)=\lambda\partial^C(d_1^2)(x)+(1-\lambda)\partial^C(d_2^2)(x),
\]
where the right-hand side is a weighted Minkowski sum. Write
\[
\operatorname{Crit}(\Phi_\lambda)=\{x:0\in\partial^C\Phi_\lambda(x)\},\qquad
\operatorname{Crit}_{out}(\Phi_\lambda)=\{x:0\in\widehat\partial\Phi_\lambda(x)\},
\]
and let \(\operatorname{Min}(\Phi_\lambda)\) be the set of local minimizers of \(\Phi_\lambda\). A global Caratheodory solution of \(\dot Z\in F(Z)\), \(Z_0=z_0\), is a curve \(Z:[0,\infty)\to\mathbb R^d\) that is absolutely continuous on every bounded interval and has a measurable selection \(\xi(s)\in F(Z_s)\) almost everywhere such that
\[
Z_s=z_0+\int_0^s\xi(r)\,dr\qquad(s\ge0).
\]

Fix \(\lambda\ge0\), \(T>0\), and \(x_T\in\mathbb R^d\). Let \(X_t\) solve on \((0,T]\) the generation ODE
\[
\dot X_t=-\lambda\nabla\log u_1(X_t,t)-(1-\lambda)\nabla\log u_2(X_t,t),\qquad X_T=x_T,
\]
and define \(Y_\tau=X_{Te^{-\tau}}\) for \(\tau\ge0\). Let \(\omega(Y)\) denote the set of limits of sequences \(Y_{\tau_j}\) with \(\tau_j\to\infty\).

## Task

Prove that for every sequence \(\tau_j\to\infty\), the forward time shifts
\[
Y^j_s=Y_{\tau_j+s},\qquad s\ge0,
\]
are relatively compact for uniform convergence on every bounded interval of \([0,\infty)\), and that every subsequential limit \(Z\) is a global Caratheodory solution of
\[
\dot Z_s\in-\tfrac14\partial^C\Phi_\lambda(Z_s)\quad(0\le\lambda\le1),
\qquad
\dot Z_s\in-\tfrac14\widehat\partial\Phi_\lambda(Z_s)\quad(\lambda>1),
\]
with the inclusion holding almost everywhere.

Prove also that every global solution of the corresponding autonomous inclusion converges to a single point in \(\operatorname{Crit}(\Phi_\lambda)\) for \(0\le\lambda\le1\), respectively in \(\operatorname{Crit}_{out}(\Phi_\lambda)\) for \(\lambda>1\).

Finally, assume
\[
\omega(Y)\cap\bigl(\operatorname{Crit}(\Phi_\lambda)\setminus\operatorname{Min}(\Phi_\lambda)\bigr)=\varnothing
\quad\text{if }0\le\lambda\le1,
\]
or
\[
\omega(Y)\cap\bigl(\operatorname{Crit}_{out}(\Phi_\lambda)\setminus\operatorname{Min}(\Phi_\lambda)\bigr)=\varnothing
\quad\text{if }\lambda>1.
\]
Prove that for some \(x_*\in\operatorname{Min}(\Phi_\lambda)\), \(Y_\tau\to x_*\) as \(\tau\to\infty\), equivalently \(X_t\to x_*\) as \(t\downarrow0\).
