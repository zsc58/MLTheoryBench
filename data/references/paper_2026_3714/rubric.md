# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Set up the blockwise comparison (2 points).** Correctly uses the two admissible deterministic representations of the same observed blocks, including the relabeling permutation and bimeasurable-bijection assumptions.
2. **Construct and validate the latent reparameterizations (3 points).** Defines \(g_b=\widetilde f_{\pi(b)}^{-1}\circ f_b\) and proves that each \(g_b\) is a bimeasurable bijection, including a valid inverse.
3. **Derive the necessary transformed representation (3 points).** From equality of the observed blocks, rigorously obtains \(\widetilde S_{\pi(b)}=g_b(S_b)\) almost surely. Also establishes \(\widetilde f_{\pi(b)}=f_b\circ g_b^{-1}\) pointwise on the entire corresponding latent state space, using the definition or inverse formula for \(g_b\), or an equivalent valid argument.
4. **Prove sufficiency and exactness (2 points).** Shows that every permutation and every family of within-block bimeasurable bijections constructs an admissible representation with the same proxy law, establishing the stated ``exactly up to'' characterization.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof that only names reparameterization or permutation without establishing both directions and the bimeasurability claims is incomplete. Propagate errors only when they leave the final equivalence-class conclusion unsupported.

Distinguish almost-sure equality of random variables from pointwise equality of measurement maps. Substitution into an almost-sure identity alone does not prove a functional identity everywhere, even if the observed space is called a support. A concise algebraic rearrangement of the definition of \(g_b\) is sufficient; a separate long calculation is not required.

The public setup already compares representations of the same observed vector. Do not require a separate common-realization argument for full credit on that stated comparison. If a solution discusses representations originally given on different probability spaces, equality of their observed laws permits common-observation realizations via the measurable inverse maps; it does not imply almost-sure equality under an arbitrary coupling.
