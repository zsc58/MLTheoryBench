# Reference Proof

## Proof Obligations

1. Identify the local differentiable objectives and the quantities held fixed.
2. Differentiate reconstruction twice and identify its matrix in column-stacked coordinates.
3. Derive the exact Hessian of a selected weighted negative cosine, including the cosine factor multiplying the identity matrix.
4. Aggregate the clustering blocks using activation-weighted mass, derive the tangent decomposition, and handle unsupported indices.
5. Establish the conditioning formulas on a nonempty, consistently indexed supported coordinate space.
6. Verify positive semidefiniteness and derive the spectral-norm condition-number bound.

All six obligations are discharged below. No specialized external result is needed.

## Complete Proof

### Local differentiation convention

All token states, selected indices, coefficients c_s, and numerical reconstruction vectors a_t are fixed. The selected clustering similarities remain functions of the variable prototype matrix. Since each reference prototype is nonzero, the displayed objectives are smooth in a sufficiently small neighborhood of P with nonzero columns. The frozen selections and strictly positive selected branches identify the local clustering objective with its displayed sum of negative cosines.

### Reconstruction

For a perturbation \(\Delta P\), differentiation with the vectors \(a_t\) held fixed gives
\[
\nabla_P L_{\rm rec}
=\eta\sum_{t\in T}(Pa_t-z_t)a_t^{\mathsf T},
\qquad
 d(\nabla_P L_{\rm rec})[\Delta P]
=\eta\sum_{t\in T}\Delta P\,a_ta_t^{\mathsf T}
=\eta\Delta P G_A.
\]
The j-th column of this operator is \(\eta\sum_i(G_A)_{ij}\Delta p_i\). Because \(G_A\) is symmetric, the block matrix in column-stacked coordinates is therefore
\[
H_{\rm rec}=\eta G_A\otimes I_d.
\]

### A selected cosine term

Consider \(f(p)=-c\,v^{\mathsf T}p/\|p\|_2\), where \(c\) and \(v\) are fixed. Write \(\ell=\|p\|_2\), \(q=p/\ell\), and \(\alpha=v^{\mathsf T}q\). For a perturbation \(h\),
\[
d\ell[h]=q^{\mathsf T}h,\qquad
dq[h]=\ell^{-1}(I_d-qq^{\mathsf T})h,\qquad
d\alpha[h]=\ell^{-1}(v-\alpha q)^{\mathsf T}h.
\]
The gradient is
\[
\nabla f(p)=-\frac c\ell(v-\alpha q).
\]
Differentiating this expression yields
\[
d(\nabla f)[h]
=\frac c{\ell^2}\left[\alpha I_d+qv^{\mathsf T}+vq^{\mathsf T}-3\alpha qq^{\mathsf T}\right]h.
\]
Consequently, for an occurrence \(s\) assigned to prototype \(j\), with \(\alpha_s=v_{t(s)}^{\mathsf T}q_j\), its Hessian block is
\[
\frac{c_s}{\|p_j\|_2^2}
\left[\alpha_s I_d+q_jv_{t(s)}^{\mathsf T}+v_{t(s)}q_j^{\mathsf T}-3\alpha_s q_jq_j^{\mathsf T}\right].
\]
In particular, the identity coefficient is \(c_s\alpha_s\), not \(c_s\).

### Aggregation and tangent decomposition

Each clustering summand depends on exactly one prototype column, so mixed second derivatives between distinct prototype columns vanish. Summing all occurrences assigned to \(j\) gives
\[
B_j=\frac1{\|p_j\|_2^2}
\left[A_j I_d+q_jb_j^{\mathsf T}+b_jq_j^{\mathsf T}-3A_jq_jq_j^{\mathsf T}\right],
\]
where
\[
A_j=\sum_{s:k(s)=j}c_s\alpha_s,
\qquad b_j=\sum_{s:k(s)=j}c_sv_{t(s)}.
\]
These definitions imply
\[
q_j^{\mathsf T}b_j=\sum_{s:k(s)=j}c_s\alpha_s=A_j.
\]
Since \(q_j\) has unit norm, \(t_j=b_j-A_jq_j\) satisfies \(q_j^{\mathsf T}t_j=0\). This is a consequence of the activation-weighted definition, not an additional alignment assumption. Substituting \(b_j=A_jq_j+t_j\) gives
\[
B_j=\frac1{\|p_j\|_2^2}
\left[A_j(I_d-q_jq_j^{\mathsf T})+q_jt_j^{\mathsf T}+t_jq_j^{\mathsf T}\right].
\]
If \(j\notin S\), every occurrence assigned to \(j\) has zero coefficient, or there are no such occurrences. Hence \(A_j=b_j=t_j=0\) and \(B_j=0\). This does not require the corresponding reconstruction block to vanish.

