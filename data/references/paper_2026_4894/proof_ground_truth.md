# Reference Proof

## Contract and Proof Obligations

This is a conditional statement about a given classical solution, not an existence theorem for the coupled PDE. The matrices A and V are fixed; A is symmetric positive definite and V is symmetric. No commutation condition or sign condition on V is assumed. The generator has unit radial mass and finite second moment. The equations apply at positive times, with continuous initial traces and nonnegative damping; damping need not be integrable through zero.

The obligations are:

1. Identify the actual solution's spatially linear velocity and justify its time regularity.
2. Construct its invertible linear characteristic flow, derive the density pushforward directly, and obtain preservation of the elliptic family and the mean/scatter equations.
3. Prove that the given potential, rather than merely a proposed ansatz, is purely quadratic; then derive its symmetric coefficient equation and initial condition.
4. Derive the elliptic moment identity and close the matrix system.

All four obligations are proved below. No external mean-field limit, accelerated-convergence theorem, or particle approximation is needed.

## Complete Proof

If T=0, the conclusion follows immediately from the initial values, with C_0=0. Assume henceforth T>0.

### 1. The actual velocity and its linear flow

Define
\[
M_t=\int_{\mathbb R^d}\nabla\Phi_t(y)y^\top\rho_t(y)\,dy,
\qquad C_t=M_tA.
\]
These entries are absolutely integrable: since A is invertible, testing the stipulated absolute convergence of the vector integral at x=A^{-1}e_j gives integrability of each component of y_j\nabla\Phi_t(y)\rho_t(y). Consequently,
\[
\int_{\mathbb R^d}(y^\top Ax)\nabla\Phi_t(y)\rho_t(y)\,dy=C_tx.
\]
Evaluating this identity at the coordinate vectors shows that continuity of the stipulated vector integral makes C continuous on [0,T]. Also C_0=0 because \(\Phi_0\equiv0\).

The density equation becomes
\[
\partial_t\rho_t+\nabla\!\cdot(\rho_tC_tx)=0. \tag{1}
\]
Let G solve
\[
\dot G_t=C_tG_t,\qquad G_0=I_d.
\]
Existence on [0,T] follows, for example, from the time-ordered Picard series: if B=max_{[0,T]}\|C_t\|, its term of order n is bounded by (Bt)^n/n!, so the series converges uniformly and solves the integral equation. The same construction gives H solving \(\dot H_t=-H_tC_t\), \(H_0=I_d\). Differentiating H_tG_t gives H_tG_t=I_d, so G_t is invertible throughout the interval. Jacobi's formula now yields
\[
J_t:=\det G_t=\exp\!\left(\int_0^t\operatorname{tr}C_s\,ds\right)>0.
\]

### 2. Density pushforward and elliptic preservation

For each fixed z, the chain rule and (1) imply, at positive times,
\[
\frac{d}{dt}\bigl[\rho_t(G_tz)J_t\bigr]
=J_t\bigl[\partial_t\rho_t+\nabla\rho_t\cdot C_tG_tz
+\rho_t\operatorname{tr}C_t\bigr](G_tz)=0.
\]
Continuity at zero therefore gives
\[
\rho_t(x)=J_t^{-1}\rho_0(G_t^{-1}x). \tag{2}
\]
This proves the characteristic pushforward directly; it does not rely on an unchecked application of a general continuity-equation theorem.

Set
\[
m_t=G_tm_0,\qquad \Sigma_t=G_t\Sigma_0G_t^\top.
\]
For every nonzero v,
\[
v^\top\Sigma_tv=(G_t^\top v)^\top\Sigma_0(G_t^\top v)>0.
\]
Moreover,
\[
\Sigma_t^{-1}=G_t^{-\top}\Sigma_0^{-1}G_t^{-1},
\qquad
\det\Sigma_t=J_t^2\det\Sigma_0.
\]
Substitution into (2) proves
\[
\rho_t=\mathcal E(m_t,\Sigma_t,g).
\]
Differentiating the parameter definitions yields
\[
\dot m_t=C_tm_t,
\qquad
\dot\Sigma_t=C_t\Sigma_t+\Sigma_tC_t^\top. \tag{3}
\]
Here \(\Sigma_t\) is the scatter parameter; its relation to the covariance is established below.

### 3. Quadratic preservation for the given potential

The same C, defined from the given solution rather than from an ansatz, rewrites the potential equation as
\[
\partial_t\Phi_t(x)+(C_tx)\cdot\nabla\Phi_t(x)
=-\alpha_t\Phi_t(x)+\frac12x^\top Vx. \tag{4}
\]
Define, privately for the proof,
\[
q_t(z)=\Phi_t(G_tz),\qquad Q_t=G_t^\top VG_t.
\]
Then Q_t is symmetric and
\[
\dot q_t(z)+\alpha_tq_t(z)=\frac12z^\top Q_tz,
\qquad q_0(z)=0. \tag{5}
\]
The initial condition follows from joint continuity and G_0=I_d.

