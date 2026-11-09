# Reference Proof

## Proof Structure

Construct a coupling that replaces each draw by its partition cell's chosen local median. Verify its second marginal and compute its transport cost. For each cell, average median optimality over an independent draw from the conditional law, then compute the independent-copy Kendall distance by summing pairwise disagreements. Finally, aggregate over the partition.

## Complete Proof

The space S_n is finite, so every conditional risk is finite, every local minimum exists, and all maps and sums below are measurable. The argument includes n=1, with empty pair sums interpreted as zero.

Let \(\Sigma\sim P\), and let \(C(\Sigma)\) be the unique cell of \(\mathcal P\) containing \(\Sigma\). Define \(\widetilde\Sigma=\sigma^*_{C(\Sigma)}\). For every \(t\in S_n\),
\[
\Pr\{\widetilde\Sigma=t\}
=\sum_{C\in\mathcal P}P(C)\mathbf 1\{\sigma_C^*=t\}
=P_{\mathcal P}(\{t\}).
\]
This also handles different cells with the same chosen median. Thus \((\Sigma,\widetilde\Sigma)\) is a coupling of \(P\) and \(P_{\mathcal P}\). Its expected cost gives
\[
W_\tau(P,P_{\mathcal P})
\le \mathbb E[d_\tau(\Sigma,\widetilde\Sigma)]
=\sum_{C\in\mathcal P}P(C)\,\mathbb E[d_\tau(\Sigma,\sigma_C^*)\mid\Sigma\in C]
=\sum_{C\in\mathcal P}P(C)V(C).
\]
The chosen median need not lie in its cell; the coupling only uses the cell to select its output.

Fix a cell \(C\). For \(t\in S_n\), put
\[
R_C(t)=\sum_{s\in S_n}P_C(\{s\})d_\tau(s,t).
\]
Median optimality gives \(V(C)\le R_C(t)\) for every \(t\). Averaging this inequality with weights \(P_C(\{t\})\) yields
\[
V(C)\le\sum_{s,t\in S_n}P_C(\{s\})P_C(\{t\})d_\tau(s,t)
=\mathbb E[d_\tau(X,Y)],
\]
where \(X,Y\) are independent with law \(P_C\).

For each item pair \(i<j\), the relative-order indicators of \(X\) and \(Y\) are independent Bernoulli variables with parameter \(p_{i,j}(C)\). Since permutations have no ties, the probability of a disagreement is
\[
p_{i,j}(C)(1-p_{i,j}(C))+(1-p_{i,j}(C))p_{i,j}(C)
=2p_{i,j}(C)(1-p_{i,j}(C)).
\]
Linearity of expectation and the definition of Kendall distance therefore give
\[
\mathbb E[d_\tau(X,Y)]
=2\sum_{i<j}p_{i,j}(C)(1-p_{i,j}(C))
=2V'(C).
\]
Consequently \(V(C)\le2V'(C)\) for every cell, including cells with zero variability. Multiplying by \(P(C)\) and summing proves
\[
\sum_{C\in\mathcal P}P(C)V(C)
\le2\sum_{C\in\mathcal P}P(C)V'(C).
\]
Combining this with the coupling bound proves the complete target for every permitted partition and every choice of local medians.

## Private Source Audit

The source defines independent-copy variability as half the expected distance at L000084 and states the correct comparison at L000087. Its proof at L000169 mistakenly writes \(V(C)\le V'(C)\); the comparison needed there is \(V(C)\le2V'(C)\), explicitly established above. The general-distance proof also needs \(W_d\), rather than the inconsistent \(W_\tau\) notation in that source display.

The selected auxiliary source passage contains a separate reversed inequality. If
\[
V''(C)=\sum_{i<j}\min\{p_{i,j}(C),1-p_{i,j}(C)\},
\]
then the risk of any fixed ranking is a sum whose pairwise terms are each at least the corresponding minimum. Thus \(V''(C)\le V(C)\), not the reverse. Also, \(p(1-p)\le\min\{p,1-p\}\), so the correct general chain is
\[
V'(C)\le V''(C)\le V(C)\le2V'(C).
\]
The uniform law on rank vectors \((1,2,3),(2,3,1),(3,1,2)\), with one cell \(S_3\), has \(V''=1\), \(V=4/3\), and \(V'=2/3\), confirming the source's direction error. The source's claim that all three quantities coincide under strict stochastic transitivity is also false: for \(n=2\) and \(p_{1,2}=3/4\), \(V=V''=1/4\) but \(V'=3/16\). Strict stochastic transitivity gives a transitive strict majority order and hence a ranking attaining every pairwise minimum, establishing only the asserted \(V=V''\) equality.

The weighted refinement inequality for \(V''\) follows from the mixture identity for pairwise probabilities and concavity, not convexity, of \(x\mapsto\min\{x,1-x\}\). None of these auxiliary \(V''\) statements or refinement statements is required by the public target.

All theorem-critical obligations have been explicitly derived. No external result or unresolved proof dependency is used.