Adding the two Hessians establishes
\[
H_{\rm rec+clst}
=\eta G_A\otimes I_d+\operatorname{diag}(B_1,\ldots,B_K).
\]
The calculation also covers an empty token or clustering collection: the relevant sums and blocks are zero.

### Supported-coordinate factorization

Suppose \(S\ne\varnothing\). For every \(j\in S\), at least one selected coefficient is positive and every selected similarity is positive. Thus \(A_j>0\), so the displayed diagonal matrix \(D\) is positive definite. In particular, it satisfies the hypothesis of the conditioning assertion. Its square root and inverse square root exist.

The matrices \(D\), \(G_{A,S}\), \(H_{\rm tan}\), and \(M\) all act on \(\mathbb R^{|S|}\). Direct multiplication gives
\[
D^{1/2}(I_{|S|}+M)D^{1/2}
=D+\eta G_{A,S}=H_{\rm tan}.
\]
Multiplying by \(D^{-1/2}\) on both sides yields
\[
D^{-1/2}H_{\rm tan}D^{-1/2}=I_{|S|}+M.
\]
Here \(H_{\rm tan}\) is the defined scalar-index surrogate; this argument does not identify it with the full Euclidean Hessian or with an exact tangent-space restriction of that Hessian.

### Spectral conditioning

Let \(a_{t,S}\) be the subvector of \(a_t\) indexed by \(S\). Then
\[
G_{A,S}=\sum_{t\in T}a_{t,S}a_{t,S}^{\mathsf T}.
\]
For every \(x\in\mathbb R^{|S|}\),
\[
x^{\mathsf T}Mx
=\eta\sum_{t\in T}\left(a_{t,S}^{\mathsf T}D^{-1/2}x\right)^2\ge0.
\]
Thus \(M\) is real symmetric positive semidefinite. In an orthonormal eigenbasis for \(M\), the matrices \(I_{|S|}+M\) and its inverse are diagonal with entries \(1+\mu_i\) and \((1+\mu_i)^{-1}\), respectively, where every \(\mu_i\ge0\). Their spectral norms are therefore \(1+\lambda_{\max}(M)\) and \((1+\lambda_{\min}(M))^{-1}\). It follows that
\[
\kappa(D^{-1/2}H_{\rm tan}D^{-1/2})
=\kappa(I_{|S|}+M)
=\frac{1+\lambda_{\max}(M)}{1+\lambda_{\min}(M)}
\le1+\lambda_{\max}(M).
\]
No positive lower eigenvalue of \(G_{A,S}\) is required. If \(S=\varnothing\), the Hessian identity remains valid, but the problem makes no assertion involving extreme eigenvalues or condition numbers of an empty matrix.

## Source Correspondence

The source distinguishes frozen reconstruction coefficients from differentiated selected clustering similarities at L000357. Its normalized clustering weights are \(\lambda_{R_1}/K\) for selected prototype winners and \(\lambda_{R_2}/n\) for selected token winners, as displayed at L001019-L001021. These are represented by the occurrence coefficients \(c_s\); a pair selected by both components can have two occurrences. The source's activation mass, pairwise Hessian, aggregate block, and tangent decomposition appear at L001021 and L001042-L001054. Reconstruction is derived at L001029-L001035, and the surrogate factorization and condition bound at L001060-L001068. The supported-coordinate convention makes the source's supported-prototype normalization explicit without assigning inverse stiffness to unsupported indices. No source formula is repaired.
