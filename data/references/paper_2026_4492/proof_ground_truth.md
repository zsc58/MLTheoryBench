# Reference Proof

## Proof Structure

Fix the input pair independently of all mechanism randomness. Compute the conditional Gaussian likelihood ratio on the common support, prove monotonicity of its two-sided tail, derive the random-subspace projection bound, and integrate the conditional event inequalities over the common law of the Wishart matrix. All privacy bounds below concern this fixed pair unless explicitly made uniform over neighbors.

## Complete Proof

Write \(\Delta=V-V'\), \(s=\min\{d,n\}\), and let \(P_M\) denote the orthogonal projector onto \(\operatorname{range}(M)\). If \(\Delta=0\), the two output laws are identical. Both required inequalities hold with \(\delta_\alpha(\varepsilon;V,V')=0\), which satisfies the stated bound. Henceforth suppose \(\Delta\ne0\).

### 1. Conditional Gaussian laws and event inequalities

The Gaussian columns of \(Z\) are linearly independent almost surely: conditionally on any preceding linearly independent columns, their span is a proper subspace of \(\mathbb R^d\), which the next Gaussian column hits with probability zero. Thus \(M\) has rank \(r\) almost surely. All subsequent conditional calculations may be restricted to this full-probability event.

Let \(P^M\) and \(Q^M\) be the conditional output laws at \(V\) and \(V'\). They have common support \(\operatorname{range}(M)^n\), means \(MV\) and \(MV'\), and vectorized covariance
\[
\Sigma_M=\sigma_G^2(I_n\otimes M^2).
\]
The covariance is positive definite on that support, so the two measures have positive Gaussian densities there and are mutually absolutely continuous. Put \(m=\operatorname{vec}(MV)\), \(m'=\operatorname{vec}(MV')\), and
\[
q(M)=(m-m')^\top\Sigma_M^\dagger(m-m').
\]
Diagonalizing the symmetric positive semidefinite matrix \(M\) gives
\[
M(M^2)^\dagger M=P_M.
\]
Consequently,
\[
q(M)=\frac{1}{\sigma_G^2}\operatorname{tr}\bigl(\Delta^\top M(M^2)^\dagger M\Delta\bigr)
=\frac{\|P_M\Delta\|_F^2}{\sigma_G^2}.
\]
Expanding the Gaussian densities on the support yields
\[
\ell_M(y):=\log\frac{dQ^M}{dP^M}(y)
=-(m-m')^\top\Sigma_M^\dagger\left(y-\frac{m+m'}2\right).
\]
For \(y\sim P^M\), this affine Gaussian variable has mean \(-q(M)/2\) and variance
\[
(m-m')^\top\Sigma_M^\dagger\Sigma_M\Sigma_M^\dagger(m-m')=q(M).
\]
If \(q(M)=0\), the means agree and the conditional laws coincide. Otherwise direct standardization gives
\[
P^M\{|\ell_M|>\varepsilon\}=T(\varepsilon;q(M)).
\]
For any measurable event \(E\), on \(\{|\ell_M|\le\varepsilon\}\) we have \(dP^M\le e^\varepsilon dQ^M\). Splitting the event therefore proves
\[
P^M(E)\le e^\varepsilon Q^M(E)+T(\varepsilon;q(M)).
\]
Interchanging the inputs, \(\log(dP^M/dQ^M)\) under \(Q^M\) also has mean \(-q(M)/2\) and variance \(q(M)\). Thus the same bound holds in the reverse direction. These statements remain valid when \(q(M)=0\).

### 2. Monotonicity of the tail

Fix \(\varepsilon>0\). For \(t>0\), normal symmetry gives
\[
T(\varepsilon;t^2)=\Phi(a(t))+\Phi(b(t)),\qquad
 a(t)=\frac t2-\frac\varepsilon t,\quad
 b(t)=-\frac t2-\frac\varepsilon t.
\]
Let \(\phi\) be the standard normal density. Since \(b(t)^2-a(t)^2=2\varepsilon\), we have \(\phi(b(t))=e^{-\varepsilon}\phi(a(t))\). Hence
\[
\frac{d}{dt}T(\varepsilon;t^2)
=\phi(a(t))\left[\frac{1-e^{-\varepsilon}}2+rac{\varepsilon}{t^2}(1+e^{-\varepsilon})\right]>0.
\]
Both arguments tend to \(-\infty\) as \(t\downarrow0\), so this is consistent with \(T(\varepsilon;0)=0\). Thus \(T(\varepsilon;\cdot)\) is increasing on \([0,\infty)\).

### 3. Projection-energy tail

For every deterministic orthogonal matrix \(U\), \(UZ\) has the same law as \(Z\). It follows that the law of the rank-\(r\) projector \(P_M\) is invariant under orthogonal conjugation.

