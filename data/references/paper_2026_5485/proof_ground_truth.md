# Reference Proof

## Audited source contract

The averaging experiment is over the symmetry group only; the parameter vector is fixed. The averaging action is orthogonal, continuous in the compact case, and uses normalized measure. The source introduces the secant relation as an approximation and then solves the matrix equation conditionally as an equality. The public exact orbit-wide assumption therefore must be used, not derived from differentiability. Positive definiteness of the displacement average is the nonsingularity condition for the inverse-root formula, not a general property of an orbit average. The structural fixed-point equations do not require that condition or the secant model.

The relevant source locations are L000028-L000041, L000073-L000100, L000240-L000267, and L000316-L000442. The Hessian-Lipschitz and random-initialization assertions belong to a different accuracy result and are not imported. Neither the empirical replacement of the displacement average by a scalar identity nor any optimizer equivalence is part of this proof.

The full-linear comparison uses ordinary commutation, as in L000311-L000312 and L000367-L000374. It is not a compact averaging experiment. The compact diagram families use defining coordinate representations, with repeated occurrences of a group label sharing one action. Arbitrary representations of an abstract group with the same name are not covered by those diagram descriptions.

## Theorem-critical obligation ledger

- **step_001 — Closed:** Gradient equivariance, invariance of both averages, and invariance of the gradient at the averaged point. Derived below from the chain rule and invariant measure.
- **step_002 — Closed:** Identification of the two centered orbit outer products and the exact equation S_g=H S_z H. Derived directly from the stipulated pointwise secant model.
- **step_003 — Closed:** Existence and uniqueness of the PSD solution, including singular S_g, and preservation of the global symmetry. Derived by congruence, the symmetric spectral theorem, and uniqueness under orthogonal conjugation.
- **step_004 — Closed:** Correct layer-pair typing, the diagram spanning claims, independent product labels, passive factors, represented-space complexity, and weak monotonicity. The finite-group and product arguments are derived below. The GL and orthogonal spanning results use the explicitly stated standard-independent classical results recorded in theory_011; their hypotheses are checked below. No paper-specific external construction is needed.

## 1. Equivariance and orbit invariance

Write Q=ρ(A). Differentiating L(Qx)=L(x) gives Q^T∇L(Qx)=∇L(x). Since Q is orthogonal,
\[
\nabla L(\rho(A)x)=\rho(A)\nabla L(x).
\]
The averages exist: the representation is continuous on a compact group, hence its matrix entries are bounded and measurable; the finite case is immediate. Left invariance of normalized measure gives
\[
\rho(B)R_1(v)=\mathbb E_A[\rho(BA)v]=R_1(v),
\]
\[
\rho(B)R_2(u,v)\rho(B)^T
=\mathbb E_A[\rho(BA)uv^T\rho(BA)^T]=R_2(u,v).
\]
Thus ρ(A)\bar z=\bar z. Gradient equivariance at \bar z then gives ρ(A)\bar g=\bar g. In particular, both S_z and S_g are invariant. They are symmetric PSD because each is an average of a vector outer product with itself. General R_2(u,v), however, need not be symmetric.

## 2. The secant equation

Set z_A=ρ(A)z and g_A=∇L(z_A)=ρ(A)g. The fixedness just proved implies
\[
z_A-\bar z=\rho(A)(z-\bar z),\qquad
g_A-\bar g=\rho(A)(g-\bar g).
\]
By the public secant assumption, g_A-\bar g=H(z_A-\bar z) for every A. The Hessian H is symmetric. Taking outer products and averaging therefore gives
\[
\begin{aligned}
S_g
&=\mathbb E_A[(g_A-\bar g)(g_A-\bar g)^T]\\
&=H\,\mathbb E_A[(z_A-\bar z)(z_A-\bar z)^T]H^T\\
&=H S_z H.
\end{aligned}
\]
This calculation does not assert that \bar g equals the gradient at z or assume a zero gradient at \bar z. It also does not turn a Taylor approximation into an exact equation without the stated assumption.

## 3. PSD solution and its invariant structure

Assume S_z is positive definite and put
\[
M=S_z^{1/2}S_gS_z^{1/2}.
\]
For a symmetric PSD unknown X, set C=S_z^{1/2}X S_z^{1/2}. Congruence is a bijection between symmetric PSD X and symmetric PSD C, and
\[
X S_z X=S_g\quad\Longleftrightarrow\quad C^2=M.
\]
For completeness, the symmetric spectral theorem supplies M=U diag(λ_i)U^T with λ_i≥0 and the PSD root U diag(√λ_i)U^T. Any symmetric PSD C satisfying C²=M commutes with M. On an eigenspace of M with eigenvalue λ, the eigenvalues of the restriction of C are nonnegative and square to λ; consequently that restriction is √λ times the identity. This proves uniqueness, including λ=0 and repeated eigenvalues. Hence
\[
X=S_z^{-1/2}M^{1/2}S_z^{-1/2}=\widehat H.
\]
Substitution verifies the equation, and congruence verifies positive semidefiniteness. S_g need not be invertible. The actual Hessian H is a symmetric solution of the equation but need not be the PSD solution.

