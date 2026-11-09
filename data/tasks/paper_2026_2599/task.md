# Problem

## Setup

Let \(G_0=(V,E_0)\) be a DAG on \(p\) variables. In an ordering in which the edges of \(G_0\) point from lower to higher indices, consider the Gaussian linear SEM
\[
X=BX+\varepsilon,
\]
where \(B\) is strictly lower triangular, the components of \(\varepsilon\) are independent and mean zero, and \(\operatorname{Cov}(\varepsilon)=D\) is diagonal with strictly positive entries. Let
\[
\Sigma=(I-B)^{-1}D(I-B)^{-T},\qquad \Omega=\Sigma^{-1}.
\]
For a matrix \(A\), write \(\operatorname{supp}_*(A)\) for its off-diagonal support. The moralized skeleton \(\operatorname{skel}(G_0^m)\) is obtained by adding an undirected edge between every pair of co-parents and then forgetting directions. Let \(\mathcal M(G_0)\) denote the Markov-equivalence class of \(G_0\).

Assume the no-cancellation condition: for every \(j<k\), if \(\Omega_{kj}=0\), then \(B_{kj}=0\) and \(B_{\ell j}B_{\ell k}=0\) for every \(\ell>k\).

For a permutation \(\pi\), let \(P_\pi\) be its permutation matrix, \(\Omega_\pi=P_\pi\Omega P_\pi^T\), and let \(M\) be the support mask with \(M_{jj}=1\) and \(M_{jk}=1\) for \(j\ne k\) exactly when \(\Omega_{jk}\ne0\). Set \(M_\pi=P_\pi M P_\pi^T\). The exact lower-triangular Cholesky factor \(L_\pi^{\rm ex}\) satisfies \(\Omega_\pi=L_\pi^{\rm ex}(L_\pi^{\rm ex})^T\). Its off-diagonal nonzeros define an ordering DAG: an entry \((L_\pi^{\rm ex})_{kj}\ne0\), \(j<k\), gives the edge \((\pi(j),\pi(k))\).

Let \(T_p\) be a set of candidate orderings. For each \(\pi\in T_p\), masked IC(0) returns a lower-triangular factor \(L_\pi\) satisfying
\[
(\Omega_\pi-L_\pi L_\pi^T)\circ M_\pi=0,
\qquad
L_\pi\circ(1-M_\pi)=0,
\]
where \(\circ\) is the Hadamard product. The set \(T_p\) is IC(0)-admissible if these outputs are well posed and
\[
(L_\pi L_\pi^T)\circ(1-M_\pi)=0
\]
for every \(\pi\in T_p\). ReSP chooses a minimizer of \(\|L_\pi\|_0\) over \(\pi\in T_p\), with the induced DAG defined by the off-diagonal nonzeros of the minimizing factor.

Finally, assume that \(T_p\) contains a reverse-topological ordering \(\pi_0\) of \(G_0\), and assume SMR: for every ordering \(\pi\), if its exact-Cholesky induced DAG is not in \(\mathcal M(G_0)\), then
\[
\|L_\pi^{\rm ex}\|_0>\|L_{\pi_0}^{\rm ex}\|_0.
\]

## Task

Prove the following integrated theorem.

1. If \(T_p\) is IC(0)-admissible, then every ReSP minimizer induces a DAG in \(\mathcal M(G_0)\).
2. For any candidate set \(T_p\) (without requiring IC(0)-admissibility) and any \(\pi\in T_p\), every masked IC(0) output satisfying the displayed constraints has its induced edge set contained in \(\operatorname{skel}(G_0^m)\).
