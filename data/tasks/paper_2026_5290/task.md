# Problem

## Setup

Let \(\Omega,\widehat\Omega\subseteq\mathbb R^d\) be open sets. Let \(\phi:\Omega\to\widehat\Omega\) be a \(C^1\) diffeomorphism, and write
\[
 \widehat z=\phi(z).
\]
Let \(U:\Omega\to\mathbb R^m\) and \(\widehat U:\widehat\Omega\to\mathbb R^m\) be \(C^1\) task maps satisfying
\[
 \widehat U(\widehat z)=U(\phi^{-1}(\widehat z)). \tag{1}
\]

For a numerical vector or matrix, \(\operatorname{supp}\) denotes its nonzero coordinate or entry set. For a vector- or matrix-valued function on a specified neighborhood, its support consists of the coordinates or entries that are not identically zero there.

Work on a fixed pair of corresponding coordinate neighborhoods \(V\subseteq\Omega\) and \(\widehat V=\phi(V)\subseteq\widehat\Omega\). Compute the function supports of \(J_U\) on \(V\), and those of \(J_{\widehat U}\) and \(D\phi^{-1}\) on \(\widehat V\). Define
\[
 I_i=\operatorname{supp}((J_U)_{i,\cdot}),\qquad
 \widehat I_i=\operatorname{supp}((J_{\widehat U})_{i,\cdot}),\qquad
 r_i=|I_i|.
\]
The set \(I_i\) is the true latent-coordinate set relevant to task \(i\).

Assume the following on these neighborhoods.

1. For every \(i\in[m]\), there are points \(z_i^{(1)},\ldots,z_i^{(r_i)}\in V\) such that the \(r_i\) row vectors
\[
 (J_U(z_i^{(1)}))_{i,\cdot},\ldots,(J_U(z_i^{(r_i)}))_{i,\cdot}
\]
are linearly independent.

2. There is one auxiliary matrix \(M\in\mathbb R^{d\times d}\) whose nonzero index set equals the function support of \(D\phi^{-1}\) on \(\widehat V\). At the same points chosen in assumption 1, put \(\widehat z_i^{(\ell)}=\phi(z_i^{(\ell)})\). For every \(i\) and \(\ell\in[r_i]\), assume
\[
 \operatorname{supp}\!\left((J_U(z_i^{(\ell)}))_{i,\cdot}M\right)
 \subseteq
 \operatorname{supp}\!\left((J_{\widehat U}(\widehat z_i^{(\ell)}))_{i,\cdot}\right). \tag{2}
\]
Both supports in (2) are supports of numerical row vectors evaluated at the displayed points.

3. The estimated task map is no denser than the true one:
\[
 |\operatorname{supp}(J_{\widehat U})|
 \le |\operatorname{supp}(J_U)|. \tag{3}
\]

All conclusions below concerning coordinate transformations are local on coordinate neighborhoods.

## Task

Prove that there is a permutation \(\pi\) of \([d]\) such that, for every task \(i\in[m]\),
\[
 \widehat I_i=\pi(I_i),
\]
and there is a locally invertible function \(h_i\) for which
\[
 \widehat z_{\pi(I_i)}=h_i(z_{I_i}).
\]
In particular, the estimated subgroup for task \(i\) depends only on the true subgroup relevant to that task, up to the same permutation and an invertible within-subgroup transformation.
