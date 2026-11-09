# Reference Proof

## Proof Structure

First verify directly from the filtering definition that each document has a closed interval of safe thresholds. Then condition on the test group and the calibration group-index set, apply an explicit tie-safe rank argument, and average over the group-index set. The endpoint threshold handles empty calibration groups and ranks beyond the calibration sample size.

## Complete Proof

All score and grouping functions and the measurable claim tie-breaking rule are fixed. The documents are i.i.d., and the auxiliary uniforms are mutually independent and independent of the documents.

### 1. Filtering and the safe-threshold interval

Fix a document, order its claims as in the task, and write its cumulative products as \(\Pi_0=1,\Pi_1,\ldots,\Pi_N\). Fix \(u\in(0,1)\). For each \(j\in\{1,\ldots,N\}\), define, for this proof only,
\[
b_j=(1-u)\Pi_{j-1}+u\Pi_j.
\]
We show that the corrected filtering rule retains claim \(c_{(j)}\) exactly when \(\tau<b_j\).

At \(\tau=1\), the cutoff is zero and the boundary inclusion probability is zero, so no claim is retained. Since every \(b_j\le1\), the asserted characterization holds.

Now let \(0\le\tau<1\), and denote the cutoff in the filtering definition by \(L\). If \(j\le L\), then \(\Pi_j>\tau\), and therefore \(b_j\ge\Pi_j>\tau\); these claims are retained. If \(L<N\), then \(\Pi_L>\tau\ge\Pi_{L+1}\), where \(\Pi_L>\tau\) also holds when \(L=0\) because \(\Pi_0=1\). Thus the denominator in the boundary probability is positive. Its boundary claim is retained precisely when
\[
u<\frac{\Pi_L-\tau}{\Pi_L-\Pi_{L+1}},
\]
which is equivalent to
\[
\tau<(1-u)\Pi_L+u\Pi_{L+1}=b_{L+1}.
\]
Finally, if \(j>L+1\), then \(\Pi_{j-1}\le\tau\), so \(b_j\le\Pi_{j-1}\le\tau\); these claims are not retained. This proves the characterization, including cases with zero or unit scores.

Let \(A\) be the factual claim set and define
\[
e=\max\bigl(\{0\}\cup\{b_j:c_{(j)}\notin A\}\bigr).
\]
For an empty document or a document with no false claims, this maximum is zero. The characterization just proved gives
\[
F(\hat p,\tau,u;P,C)\subseteq A
\quad\Longleftrightarrow\quad
\tau\ge e.
\]
Consequently the set in the definition of \(E\) is exactly \([e,1]\). In particular, its infimum exists, belongs to \([0,1]\), and is attained. It follows that, for every document and \(u\in(0,1)\),
\[
E\le\tau
\quad\Longleftrightarrow\quad
F(\hat p,\tau,u;P,C)\subseteq A.
\]
This also verifies threshold monotonicity directly from the definition. Measurability follows from the measurable score and ordering functions and finite products and maxima on each document-size stratum.

### 2. Conditional group exchangeability

Fix a group \(k\) with \(\Pr(G_{n+1}=k)>0\). Fix a subset \(S\subseteq\{1,\ldots,n\}\) for which the conditioning event
\[
H_S=\{G_{n+1}=k,\ I_k=S\}
\]
has positive probability, and write \(m=|S|\).

Because group membership is a fixed function of an individual document, conditioning on \(H_S\) conditions each selected calibration document and the test document to belong to group \(k\). Independence of the documents implies that these \(m+1\) documents are independent with the common conditional law \(\mathcal L(D\mid g(P,C)=k)\). The conditions on the remaining documents do not change that conclusion. The auxiliary uniforms remain independent uniforms and are independent of these documents.

The conformity score is the same measurable function of a document and its auxiliary uniform at every selected index. Hence the selected calibration scores and the test score are exchangeable conditional on \(H_S\).

### 3. Adjusted order statistic, ties, and endpoints

Write \(r=\lceil(m+1)(1-\alpha)\rceil\). Since \(0<\alpha<1\), we have \(1\le r\le m+1\).

If \(r=m+1\), the task defines \(q_k=1\). Every conformity score is at most one, so
\[
\Pr(E_{n+1}\le q_k\mid H_S)=1.
\]
This includes \(m=0\). The filter at that endpoint is empty.

Suppose instead that \(r\le m\). Attach to the \(m+1\) selected scores fresh independent continuous uniform tie-breakers, independent of all existing variables, solely for this proof. Order the score/tie-breaker pairs lexicographically. They are exchangeable conditional on \(H_S\) and are distinct almost surely. For each rank, exactly one index occupies it, and symmetry gives each index the same probability of doing so. Therefore the test pair's rank \(R\) is uniform on \(\{1,\ldots,m+1\}\).

The event \(R\le r\) implies \(E_{n+1}\le q_k\). Indeed, if \(E_{n+1}>q_k\), at least \(r\) calibration scores are strictly smaller than \(E_{n+1}\), so the test pair's rank is at least \(r+1\), regardless of tie-breakers. Thus
\[
\Pr(E_{n+1}\le q_k\mid H_S)
\ge \Pr(R\le r\mid H_S)
=\frac{r}{m+1}
\ge1-\alpha.
\]
The argument permits arbitrary ties in the original scores.

### 4. Transfer to filtering and average

The pointwise equivalence in Step 1 remains valid at the random threshold \(q_k\). Hence, in both rank cases,
\[
\Pr\!\left(F(\hat p,q_k,U_{n+1};P_{n+1},C_{n+1})\subseteq A_{n+1}\mid H_S\right)\ge1-\alpha.
\]
On \(G_{n+1}=k\), this is the filtering rule in the task. Average over all calibration index sets \(S\) conditional on \(G_{n+1}=k\). Their conditional probabilities sum to one, giving
\[
\Pr\!\left(F_{n,\alpha}(P_{n+1},C_{n+1})\subseteq A_{n+1}\mid G_{n+1}=k\right)\ge1-\alpha.
\]
The group \(k\) was arbitrary among positive-probability groups, proving the claim.

## Private Source-Audit Notes

The source's adjusted-rank intent is preserved. Its original non-strict boundary inclusion does not justify replacing an infimum by a minimum; finite-valued prefix paths can have open safe-threshold sets. The explicit boundary completion in the task repairs that issue and the zero/unit-score endpoints without assuming score accuracy or atomlessness. Oracle exact coverage and independence of claim labels are not used. All theorem-critical obligations are derived above; no unresolved private proof dependency remains.
