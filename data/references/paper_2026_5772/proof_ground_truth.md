# Reference Proof

## Proof Structure

1. Derive the observable moment factorizations from the proxy conditional-independence assumptions, checking integrability and causal mean identification.
2. Use positivity and rank to identify the common row space and its invertible coordinate representation.
3. Compress the moments and verify the full-rank Moore-Penrose product identity to obtain a common similarity representation; subtraction yields the diagonal treatment-effect matrix.
4. Use spectral separation, lifting, and anchor normalization to recover the target-proxy features up to a common permutation.
5. Solve the marginal mean equation for the latent proportions.
6. Express powers of the difference operator as the complete treatment-effect moment sequence and derive the resolvent series.

## Complete Proof

### Step 001: Integrability, causal means, and moment factorizations

For each t in {0,1}, define
\[
\pi_{u|t}=\Pr(C=u\mid T=t),\qquad P_t=\operatorname{diag}(\pi_{1|t},\dots,\pi_{k|t}),
\]
\[
\mu_t(u)=\mathbb E[Y\mid C=u,T=t],\qquad G_t=\operatorname{diag}(\mu_t(1),\dots,\mu_t(k)).
\]
Every event {C=u,T=t} has positive probability. The assumed first moments therefore give finite conditional absolute first moments on each such event. Also |Y| is bounded by |Y^{(0)}|+|Y^{(1)}|, so Y is integrable.

The assumption X independent of (Y,T) given C implies that, conditional on C=u,T=t, X has its conditional law given C=u and is independent of Y. Together with the conditional independence of Z from (X,Y), this gives, for every coordinate pair i,j,
\[
\mathbb E[|Z_iX_jY|\mid C=u,T=t]
=\mathbb E[|Z_i|\mid C=u,T=t]\,
\mathbb E[|X_j|\mid C=u]\,
\mathbb E[|Y|\mid C=u,T=t]<\infty.
\]
The same argument without Y gives finite conditional absolute moments for Z_iX_j. Summing over the finitely many cells proves that S_t and H_t are well-defined finite matrices.

The proxy assumptions give
\[
\mathbb E[X\mid C=u,T=t]=B[:,u].
\]
Consistency and latent ignorability give
\[
\mu_t(u)=\mathbb E[Y^{(t)}\mid C=u,T=t]=\mathbb E[Y^{(t)}\mid C=u].
\]
Consequently, conditional factorization and total expectation yield
\[
S_t=A_tP_tB^\top,\qquad H_t=A_tP_tG_tB^\top.
\]

### Step 002: Common row space and invertible compression

Put C_t=A_tP_t. Positivity makes P_t invertible, so C_t has full column rank. The factorization S_t=C_tB^\top shows that every row of S_t lies in the row space of B^\top. Conversely,
\[
B^\top=(C_t^\top C_t)^{-1}C_t^\top S_t,
\]
so every row of B^\top lies in the row space of S_t. Thus each S_t has rank k and the same row space as B^\top. Their vertical stack has that same row space and rank k.

An orthonormal basis V with k columns therefore exists. Since VV^\top is the orthogonal projector onto this row space,
\[
B^\top=B^\top VV^\top.
\]
Set R=B^\top V. Then B^\top=RV^\top, and
\[
k=\operatorname{rank}(B^\top)\leq\operatorname{rank}(R)\leq k.
\]
Hence R is invertible. These conclusions hold for every allowed choice of V.

### Step 003: Common similarity and spectral identification

The compressed moments satisfy
\[
S_tV=C_tR,\qquad H_tV=C_tG_tR.
\]
We verify the required pseudoinverse identity. Let M=C_tR and N=R^{-1}C_t^\dagger. Since C_t has full column rank, C_t^\dagger C_t=I_k. Therefore
\[
MN=C_tC_t^\dagger,\qquad NM=I_k.
\]
Both products are symmetric: the first is the orthogonal projector onto the column space of C_t, and the second is the identity. Moreover,
\[
MNM=M,\qquad NMN=N.
\]
These are all four Moore-Penrose equations, so
\[
(C_tR)^\dagger=R^{-1}C_t^\dagger.
\]
It follows that
\[
K_t=R^{-1}C_t^\dagger C_tG_tR=R^{-1}G_tR.
\]
By causal mean identification,
\[
\Theta:=G_1-G_0=\operatorname{diag}(\theta_1,\dots,\theta_k).
\]
Thus
\[
L=R^{-1}\Theta R.
\]
For every scalar \lambda,
\[
\det(\lambda I_k-L)=\det\bigl(R^{-1}(\lambda I_k-\Theta)R\bigr)
=\prod_{u=1}^k(\lambda-\theta_u).
\]
The eigenvalues of L, including multiplicities, are exactly the latent effects.

