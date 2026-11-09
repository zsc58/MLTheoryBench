# Reference Proof

## Proof Obligations

1. Verify integrability and legitimate conditional multiplication, and prove adjoint unbiasedness by reverse induction.
2. Prove parameter-gradient unbiasedness and the unbiasedness of minibatch means.
3. Derive the error decomposition and establish conditional orthogonality, including pairs with different sample indices; obtain the samplewise identity.
4. Prove the squared-error identity for minibatch means while retaining the within-edge cross-sample terms.

Every obligation is closed below. No independence across samples or external theorem specific to this paper is used.

## Step 001 — Integrability and Adjoint Unbiasedness

All exact forward quantities and exact maps are fixed. The output adjoint is deterministic. At a nonoutput node with d outgoing edges, its randomized adjoint is a finite sum of square-integrable edge products. For d>0,
\[
\mathbb E\|\widetilde g_v^b\|^2
\leq d\sum_{v\to w}\mathbb E\|\widetilde A_{vw}^b\widetilde g_w^b\|^2<\infty.
\]
For d=0 the sum is zero. Hence every randomized adjoint is square-integrable. Parameter products are integrable by hypothesis.

We will use the following conditional multiplication fact with its hypotheses checked explicitly. If M is an integrable random linear map, z is measurable with respect to a sigma-field H, and Mz is integrable, then
\[
\mathbb E[Mz\mid H]=\mathbb E[M\mid H]z.
\]
Indeed, on C_n={\|z\|\leq n}, the vector 1_{C_n}z is bounded and H-measurable, so coordinatewise conditional multiplication gives
\[
1_{C_n}\mathbb E[Mz\mid H]
=\mathbb E[M(1_{C_n}z)\mid H]
=1_{C_n}\mathbb E[M\mid H]z.
\]
The sets C_n increase to the whole probability space. This proves the equality without assuming integrability of an unbounded scalar factor separately.

For each nonoutput node set
\[
\mathcal F_v=\sigma\{\widetilde g_u^c:v\to u,\ 1\leq c\leq B\}.
\]
For every edge v→w, we have \(\mathcal F_v\subseteq\mathcal D_{v,w}\). The map is integrable by its finite expected operator norm; its action on \(\widetilde g_w^b\) is integrable by the edge-product second-moment assumption. Therefore
\[
\mathbb E[\widetilde A_{vw}^b\widetilde g_w^b\mid\mathcal D_{v,w}]
=A_{vw}^b\widetilde g_w^b.
\]
Taking conditional expectation again, now with respect to \(\mathcal F_v\), and summing gives
\[
\mathbb E[\widetilde g_v^b\mid\mathcal F_v]
=\sum_{v\to w}A_{vw}^b\widetilde g_w^b.
\]
This is a common downstream-message conditioning statement. It is not obtained by replacing every map after conditioning the entire sum on a single edge-specific sigma-field: the other maps in that sigma-field are already measurable and need not equal their means.

The exact seed proves unbiasedness at o. Any other terminal node has exact and approximate adjoints equal to zero. In reverse topological order, the induction hypothesis for all successors gives
\[
\mathbb E[\widetilde g_v^b]
=\sum_{v\to w}A_{vw}^b\mathbb E[\widetilde g_w^b]
=\sum_{v\to w}A_{vw}^b g_w^b
=g_v^b.
\]
Finiteness and acyclicity ensure this covers every node, including components not reaching o.

## Step 002 — Parameter Gradients and Means

Apply the conditional multiplication fact with M=\(\widetilde A_v^b\), z=\(\widetilde g_v^b\), and H=\(\sigma(\widetilde g_v^b)\). The required map and product integrability are explicit assumptions. Thus
\[
\mathbb E[\widetilde h_v^b\mid\sigma(\widetilde g_v^b)]
=A_v^b\widetilde g_v^b,
\qquad
\mathbb E[\widetilde h_v^b]=A_v^b g_v^b=h_v^b.
\]
Linearity of expectation over the finite minibatch establishes
\[
\mathbb E[\widetilde g_v]=g_v,\qquad
\mathbb E[\widetilde h_v]=h_v.
\]
Since all exact quantities are fixed, this also agrees with the source's conditional notation given the exact batch gradients.

## Step 003 — Error Decomposition and Orthogonality

For each edge and sample define
\[
\varepsilon_{vw}^b=(\widetilde A_{vw}^b-A_{vw}^b)\widetilde g_w^b,
\qquad
p_v^b=\sum_{v\to w}A_{vw}^b(\widetilde g_w^b-g_w^b).
\]
These are square-integrable: the edge products are square-integrable, every downstream adjoint is square-integrable, and the exact linear maps are bounded in finite dimensions. Subtracting the exact recursion from the approximate recursion yields
\[
\widetilde g_v^b-g_v^b=\sum_{v\to w}\varepsilon_{vw}^b+p_v^b.
\]
The same relation at o is the zero identity, with empty outgoing sums.

