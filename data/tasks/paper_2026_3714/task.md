# Problem

## Setup

Let \(B\ge 1\) and let the latent and observed variables be block-partitioned as
\[
S=(S_1,\ldots,S_B),\qquad X=(X_1,\ldots,X_B),
\]
with \(X\) having law \(P_X\). For each block \(b\), let \(\mathcal S_b\) and \(\mathsf X_b\) be measurable state spaces, where \(\mathsf X_b\) is the observed support of \(X_b\). Assume the deterministic modular measurement model
\[
X_b=f_b(S_b)\quad\text{almost surely},
\]
where each \(f_b:\mathcal S_b\to\mathsf X_b\) is a bimeasurable bijection (both the map and its inverse are measurable).

A second admissible representation of the same observed vector may use latent blocks \(\widetilde S_1,\ldots,\widetilde S_B\), bimeasurable bijections \(\widetilde f_j\), and a permutation \(\pi\) of \(\{1,\ldots,B\}\), so that for every \(b\), \(\widetilde f_{\pi(b)}:\widetilde{\mathcal S}_{\pi(b)}\to\mathsf X_b\) is a bimeasurable bijection and
\[
X_b=\widetilde f_{\pi(b)}(\widetilde S_{\pi(b)})\quad\text{almost surely}.
\]

## Task

Prove that the deterministic observational equivalence class is exactly characterized as follows: for every second admissible representation there are within-block bimeasurable bijections
\[
g_b:\mathcal S_b\to\widetilde{\mathcal S}_{\pi(b)}
\]
such that, for each \(b\),
\[
\widetilde S_{\pi(b)}=g_b(S_b)\quad\text{almost surely},
\qquad
\widetilde f_{\pi(b)}=f_b\circ g_b^{-1},
\]
and conversely every choice of a block permutation \(\pi\) and such a family \((g_b)_{b=1}^B\) produces an admissible representation of the same proxy law by these formulas.
