# Problem

## Setup

Let \(E=\bigoplus_{\ell\in\Lambda}E_\ell\) be a finite-dimensional real Euclidean space, with a finite set of layer labels \(\Lambda\). Let a finite or compact group \(G\) act through a continuous orthogonal representation \(\rho=\bigoplus_\ell\rho_\ell\). Each layer representation is a tensor-product representation. Let \(L:E\to\mathbb R\) be twice continuously differentiable and satisfy
\[
L(\rho(A)x)=L(x)\qquad(A\in G,\ x\in E).
\]
Use uniform probability measure for a finite group and normalized Haar measure for a compact group. For \(u,v\in E\), define
\[
R_1(v)=\mathbb E_A[\rho(A)v],\qquad
R_2(u,v)=\mathbb E_A[\rho(A)uv^T\rho(A)^T].
\]
Fix \(z\in E\), and write
\[
\bar z=R_1(z),\quad g=\nabla L(z),\quad
\bar g=\nabla L(\bar z),\quad H=\nabla^2L(\bar z),
\]
\[
S_z=R_2(z-\bar z,z-\bar z),\qquad
S_g=R_2(g-\bar g,g-\bar g).
\]
The secant conclusion below is conditional on the exact orbit-wide model
\[
\nabla L(\rho(A)z)-\bar g=H(\rho(A)z-\bar z)
\qquad\text{for every }A\in G.
\]
The inverse-square-root formula is additionally conditional on \(S_z\) being positive definite. These two conditions are not assumptions of the structural assertion in part 2.

Define the global commutant and its layer-pair intertwiner spaces by
\[
\mathcal C_G=\{T\in\operatorname{End}(E):T\rho(A)=\rho(A)T\text{ for all }A\in G\},
\]
\[
\mathcal C_{\ell m}=\{T:E_m\to E_\ell:
\rho_\ell(A)T=T\rho_m(A)\text{ for all }A\in G\}.
\]
Representation complexity means the real dimension of the full linear space \(\mathcal C_G\), without additionally imposing matrix symmetry or positive semidefiniteness.

### Representations for the diagrammatic assertion

For the compact-group diagrammatic assertion, take \(G=\prod_{j=1}^q G_j\), where each \(G_j\) is one of the following groups in its defining action on \(V_j=\mathbb R^{n_j}\), with \(n_j\geq1\):

- the full orthogonal group \(O(n_j)\);
- the full signed-permutation group, consisting of matrices with exactly one nonzero entry, equal to \(1\) or \(-1\), in each row and column;
- the full group of permutation matrices.

In fixed tensor coordinates, allow
\[
E_\ell=F_\ell\otimes\bigotimes_{j=1}^q V_j^{\otimes a_{\ell j}},
\qquad a_{\ell j}\in\{0,1,2,\ldots\},
\]
up to a fixed ordering of the tensor factors. The action on \(F_\ell\) is the identity. The same group element acts on every occurrence of a given \(V_j\), including occurrences in different layers; distinct labels \(j\) denote independent groups. Identity axes are included in \(F_\ell\). Tensor powers of order zero and empty tensor products are \(\mathbb R\). The spaces \(F_\ell\) may have dimension zero.

For a set partition \(\pi\) of tensor-index positions having a common index range, its delta-diagram tensor \(D_\pi\) has entry \(1\) when the indices within every block of \(\pi\) agree, and entry \(0\) otherwise. Different blocks need not have different indices. The empty diagram has value \(1\). A pairing is a partition all of whose blocks have size two. A tensor-factor permutation operator permutes the factors of a tensor power; its diagram matches each output position to one input position. A diagram description refers to these delta tensors, not to a bound on the number of nonzero matrix entries.

For the full-linear comparison, separately let \(V=\mathbb R^n\), \(n\geq1\), and \(k\geq0\), and consider
\[
\mathcal C_{\mathrm{lin}}(n,k)=
\{T\in\operatorname{End}(V^{\otimes k}):
T A^{\otimes k}=A^{\otimes k}T\text{ for every }A\in\operatorname{GL}_n(\mathbb R)\}.
\]
This is an algebraic commutant comparison only; no normalized group average over the full linear group is defined or assumed.

## Task

Prove the following integrated theorem.

1. For every \(B\in G\) and \(u,v\in E\),
\[
\rho(B)R_1(v)=R_1(v),\qquad
\rho(B)R_2(u,v)\rho(B)^T=R_2(u,v).
\]
Under the exact orbit-wide secant model,
\[
S_g=H S_z H.
\]
If also \(S_z\) is positive definite, the equation \(X S_z X=S_g\) has exactly one symmetric positive-semidefinite solution, namely
\[
\widehat H=S_z^{-1/2}
\bigl(S_z^{1/2}S_gS_z^{1/2}\bigr)^{1/2}
S_z^{-1/2}.
\]
Here every square root is the principal positive-semidefinite square root. Prove also that \(\widehat H\in\mathcal C_G\), so it is a positive-semidefinite curvature approximation with the same invariant structure. No equality \(\widehat H=H\) is asserted when \(H\) is indefinite.

2. Every second-order orbit average belongs to \(\mathcal C_G\). Its \((\ell,m)\) block belongs to \(\mathcal C_{\ell m}\), and the global commutant is the direct sum of these spaces as a real vector space. Only diagonal intertwiner spaces are automatically algebras under composition.

For the specified compact tensor representations, prove that the layer-pair spaces are spanned by tensor products of the following diagram tensors, together with arbitrary factors in \(\operatorname{Hom}(F_m,F_\ell)\):

- for an orthogonal-group label, pairings of all positions carrying that label;
- for a signed-permutation label, set partitions of its positions into blocks of even size;
- for a permutation label, all set partitions of its positions.

Connections do not join different group labels. An odd number of positions has no pairing or even-block partition, and a spanning family with no elements spans the zero space. Show that a basis can be selected from the represented diagram tensors. Do not assume that all diagram tensors are linearly independent in every dimension.

For the full-linear comparison, prove that \(\mathcal C_{\mathrm{lin}}(n,k)\) is spanned by the tensor-factor permutation operators, again taking a linearly independent subset if necessary.

Consequently, the number of independent scalar coefficients in a basis parametrization of the full invariant-operator space is its dimension, with
\[
\dim\mathcal C_G=\sum_{\ell,m}\dim\mathcal C_{\ell m}.
\]
Finally, show that restricting an acting group to a subgroup on the same space weakly increases the commutant dimension. The specified diagram descriptions apply to restrictions that retain one of the stated representation forms.
