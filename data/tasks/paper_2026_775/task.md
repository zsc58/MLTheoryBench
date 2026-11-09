# Problem

## Setup

Let \(S_n\) be the set of permutations of \(n\) items. For \(\sigma,\sigma'\in S_n\), define the Kendall distance
\[
d_\tau(\sigma,\sigma')=\sum_{i<j}\mathbf 1\{(\sigma(i)-\sigma(j))(\sigma'(i)-\sigma'(j))<0\}.
\]
Let \(P\) be a probability law on \(S_n\), and let \(\mathcal P\) be a finite partition of \(S_n\) whose cells all have positive \(P\)-mass. For a cell \(C\), write \(P_C\) for the conditional law of \(\Sigma\sim P\) given \(\Sigma\in C\). Define
\[
p_{i,j}(C)=\Pr_{\Sigma\sim P_C}[\Sigma(i)<\Sigma(j)]\qquad(i<j).
\]
Choose a local Kemeny median \(\sigma_C^*\in S_n\) minimizing \(\mathbb E_{\Sigma\sim P_C}d_\tau(\Sigma,\sigma)\), and set
\[
V(C)=\mathbb E_{\Sigma\sim P_C}d_\tau(\Sigma,\sigma_C^*),\qquad
V'(C)=\sum_{i<j}p_{i,j}(C)(1-p_{i,j}(C)).
\]
The consensus ranking distribution associated with \(\mathcal P\) is
\[
P_{\mathcal P}=\sum_{C\in\mathcal P}P(C)\,\delta_{\sigma_C^*}.
\]
For probability laws on \(S_n\), define
\[
W_\tau(P,Q)=\inf\mathbb E[d_\tau(X,Y)],
\]
where the infimum ranges over all couplings \((X,Y)\) with marginals \(P\) and \(Q\).

## Task

Prove that every such partition and choice of local medians satisfy
\[
W_\tau(P,P_{\mathcal P})\;\le\;\sum_{C\in\mathcal P}P(C)V(C)\;\le\;2\sum_{C\in\mathcal P}P(C)V'(C),
\]
with the pairwise expression for \(V'(C)\) given above.
