# Problem

## Setup

Let d be an integer with $d\ge2$, let $I=(0,1)$, and let $\mathbb S^{d-1}=\{x\in\mathbb R^d:\|x\|=1\}$. Norms and inner products are Euclidean. Write $\sigma$ for Riemannian surface-volume measure on the sphere; a density $p_t$ is nonnegative and satisfies $\int_{\mathbb S^{d-1}}p_t\,d\sigma=1$.

For $x\in\mathbb S^{d-1}$ define
\[
P_x(z)=z-\langle z,x\rangle x,\qquad
T_x\mathbb S^{d-1}=\{v\in\mathbb R^d:\langle v,x\rangle=0\}.
\]
For each fixed time, spherical functions and tangent fields under consideration are assumed to admit smooth spatial ambient extensions to $\mathbb R^d$. For such an extension, use
\[
\operatorname{div}_{\mathbb S^{d-1}}u
=\operatorname{tr}(\nabla u)-x^T(\nabla u)x.
\]

Fix $w\in\mathbb S^{d-1}$. A density is radial around $w$ if $p_t(x)=\bar p_t(\langle w,x\rangle)$, where $\bar p_t$ is defined on $[-1,1]$. A radial tangent field has the form $v_t(x)=\psi_t(\langle w,x\rangle)P_x(w)$, where $\psi_t$ is real-valued on $[-1,1]$. Assume $(t,s)\mapsto\bar p_t(s)$ belongs to $C^1(I\times(-1,1))$ and $\psi_t\in C^1((-1,1))$ for each $t\in I$. If $S=\langle w,X\rangle$ for $X$ with density $p_t$, write its density with respect to Lebesgue measure as
\[
f_t(s)=C_d(1-s^2)^{(d-3)/2}\bar p_t(s),\qquad -1<s<1,
\]
where $C_d>0$ is the geometric constant depending only on $d$.

For $\kappa\ge0$, let
\[
\phi(x;w,\kappa)=C_d^{\mathrm{vMF}}(\kappa)e^{\kappa\langle w,x\rangle}
\]
be the normalized von Mises--Fisher density with respect to $\sigma$, and define
\[
A_d(\kappa)=\frac{I_{d/2}(\kappa)}{I_{d/2-1}(\kappa)},\qquad A_d(0)=0,
\]
where $I_\nu$ is the modified Bessel function of the first kind. Let $\kappa:[0,1]\to[0,\infty)$ be a continuously differentiable strictly increasing schedule with $\kappa_0=0$, write $\dot\kappa_t$ for its derivative on $I$, and set $p_t(\cdot\mid w)=\phi(\cdot;w,\kappa_t)$. The quantities $A_d$ and the normalizing constant have their continuous values at $\kappa=0$.

## Task

Prove the following integrated theorem. First, for every radial density and radial tangent field above, the spherical continuity equation
\[
\partial_t p_t+\operatorname{div}_{\mathbb S^{d-1}}(p_tv_t)=0,
\qquad t\in I,
\]
on $\mathbb S^{d-1}\setminus\{\pm w\}$ is equivalent to
\[
\partial_t f_t+\partial_s\!\left(f_t\psi_t(s)(1-s^2)\right)=0,
\qquad t\in I,\quad -1<s<1.
\]
Second, for the vMF path and each $t\in I$, prove that the scalar equation
\[
(1-s^2)\psi_t'(s)+[\kappa_t(1-s^2)-(d-1)s]\psi_t(s)
=[A_d(\kappa_t)-s]\dot\kappa_t,\qquad -1<s<1,
\]
has a unique solution $\psi_t\in C([-1,1])$, smooth on $(-1,1)$, with
\[
\psi_t(1)=\frac{[1-A_d(\kappa_t)]\dot\kappa_t}{d-1},\qquad
\psi_t(-1)=\frac{[1+A_d(\kappa_t)]\dot\kappa_t}{d-1}.
\]
Show that $v_t(x\mid w)=\psi_t(\langle w,x\rangle)P_x(w)$ with this solution satisfies the spherical continuity equation for the vMF path, with the identity extending continuously to the poles.
