# Reference Proof

## Proof Structure

Differentiate the zero-nudge update through the perturbed equilibrium, combine the resulting expression with the separable-energy identity, and use first-order optimality at the free constrained equilibrium. Then evaluate the invariant for the two circuit parameterizations. No Hessian inverse or derivative of the free equilibrium with respect to the parameters is needed.

## Complete Proof

Fix a time and hold the parameter vector fixed while varying the nudge. Write
\[
 y:=\left.\frac{d z_\varepsilon}{d\varepsilon}\right|_{\varepsilon=0}.
\]
In Scheme I, the minimization problem at zero nudge is exactly the free problem. In Scheme II, the free minimizer satisfies the additional zero-nudge output constraint. Every competitor in that smaller feasible set is also feasible for the free problem, so the free minimizer remains its unique minimizer. Thus, in either scheme, the perturbed state at zero is the specified \(z_0\).

Smoothness of \(E\), differentiability of the perturbed state, and the update definition now give
\[
 \dot\theta_i
 =\left.\frac{d}{d\varepsilon}\partial_{\theta_i}E(z_\varepsilon;\theta)\right|_{\varepsilon=0}
 =\left\langle\partial_{\theta_i}\nabla_zE(z_0;\theta),y\right\rangle.
\]
The parameter partial derivative in this formula acts only on the parameter argument of the energy.

Both schemes retain \(A^Tz_\varepsilon=a\), so differentiation gives \(A^Ty=0\). Consequently \(z_0+\tau y\) is feasible for the free minimization problem for every real \(\tau\). The differentiable scalar function \(\tau\mapsto E(z_0+\tau y;\theta)\) has a minimum at zero. Its derivative there is therefore zero:
\[
 \langle\nabla_zE(z_0;\theta),y\rangle=0. \tag{1}
\]
This argument works separately for either scheme and does not require independent constraint columns, a nondegenerate Hessian, or an inverse-based formula for \(y\).

The state derivatives of the separable factors are well-defined under the stated assumptions. Indeed, differentiating the energy representation in the parameter argument gives
\[
 \partial_{\theta_i}E(z;\theta)=h_i'(\theta_i)U_i(z).
\]
At any fixed parameter vector, the nonzero scalar \(h_i'(\theta_i)\) expresses \(U_i\) as a constant multiple of the smooth function \(\partial_{\theta_i}E(\cdot;\theta)\). Hence \(U_i\) is smooth in the state variables, and
\[
 \partial_{\theta_i}\nabla_zE(z;\theta)=h_i'(\theta_i)\nabla U_i(z).
\]
Using \(F_i'=h_i/h_i'\), it follows that
\[
 \sum_{i=1}^mF_i'(\theta_i)\partial_{\theta_i}\nabla_zE(z_0;\theta)
 =\sum_{i=1}^m h_i(\theta_i)\nabla U_i(z_0)
 =\nabla_zE(z_0;\theta). \tag{2}
\]
The chain rule along a differentiable parameter trajectory, followed by (2) and (1), yields
\[
 \begin{aligned}
 \frac{dM}{dt}
 &=\frac12\sum_{i=1}^m F_i'(\theta_i)\dot\theta_i\\
 &=\frac12\left\langle\sum_{i=1}^mF_i'(\theta_i)\partial_{\theta_i}\nabla_zE(z_0;\theta),y\right\rangle\\
 &=\frac12\langle\nabla_zE(z_0;\theta),y\rangle=0.
 \end{aligned}
\]
A differentiable real-valued function with zero derivative on an interval is constant there. This proves the general claim on every interval covered by the task. No continuation through parameter-domain boundaries is asserted.

For the conductance circuit, write
\[
 U_j(z)=\frac12(d_j^Tz)^2,
 \qquad E(z;c)=\sum_jc_jU_j(z).
\]
Here \(h_j(c_j)=c_j\), so \(F_j'(c_j)=c_j\). Taking \(F_j(c_j)=c_j^2/2\), the general result conserves \(\frac14\sum_jc_j^2\). Multiplying by \(2\) gives conservation of the requested \(\frac12\sum_jc_j^2\).

For the resistance circuit,
\[
 E(z;s)=\sum_js_j^{-1}U_j(z).
\]
Positivity of the resistance parameters makes this parameterization smooth. We have \(h_j(s_j)=s_j^{-1}\), \(h_j'(s_j)=-s_j^{-2}\), and therefore \(F_j'(s_j)=-s_j\). Taking \(F_j(s_j)=-s_j^2/2\), the general result conserves \(-\frac14\sum_js_j^2\). Multiplying by \(-2\) gives conservation of the requested positive quantity \(\frac12\sum_js_j^2\).

## Source Audit Notes

All theorem-critical obligations above are closed directly. The source's assertion that strict convexity implies a positive-definite constrained Hessian is not used and is false in general, as documented in theory_008. Its inverse-based sensitivity formulas must not be treated as automatic consequences of the public assumptions. The retained factor \(1/2\) implements the normalization correction recorded in theory_003 and theory_004; the resistance rescaling implements the sign correction already recorded in theory_006.
