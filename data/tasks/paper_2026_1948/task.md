# Problem

## Setup

Let \(d\ge1\). Write \(\mathcal P_2(\mathbb R^d)\) for the Borel probability measures with finite second moment, and \(\Pi(\mu,\nu)\) for their couplings. Let \(\gamma\) be the restriction to positive-semidefinite matrices of a norm on the symmetric \(d\times d\) matrices. Assume
\[
0\preceq A\preceq B\quad\Longrightarrow\quad\gamma(A)\le\gamma(B).
\]
Let \(K_\gamma\subseteq\mathbb S_+^d\) be a nonempty convex compact set such that
\[
\gamma(S)=\max_{Q\in K_\gamma}\operatorname{tr}(QS),\qquad S\succeq0.
\]
For \(\mu,\nu\in\mathcal P_2(\mathbb R^d)\), define the nonnegative quantities \(W_\gamma\) and \(W_Q\) by
\[
W_\gamma(\mu,\nu)^2
:=\inf_{\pi\in\Pi(\mu,\nu)}
\gamma\!\left(\int(y-x)(y-x)^\top\,d\pi(x,y)\right),
\]
\[
W_Q(\mu,\nu)^2
:=\inf_{\pi\in\Pi(\mu,\nu)}
\int(y-x)^\top Q(y-x)\,d\pi(x,y),\qquad Q\in K_\gamma.
\]
Define the nonnegative quantity \(W_\gamma^{\rm BB}\) by
\[
\bigl(W_\gamma^{\rm BB}(\mu_0,\mu_1)\bigr)^2
:=\inf_{(\mu_t,v_t)}
\int_0^1\gamma\!\left(\int v_t(x)v_t(x)^\top\,d\mu_t(x)\right)dt.
\]
Here the infimum is over narrowly continuous curves \(\mu_t\in\mathcal P_2(\mathbb R^d)\) with the prescribed endpoints and jointly Borel measurable vector fields \(v_t(x)\) satisfying
\[
\int_0^1\int |v_t(x)|^2\,d\mu_t(x)dt<\infty,
\qquad
\partial_t\mu_t+\nabla\!\cdot(\mu_tv_t)=0
\]
in distributions.

For \(v\in L^2(\mu;\mathbb R^d)\), set
\[
N_\mu(v)^2=\gamma\!\left(\int vv^\top\,d\mu\right).
\]
For \(g\in L^2(\mu;\mathbb R^d)\), let \(J_\gamma^\mu(g)\) denote any minimizer over \(v\in L^2(\mu;\mathbb R^d)\) of
\[
\int g\cdot v\,d\mu+\tfrac12N_\mu(v)^2.
\]
No uniqueness of this minimizer is assumed.

## Functional and solution regularity

Let \(F:\mathcal P_2(\mathbb R^d)\to\mathbb R\) have scalar first variations \(f_\mu\in C^1(\mathbb R^d)\), and set
\[
g_\mu(x)=\nabla f_\mu(x)\in L^2(\mu;\mathbb R^d).
\]
Here scalar first variation means that
\[
\left.\frac{d}{d\varepsilon}F((1-\varepsilon)\mu+\varepsilon\nu)\right|_{\varepsilon=0+}
=\int f_\mu\,d(\nu-\mu)
\]
whenever \(\nu\in\mathcal P_2(\mathbb R^d)\) and \(\int|f_\mu|\,d(\mu+\nu)<\infty\).

Use the following precise transport-differentiability requirement: for every fixed \(\mu\), every sequence \(\nu_n\in\mathcal P_2(\mathbb R^d)\), and every sequence \(\pi_n\in\Pi(\mu,\nu_n)\) with
\[
0<r_n:=\left(\int|y-x|^2\,d\pi_n(x,y)\right)^{1/2}\longrightarrow0,
\]
one has
\[
\frac{F(\nu_n)-F(\mu)-\int g_\mu(x)\cdot(y-x)\,d\pi_n(x,y)}{r_n}
\longrightarrow0.
\]

Let \(T>0\), and let \((\mu_t,v_t)_{t\in[0,T]}\) be a narrowly continuous \(\mathcal P_2\)-curve with a jointly Borel measurable velocity satisfying the continuity equation in distributions and
\[
\int_0^T\int|v_t|^2\,d\mu_tdt<\infty,
\qquad
v_t\in J_\gamma^{\mu_t}(g_{\mu_t})
\quad\text{for almost every }t.
\]
Assume \((t,x)\mapsto g_{\mu_t}(x)\) is jointly measurable, \(t\mapsto F(\mu_t)\) is absolutely continuous, and the continuity-equation chain rule holds:
\[
\frac{d}{dt}F(\mu_t)=\int g_{\mu_t}\cdot v_t\,d\mu_t
\quad\text{for almost every }t.
\]

For a metric \(D\), its metric derivative along a curve is
\[
|\mu'|_D(t)=\lim_{h\to0}\frac{D(\mu_{t+h},\mu_t)}{|h|}
\]
when the limit exists. The descending local slope is
\[
|\partial F|_D(\mu)
=\limsup_{\substack{\nu\to\mu\text{ in }D\\\nu\ne\mu}}
\frac{(F(\mu)-F(\nu))_+}{D(\mu,\nu)},
\qquad a_+=\max\{a,0\}.
\]
In this problem, a curve of maximal slope means a metrically absolutely continuous curve with absolutely continuous energy satisfying the energy-dissipation identity displayed below.

## Task

Prove that, for every \(\mu,\nu\in\mathcal P_2(\mathbb R^d)\),
\[
W_\gamma(\mu,\nu)^2=\max_{Q\in K_\gamma}W_Q(\mu,\nu)^2,
\qquad
W_\gamma(\mu,\nu)=W_\gamma^{\rm BB}(\mu,\nu).
\]
Moreover, prove that every solution satisfying the stated regularity conditions is a curve of maximal slope for \(F\) with respect to \(W_\gamma\), and satisfies
\[
\frac{d}{dt}F(\mu_t)
=-\tfrac12|\mu'|_{W_\gamma}(t)^2
-\tfrac12|\partial F|_{W_\gamma}(\mu_t)^2
\]
for almost every \(t\in(0,T)\).
