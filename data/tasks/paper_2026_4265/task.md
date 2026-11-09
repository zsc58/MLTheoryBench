# Problem

## Setup

Let \(T\ge1\) be an integer. Let \(X\subset\mathbb R^n\) and \(A\subset\mathbb R^m\) be nonempty compact sets, with their Borel sigma-algebras. Equip \(X\) with a metric \(d_X\) inducing its compact topology. Write \(\mathsf P(X)\) for the Borel probability measures on \(X\). Fix \(q\ge1\) and \(\varepsilon>0\). For \(P,Q\in\mathsf P(X)\), define
\[
W_q(P,Q)=\left(\inf_{\gamma\in\Gamma(P,Q)}\int_{X\times X}d_X(y,z)^q\,\gamma(dy,dz)\right)^{1/q},
\]
where \(\Gamma(P,Q)\) is the set of probability measures with marginals \(P\) and \(Q\).

For each \(t=0,\ldots,T-1\), let \(P_t^0:X\times A\to\mathsf P(X)\) be a weakly continuous probability kernel, and set
\[
\mathcal P_t(x,a)=\{P\in\mathsf P(X):W_q(P,P_t^0(x,a))\le\varepsilon\}.
\]
Assume these correspondences are nonempty, compact-valued, and continuous in the Hausdorff distance induced by \(W_q\). The ambiguity model permits every sequence of Borel kernels \(K_t:X\times A\to\mathsf P(X)\) satisfying \(K_t(x,a)\in\mathcal P_t(x,a)\), without additional coupling constraints. Under such a sequence and a policy, the action at time \(t\) is sampled from the policy at the current state, and the next state is sampled from \(K_t\) at the realized state-action pair.

For each \(t<T\), the running reward \(f(t,\cdot,\cdot,\cdot):X\times A\times X\to\mathbb R\) is continuous, and the terminal reward \(g:X\to\mathbb R\) is continuous. The rewards, nominal kernels, ambiguity sets, \(q\), and \(\varepsilon\) do not depend on the policy parameter.

Let \(\Theta\subset\mathbb R^d\) be a nonempty compact parameter set. For each \(\theta\in\Theta\), the policies are probability kernels
\[
\pi_t^\theta(da\mid x)=\pi_t^\theta(a\mid x)\,\nu(da),
\qquad
\int_A\pi_t^\theta(a\mid x)\,\nu(da)=1,
\]
relative to a fixed Borel reference measure \(\nu\). Take Borel versions of the densities that are positive and differentiable in \(\theta\), so that their logarithmic scores are defined and measurable. Parameter differentiability at a boundary point is interpreted using differentiable extensions to a neighborhood; directional limits of the policies and values below use only parameters in \(\Theta\).

Assume \((\theta,x)\mapsto\pi_t^\theta(\cdot\mid x)\) is weakly continuous. For every \(\varphi\in C(A)\), assume
\[
\theta\longmapsto\int_A\varphi(a)\,\pi_t^\theta(da\mid x)
\]
is \(C^1\), with parameter derivative continuous in \((\theta,x)\). Here \(C^1\) on the compact parameter set means restriction of a \(C^1\) function defined on a neighborhood. Suppose there is a constant \(C_\pi<\infty\) such that
\[
\sup_{\theta\in\Theta}\sup_{t<T,\,x\in X,\,a\in A}
\|\nabla_\theta\log\pi_t^\theta(a\mid x)\|\le C_\pi.
\]

Define recursively
\[
V_T^\theta(x)=g(x),
\]
\[
G_t^\theta(x,a)=\inf_{P\in\mathcal P_t(x,a)}\int_X\bigl[f(t,x,a,y)+V_{t+1}^\theta(y)\bigr]P(dy),
\qquad
V_t^\theta(x)=\int_A G_t^\theta(x,a)\,\pi_t^\theta(da\mid x).
\]
Let \(\mu_0\in\mathsf P(X)\) be fixed independently of \(\theta\), and set
\[
J(\theta)=\int_XV_0^\theta(x)\,\mu_0(dx).
\]

Put \(I_+(\delta)=(0,\delta)\) and \(I_-(\delta)=(-\delta,0)\). For \(\sigma\in\{+,-\}\), call \((\theta,r)\), with \(\theta\in\Theta\) and \(r\in\mathbb R^d\), feasible on side \(\sigma\) if there is \(\delta>0\) such that \(\theta+hr\in\Theta\) for every \(h\in I_\sigma(\delta)\). On the respective feasible sides, define
\[
D_r^+F(\theta)=\lim_{h\downarrow0}\frac{F(\theta+hr)-F(\theta)}h,
\qquad
D_r^-F(\theta)=\lim_{h\uparrow0}\frac{F(\theta+hr)-F(\theta)}h,
\]
when the limits exist. Also define
\[
S_t^\theta(x,a;r)=\langle\nabla_\theta\log\pi_t^\theta(a\mid x),r\rangle.
\]

Assume the following value regularity. For every \(\theta,r,\sigma\) feasible on side \(\sigma\), there is \(h_0>0\) with \(\theta+hr\in\Theta\) for all \(h\in I_\sigma(h_0)\), such that, for each \(s=0,\ldots,T\), the family
\[
Q_{s,h}^{\theta,r}(x)=\frac{V_s^{\theta+hr}(x)-V_s^\theta(x)}h,
\qquad h\in I_\sigma(h_0),
\]
is equicontinuous on \(X\): for every \(\eta>0\), there is \(\delta>0\) such that
\[
d_X(x,z)<\delta\quad\Longrightarrow\quad
|Q_{s,h}^{\theta,r}(x)-Q_{s,h}^{\theta,r}(z)|<\eta
\]
for all \(x,z\in X\) and all \(h\in I_\sigma(h_0)\). The constants may depend on \(\theta,r,\sigma,s\), but not on \(h,x,z\).

## Task

Prove that, for every \(\theta\in\Theta\), \(t<T\), and \((x,a)\in X\times A\), the set
\[
\mathcal P_t^*(x,a,\theta)=\operatorname*{argmin}_{P\in\mathcal P_t(x,a)}\int_X[f(t,x,a,y)+V_{t+1}^\theta(y)]P(dy)
\]
is nonempty and compact.

Prove the following conclusions separately on each feasible side. If \((\theta,r)\) is feasible on the positive side, the right derivatives exist and satisfy
\[
D_r^+G_t^\theta(x,a)=\min_{P\in\mathcal P_t^*(x,a,\theta)}\int_XD_r^+V_{t+1}^\theta(y)\,P(dy).
\]
If \((\theta,r)\) is feasible on the negative side, the left derivatives exist and satisfy
\[
D_r^-G_t^\theta(x,a)=\max_{P\in\mathcal P_t^*(x,a,\theta)}\int_XD_r^-V_{t+1}^\theta(y)\,P(dy).
\]
For each feasible side \(\sigma\in\{+,-\}\), prove the backward recursion
\[
D_r^\sigma V_T^\theta(x)=0,
\qquad
D_r^\sigma V_t^\theta(x)=\int_A\left[G_t^\theta(x,a)S_t^\theta(x,a;r)+D_r^\sigma G_t^\theta(x,a)\right]\pi_t^\theta(da\mid x),
\]
and consequently
\[
D_r^\sigma J(\theta)=\int_XD_r^\sigma V_0^\theta(x)\,\mu_0(dx).
\]
