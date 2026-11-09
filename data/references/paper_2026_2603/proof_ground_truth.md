# Reference Proof

## Proof Structure and Obligations

The theorem-critical obligations are: (1) compute the radial spherical divergence and prove both directions of the flux equivalence; (2) establish that the publicly defined Bessel ratio is the cosine mean and differentiate the vMF normalization; (3) derive the scalar ODE; (4) construct its bounded interior solution and prove cancellation at the opposite endpoint; (5) prove continuous endpoint values and uniqueness in the stated solution class; and (6) justify the classical continuity equation at the poles, including the spatial regularity of the constructed field. All six obligations are derived below. No continuity-equation/flow equivalence, marginal-velocity theorem, or specialized singular-ODE result is invoked.

## Complete Proof

### Radial reduction

Fix t in I=(0,1). Write s=\langle w,x\rangle, q(x)=w-sx=P_x(w), and g_t(s)=\bar p_t(s)\psi_t(s). On the punctured sphere, the local ambient formula u_t(x)=g_t(s)q(x) agrees with the radial flux p_tv_t. Since \nabla g_t(s)=g_t'(s)w and \nabla q=-sI_d-xw^T, its Jacobian is
\[
\nabla u_t=g_t'qw^T+g_t(-sI_d-xw^T).
\]
On the unit sphere, \langle q,x\rangle=0 and \langle q,w\rangle=1-s^2. Therefore
\[
\operatorname{tr}(\nabla u_t)=(1-s^2)g_t'-(d+1)sg_t,
\qquad x^T(\nabla u_t)x=-2sg_t.
\]
The spherical divergence is consequently
\[
\operatorname{div}_{\mathbb S^{d-1}}(p_tv_t)
=(1-s^2)g_t'(s)-(d-1)sg_t(s).
\]
The spherical continuity equation on the punctured sphere is equivalent to
\[
\partial_t\bar p_t+(1-s^2)\partial_s(\bar p_t\psi_t)
-(d-1)s\bar p_t\psi_t=0. \tag{1}
\]
For the cosine density
\[
f_t(s)=C_d(1-s^2)^{(d-3)/2}\bar p_t(s),
\]
its flux derivative is
\[
\partial_s\bigl(f_t\psi_t(1-s^2)\bigr)
=C_d(1-s^2)^{(d-3)/2}
\bigl[(1-s^2)g_t'-(d-1)sg_t\bigr].
\]
Because C_d is independent of t and the prefactor is positive for -1<s<1, division shows that (1) is equivalent to
\[
\partial_tf_t+\partial_s\bigl(f_t\psi_t(1-s^2)\bigr)=0. \tag{2}
\]
Every s in (-1,1) occurs as \langle w,x\rangle for a point on the punctured sphere when d\ge2. Thus the pointwise domains also match, and the same algebra proves the reverse implication.

### Normalization and the Bessel ratio

Put \alpha=(d-1)/2>0 and \nu=d/2-1=\alpha-1/2\ge0. Define
\[
G(\kappa)=\int_{-1}^1 e^{\kappa r}(1-r^2)^{\alpha-1}\,dr.
\]
The weight is integrable, including when d=2. Differentiation with respect to \kappa is justified on every bounded concentration interval by domination by a constant times this weight. The geometric cosine-density constant gives
\[
C_d^{\mathrm{vMF}}(\kappa)\,C_d\,G(\kappa)=1. \tag{3}
\]
For completeness, the special-function identity needed here follows by expanding the exponential and integrating its even terms. The elementary beta integral gives
\[
\int_{-1}^1r^{2m}(1-r^2)^{\alpha-1}\,dr
=\frac{\Gamma(m+1/2)\Gamma(\alpha)}{\Gamma(m+\nu+1)}.
\]
Using \Gamma(m+1/2)/(2m)!=\sqrt\pi/(4^m m!) and the defining Bessel series
\[
I_\nu(\kappa)=\sum_{m=0}^\infty
\frac{(\kappa/2)^{2m+\nu}}{m!\Gamma(m+\nu+1)},
\]
we obtain, for \kappa>0,
\[
G(\kappa)=\sqrt\pi\,\Gamma(\alpha)
(2/\kappa)^\nu I_\nu(\kappa).
\]
Termwise differentiation of the same convergent series yields
\[
I_\nu'(\kappa)-\frac{\nu}{\kappa}I_\nu(\kappa)
=I_{\nu+1}(\kappa).
\]
It follows that
\[
\frac{G'(\kappa)}{G(\kappa)}
=\frac{I_{\nu+1}(\kappa)}{I_\nu(\kappa)}
=A_d(\kappa). \tag{4}
\]
At \kappa=0 the integral G is positive and even, so G'(0)=0; (4) therefore holds with the stipulated continuous value A_d(0)=0. In particular, A_d(\kappa) is the mean of r under the probability density proportional to e^{\kappa r}(1-r^2)^{\alpha-1}. Differentiating (3) now gives
\[
\partial_\kappa\log C_d^{\mathrm{vMF}}(\kappa)=-A_d(\kappa), \tag{5}
\]
including its continuous value at zero.

### Scalar ODE and bounded solution

For a fixed t, abbreviate \kappa=\kappa_t, \dot\kappa=\dot\kappa_t, and A=A_d(\kappa). The vMF cosine density is
\[
f_t(s)=C_dC_d^{\mathrm{vMF}}(\kappa_t)
(1-s^2)^{(d-3)/2}e^{\kappa_ts}.
\]
By (5),
\[
\frac{\partial_tf_t}{f_t}=\dot\kappa(s-A),
\qquad
\partial_s\log f_t=\kappa-\frac{(d-3)s}{1-s^2}.
\]
Expanding (2) and dividing by f_t>0 gives precisely
\[
(1-s^2)\psi_t'(s)
+[\kappa(1-s^2)-(d-1)s]\psi_t(s)
=(A-s)\dot\kappa. \tag{6}
\]
Conversely, reversing this calculation shows that (6) implies (2).

An integrating factor for (6) divided by 1-s^2 is
\[
\mu(s)=e^{\kappa s}(1-s^2)^\alpha.
\]
Thus
\[
(\mu\psi_t)'=\dot\kappa(A-s)e^{\kappa s}(1-s^2)^{\alpha-1}.
\]
The right-hand side is integrable up to both endpoints. If \psi_t is bounded near -1, then \mu(s)\psi_t(s)\to0 there. Integration consequently forces
\[
\psi_t(s)=\dot\kappa e^{-\kappa s}(1-s^2)^{-\alpha}
\int_{-1}^{s}(A-r)e^{\kappa r}(1-r^2)^{\alpha-1}\,dr. \tag{7}
\]
This expression is smooth on (-1,1) and solves (6). Equation (4) proves the necessary cancellation:
\[
\int_{-1}^1(A-r)e^{\kappa r}(1-r^2)^{\alpha-1}\,dr
=AG(\kappa)-G'(\kappa)=0. \tag{8}
\]

### Endpoint values, regularity, and uniqueness

The endpoint behavior can be established without substituting into the singular ODE. For 0<h sufficiently small, substitute r=-1+hu in (7) to obtain
\[
\psi_t(-1+h)=\dot\kappa e^{-\kappa h}(2-h)^{-\alpha}
\int_0^1(A+1-hu)e^{\kappa hu}
 u^{\alpha-1}(2-hu)^{\alpha-1}\,du. \tag{9}
\]
Using (8) to replace the lower integral by minus the upper tail, and then substituting r=1-hu, similarly gives
\[
\psi_t(1-h)=\dot\kappa e^{\kappa h}(2-h)^{-\alpha}
\int_0^1(1-A-hu)e^{-\kappa hu}
 u^{\alpha-1}(2-hu)^{\alpha-1}\,du. \tag{10}
\]
Both right-hand sides are defined for h in an open neighborhood of zero. For example, when |h|<1/2, the factors 2-h and 2-hu stay positive and bounded away from zero. For every fixed derivative order in h, the differentiated integrands are bounded by a constant times u^{\alpha-1}. This is integrable because \alpha>0. Differentiation under the integral therefore proves smooth extensions through h=0, in particular finite endpoint derivatives.

Evaluation at h=0, using \int_0^1u^{\alpha-1}du=1/\alpha, yields
\[
\psi_t(-1)=\frac{(1+A)\dot\kappa}{2\alpha}
=\frac{[1+A_d(\kappa_t)]\dot\kappa_t}{d-1},
\]
\[
\psi_t(1)=\frac{(1-A)\dot\kappa}{2\alpha}
=\frac{[1-A_d(\kappa_t)]\dot\kappa_t}{d-1}.
\]
Hence (7) extends continuously to [-1,1] and is bounded there. If two bounded interior solutions existed, their difference would satisfy the homogeneous equation and would have the form
\[
C e^{-\kappa s}(1-s^2)^{-\alpha}.
\]
Since \alpha>0, this is unbounded near -1 unless C=0. The interior solution is unique, and continuity uniquely determines its endpoint values. Thus there is exactly one solution in C([-1,1]). No division by \dot\kappa has been used; if \dot\kappa=0, the unique bounded solution is identically zero. All endpoint arguments remain valid for d=2.

### Continuity equation at the poles

Equation (6), the flux calculation, and the radial reduction imply the spherical continuity equation on the punctured sphere. Equations (9)-(10) show more than boundedness: \psi_t extends smoothly past both scalar endpoints. Together with its interior smoothness, this gives a smooth extension to a neighborhood of [-1,1]. Consequently
\[
x\longmapsto\psi_t(\langle w,x\rangle)
\bigl(w-\langle w,x\rangle x\bigr)
\]
is smooth on an ambient neighborhood of the sphere. A smooth cutoff equal to one near the sphere gives an extension to all of \mathbb R^d. The vMF density likewise has a smooth spatial ambient extension, so the constructed field meets the standing convention.

With g_t(s)=C_d^{\mathrm{vMF}}(\kappa_t)e^{\kappa_ts}\psi_t(s), both g_t and g_t' have finite continuous endpoint values. Therefore the radial divergence
\[
(1-s^2)g_t'(s)-(d-1)sg_t(s)
\]
is continuous up to s=\pm1, and the first term vanishes at each endpoint. At x=w its value is
\[
-(d-1)p_t(w\mid w)\psi_t(1)
=-p_t(w\mid w)(1-A)\dot\kappa,
\]
which cancels \partial_tp_t(w\mid w)=p_t(w\mid w)(1-A)\dot\kappa. At x=-w its value is
\[
(d-1)p_t(-w\mid w)\psi_t(-1)
=p_t(-w\mid w)(1+A)\dot\kappa,
\]
which cancels \partial_tp_t(-w\mid w)=-p_t(-w\mid w)(1+A)\dot\kappa. The classical continuity equation therefore holds on the whole sphere, and its identity extends continuously to both poles.