For each w and b,
\[
\mathbb E[\varepsilon_{vw}^b\mid\mathcal D_{v,w}]=0.
\]
For every sample index c, the vector \(p_v^c\) is \(\mathcal D_{v,w}\)-measurable, because that sigma-field contains all downstream messages from every sample. For every different successor u≠w and every c, \(\varepsilon_{vu}^c\) is also \(\mathcal D_{v,w}\)-measurable, because it contains both the other-edge map and its downstream message.

To justify orthogonality for potentially unbounded vectors, let Z be any square-integrable H-measurable vector and let Y be square-integrable with \(\mathbb E[Y\mid H]=0\). For \(Z_n=Z1_{\{\|Z\|\leq n\}}\), the defining property of conditional expectation gives \(\mathbb E\langle Y,Z_n\rangle=0\). Moreover,
\[
|\mathbb E\langle Y,Z-Z_n\rangle|
\leq (\mathbb E\|Y\|^2)^{1/2}(\mathbb E\|Z-Z_n\|^2)^{1/2}\longrightarrow0.
\]
Hence \(\mathbb E\langle Y,Z\rangle=0\). Applying this argument to the preceding measurable vectors proves, for all b,c,
\[
\mathbb E\langle\varepsilon_{vw}^b,p_v^c\rangle=0,
\qquad
\mathbb E\langle\varepsilon_{vw}^b,\varepsilon_{vu}^c\rangle=0\quad(u\ne w).
\]
Taking c=b and expanding the squared norm of the samplewise error decomposition proves
\[
\mathbb E\|\widetilde g_v^b-g_v^b\|^2
=\sum_{v\to w}\mathbb E\|\varepsilon_{vw}^b\|^2
+\mathbb E\|p_v^b\|^2.
\]
Multiplying by 1/B and summing over b proves the stated arithmetic-average consequence. Cross terms vanish in expectation, not generally pointwise.

## Step 004 — Minibatch-Mean Identity

Define
\[
L_{vw}=\frac1B\sum_{b=1}^B\varepsilon_{vw}^b,
\qquad
P_v=\frac1B\sum_{b=1}^B p_v^b.
\]
Average the vector error decompositions before taking a squared norm:
\[
\widetilde g_v-g_v=\sum_{v\to w}L_{vw}+P_v.
\]
All these vectors are square-integrable. The cross-sample orthogonality established in Step 003 gives
\[
\mathbb E\langle L_{vw},P_v\rangle
=\frac1{B^2}\sum_{b,c=1}^B\mathbb E\langle\varepsilon_{vw}^b,p_v^c\rangle=0,
\]
and, for u≠w,
\[
\mathbb E\langle L_{vw},L_{vu}\rangle
=\frac1{B^2}\sum_{b,c=1}^B\mathbb E\langle\varepsilon_{vw}^b,\varepsilon_{vu}^c\rangle=0.
\]
Consequently,
\[
\mathbb E\|\widetilde g_v-g_v\|^2
=\sum_{v\to w}\mathbb E\|L_{vw}\|^2+\mathbb E\|P_v\|^2.
\]
Substituting the definitions gives exactly
\[
\mathbb E\|\widetilde g_v-g_v\|^2
=\sum_{v\to w}\mathbb E\left\|
\frac1B\sum_{b=1}^B(\widetilde A_{vw}^b-A_{vw}^b)\widetilde g_w^b
\right\|^2
+\mathbb E\left\|
\frac1B\sum_{b=1}^B\sum_{v\to w}A_{vw}^b(\widetilde g_w^b-g_w^b)
\right\|^2.
\]
No claim was made that local errors on the same edge are orthogonal across samples; their cross-sample terms remain inside \(\mathbb E\|L_{vw}\|^2\). Nor were cross-sample terms inside \(\mathbb E\|P_v\|^2\) removed. Thus shared batch randomness is allowed. Merely averaging the samplewise squared-error identities would not prove this batch-mean identity.

At the output and every other terminal node, both variance identities are zero identities. The argument also covers B=1, zero-dimensional spaces, zero adjoints, and zero exact or randomized maps whenever the displayed assumptions hold.

## Source-Repair Record

The selected source chain is theory_002, theory_003, theory_004. The node/derivative indices in L000309 and L000324 are normalized to the uniquely typed forward and reverse maps. In the source proof, L002250 must be read as an equality after taking expectations; L002247 establishes expected, not pathwise, cancellation. The appeal to samplewise independence at L002252 is replaced by the explicit cross-sample orthogonality calculation above, which uses precisely the all-sample conditioning already present at L000370. This recovers the unchanged source conclusion at L000391–L000395 and L002254–L002255. All proof obligations are closed.