It remains to prove the claimed structure of \widehat H, rather than infer it merely from the structures of the input matrices. Let Q=ρ(B). Since Q S_z Q^T=S_z and Q S_g Q^T=S_g, the matrix Y=Q\widehat H Q^T is PSD and satisfies
\[
Y S_z Y=Q\widehat H S_z\widehat H Q^T=Q S_g Q^T=S_g.
\]
Uniqueness yields Q\widehat H Q^T=\widehat H. Orthogonality makes this equivalent to Q\widehat H=\widehat H Q, proving \widehat H∈\mathcal C_G.

The source's enumeration of general roots is unnecessary for this argument. If general symmetric roots are discussed, the correct description permits an arbitrary symmetric involution on each positive-eigenvalue eigenspace of M, multiplied by the square root of that eigenvalue, and is zero on ker M. Restricting to one fixed eigenbasis and finitely many sign choices need not enumerate all roots when positive eigenvalues repeat.

## 4. Global and layer-pair fixed spaces

For an orthogonal representation, Q T Q^T=T is equivalent to QT=TQ. Write T in layer-pair blocks. Because Q is block diagonal, commutation is equivalent to
\[
\rho_\ell(A)T_{\ell m}=T_{\ell m}\rho_m(A)
\qquad\text{for every }\ell,m,A.
\]
The equations on different ordered pairs are independent, so
\[
\mathcal C_G\cong\bigoplus_{\ell,m}\mathcal C_{\ell m}
\]
as vector spaces. A rectangular block is an intertwiner E_m→E_ℓ, not an algebra under multiplication with itself. The assertion also does not say that T is block diagonal. The global space is an algebra with ordinary block-matrix multiplication.

These are exactly the spaces relevant to second-order averages. Indeed, averaging conjugation defines a linear map on End(E) whose image is contained in \mathcal C_G by part 1 and which fixes every element of \mathcal C_G. Since rank-one matrices uv^T span End(E), the linear span of all R_2(u,v) is \mathcal C_G. The complexity statement concerns this full linear space, not the set attainable from one fixed pair or the PSD cone.

## 5. Independent labels and passive factors

Using the Euclidean inner products to identify each defining orthogonal module with its dual, and reordering tensor factors, the coefficient space of a block E_m→E_ℓ identifies with
\[
\operatorname{Hom}(F_m,F_\ell)\otimes
\bigotimes_{j=1}^q V_j^{\otimes r_j},
\qquad r_j=a_{\ell j}+a_{mj}.
\]
The j-th group acts only on its j-th tensor factor. Averaging its action gives a projection onto that factor's invariant tensors: the image is invariant by reindexing, and invariant tensors are fixed by averaging. Product Haar measure, or product uniform measure, therefore averages the full action by the tensor product of these projections. Its image is
\[
\operatorname{Hom}(F_m,F_\ell)\otimes
\bigotimes_j (V_j^{\otimes r_j})^{G_j}.
\]
This proves the independence of colors and the absence of cross-color contractions. The passive factor is the entire Hom space, of dimension (dim F_ℓ)(dim F_m). With only one passive index it is a vector factor, not a square matrix. With several passive indices it is the tensor of the appropriate order. No passive indices give a scalar factor.

## 6. Permutations and signed permutations

Fix V=R^n and r tensor positions. An index tuple in {1,…,n}^r determines its exact equality partition λ: positions are in the same block exactly when their indices are equal. The coordinate-permutation group has one orbit for each such partition with at most n blocks. Let E_λ be the indicator tensor of this orbit. These tensors have disjoint nonempty supports and form a basis of the permutation-invariant tensors.

For the delta diagram D_π,
\[
D_\pi=\sum_{\lambda\text{ coarser than }\pi,\ |\lambda|\leq n}E_\lambda.
\]
Restrict π to partitions with at most n blocks. Ordering this finite set compatibly with refinement makes this change of coordinates triangular with diagonal entries one. Thus those D_π form a basis, and all partition diagrams certainly span. This proves the permutation assertion without any large-n assumption.

For the signed-permutation group, first apply the independent coordinate sign changes. A tensor coefficient can be nonzero only if every coordinate value occurring in its tuple occurs an even number of times: flipping one coordinate changes that coefficient by the parity of its multiplicity. Permutations then make the coefficients constant on exact equality patterns. Consequently a basis is given by E_λ for partitions λ with at most n blocks and every block even. For an even-block π, every coarser partition also has even blocks. The same triangular argument proves that the even-block delta diagrams span, and that those with at most n blocks form a basis. In particular, the space is zero when r is odd. This supplies the signed-permutation rule rather than relying on an unexplained diagram-algebra name.