For a fixed unit vector \(u\), conjugation invariance implies that the law of \(u^\top P_Mu\) is the same for every unit vector. Let \(h=g/\|g\|_2\), where \(g\sim\mathcal N(0,I_d)\) is independent of \(P_M\). Averaging over \(h\) shows that \(u^\top P_Mu\) has the same law as \(h^\top P_Mh\). Conditional on any rank-\(r\) projector, choose an orthonormal eigenbasis. Gaussian rotational invariance then gives
\[
h^\top P_Mh\ \overset d=\ \frac A{A+B},\qquad
A=\sum_{i=1}^r g_i^2,\quad B=\sum_{i=r+1}^d g_i^2.
\]
The variables \(A\) and \(B\) are independent. Polar coordinates for a standard Gaussian in \(k\) dimensions give the squared-radius density proportional to \(x^{k/2-1}e^{-x/2}\) on \(x>0\). Thus, writing \(a=r/2\) and \(b=(d-r)/2\), the joint density of \((A,B)\) is proportional to
\[
x^{a-1}z^{b-1}e^{-(x+z)/2}.
\]
The change of variables \(w=x/(x+z)\), \(t=x+z\) has Jacobian \(t\). Its joint density is proportional to
\[
w^{a-1}(1-w)^{b-1}t^{a+b-1}e^{-t/2},\qquad 0<w<1,\ t>0.
\]
Integrating out \(t\) and normalizing shows that \(w\) has the \(\operatorname{Beta}(a,b)\) density. Therefore
\[
\Pr\{\|P_Mu\|_2^2>\alpha\}=1-I_\alpha\left(\frac r2,\frac{d-r}2\right).
\]
Both Beta parameters are positive because \(1\le r<d\).

Take an SVD
\[
\Delta=\sum_{j=1}^k\lambda_j u_jv_j^\top,
\qquad k=\operatorname{rank}(\Delta)\le s,\quad \lambda_j>0.
\]
The singular vectors are deterministic because the pair is fixed. Orthonormality of the right singular vectors gives
\[
\|P_M\Delta\|_F^2=\sum_{j=1}^k\lambda_j^2\|P_Mu_j\|_2^2,
\qquad \|\Delta\|_F^2=\sum_{j=1}^k\lambda_j^2.
\]
The ratio of these quantities is a convex combination of the projection fractions. If it exceeds \(\alpha\), some fraction exceeds \(\alpha\). Therefore, with
\[
\mu_\alpha=\frac{\alpha\|\Delta\|_F^2}{\sigma_G^2},\qquad
G=\{M:q(M)\le\mu_\alpha\},
\]
a union bound yields
\[
\Pr(G^c)\le k\left[1-I_\alpha\left(\frac r2,\frac{d-r}2\right)\right]
\le s\left[1-I_\alpha\left(\frac r2,\frac{d-r}2\right)\right].
\]
No independence among the singular-direction projection fractions is used.

### 4. Remove the conditioning

Let \(\nu\) be the law of \(M\), which is the same under both inputs. The event \(G\) depends on the fixed pair and \(M\), not on the noise or output. For every measurable event \(E\), the conditional event inequality and monotonicity give
\[
\begin{aligned}
\Pr[\mathcal M_2(V)\in E]
&\le\int_G P^M(E)\,d\nu(M)+\nu(G^c)\\
&\le e^\varepsilon\int_G Q^M(E)\,d\nu(M)
 +T(\varepsilon;\mu_\alpha)\nu(G)+\nu(G^c)\\
&\le e^\varepsilon\Pr[\mathcal M_2(V')\in E]
 +T(\varepsilon;\mu_\alpha)+\nu(G^c).
\end{aligned}
\]
The same reasoning applies with the pair reversed, since \(q(M)\) and \(G\) are unchanged. Set
\[
B_\alpha=T\left(\varepsilon;\frac{\alpha\|V-V'\|_F^2}{\sigma_G^2}\right)
+s\left[1-I_\alpha\left(\frac r2,\frac{d-r}2\right)\right].
\]
Both inequalities hold with \(\delta_\alpha(\varepsilon;V,V')=\min\{1,B_\alpha\}\): if \(B_\alpha\le1\), this follows from the preceding estimates; otherwise the inequalities with additive constant 1 are automatic. This proves the claimed existence and bound. The parameter is valid for the fixed pair. A global DP statement requires a single additive constant valid for all neighboring pairs.

## Source Corrections and Proof Closure

The inverse-ratio convention resolves the source's sign inconsistency without changing its absolute-value tail. The quadratic form and variance both retain the factor \(\sigma_G^{-2}\), and the variance has no extra factor \(1/2\). The SVD implements the source's complete projection argument rather than its inaccurate arbitrary-basis sketch. Rank, common support, likelihood-ratio conversion, monotonicity, the Beta law, the union bound, mixture integration, both privacy directions, and the zero-difference case have all been established above. No specialized external dependency remains unresolved.
