# Reference Proof

## Proof Structure

Differentiate the supported orthogonal perturbation at initialization and identify its Frobenius first-variation gradient. Verify the standard skew-compression bound through singular-value min-max. Finally construct an attaining support and check all completion cases.

## Theorem-Critical Obligations

1. Derive the weight derivative and justify differentiation of the loss using differentiability at \(W_0\).
2. Identify the skew-symmetric Frobenius representative, including its normalization and uniqueness.
3. Establish the compression bound with spectral multiplicities, zero padding, and the floor convention.
4. Verify attainment for all allowed dimensions and ranks, including arbitrary orthogonal completion in the cases specified by the task.

All four obligations are closed below. The standard-independent linear-algebra content of theory_009 is stated and verified rather than used as an unexplained paper-specific premise.

## Complete Proof

### 1. First-order perturbation

For a fixed \(E\in\operatorname{Skew}(r)\), the path assumptions give
\[
W(0)=W_0,\qquad W'(0)=W_0P^TEP.
\]
Differentiability of \(L\) at \(W_0\) therefore gives
\[
\frac{d}{dt}L(W(t))\Big|_{t=0}
=\langle G,W_0P^TEP\rangle_F.
\]
Only the behavior of this path at zero and differentiability of \(L\) at \(W_0\) are used; differentiability of \(L\) elsewhere is unnecessary.

### 2. Frobenius first-variation gradient

Set \(A=PW_0^TGP^T\). Cyclicity of trace yields
\[
\langle G,W_0P^TEP\rangle_F
=\operatorname{tr}(PG^TW_0P^TE)
=\operatorname{tr}(A^TE)
=\langle A,E\rangle_F.
\]
The Frobenius inner product of a symmetric matrix and a skew-symmetric matrix is zero. Consequently,
\[
\langle A,E\rangle_F
=\langle\operatorname{skew}(A),E\rangle_F
=\langle P\operatorname{skew}(W_0^TG)P^T,E\rangle_F
=\langle PFP^T,E\rangle_F.
\]
Since \((PFP^T)^T=-PFP^T\), this matrix belongs to \(\operatorname{Skew}(r)\) and represents the first variation in every direction. The representative is unique: if two skew-symmetric matrices represent it, their difference pairs to zero with every skew-symmetric matrix, including itself. Thus the initialization gradient specified in the task is \(PFP^T\), with squared norm \(\|PFP^T\|_F^2\).

This is the first-variation gradient defined in the public task. The argument does not infer joint differentiability of a parameterization from smoothness of its individual radial paths.

### 3. Standard spectral facts and the compression inequality

We use the finite-dimensional symmetric spectral theorem: every real symmetric matrix admits an orthonormal eigenbasis with real eigenvalues. The matrices to which it is applied below are explicitly symmetric and positive semidefinite.

First, recall the real block structure of a skew-symmetric matrix \(T\). The matrix \(T^TT=-T^2\) is symmetric positive semidefinite. If \(u\) is a unit eigenvector with positive eigenvalue \(\alpha^2\), put \(v=-Tu/\alpha\). Then
\[
\|v\|=1,\qquad u^Tv=0,\qquad Tu=-\alpha v,\qquad Tv=\alpha u.
\]
Thus \(\operatorname{span}\{u,v\}\) is invariant and, in this orthonormal basis, the restriction is
\[
B(\alpha)=\begin{pmatrix}0&\alpha\\-\alpha&0\end{pmatrix}.
\]
Its orthogonal complement is invariant as well: if \(x\) is orthogonal to the plane and \(y\) lies in it, then \(y^TTx=-(Ty)^Tx=0\). Repeating this construction gives an orthogonal direct sum of such positive blocks and a zero block. If no positive eigenvalue of \(T^TT\) remains, \(T\) vanishes on the remaining space. Each positive block has eigenvalues \(\pm i\alpha\), two singular values equal to \(\alpha\), and squared Frobenius norm \(2\alpha^2\).

It follows that, with the public zero-padding convention, the ordered singular values of \(F\) satisfy
\[
s_{2j-1}(F)=s_{2j}(F)=\mu_j
\quad (1\le j\le\lfloor d/2\rfloor),
\]
with one additional zero singular value when \(d\) is odd. Similarly, \(C=PFP^T\) is skew-symmetric. Write its pair magnitudes, padded with zeros, as \(\nu_1\ge\cdots\ge\nu_k\ge0\), where \(k=\lfloor r/2\rfloor\). Then
\[
s_{2j-1}(C)=s_{2j}(C)=\nu_j,\qquad
\|C\|_F^2=2\sum_{j=1}^k\nu_j^2.
\]

