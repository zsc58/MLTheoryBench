# Reference Proof

## Proof Structure

For each initial cluster, identify the second stage with greedy set cover on the alpha-ball family. Reflexivity gives progress and termination, while membership in a selected ball gives both guardrails. The classical greedy set-cover bound then gives the representative-count guarantee.

## Complete Proof

Fix a cluster C_k. Define U_0=C_k. At iteration t, let
\[
M_t(i)=B(i)\cap U_t\qquad(i\in C_k),
\]
choose r_t in C_k maximizing |M_t(i)|, assign every point of M_t(r_t) to r_t, set R_k←R_k union {r_t}, and set U_{t+1}=U_t minus M_t(r_t).

If U_t is nonempty, choose u in U_t. The similarity relation is reflexive, so u∈B(u), and therefore u∈M_t(u). Hence the maximum row size is at least one, so |M_t(r_t)|≥1 and U_{t+1} is strictly smaller than U_t. Since C_k is finite, the process terminates with U_t=emptyset, and every point of C_k is assigned exactly once.

Whenever i is assigned to r_t, i∈M_t(r_t)⊆B(r_t). Thus i~r_t, which by definition means s(z_i,z_{r_t})≥alpha and a_i=a_{r_t}. This proves both exact per-sample guardrails. Applying the same argument to every cluster of the partition proves the global assignment guarantee.

Let OPT_k be the minimum number of sets from F_k={B(i)∩C_k:i∈C_k} whose union is C_k. The sets selected above are exactly the sets chosen by greedy set cover: at each iteration the set covering the largest number of currently uncovered elements is selected. The family covers C_k because each u∈C_k lies in B(u)∩C_k by reflexivity. By the classical greedy set-cover theorem, greedy uses at most (1+ln|C_k|)OPT_k sets. Therefore |R_k|≤(1+ln|C_k|)OPT_k for every k.
