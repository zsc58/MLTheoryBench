# Reference Proof

## Proof Structure

For a second admissible representation, compose the first measurement map with the inverse of the relabeled second map. This gives a within-block bimeasurable bijection. Equality of the two representations of each observed block yields the transformed latent block almost surely. The definition of the bijection yields the transformed measurement map pointwise. Finally, construct a second representation from any such family of bijections and any block permutation, proving that the characterization is exact. Realizing representations using a common observed vector also gives the observational-law interpretation.

## Complete Proof

Fix a second admissible representation and its permutation \(\pi\). For each block \(b\), define
\[
g_b=\widetilde f_{\pi(b)}^{-1}\circ f_b.
\]
The map \(f_b\) maps \(\mathcal S_b\) bijectively onto \(\mathsf X_b\), and \(\widetilde f_{\pi(b)}^{-1}\) maps \(\mathsf X_b\) bijectively onto \(\widetilde{\mathcal S}_{\pi(b)}\). Thus \(g_b\) is a bijection between the required spaces, with inverse
\[
g_b^{-1}=f_b^{-1}\circ\widetilde f_{\pi(b)}.
\]
Each displayed composition consists of measurable maps, so both \(g_b\) and its inverse are measurable. Hence \(g_b\) is bimeasurable.

The two representations describe the same observed block, so
\[
f_b(S_b)=X_b=\widetilde f_{\pi(b)}(\widetilde S_{\pi(b)})
\quad\text{almost surely}.
\]
Applying \(\widetilde f_{\pi(b)}^{-1}\) on this probability-one event gives
\[
\widetilde S_{\pi(b)}
=\widetilde f_{\pi(b)}^{-1}(f_b(S_b))
=g_b(S_b)
\quad\text{almost surely}.
\]
Because there are finitely many blocks, these equalities also hold simultaneously on a probability-one event.

The measurement-map identity follows pointwise from the inverse formula, rather than from the almost-sure latent equality. For every \(\widetilde s\in\widetilde{\mathcal S}_{\pi(b)}\),
\[
(f_b\circ g_b^{-1})(\widetilde s)
=f_b\bigl(f_b^{-1}(\widetilde f_{\pi(b)}(\widetilde s))\bigr)
=\widetilde f_{\pi(b)}(\widetilde s).
\]
The cancellation is valid because \(\widetilde f_{\pi(b)}(\widetilde s)\in\mathsf X_b\). Therefore
\[
\widetilde f_{\pi(b)}=f_b\circ g_b^{-1}
\]
as functions on the entire corresponding latent state space. This proves necessity.

Conversely, choose any permutation \(\pi\) and any family of bimeasurable bijections \(g_b:\mathcal S_b\to\widetilde{\mathcal S}_{\pi(b)}\). Define
\[
\widetilde S_{\pi(b)}:=g_b(S_b),\qquad
\widetilde f_{\pi(b)}:=f_b\circ g_b^{-1}.
\]
Since \(\pi\) is a permutation, these definitions assign every new latent block and measurement map exactly once. Each new latent block is measurable. Each new measurement map is a bimeasurable bijection onto \(\mathsf X_b\), with measurable inverse \(g_b\circ f_b^{-1}\). Moreover,
\[
\widetilde f_{\pi(b)}(\widetilde S_{\pi(b)})
=(f_b\circ g_b^{-1})(g_b(S_b))
=f_b(S_b)=X_b
\quad\text{almost surely}.
\]
Thus the constructed representation is admissible and reproduces the same observed vector, hence the same joint proxy law \(P_X\).

For completeness, the comparison using a common observed vector also covers admissible representations initially given on different probability spaces but inducing the same joint proxy law. In any admissible representation, inversion gives \(S_b=f_b^{-1}(X_b)\) almost surely. Consequently its entire latent vector is almost surely a specified measurable function of its observed vector, and its joint latent law is determined by \(P_X\) and these inverse maps. Taking one vector \(X\) with law \(P_X\) and applying the inverse maps from each representation therefore realizes both representations with their original latent laws on this common probability space. The preceding comparison applies to these realizations; it does not assert almost-sure equality under an arbitrary preexisting coupling of different observed vectors.

Both directions hold. Within the stated admissible deterministic class, the observational equivalence class is exactly the family of within-block bimeasurable reparameterizations, together with the permitted relabeling of latent blocks.
