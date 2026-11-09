# Reference Proof

## Proof Structure

1. On a window containing a switch, split the exact residual into its pre-switch and post-switch parts and use the affine parameterization plus the information-matrix lower bound.
2. Minimize the resulting weighted quadratic and derive both the harmonic-length and half-minimum lower bounds; if there is no switch, choose the active parameter.
3. On a post-switch set, decompose the approximate residual into derivative error, state error, and parameter mismatch, then apply the triangle inequality, Lipschitz control, and mismatch identifiability.
4. Transfer the continuous bound to the weighted discrete residual using the stated quadrature error, and specialize to the opposite regime parameter under the hypotheses for that choice.

## Complete Proof

All integral identities are understood almost everywhere. The isolated switching time and interval endpoints have zero Lebesgue measure.

If the interval window \(I\) does not contain \(\tau\), it lies on one side of the switch. The true trajectory therefore satisfies the equation with one active parameter \(\theta^{\mathrm{true}}\in\{\theta^-,\theta^+\}\subseteq\Theta\) almost everywhere on \(I\). Choosing this parameter gives \(R_I(\theta^{\mathrm{true}})=0\). Since residual energies are nonnegative, \(\underline R_I=0\).

Now suppose \(a=|I^-|>0\) and \(b=|I^+|>0\). Both pieces are subintervals, so the information-matrix bound applies to them. For every \(\theta\in\Theta\), the exact equations and affine representation give
\[
R_I(\theta)
=(\theta^- -\theta)^\top M(I^-)(\theta^- -\theta)
 +(\theta^+ -\theta)^\top M(I^+)(\theta^+ -\theta).
\]
The common offset cancels on each piece. The matrix eigenvalue bound consequently yields
\[
R_I(\theta)\ge\alpha\bigl(a\|\theta^- -\theta\|_2^2+b\|\theta^+ -\theta\|_2^2\bigr).
\]
Set
\[
\theta_0=\frac{a\theta^-+b\theta^+}{a+b}.
\]
Expanding the squares and using
\(a(\theta^- -\theta_0)+b(\theta^+ -\theta_0)=0\) gives
\[
a\|\theta^- -\theta\|_2^2+b\|\theta^+ -\theta\|_2^2
=(a+b)\|\theta-\theta_0\|_2^2
+\frac{ab}{a+b}\|\theta^- -\theta^+\|_2^2.
\]
Indeed, \(\theta^- -\theta_0=b(\theta^- -\theta^+)/(a+b)\) and \(\theta^+ -\theta_0=-a(\theta^- -\theta^+)/(a+b)\), giving the displayed constant term. Thus the unconstrained minimum is the second term. It is unnecessary for \(\theta_0\) to belong to \(\Theta\): the identity lower-bounds the quadratic for every admissible parameter. Taking the infimum gives
\[
\underline R_I\ge\alpha\frac{ab}{a+b}\|\theta^- -\theta^+\|_2^2.
\]
If \(a\le b\), then \(a+b\le2b\), so \(ab/(a+b)\ge a/2\). Interchanging \(a,b\) proves
\[
\frac{ab}{a+b}\ge\frac12\min\{a,b\},
\]
and hence the second claimed lower bound.

For the approximate statement, fix the parameter and other objects satisfying its hypotheses. Write
\[
D(t)=\dot{\widehat x}(t)-f(t,\widehat x(t);\widetilde\theta),
\quad
D_*(t)=\dot x^*(t)-f(t,x^*(t);\widetilde\theta).
\]
On \(E_+\), the exact equation gives
\[
D_*(t)=f(t,x^*(t);\theta^+)-f(t,x^*(t);\widetilde\theta)
\]
almost everywhere. Adding and subtracting the exact derivative and the field at the exact state yields
\[
D-D_*=(\dot{\widehat x}-\dot x^*)
+f(\cdot,x^*;\widetilde\theta)-f(\cdot,\widehat x;\widetilde\theta).
\]
The pointwise state-Lipschitz hypothesis and integration give
\[
\|f(\cdot,x^*;\widetilde\theta)-f(\cdot,\widehat x;\widetilde\theta)\|_{L^{p_y}(E_+)}
\le L\|\widehat x-x^*\|_{L^{p_y}(E_+)}.
\]
All norms are finite and \(1\le p_y<\infty\), so the triangle inequality applies. Applying it first to \(D-D_*\) and then to \(D_*=D-(D-D_*)\) shows
\[
\|D\|_{L^{p_y}(E_+)}
\ge\|D_*\|_{L^{p_y}(E_+)}
-\|\dot{\widehat x}-\dot x^*\|_{L^{p_y}(E_+)}
-L\|\widehat x-x^*\|_{L^{p_y}(E_+)}.
\]
Mismatch identifiability therefore gives
\[
\|D\|_{L^{p_y}(E_+)}
\ge\gamma_+\|\theta^+-\widetilde\theta\|_2-\varepsilon_+.
\]
The left side is also nonnegative, so, with
\(A=(\gamma_+\|\theta^+-\widetilde\theta\|_2-\varepsilon_+)_+\), we have \(\|D\|_{L^{p_y}(E_+)}\ge A\).

Let
\[
q=\|D\|_{L^{p_y}(E_+)}^{p_y},
\qquad
q_N=\sum_{j=1}^{N_{r,+}}w_j\|D(t_j)\|_2^{p_y}
=\mathcal R_{N,+}^{p_y}.
\]
The powered quadrature assumption, with its distinct exponent \(\alpha_q\), implies
\[
q_N\ge q-C_{q,+}N_{r,+}^{-\alpha_q}
\ge A^{p_y}-C_{q,+}N_{r,+}^{-\alpha_q}.
\]
Positive weights give \(q_N\ge0\). Hence
\[
q_N\ge\left[A^{p_y}-C_{q,+}N_{r,+}^{-\alpha_q}\right]_+.
\]
Taking the increasing \(1/p_y\) power proves
\[
\mathcal R_{N,+}\ge
\left[
\bigl(\gamma_+\|\theta^+-\widetilde\theta\|_2-\varepsilon_+\bigr)_+^{p_y}
-C_{q,+}N_{r,+}^{-\alpha_q}
\right]_+^{1/p_y}.
\]
This also covers a nonpositive expression inside either positive part and \(C_{q,+}=0\); no division by these quantities occurs.

Finally, apply this same conditional statement with \(\widetilde\theta=\theta^-\), when its hypotheses hold for that choice. The mismatch factor becomes \(\|\theta^+-\theta^-\|_2\). The Lipschitz, mismatch, and quadrature constants are those valid for this parameter choice; the argument does not assert that constants for a different fixed parameter remain valid.

## Obligation Closure

The no-switch choice, exact residual decomposition, eigenvalue comparison, constrained-infimum comparison, quadratic minimum, half-minimum comparison, finite-norm residual estimate, mismatch comparison, positive-part quadrature transfer, and parameter specialization have all been derived above. No external theorem conclusion is used, and no unresolved ground-truth obligation remains.
