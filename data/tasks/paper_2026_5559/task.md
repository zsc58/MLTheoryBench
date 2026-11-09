# Problem

The two settings below are separate. The quantizer-compatibility assumptions in the general recovery setting are not imposed on the explicit PTQ example.

## General recovery setting

All unqualified norms and inner products are Euclidean. Let \(M\subset\mathbb R^d\) be a local \(m\)-dimensional \(C^{2,1}\) embedded manifold. Write \(T_\pi M\) for its tangent space and \(N_M(\pi)=(T_\pi M)^\perp\) for its normal space. Let
\[
U=\{w\in\mathbb R^d:\operatorname{dist}(w,M)<R_U\}
\]
be a tubular neighborhood containing a distinguished reference point \(\bar w\), with a well-defined \(L_P\)-Lipschitz nearest-point projection \(P_M:U\to M\). Let \(H\) be a fixed symmetric positive-definite matrix satisfying
\[
H N_M(\pi)\subseteq N_M(\pi)\qquad(\pi\in M),
\]
with largest and smallest eigenvalues \(\lambda_1\ge\lambda_d>0\). Set
\[
\|v\|_H=(v^\top Hv)^{1/2},\qquad
\mathcal B=\{w\in U:\|w-P_M(w)\|_H\le R\}.
\]
Here \(R,R_U>0\), \(L,L_P\ge0\), \(\varepsilon_{\rm flat}\ge0\), and \(c_\perp,\rho,G,\kappa_M>0\).

Assume \(f:U\to\mathbb R\) is differentiable with \(L\)-Lipschitz gradient on \(U\). Suppose
\[
|f(w)-f(\pi)|\le\varepsilon_{\rm flat}
\]
whenever \(\pi\in M\), \(w\in U\), \(w-\pi\in N_M(\pi)\), and \(\|w-\pi\|_H\le R\). Also assume \(\nabla f(\pi)\in T_\pi M\) for every \(\pi\in M\). For every \(w\in U\setminus\mathcal B\), define
\[
\nu_H(w)=\frac{H(w-P_M(w))}{\|H(w-P_M(w))\|}
\]
and assume
\[
\langle\nabla f(w),\nu_H(w)\rangle\ge c_\perp.
\]

Let \(\mathsf Q:U\to\mathbb R^d\) satisfy
\[
\|\mathsf Q(w)-w\|\le\rho,\qquad \|\nabla f(w)\|\le G\qquad(w\in U).
\]
Assume \(P_M\) is \(C^{1,1}\) on \(U\), with
\[
\|DP_M(w)-DP_M(w')\|_{\rm op}\le\kappa_M\|w-w'\|
\qquad(w,w'\in U),
\]
where \(\|\cdot\|_{\rm op}\) is the Euclidean operator norm. Require
\[
\rho(1+L_P)\sqrt{\lambda_1}
\max\!\left\{\frac G{c_\perp}\sqrt{\frac{\lambda_1}{\lambda_d}},1\right\}
<R<\sqrt{\lambda_d}(R_U-\rho).
\]

When \(\nabla^2f(\bar w)\) exists, the associated Hessian-based post-training proxy is
\[
S(q)=\tfrac12(q-\bar w)^\top\nabla^2f(\bar w)(q-\bar w).
\]
Hessian existence is not an additional hypothesis for the recovery statement. The STE update is
\[
x_{k+1}=x_k-\eta\nabla f(\mathsf Q(x_k)),
\]
with deployed iterate \(\mathsf Q(x_k)\); only its evolution through the first deployed entry into \(\mathcal B\) is considered.

## Explicit PTQ setting

Fix \(\theta\in[\pi/6,\pi/4)\), and define
\[
w_0=(1,0),\quad \tau=(\cos\theta,\sin\theta),\quad
\nu=(-\sin\theta,\cos\theta),\quad
\alpha=\cos\theta-\sin\theta,\quad \delta=\cos\theta+\sin\theta.
\]
Choose \(\mu,r,\varepsilon>0\) and \(u\in(\alpha/2,\alpha)\). Set
\[
R_{\rm ex}=r+\sqrt{2\varepsilon/\mu},
\]
and assume \(R_{\rm ex}<\delta\). Fix \(R_{U,\rm ex}>R_{\rm ex}\). Define, on all of \(\mathbb R^2\),
\[
t(w)=\langle\tau,w-w_0\rangle,\qquad z(w)=\langle\nu,w-w_0\rangle,
\]
\[
f_\theta(w)=\tfrac12(t(w)+u)^2+
\tfrac\mu2\bigl(\max\{|z(w)|-r,0\}\bigr)^2.
\]
The manifold, neighborhood, and basin for this setting are
\[
M_{\rm ex}=\{w_0+\lambda\tau:\lambda\in\mathbb R\},\qquad
U_{\rm ex}=\{w:|z(w)|<R_{U,\rm ex}\},\qquad
\mathcal B_{\rm ex}=\{w\in U_{\rm ex}:|z(w)|\le R_{\rm ex}\}.
\]
Define the proxy reference point and proxy by
\[
\bar w_{\rm ex}=w_0-u\tau,\qquad
S_{\rm ex}(q)=\tfrac12(q-\bar w_{\rm ex})^\top
\nabla^2f_\theta(\bar w_{\rm ex})(q-\bar w_{\rm ex}).
\]
For an independent grid scale \(\sigma>0\) and an integer bitwidth \(B\ge2\), let
\[
\mathcal C_{\sigma,B}=\sigma\{0,\pm1,\ldots,\pm(2^{B-1}-1)\}^2,
\qquad q_g(\sigma)=(\sigma,0).
\]

## Task

Prove both statements below.

1. In the explicit PTQ setting, there exists an open interval \(I_{\rm fail}\subset(0,\infty)\) containing \(1\) such that, for every \(\sigma\in I_{\rm fail}\) and every integer \(B\ge2\), \(q_g(\sigma)\in\mathcal B_{\rm ex}\), every
\[
q_*\in\arg\min_{q\in\mathcal C_{\sigma,B}}S_{\rm ex}(q)
\]
lies outside \(\mathcal B_{\rm ex}\), and
\[
f_\theta(q_*)-f_\theta(q_g(\sigma))
\ge\frac\mu8(\delta-r)^2-
\frac12\bigl(u+\cos\theta\,(\sigma-1)\bigr)^2.
\]

2. In the general recovery setting, suppose \(\bar w\in\mathcal B\) and \(\mathsf Q(\bar w)\notin\mathcal B\). Initialize exactly at \(x_0=\bar w\), put
\[
D=c_\perp\sqrt{\lambda_d}R-\lambda_1(1+L_P)\rho G,
\]
and choose
\[
0<\eta\le\min\!\left\{\frac{D}{\lambda_1(1+L_P)G^2},\frac\rho G\right\}.
\]
The iteration and its required evaluations are well defined through the first deployed entry into \(\mathcal B\). Its first-entry index
\[
T=\inf\{k\ge0:\mathsf Q(x_k)\in\mathcal B\},\qquad\inf\varnothing=+\infty,
\]
is finite and satisfies
\[
T\le1+\frac{
\max\{\|x_0-P_M(x_0)\|_H^2-[R-\sqrt{\lambda_1}\rho(1+L_P)]^2,0\}
}{\eta D}.
\]