For completeness, the singular-value min-max formula for a real \(n\times n\) matrix \(T\) is
\[
s_\ell(T)=
\min_{\substack{V\subseteq\mathbb R^n\\\dim V=n-\ell+1}}
\max_{\substack{x\in V\\\|x\|=1}}\|Tx\|,
\qquad 1\le\ell\le n.
\]
To verify it, diagonalize the symmetric positive semidefinite matrix \(T^TT\). The span of its eigenvectors numbered \(\ell,\ldots,n\), in decreasing eigenvalue order, gives an upper bound of \(s_\ell(T)\). Conversely, every \((n-\ell+1)\)-dimensional subspace intersects the span of the first \(\ell\) eigenvectors nontrivially. A unit vector in that intersection has image norm at least \(s_\ell(T)\). This proves the formula, including repeated and zero singular values.

We now verify the compression application. Fix \(1\le\ell\le r\), and let \(V\subseteq\mathbb R^d\) be the span of right singular vectors of \(F\) numbered \(\ell,\ldots,d\). Thus
\[
\dim V=d-\ell+1,\qquad
\|Fx\|\le s_\ell(F)\|x\|\quad(x\in V).
\]
Let \(U=\operatorname{range}(P^T)\), which has dimension \(r\). Dimension counting gives
\[
\dim(U\cap V)\ge r-\ell+1.
\]
Choose an \((r-\ell+1)\)-dimensional subspace \(K\subseteq U\cap V\). Since \(PP^T=I_r\), the map \(P^T\) is an isometry, \(P\) is its inverse on \(U\), and \(P\) is a contraction on \(\mathbb R^d\). Therefore \(PK\subseteq\mathbb R^r\) has dimension \(r-\ell+1\). For \(y\in PK\), writing \(x=P^Ty\in K\), we obtain
\[
\|Cy\|=\|PFx\|\le\|Fx\|
\le s_\ell(F)\|x\|=s_\ell(F)\|y\|.
\]
The min-max formula for \(C\) now gives \(s_\ell(C)\le s_\ell(F)\). Taking \(\ell=2j-1\) proves
\[
\nu_j\le\mu_j\qquad(1\le j\le k).
\]
Consequently,
\[
\|PFP^T\|_F^2
=2\sum_{j=1}^k\nu_j^2
\le2\sum_{j=1}^k\mu_j^2.
\]
If \(k=0\), the block formula already gives \(C=0\) and both sums are empty. Thus this argument includes \(r=1\).

### 4. Attainment and all completion cases

Let \(a=\min\{q,k\}\). Choose mutually orthogonal real invariant planes for the first \(a\) positive pair magnitudes and let \(S\) be their direct sum. The block construction above permits this choice even when magnitudes are repeated. We have \(\dim S=2a\), and \(S^\perp\) is invariant under \(F\).

Complete an orthonormal basis of \(S\) by \(t=r-2a\) orthonormal vectors in \(S^\perp\). Such a completion exists because \(r\le d\). Use these vectors as the rows of \(P\). There are no compression cross terms between \(S\) and the additional directions: for \(u\in S\) and \(v\in S^\perp\),
\[
u^TFv=-(Fu)^Tv=0.
\]
There are two cases.

- If \(a=k\), then \(t=r-2k\) is either zero or one. In the one-dimensional case, the remaining compressed entry is zero because \(v^TFv=0\). The extra direction may be any unit vector in \(S^\perp\); the full odd-dimensional support need not be invariant under \(F\).
- If \(a<k\), then \(a=q\), so \(S\) contains all nonzero blocks of \(F\). The block decomposition gives \(S^\perp=\ker F\), and any required number of orthonormal completion vectors contributes a zero block.

In the chosen row basis, the compression therefore consists of \(B(\mu_1),\ldots,B(\mu_a)\) and a zero block of size \(t\). Hence
\[
\|PFP^T\|_F^2
=2\sum_{j=1}^a\mu_j^2
=2\sum_{j=1}^k\mu_j^2,
\]
where the last equality uses zero padding when \(a<k\). Any other orthonormal basis of the same row space changes the compression by orthogonal conjugation and leaves its Frobenius norm unchanged.

This proves sharpness and the stated attainment rule. The argument covers \(F=0\), insufficiently many nonzero pairs, tied magnitudes, \(r=1\), \(d=1\), odd \(r\), and \(r=d\), without adding a rank or spectral-gap assumption.

## Private Source Alignment

The first-variation calculation follows L000260-L000275. The spectral step verifies the standard-independent fact invoked at L000276-L000277. The attainment argument completes L000281-L000282 with the odd-r convention already supplied at L000280 and with the implicit zero-padding convention made explicit. No necessity characterization of all maximizing supports, training-dynamics approximation, or separate source contribution is used.
