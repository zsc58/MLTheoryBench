# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Cell-based coupling and first bound (3 points):** Defines a coupling sending every ranking in cell C to its chosen local median, verifies that its second marginal is the consensus ranking distribution, and derives the first Wasserstein bound. Coincident medians from different cells contribute their combined mass; no distinctness assumption is allowed.
2. **Independent-copy Kendall calculation (3 points):** For each cell, introduces independent draws from its conditional law and computes their expected Kendall distance as twice the sum of p_{i,j}(C)(1-p_{i,j}(C)), hence as 2V'(C).
3. **Median-risk comparison (2 points):** Uses local median optimality, averaged over an independent conditional draw or an equivalent valid argument, to obtain V(C)<=2V'(C). Merely citing a named method or the incorrect stronger comparison V(C)<=V'(C) does not establish this step.
4. **Aggregation and conclusion (2 points):** Weights the cellwise inequalities by P(C), sums over the partition, and states the complete chained distortion bound.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The partition must have positive-mass cells, and the Kendall pairwise probabilities must be used consistently.

The median is minimized over all of S_n, not necessarily over its cell. A proof that requires cell membership, unique medians, distinct medians, or stochastic transitivity has not proved the full stated result unless that restriction is independently removed.

The source contains local errors that are corrected in the private reference: its proof omits a factor two in the median-risk comparison, and an auxiliary passage reverses the inequality involving the sum of separate pairwise minima. Do not accept V(C)<=V'(C) or V(C)<=sum_{i<j}min{p_{i,j}(C),1-p_{i,j}(C)} as generally valid. The latter sum is a lower bound on V(C). A solver need not introduce this auxiliary quantity or discuss these source errors.

The cases n=1, deterministic conditional laws, and pairwise probabilities zero or one are covered by the same calculations. Do not demand separate case discussions when the proof already handles empty sums and zero terms. No refinement theorem, sampling model, or external ranking theorem is required.
