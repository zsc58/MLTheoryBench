# Problem

## Setup

Let \(\Xi\subseteq\mathbb R^{d_\Xi}\) be a nonempty closed convex set, let \(\mathcal U\) be a measurable space, and let \(U_1,U_2,\ldots\) be i.i.d. innovations. Let \(\Phi:\Xi\times\mathcal U\to\Xi\) and \(g:\mathbb R^d\times\Xi\to\mathbb R^d\) be measurable. At each transition the innovation is independent of the current state; equivalently, the innovation sequence is independent of the initial state and the recursion uses successive innovations. Define
\[
\xi_{n+1}=\Phi(\xi_n,U_{n+1}),\qquad
X_{n+1}=X_n-\alpha G(X_n,\xi_{n+1}),
\qquad G(x,\xi)=h(x)+g(x,\xi),\quad h=\nabla H.
\]
Let \(P_\alpha\) denote the transition kernel of \((X_n,\xi_n)\) on \(\mathsf Z=\mathbb R^d\times\Xi\).

Assume the following, with constants fixed independently of \(\alpha\).

### 1. Objective geometry

The function \(H:\mathbb R^d\to\mathbb R\) is convex and \(C^2\), and \(0\) is a minimizer. Fix \(m\ge2\) and \(\beta\in[1,2]\). There are \(R_H,c_{in},C_{in}>0\) such that, for \(0<\|x\|\le R_H\),
\[
\nabla^2H(x)\succeq c_{in}\|x\|^{m-2}I_d,
\qquad \|h(x)\|\le C_{in}\|x\|^{m-1}.
\]
For \(m=2\), the Hessian inequality also holds at zero.

If \(\beta=2\), there is \(c_{out}>0\) such that
\[
\nabla^2H(x)\succeq c_{out}I_d,\qquad \|x\|\ge R_H.
\]
If \(1\le\beta<2\), there are \(c_{out},C_{out}>0\) such that
\[
\langle x,h(x)\rangle\ge c_{out}\|x\|^\beta,
\qquad \|h(x)\|\le C_{out}\|x\|^{\beta-1},
\qquad \|x\|\ge R_H.
\]

### 2. Markovian noise and update regularity

There is a measurable \(L_\Phi:\mathcal U\to[0,1]\) such that
\[
\|\Phi(\xi,u)-\Phi(\eta,u)\|
\le L_\Phi(u)\|\xi-\eta\|,
\qquad \rho_\Xi:=\mathbb E L_\Phi(U_1)<1
\]
for all \(\xi,\eta\in\Xi\) and \(u\in\mathcal U\). There is \(L_{g,\Phi}>0\) such that
\[
\|g(x,\Phi(\xi,u))-g(x,\Phi(\eta,u))\|
\le L_{g,\Phi}\|\xi-\eta\|
\]
for all \(x\in\mathbb R^d\), \(\xi,\eta\in\Xi\), and \(u\in\mathcal U\).

There is a reference point \(\xi_*\in\Xi\) with
\[
\mathbb E\|\Phi(\xi_*,U_1)-\xi_*\|<\infty.
\]
If \(\beta=2\), also assume
\[
\mathbb E\|g(0,\Phi(\xi_*,U_1))\|<\infty.
\]
Write
\[
\bar g(x,\xi)=\mathbb E[g(x,\Phi(\xi,U_1))].
\]

When \(1\le\beta<2\), assume that there are \(c_{diss},\lambda_0>0\) such that
\[
\langle x,h(x)+\bar g(x,\xi)\rangle\ge c_{diss}\|x\|^\beta
\quad\text{for all }\|x\|\ge R_H,\ \xi\in\Xi,
\]
and
\[
\sup_{x\in\mathbb R^d,\,\xi\in\Xi}
\mathbb E\exp\!\left(
\lambda_0\frac{\|g(x,\Phi(\xi,U_1))\|}{1+\|x\|^{\beta-1}}
\right)<\infty.
\]
Here \(\|x\|^0=1\), including at zero. These two conditions are not imposed when \(\beta=2\).

If \(m>2\), assume that there are \(\varepsilon_g,p_g>0\) such that
\[
\inf_{\xi\in\Xi}\mathbb P\bigl(\|g(0,\Phi(\xi,U_1))\|\ge\varepsilon_g\bigr)\ge p_g.
\]
This condition is not imposed when \(m=2\).

