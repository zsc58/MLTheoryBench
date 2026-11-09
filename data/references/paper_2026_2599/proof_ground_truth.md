# Reference Proof

## Proof Structure

1. Derive the off-diagonal precision support from the SEM and the no-cancellation condition.
2. Combine the masked equations and IC(0)-admissibility to obtain exact factorization, including the possible diagonal-sign convention for triangular factors.
3. Compare a ReSP minimizer with the candidate output for the reverse-topological reference ordering and apply SMR.
4. Use the support constraint to prove containment in the moralized skeleton for arbitrary orderings.

## Complete Proof

Let \(D=\operatorname{Cov}(\varepsilon)\). Since \(B\) is strictly lower triangular,
\[
\Omega=(I-B)^T D^{-1}(I-B).
\]
For \(j<k\),
\[
\Omega_{kj}=-D_{kk}^{-1}B_{kj}+\sum_{\ell>k}D_{\ell\ell}^{-1}B_{\ell k}B_{\ell j}.
\]
If \(j\) and \(k\) are neither adjacent nor co-parents of a common child, then \(B_{kj}=0\) and every product in the sum is zero, so \(\Omega_{kj}=0\). Conversely, if \(\Omega_{kj}=0\), the no-cancellation condition gives \(B_{kj}=0\) and \(B_{\ell j}B_{\ell k}=0\) for every \(\ell>k\). Thus there is neither an adjacency nor a common child. Interpreting off-diagonal support as unordered variable pairs, this yields
\[
\operatorname{supp}_*(\Omega)=\operatorname{skel}(G_0^m).
\]
Permuting indices gives
\[
\operatorname{supp}_*(\Omega_\pi)=\pi(\operatorname{skel}(G_0^m)).
\]

Fix \(\pi\in T_p\). The masked IC(0) output satisfies
\[
(\Omega_\pi-L_\pi L_\pi^T)\circ M_\pi=0,
\qquad
L_\pi\circ(1-M_\pi)=0.
\]
Because \(M\) is the support mask, \(\Omega_\pi\circ(1-M_\pi)=0\). IC(0)-admissibility gives
\[
(L_\pi L_\pi^T)\circ(1-M_\pi)=0.
\]
Therefore the difference \(\Omega_\pi-L_\pi L_\pi^T\) vanishes both on \(M_\pi\) and on its complement, so
\[
\Omega_\pi=L_\pi L_\pi^T.
\]

Since \(\Omega_\pi\) is positive definite, the diagonal entries of the lower-triangular \(L_\pi\) are nonzero. Multiplying \(L_\pi\) on the right by a diagonal sign matrix makes its diagonal positive without changing \(L_\pi L_\pi^T\), its zero pattern, or its \(\ell_0\) norm. Hence \(L_\pi\) has the same sparsity as the unique exact Cholesky factor \(L_\pi^{\rm ex}\).

Let \(\pi_0\in T_p\) be the assumed reverse-topological ordering of \(G_0\). The masked IC(0) output for \(\pi_0\) is feasible by definition and, by the exact-factorization argument above, is an exact factor of \(\Omega_{\pi_0}\). Thus its sparsity equals \(\|L_{\pi_0}^{\rm ex}\|_0\). If \((\hat\pi,\hat L)\) is any ReSP minimizer, optimality gives
\[
\|\hat L\|_0\leq \|L_{\pi_0}^{\rm ex}\|_0.
\]
The induced DAG of \(\hat L\) is the same as that of \(L_{\hat\pi}^{\rm ex}\), because the factors have the same off-diagonal zero pattern. If this DAG were outside \(\mathcal M(G_0)\), SMR would imply
\[
\|\hat L\|_0=\|L_{\hat\pi}^{\rm ex}\|_0
>\|L_{\pi_0}^{\rm ex}\|_0,
\]
contradicting optimality. Therefore every ReSP minimizer induces a DAG in \(\mathcal M(G_0)\).

For the robustness claim, let \(\pi\in T_p\) be arbitrary and let \(L_\pi\) be any masked IC(0) output satisfying the displayed constraints. If \((L_\pi)_{kj}\neq0\) for \(j<k\), then the support constraint implies \((M_\pi)_{kj}=1\), hence \((\Omega_\pi)_{kj}\neq0\). Returning to the original labels, the unordered pair \(\{\pi(j),\pi(k)\}\) belongs to \(\operatorname{supp}_*(\Omega)=\operatorname{skel}(G_0^m)\). Consequently every induced edge belongs to the moralized skeleton:
\[
E_{\mathrm{ind}}(\pi,L_\pi)\subseteq \operatorname{skel}(G_0^m).
\]
This proves both claims.
