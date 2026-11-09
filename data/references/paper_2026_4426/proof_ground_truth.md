# Reference Proof

## Audited scope and obligations

The target is finite-sample equality of regression representations. It does not assert equality between the KGC and GRBF models themselves, correctness of causal discoveries, equality of different significance-testing procedures, or an F null distribution. All positive principal components are retained; an additional truncation rule is not part of the target.

The obligations are: (1) identify the centered KGC and KPCR projectors; (2) verify the normalized kernel construction; (3) establish the GRBF/Nyström fitted-space equivalence for each block; (4) justify the positive-component PCA step even when centered features are rank deficient; (5) pass to the additive unrestricted regression; and (6) compare residual quantities with correct domains and intercept accounting. Each is proved below.

## 1. Centered spectral regression

Let H=I_n-11^T/n. For T=X,Z, write the centered positive-semidefinite Gram matrix as
\[
\bar K_T=A_T\Lambda_TA_T^\top,
\]
where A_T contains every positive-eigenvalue eigenvector. Since H\bar K_T=\bar K_T, its range lies in 1^\perp. Its column space is col(A_T), so the centered KGC projector is A_TA_T^T. The KPCR score matrix is
\[
F_T=\bar K_TA_T\Lambda_T^{-1/2}=A_T\Lambda_T^{1/2}.
\]
It has the same column space and hence the same projector. If there are no positive eigenvalues, both column spaces are {0} and both projectors are zero. Adding the common intercept adds the projector 11^T/n to each and preserves equality. This closes obligation (1).

## 2. The scaled kernel and Nyström coordinates

Fix one block T in {X,W}, with its own inducing set J_T and positive bandwidth \sigma. Suppress the block subscript temporarily. Put
\[
E=K_{TJ},\qquad G=K_{JJ},\qquad
D=\operatorname{diag}(r(t_1),\ldots,r(t_n)),\qquad
D_J=\operatorname{diag}(r(j_1),\ldots,r(j_m)).
\]
Every normalization sum is finite and strictly positive because the inducing set is finite and nonempty and the Gaussian kernel is strictly positive at finite inputs. For any finite list of inputs, the Gram matrix of
\[
\widetilde k(u,v)=k_\sigma(u,v)/(r(u)r(v))
\]
is a diagonal congruence of the Gaussian Gram matrix. For every vector c its quadratic form is the Gaussian quadratic form evaluated at the diagonally rescaled vector. It is therefore nonnegative, proving that this is a valid kernel. Its inducing Gram matrix is
\[
\widetilde G=D_J^{-1}GD_J^{-1},
\]
which is positive definite by the assumed positive definiteness of G and invertibility of D_J. This closes obligation (2).

The actual normalized GRBF activation matrix is B=D^{-1}E. The normalized cross-Gram matrix is
\[
\widetilde K_{TJ}=D^{-1}ED_J^{-1}=BD_J^{-1}.
\]
Thus the specified Nyström feature matrix satisfies
\[
N=\widetilde K_{TJ}\widetilde G^{-1/2}=BC,
\qquad C=D_J^{-1}\widetilde G^{-1/2}.
\]
Both factors defining C are invertible, so C is invertible. Consequently col(N)=col(B) and col(HN)=col(HB). No inverse of a data-feature covariance matrix is needed. This closes obligation (3) for each block.

For comparison with the source calculation, the same approximate Gram matrix can also be written
\[
NN^\top=BG^{-1}B^\top.
\]
Hence BG^{-1/2} is another feature factor. The source's extra D_J in its coefficient transformation is unnecessary: its activation matrix is B=D^{-1}E, not BD_J^{-1}. This identity is private proof material, not an additional public assumption.

## 3. All positive PCA components preserve the fitted space

Let M be any real matrix and put L=HM. Take an orthonormal eigenbasis of the symmetric matrix L^TL, and let V_+ contain exactly the eigenvectors with positive eigenvalues. If v has eigenvalue zero, then
\[
\|Lv\|^2=v^TL^TLv=0,
\]
so Lv=0. Expanding in the complete eigenbasis gives L=LV_+V_+^T. Therefore col(LV_+)=col(L). If L=0, both spaces are {0}. This proves directly that the PCA score matrix used in the task preserves the centered feature column space, including all rank-deficient cases, closing obligation (4).

Applying this to each N_T and combining it with Section 2 shows that its Nyström principal-component scores S_T satisfy
\[
\operatorname{col}(S_T)=\operatorname{col}(HB_T),\qquad T=X,W.
\]

## 4. Restricted and additive unrestricted models

For any matrix M,
\[
\operatorname{col}([1,M])=
\operatorname{span}\{1\}\mathbin{\oplus}\operatorname{col}(HM).
\]
Indeed every column decomposes into its mean times 1 plus its centered column, and the centered columns are orthogonal to 1. Thus the restricted GRBF design [1,B_X] and the restricted Nyström-PCR design [1,S_X] have the same column space. The unrestricted designs [1,B_X,B_W] and [1,S_X,S_W] likewise have the same column space, because equality holds separately for both centered blocks. The restricted space is contained in the unrestricted space by their explicit additive construction. This closes obligation (5).

Also B_T1=1 by its row-normalized definition. Consequently the GRBF spaces already contain the intercept even if it is not separately displayed. In particular, [B_X,B_W] has a redundant coefficient direction. This explains why one must use least-squares fitted projections rather than the source's ordinary inverse for unrestricted coefficients.

For completeness, if P is the orthogonal projector onto a design's column space and v belongs to that space, orthogonality gives
\[
\|y-v\|^2=\|(I-P)y\|^2+\|Py-v\|^2.
\]
The unique minimizing fitted vector is Py, whether or not coefficients are unique. Equal column spaces therefore give equal projectors, fitted values, residual vectors, and residual sums of squares. Since the response is centered, the intercept component of its fitted vector is zero, but the intercept still belongs to the full fitted space and counts in its rank.

## 5. Residual comparisons and their domains

Write P_R,P_U for the full restricted and unrestricted projectors of the GRBF representation and use the corresponding projectors for the Nyström-PCR representation. Section 4 identifies them pairwise. Hence p_R=rank(P_R), p_U=rank(P_U), q=p_U-p_R, RSS_R, and RSS_U are identical between representations. In particular RSS_R-RSS_U is identical. Nestedness also gives RSS_R\ge RSS_U.

If q>0, n-p_U>0, and RSS_U>0, the real-valued ratio
\[
F=\frac{(\operatorname{RSS}_R-\operatorname{RSS}_U)/q}
{\operatorname{RSS}_U/(n-p_U)}
\]
is defined and equal between the two representations. If any required divisor vanishes, the theorem still gives the identical fitted vectors and RSS values but does not assert a defined F ratio. This closes obligation (6).

The proof uses only the displayed source constructions and elementary finite-dimensional linear algebra, with the local coefficient-formula repairs recorded in provenance. There are no unresolved obligations.
