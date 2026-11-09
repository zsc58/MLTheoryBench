# Reference Proof

## Proof Structure

The theorem-critical obligations are: derive both constrained stationarity equations; subtract them and control the normal-cone contribution; justify the masked symmetrization inequality; establish the spectral and Frobenius comparisons; use strictness to force equality of the factors; and transfer stationarity with the correct symmetric-objective gradient normalization. Each obligation is derived below.

## Complete Proof

Write \(U=U^*\), \(V=V^*\), and set
\[
C=\mathbb R_+^{n\times r},\qquad M=P_E(X),\qquad A=UV^\top,\qquad Q=P_E(A),\qquad D=U-V.
\]
Use the Frobenius inner product \(\langle B,H\rangle=\operatorname{Tr}(B^\top H)\). The coordinate mask is self-adjoint and idempotent. In particular, for every matrix \(B\),
\[
\langle P_E(B),B\rangle=\sum_{(i,j)\in E}B_{ij}^2=\|P_E(B)\|_F^2.
\]
Symmetry of the mask implies \(P_E(B^\top)=P_E(B)^\top\). Thus \(M=M^\top\) and \(Q^\top=P_E(VU^\top)\).

### 1. Stationarity, subtraction, and normal-cone signs

For \(Z\in C\), the normal cone is
\[
N_C(Z)=\{\xi:\langle\xi,Y-Z\rangle\le0\text{ for every }Y\in C\}.
\]
Differentiating the asymmetric objective and using criticality gives normals \(\xi_U\in N_C(U)\), \(\xi_V\in N_C(V)\) such that
\[
0=(Q-M)V+\lambda D+\xi_U,
\qquad
0=(Q-M)^\top U-\lambda D+\xi_V.
\]
Subtracting yields
\[
(2\lambda I_n+M)D=Q^\top U-QV-\xi_U+\xi_V. \tag{1}
\]
Since \(U,V\in C\), the normal-cone definition gives
\[
\langle\xi_U,V-U\rangle\le0,
\qquad
\langle\xi_V,U-V\rangle\le0.
\]
Consequently,
\[
\langle-\xi_U+\xi_V,D\rangle\le0. \tag{2}
\]
These inequalities hold also when either factor has zero entries.

### 2. Spectral lower bound and masked symmetrization

For any real symmetric matrix \(H\) and positive semidefinite matrix \(B\),
\[
\lambda_{\min}(H)\operatorname{Tr}(B)
\le\operatorname{Tr}(HB)
\le\lambda_{\max}(H)\operatorname{Tr}(B).
\]
Indeed, in an orthonormal eigenbasis of \(H\), the diagonal entries of \(B\) are nonnegative and sum to its trace, so the middle expression is a weighted sum of the eigenvalues of \(H\). This verifies the spectral trace bound used here without an unresolved external dependency.

Apply the lower bound to \(H=2\lambda I_n+M\) and \(B=DD^\top\succeq0\):
\[
\langle(2\lambda I_n+M)D,D\rangle
\ge (2\lambda+\sigma_n(M))\|D\|_F^2. \tag{3}
\]
Set \(S=(Q+Q^\top)/2\), which is symmetric. Direct expansion gives
\[
\begin{aligned}
\langle Q^\top U-QV,D\rangle
&=\langle S,UU^\top+VV^\top\rangle-2\langle Q,A\rangle,\\
\langle S,DD^\top\rangle
&=\langle S,UU^\top+VV^\top\rangle
-\langle Q,A\rangle-\langle Q^\top,A\rangle.
\end{aligned}
\]
Since \(Q-Q^\top\) is skew-symmetric, subtraction of these identities yields
\[
\begin{aligned}
\langle Q^\top U-QV,D\rangle
&=\langle S,DD^\top\rangle
-\tfrac12\langle Q-Q^\top,A-A^\top\rangle\\
&=\langle S,DD^\top\rangle
-\tfrac12\|P_E(A-A^\top)\|_F^2\\
&\le\operatorname{Tr}(SDD^\top). \tag{4}
\end{aligned}
\]
The second equality follows from \(Q-Q^\top=P_E(A-A^\top)\) and the coordinate-mask identity. In particular, the sign of this remainder does not require nonnegativity of \(U,V\); nonnegativity was used for feasibility in (2).

### 3. Upper bound and equality of the factors

The spectral trace bound applies to the symmetric matrix \(S\) and \(DD^\top\succeq0\), giving
\[
\operatorname{Tr}(SDD^\top)\le\lambda_{\max}(S)\|D\|_F^2.
\]
The eigenvalue/Frobenius bound, triangle inequality, and transpose invariance imply
\[
\lambda_{\max}(S)\le\|S\|_F
\le\tfrac12(\|Q\|_F+\|Q^\top\|_F)
=\|Q\|_F. \tag{5}
\]
Taking the inner product of (1) with \(D\) and combining (2)--(5) therefore gives
\[
(2\lambda+\sigma_n(M))\|D\|_F^2
\le\|Q\|_F\|D\|_F^2.
\]
The hypothesis says that \(2\lambda+\sigma_n(M)-\|Q\|_F>0\). Hence \(\|D\|_F^2=0\), so \(U^*=V^*\). This argument divides by neither \(\|D\|_F\) nor \(\|Q\|_F\), and remains valid for an empty mask or zero factors.

### 4. Transfer of stationarity

Let \(W=U^*=V^*\) and \(R=P_E(WW^\top-X)\). Substitution into the first stationarity equation gives
\[
RW+\xi_U=0,\qquad \xi_U\in N_C(W).
\]
The matrix \(R\) is symmetric. For an arbitrary perturbation \(H\), the differential of the symmetric objective is
\[
\mathrm dG(W)[H]
=\langle R,HW^\top+WH^\top\rangle
=\langle2RW,H\rangle.
\]
Thus \(\nabla G(W)=2RW\). The normal cone is a cone, so \(2\xi_U\in N_C(W)\). Multiplying the preceding stationarity equation by two yields
\[
0=\nabla G(W)+2\xi_U\in\nabla G(W)+N_C(W).
\]
Therefore the common factor is a critical point of \(G\), as required.
