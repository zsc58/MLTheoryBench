# Reference Proof

## Obligations and source basis

The proof must establish: (1) the unrestricted conditional optimization and its upper bound for neural candidates; (2) unique conditional diagonalization and global maximization in the compact stable region; (3) an expectation-valid second-order expansion and positive definiteness; (4) transfer to the local neural supremum with the correct baseline and delta quantifier; and (5) the full-coordinate Moore-Penrose Schur-complement identity. The relevant source material is theory_001, theory_002, theory_004, theory_005, theory_006, theory_007, theory_008, and theory_009. The calculations below close every obligation directly; no specialized external result or unavailable appendix is assumed.

## 1. Unrestricted conditional optimization

Use the normalization of Q^* specified in the task, including the constant -log(2pi)-1. Write Gamma_0=Gamma(gamma_0), d_0=d(gamma_0), and D_0(x)=diag(g_10(x),g_20(x)).

For a fixed gamma, let m_k=m^*_{gamma,k}(x), v_k=v^*_{gamma,k}(x), and let f_k and g_k>0 be any candidate conditional mean and variance functions. Conditional second moments give
\[
E[e_k^2\mid x]=v_k+(m_k-f_k)^2.
\]
Consequently, the conditional expected criterion loss relative to the unrestricted optimum is
\[
\frac12\sum_{k=1}^2\left[\log\frac{g_k}{v_k}+\frac{v_k}{g_k}-1+\frac{(m_k-f_k)^2}{g_k}\right]\geq0.
\]
Indeed, for t>0, log(t)+t^{-1}-1 is minimized at t=1, with value zero. This proves the conditional optimum is attained at f_k=m_k and g_k=v_k and proves Q(gamma,eta)<=Q^*(gamma) wherever Q is finite. No Gaussian distributional assumption is used. Exact representation at eta_0 gives Q(gamma_0,eta_0)=Q^*(gamma_0).

## 2. Residual representation and global uniqueness

The structural system implies
\[
\Gamma_0y=f_0(x)+\varepsilon.
\]
Taking conditional means and subtracting yields
\[
r_\gamma=A(\gamma)\varepsilon,\qquad A(\gamma)=\Gamma(\gamma)\Gamma_0^{-1}
=\frac1{d_0}\begin{pmatrix}
1-\gamma_1\gamma_{20}&\gamma_{10}-\gamma_1\\
\gamma_{20}-\gamma_2&1-\gamma_2\gamma_{10}
\end{pmatrix}.
\]
Let S_gamma(x)=A(gamma)D_0(x)A(gamma)^T and C_gamma(x)=(S_gamma(x))_12. Then
\[
C_\gamma(x)=\frac{(1-\gamma_1\gamma_{20})(\gamma_{20}-\gamma_2)g_{10}(x)
 +(\gamma_{10}-\gamma_1)(1-\gamma_2\gamma_{10})g_{20}(x)}{d_0^2}.
\]
If C_gamma=0 almost surely, division by g_20 shows that a constant multiple of rho_0 plus a constant is zero almost surely. Nonconstancy of rho_0 forces both coefficients to vanish. For gamma in the stable candidate region, both 1-gamma_1 gamma_20 and 1-gamma_2 gamma_10 are at least 1-bar_gamma^2>0. Thus gamma_2=gamma_20 and gamma_1=gamma_10. This argument includes zero true coefficients and coefficients on the boundary of the compact region.

The determinant satisfies
\[
\det S_\gamma(x)=\frac{d(\gamma)^2}{d_0^2}g_{10}(x)g_{20}(x)>0.
\]
Its diagonal entries are v^*_{gamma,1},v^*_{gamma,2}, so
\[
v^*_{\gamma,1}v^*_{\gamma,2}=\det S_\gamma+C_\gamma^2.
\]
All required logarithms are integrable. In fact, if A=(a_jk), then
\[
\frac{v^*_{\gamma,1}}{g_{10}}=a_{11}^2+\frac{a_{12}^2}{\rho_0},\qquad
\frac{v^*_{\gamma,2}}{g_{20}}=a_{22}^2+a_{21}^2\rho_0.
\]
The bounded ratio and compact stability restriction bound these quantities above and away from zero uniformly over the candidate region. Hence each log v^* differs from its corresponding log g_k0 by a uniformly bounded function. The same conclusion holds in a sufficiently small ambient neighborhood of gamma_0.

Subtracting the two normalized profile values gives
\[
Q^*(\gamma)-Q^*(\gamma_0)
=-\frac12E\log\left(\frac{v^*_{\gamma,1}v^*_{\gamma,2}}{\det S_\gamma}\right)
=-\frac12E\log\left(1+\frac{C_\gamma^2}{\det S_\gamma}\right)\leq0.
\]
The nonnegative integrand has expectation zero exactly when C_gamma=0 almost surely. The preceding diagonalization argument therefore proves that gamma_0 is the unique maximizer over the stable candidate region. The non-strict comparison also holds in the ambient nonsingular neighborhood, which will justify local first-order conditions.

## 3. Uniform local expansion