We prove polynomial preservation without assuming integrability of \(\alpha\) at zero. Construct a symmetric matrix R_t from the values of the actual q_t by
\[
(R_t)_{ii}=2q_t(e_i),
\]
\[
(R_t)_{ij}=(R_t)_{ji}
=q_t(e_i+e_j)-q_t(e_i)-q_t(e_j),\qquad i<j.
\]
Equation (5), evaluated at these finitely many points, gives
\[
\dot R_t+\alpha_tR_t=Q_t,\qquad R_0=0.
\]
For any fixed z, set
\[
r_t(z)=q_t(z)-\frac12z^\top R_tz.
\]
It satisfies \(\dot r_t(z)=-\alpha_tr_t(z)\) for t>0 and is continuous with r_0(z)=0. Hence
\[
\frac{d}{dt}r_t(z)^2=-2\alpha_tr_t(z)^2\leq0.
\]
For 0<s<t, this gives \(r_t(z)^2\leq r_s(z)^2\); letting s decrease to zero proves r_t(z)=0. Thus the actual transported potential is purely quadratic for every z and t.

Define
\[
P_t=G_t^{-\top}R_tG_t^{-1}.
\]
It is symmetric, continuous at zero with P_0=0, and differentiable at positive times. Since G_t is invertible,
\[
\Phi_t(x)=\frac12x^\top P_tx.
\]
Substitution into (4) and comparison of symmetric quadratic coefficients gives
\[
\dot P_t=-\alpha_tP_t-(C_t^\top P_t+P_tC_t)+V. \tag{6}
\]
In particular, no commutation of the matrices has been used.

For comparison with a general quadratic ansatz, its linear and constant coefficients would satisfy
\[
\dot b_t+C_t^\top b_t=-\alpha_tb_t,
\qquad \dot c_t=-\alpha_tc_t,
\qquad b_0=c_0=0.
\]
Then \(G_t^\top b_t\) and c_t satisfy the same homogeneous dissipative equation as r_t(z), so they vanish. These coefficient equations alone would not justify restricting an arbitrary given potential to the quadratic class; the preceding characteristic argument supplies that missing justification.

### 4. Moments and closure

Let Z have density \(g(\|z\|^2)\). Its second moment is finite by assumption, and its first absolute moment is finite by Cauchy–Schwarz and unit mass. Reflection symmetry gives \(\mathbb E Z=0\) and zero off-diagonal second moments. Coordinate permutations give equal diagonal second moments. Therefore
\[
\mathbb E[ZZ^\top]=\kappa_gI_d,
\qquad
\kappa_g=\frac1d\int_{\mathbb R^d}\|z\|^2g(\|z\|^2)\,dz.
\]
This number is finite and strictly positive because g is positive and d is positive.

For symmetric \(\Sigma\succ0\), its positive square root exists by orthogonal diagonalization. The change of variables \(Y=m+\Sigma^{1/2}Z\) gives exactly the density \(\mathcal E(m,\Sigma,g)\). Consequently,
\[
\mathbb EY=m,
\qquad \operatorname{Cov}(Y)=\kappa_g\Sigma,
\qquad
\mathbb E[YY^\top]=\kappa_g\Sigma+mm^\top. \tag{7}
\]
In particular, all the evolved densities have finite second moment.

Since \(\nabla\Phi_t(y)=P_ty\), the definition of C and (7) now give
\[
C_t=P_t\left(\int_{\mathbb R^d}yy^\top\rho_t(y)\,dy\right)A
=P_t(\kappa_g\Sigma_t+m_tm_t^\top)A. \tag{8}
\]
Equations (3), (6), and (8) are the requested closed system, with the stated initial values. Their construction proves the result for the given solution throughout its stipulated interval. Centered initial laws, V=0, and zero damping require no separate restriction or division by a potentially vanishing quantity.

## Source and Dependency Closure

The source's linear-velocity and characteristic argument appears at L000437–L000446; its transport equation and coefficient equations appear at L000447–L000454; its moment closure appears at L000455–L000456. The argument above supplies the omitted transport-to-quadratic justification and derives the precise affine-density and characteristic facts directly. Thus the uses indexed by theory_016 and theory_017 have explicit statements, verified hypotheses, and complete elementary proofs here.

The accelerated PDE itself is a premise of the public problem. Its selected source derivation is also consistent: after the source's formal integration by parts, the kinetic functional is
\[
K(\rho,\Phi)=\frac12\iint
\langle\nabla\Phi(x),\nabla\Phi(y)\rangle(y^\top Ax)
\rho(x)\rho(y)\,dx\,dy.
\]
The kernel in this double integral is symmetric because A is symmetric. Varying the two density factors therefore produces two equal terms, canceling the factor one-half and yielding precisely the interaction term in the stipulated potential equation. The potential variation is \(-x^\top Vx/2\). No invertibility of the bilinear mobility on the full cotangent space is used in this computation or in the preservation proof. Re-deriving this contextual PDE construction is not an additional scored obligation for the public problem.

There are no unresolved private proof obligations.