For every \(\xi\in\Xi\), the map \(x\mapsto G(x,\xi)\) is \(C^1\). There are \(L_G\ge1\) and \(\theta\in[0,1)\) such that, for all \(x,y\in\mathbb R^d\) and \(\xi\in\Xi\),
\[
\langle x-y,G(x,\xi)-G(y,\xi)\rangle
\ge L_G^{-1}\|G(x,\xi)-G(y,\xi)\|^2,
\]
\[
\langle x-y,\bar g(x,\xi)-\bar g(y,\xi)\rangle
\ge-\theta\langle x-y,h(x)-h(y)\rangle.
\]

### 3. Local homogeneous model and stationary noise

There is a convex \(C^2\) function \(H_0:\mathbb R^d\to\mathbb R\), homogeneous of degree \(m\), with \(H_0(0)=0\), \(\nabla H_0(0)=0\), and
\[
h(x)=h_0(x)+o(\|x\|^{m-1})\quad(x\to0),
\qquad h_0=\nabla H_0.
\]

Let \(\pi_\Xi\) denote the unique invariant probability law of the driving chain. Assume
\[
\int_\Xi g(x,\xi)\,\pi_\Xi(d\xi)=0
\quad\text{for every }x\in\mathbb R^d,
\]
and
\[
\int_\Xi\bigl(\|g(0,\xi)\|^2+\|\xi-\xi_*\|^2\bigr)\,\pi_\Xi(d\xi)<\infty.
\]
For the driving chain initialized with \(\xi_0\sim\pi_\Xi\), define
\[
\Gamma_k=\mathbb E[g(0,\xi_0)g(0,\xi_k)^\top],
\qquad
\Sigma=\Gamma_0+\sum_{k\ge1}(\Gamma_k+\Gamma_k^\top).
\]

### 4. Distances and moment classes

For a nonempty closed convex subset \(E\) of a finite-dimensional normed space with base norm \(|\cdot|_*\), and a continuous weight \(V:E\to[1,\infty)\), define
\[
d_{V,*}(z,z')=
\inf_\gamma\int_0^1 V(\gamma(t))|\gamma'(t)|_*\,dt,
\]
where the infimum is over absolutely continuous curves in \(E\) joining \(z\) to \(z'\). Define
\[
W_{V,*}(\mu,\nu)=
\inf_{\gamma\in\Pi(\mu,\nu)}\int_{E\times E}d_{V,*}(z,z')\,\gamma(dz,dz'),
\]
where \(\Pi(\mu,\nu)\) is the set of couplings of the two Borel probability laws. For a metric \(d\) on \(E\), let
\[
\mathcal P_1(E,d)=
\left\{\mu:\int_E d(z,z_0)\,\mu(dz)<\infty
\text{ for some }z_0\in E\right\}.
\]

On \(\mathsf Z\), use the base norm
\[
|(x,\xi)|_\alpha=\|x\|+\alpha^{-1}\|\xi\|,
\]
and write \(d_{V,\alpha}\) and \(W_{V,\alpha}\) for the resulting distances.

## Task

Prove that there exist \(\alpha_0\in(0,1)\) and \(c\in(0,1)\) such that, for every \(0<\alpha\le\alpha_0\), a continuous weight \(V_\alpha:\mathsf Z\to[1,\infty)\) can be chosen for which \(P_\alpha\) has a unique invariant probability law
\[
\pi_\alpha\in\mathcal P_1(\mathsf Z,d_{V_\alpha,\alpha}),
\]
and
\[
W_{V_\alpha,\alpha}(\mu P_\alpha^n,\nu P_\alpha^n)
\le(1-c\alpha^{m-1})^nW_{V_\alpha,\alpha}(\mu,\nu)
\]
for every integer \(n\ge0\) and all Borel probability laws \(\mu,\nu\) with finite \(W_{V_\alpha,\alpha}(\mu,\nu)\).

If \((X_\infty^\alpha,\xi_\infty^\alpha)\sim\pi_\alpha\) and \(Y_\alpha=\alpha^{-1/m}X_\infty^\alpha\), prove that, as \(\alpha\downarrow0\), \(Y_\alpha\) converges weakly to the unique invariant distribution of
\[
dY_t=-h_0(Y_t)\,dt+\Sigma^{1/2}dB_t,
\]
where \(B\) is a standard \(d\)-dimensional Brownian motion and \(\Sigma^{1/2}\) is the positive semidefinite square root.