Put gamma=gamma_0+h and rho=rho_0(x). The exact covariance formula gives the standardized identity
\[
\frac{C_{\gamma_0+h}(x)}{\sqrt{g_{10}(x)g_{20}(x)}}
=-\frac{h_2\sqrt\rho+h_1/\sqrt\rho}{d_0}
+\frac{h_1h_2}{d_0^2}\left(\gamma_{20}\sqrt\rho+\frac{\gamma_{10}}{\sqrt\rho}\right).
\]
Because rho and its reciprocal are bounded, the second term is O(||h||^2) uniformly in x, and the whole expression is O(||h||). Also d(gamma_0+h)=d_0+O(||h||), with d bounded away from zero. It follows that
\[
\frac{C_{\gamma_0+h}^2}{\det S_{\gamma_0+h}}
=\frac{(h_2\sqrt\rho+h_1/\sqrt\rho)^2}{d_0^2}+O(\|h\|^3)
\]
uniformly in x. Since log(1+t)=t+O(t^2) for nonnegative t near zero, the same uniform control permits taking expectations in the preceding profile comparison. Thus
\[
Q^*(\gamma_0+h)-Q^*(\gamma_0)
=-\frac1{2d_0^2}E\left[h_2^2\rho_0+2h_1h_2+h_1^2\rho_0^{-1}\right]+o(\|h\|^2)
=-\frac12h^TI_\gamma^*h+o(\|h\|^2).
\]
This justifies the expectation expansion without imposing moments on the absolute scale of the conditional variances.

Both diagonal entries of I_gamma^* are positive and finite. Cauchy-Schwarz applied to sqrt(rho_0) and 1/sqrt(rho_0) gives
\[
E\rho_0\,E\rho_0^{-1}\geq1.
\]
Equality would make these two random variables proportional almost surely and hence make rho_0 constant almost surely. Therefore
\[
\det I_\gamma^*=d_0^{-4}(E\rho_0\,E\rho_0^{-1}-1)>0,
\]
and I_gamma^* is positive definite.

## 4. Transfer to the neural supremum

Choose delta_0>0 small enough that the slice ball of radius delta_0 is inside the coordinate neighborhood on which the stated regularity holds. Fix any 0<delta<delta_0. Since a^*(0)=0 and a^* is continuous, ||a^*(h)||<delta for all sufficiently small h. The unrestricted upper bound and the assumed approximation along the path imply
\[
Q(\gamma_0+h,\eta_0+a^*(h))
\leq Q_{\delta,\eta_0}(\gamma_0+h)
\leq Q^*(\gamma_0+h).
\]
The outer values differ by o(||h||^2). At h=0, exact representation and the same upper bound give
\[
Q_{\delta,\eta_0}(\gamma_0)=Q(\gamma_0,\eta_0)=Q^*(\gamma_0).
\]
Consequently,
\[
Q_{\delta,\eta_0}(\gamma_0+h)-Q_{\delta,\eta_0}(\gamma_0)
=-\frac12h^TI_\gamma^*h+o(\|h\|^2).
\]
The little-o statement is for each fixed sufficiently small delta; no uniformity over delta is needed or asserted. Positive definiteness makes this difference strictly negative for every sufficiently small nonzero h. Thus gamma_0 is a strict local maximizer and the interaction coordinate is locally identified on the slice. This does not assert uniqueness of neural weights or identification outside the local slice neighborhood.

## 5. Schur complement with nuisance kernel

We now derive the Schur identity rather than merely invoking a profiling formula. Set Q_0=Q(gamma_0,eta_0). The inequalities Q(gamma,eta)<=Q^*(gamma)<=Q_0 near the truth show that the differentiable criterion restricted to the slice has a local maximum at (gamma_0,eta_0). Its first derivatives in gamma and slice nuisance coordinates therefore vanish.

Let U have orthonormal columns spanning T_eta0, and write a=Ub. Define
\[
H=U^TJ_{\eta\eta}U,\qquad L=J_{\gamma\eta}U,\qquad A=J_{\gamma\gamma}.
\]
For a nonzero-dimensional slice, H is positive definite. Taylor expansion on the slice gives
\[
Q(\gamma_0+h,\eta_0+Ub)-Q_0
=-\frac12\{h^TAh+2h^TLb+b^THb\}+o(\|h\|^2+\|b\|^2).
\]
Put S=A-LH^{-1}L^T. Completing the square rewrites the quadratic expression as
\[
h^TSh+(b+H^{-1}L^Th)^TH(b+H^{-1}L^Th).
\]
For the trial perturbation b=-H^{-1}L^Th, the upper bound by Q^*(gamma_0+h) and the expansion already proved imply S-I_gamma^* is positive semidefinite: substitute h=tu for each fixed u and divide by t^2.

On the other hand, differentiability of the anchored compatibility path gives
\[
U^Ta^*(h)=Dh+o(\|h\|)
\]
for a fixed matrix D. Substituting this path into the Taylor expansion and using its o(||h||^2) agreement with Q^* yields
\[
I_\gamma^*=S+(D+H^{-1}L^T)^TH(D+H^{-1}L^T).
\]
Thus I_gamma^*-S is positive semidefinite as well. It follows that S=I_gamma^*.

Finally, J_eta eta is symmetric positive semidefinite with kernel K_eta0 and orthogonal complement T_eta0. Its Moore-Penrose inverse is therefore U H^{-1} U^T: it acts as the inverse on T_eta0 and as zero on K_eta0. The cross block annihilates K_eta0, exactly as assumed. Hence
\[
J_{\gamma\gamma}-J_{\gamma\eta}J_{\eta\eta}^{+}J_{\eta\gamma}
=A-LH^{-1}L^T=S=I_\gamma^*.
\]
If T_eta0 has dimension zero, the local profile is Q(gamma,eta_0), the compatibility path is identically zero, and its expansion directly gives J_gamma gamma=I_gamma^*. In that case J_eta eta=0 and its pseudoinverse is zero, so the same identity holds. This also covers an empty nuisance coordinate vector under the usual zero-dimensional conventions.

All five obligations are closed.