The argument includes r=0: the empty pattern gives the scalar invariant. It also includes n=1 and the cases where many of the displayed diagrams coincide.

## 7. Audited standard-independent classical results

The external record theory_011 contains the following two classical spanning statements invoked in the supplied source's representation-theory discussion.

**Full-linear tensor commutant.** For V=R^n, n≥1, and k≥0, the commutant of the defining tensor-power action A↦A^{⊗k} of GL_n(R) on V^{⊗k} is the span of the operators that permute its k tensor factors. This is the statement at L000367-L000374. It asserts spanning for every n and k, not independence of all k! operators.

**Orthogonal tensor commutant.** For a real Euclidean V=R^n, n≥1, and k≥0, the commutant of the defining tensor-power action of the full O(n) on V^{⊗k} is the span of the delta tensors indexed by pairings of the 2k input and output positions, allowing both cross-row and same-row pairs. This is the classical orthogonal extension invoked at L000376 and described at L000415. The statement concerns the image of the pairing diagrams and does not assert that the abstract diagram representation is faithful in every dimension.

Both are standard-independent classical representation results. Their exact forms above, rather than the source's unqualified diagram counts, are the external facts used here. The public GL comparison has exactly the first result's real defining tensor representation and full acting group, so that result applies directly. No Haar averaging over GL is used.

For an orthogonal color with r positions, -I shows that invariant tensors vanish for odd r. If r=2k, the Euclidean identification between V^{⊗2k} and End(V^{⊗k}) converts invariant tensors into the commutant in the second result. Its hypotheses are satisfied: the space is real Euclidean, the full O(n) acts, and every position carries its defining representation. Reshaping the positions into the actual layer-pair rows and columns does not change the pairing tensors. This proves the orthogonal spanning assertion for arbitrary layer-pair orders, including unequal row and column tensor orders.

The correct vectorized GL commutation equation, if used privately, has the action (A^{-T})^{⊗k}⊗A^{⊗k}. It does not have the all-covariant action A^{⊗2k}. The latter substitution is justified only for orthogonal A and is not used for the full-linear comparison.

## 8. Basis selection, complexity, and restriction

For each color, the preceding arguments provide a finite spanning collection of binary delta tensors. Tensoring these collections with coordinate matrix units of Hom(F_m,F_ℓ) yields a finite spanning collection for each block. A maximal linearly independent subcollection is a basis. Thus the diagrammatic conclusion is valid in every dimension, while its independent coefficient count is the dimension of the represented space.

Abstract diagram counts must not be substituted for that dimension without an independence check. For example, in dimension one all pairing tensors on four positions coincide, and all partition tensors on a fixed set of positions coincide. Likewise, delta diagrams containing only singleton blocks may be dense all-ones tensors; the statement concerns a compact diagram description, not uniform entrywise sparsity.

The blockwise vector-space direct sum gives
\[
\dim\mathcal C_G=\sum_{\ell,m}\dim\mathcal C_{\ell m}.
\]
A basis has exactly this many independent scalar coefficients. The symmetric PSD matrices S_z, S_g, and \widehat H lie within this ambient space; this count is not asserted to be a minimal parametrization of its symmetric or PSD subset.

If K is a subgroup of G and the representation is restricted on the same E, any operator commuting with every element of G commutes with every element of K. Hence \mathcal C_G⊆\mathcal C_K and dim \mathcal C_G≤dim \mathcal C_K. Equality is allowed. For example, the defining representations of the full orthogonal and full signed-permutation groups both have scalar commutants. The same inclusion reasoning applies to the algebraic GL comparison and its restrictions; the diagram descriptions themselves require the specified representation forms.

## 9. Boundary and source-repair checks

Singular S_g, zero gradients, repeated eigenvalues, n=1, empty sets of tensor positions, zero block spaces, and zero intertwiner spaces are covered. No pseudoinverse, damping, positive Hessian, or stable-dimension assumption has been inserted.

A nonzero invariant vector f necessarily lies in the kernel of the centered displacement average: invariance gives ⟨f,\bar z⟩=⟨f,z⟩, so ⟨f,ρ(A)(z-\bar z)⟩=0 for every A. Thus some listed representations cannot satisfy S_z≻0 on their full parameter spaces. This is not a counterexample to the conditional formula. The structural assertion remains applicable without that condition, as in the source. The source itself acknowledges rank deficiency at L000100 and L000731-L000732.

The local source repairs recorded under theory_004 and theory_006 are explicit in the material records and provenance: PSD rather than PD when S_g is singular; the correct treatment of repeated-eigenvalue square roots; GL commutation rather than an all-covariant fixed-point equation; rectangular intertwiner and passive-factor typing; represented diagram ranks rather than unconditional abstract counts; and weak rather than necessarily strict enlargement. All theorem-critical obligations are closed.
