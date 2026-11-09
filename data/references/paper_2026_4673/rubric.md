# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Backward unbiasedness induction (3 points).** Uses the exact output seed and reverse topological order. Correctly obtains conditional unbiasedness of each edge product from the operator assumption and measurability of its downstream message. Uses the tower property through a common downstream-message sigma-field, or an equivalent valid termwise argument, to prove samplewise adjoint unbiasedness. Handles other terminal nodes by the empty-sum recursion. Conditional expectations and products must be justified under the stated integrability assumptions.
2. **Parameter-gradient and minibatch unbiasedness (2 points).** Uses the parameter-side conditional operator assumption to obtain the conditional mean of the parameter product, then combines it with adjoint unbiasedness. Applies finite-sum linearity to establish both minibatch unbiasedness claims.
3. **Error decomposition and conditional orthogonality (3 points).** Derives the local-plus-propagated vector error split. Justifies orthogonality between a local edge error and propagated errors, and between local errors on distinct outgoing edges. The justification must cover different sample indices, using the all-sample downstream messages and other-edge maps in the conditioning sigma-field. Obtains the samplewise mean-square identity; its arithmetic-average consequence follows by finite summation.
4. **Minibatch-mean variance identity (2 points).** Averages vector errors before squaring and obtains the displayed source-faithful batch identity. Preserves within-edge cross-sample terms and the terms inside the propagated-error norm. Does not substitute the average samplewise mean-square error for the mean-square error of the minibatch mean.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its exact order of steps.

The assumptions do not assert independence of randomized backward passes across samples. A proof imposing that extra assumption does not establish the full task. Conditional orthogonality is sufficient and must not be replaced by an unsupported independence claim. In particular, local errors on the same edge need not be uncorrelated across samples.

Conditioning the entire reverse sum on one edge-specific sigma-field generally leaves the other local maps random but measurable; it does not replace them all by their exact maps. The tower-property argument using a common downstream-message sigma-field, or separate valid calculations for each summand, avoids this error.

Cross terms vanish after taking expectations, not as a pathwise identity. An unexplained pathwise deletion or an unsupported conditional factorization is a proof defect. Routine integrability details may be implicit in an otherwise rigorous argument if the supplied moment assumptions clearly suffice.

A proof of only the samplewise identity and its arithmetic average omits the minibatch-mean variance target. Likewise, a claimed batch variance formula without justification of the cross-sample, distinct-edge and local/propagated cancellations leaves a theorem-critical gap.

There are no unresolved reference-proof obligations and no specialized external results that a solver must cite.