### Step 004: Eigenvector lifting and anchor normalization

Since RL=\Theta R, the u-th row of R is a left eigenvector for \theta_u. More explicitly, if a nonzero row w satisfies wL=\theta_u w, then
\[
(wR^{-1})\Theta=\theta_u(wR^{-1}).
\]
Distinctness of the effects forces wR^{-1} to have only its u-th coordinate nonzero. Hence w is a nonzero multiple of the u-th row of R.

Choose one nonzero real left eigenvector for each eigenvalue in any fixed order, and assemble them as the rows of W. There are a permutation matrix \Pi and a nonsingular diagonal matrix D such that
\[
W=D\Pi R,\qquad WV^\top=D\Pi B^\top.
\]
Because X_1=1 almost surely,
\[
(B^\top)_{u1}=\mathbb E[X_1\mid C=u]=1\qquad(1\leq u\leq k).
\]
Thus the first column of B^\top is the all-ones column, not necessarily its first row. Each first entry of WV^\top is the corresponding nonzero diagonal entry of D. Dividing each lifted row by its first entry therefore gives \Pi B^\top. Transposing recovers B\Pi^\top, namely B with the corresponding column permutation.

### Step 005: Latent proportions

Let p=(\Pr(C=1),\dots,\Pr(C=k))^\top. Total expectation gives
\[
\mathbb E[X]=Bp.
\]
Since B has full column rank, this equation has a unique solution in \mathbb R^k, namely
\[
p=(B^\top B)^{-1}B^\top\mathbb E[X]=B^\dagger\mathbb E[X].
\]
For the recovered matrix B\Pi^\top, the unique solution is \Pi p. Thus features, effects, and probabilities are recovered with the same latent-label permutation.

### Step 006: All moments and the resolvent

The anchor gives B^\top e_1=\mathbf 1_k. Consequently,
\[
Rc=RV^\top e_1=B^\top e_1=\mathbf 1_k.
\]
Also,
\[
a^\top=\mathbb E[X]^\top V=p^\top B^\top V=p^\top R.
\]
For every integer \ell\geq0, similarity and cancellation give
\[
L^\ell=R^{-1}\Theta^\ell R,
\]
including \ell=0, where both zeroth matrix powers are I_k. Therefore
\[
a^\top L^\ell c
=p^\top\Theta^\ell\mathbf 1_k
=\sum_{u=1}^k p_u\theta_u^\ell
=\mathbb E[\theta_C^\ell].
\]
Here the zeroth scalar power is the constant polynomial 1, also at a zero effect, so the zeroth moment is 1. All moments are finite because the effects form a finite set of finite real numbers.

For z in \mathbb C satisfying q:=|z|\|L\|_2<1, the series
\[
F=\sum_{\ell=0}^{\infty}(zL)^\ell
\]
converges absolutely in operator norm, since \|(zL)^\ell\|_2\leq q^\ell. For its finite partial sums F_N,
\[
(I_k-zL)F_N=F_N(I_k-zL)=I_k-(zL)^{N+1}.
\]
Passing to the limit gives (I_k-zL)F=F(I_k-zL)=I_k. Thus F=(I_k-zL)^{-1}. Multiplication by the fixed vectors a^\top and c preserves the convergent series, giving
\[
a^\top(I_k-zL)^{-1}c
=\sum_{\ell=0}^{\infty}z^\ell a^\top L^\ell c
=\sum_{\ell=0}^{\infty}z^\ell\mathbb E[\theta_C^\ell].
\]
The proof includes k=1, for which separation is vacuous. It also includes zero effects. In particular, if L=0, the norm condition holds for every finite complex z and the series has only its zeroth term.
