# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Derive the conditional product laws under each positive-probability full-label configuration satisfying the null prefix. Correctly identify dQ_0/dP_0=[P(Y=0)/Q(Y=0)]w, or an equivalent proportional-density calculation, and explain why the constant cancels from normalized assignment weights. Treat zero-probability null events without defining nonexistent conditional laws.
2. **3 points:** Derive the weighted assignment representation and the Monte Carlo distinguished-assignment law, and prove the finite weighted upper-tail bound. Account for repeated covariates, repeated sampled permutations, and tied scores, either explicitly or through a representation that handles them automatically. The argument must cover arbitrary fixed measurable scores of the entire ordered vector.
3. **3 points:** Obtain the fixed-prefix joint inequality by averaging the conditional bound, explain the conditional formulation when the null has positive probability, and apply p_N=r_N to prove the fixed-batch certification inequality. Preserve the stronger full-label conditional validity, or establish another sufficient property for the final step.
4. **2 points:** Prove the nested guarantee using the last all-negative prefix and monotonicity, explicitly excluding the no-declaration outcome. Justify the error bound at the label-determined index using validity actually established under that conditioning, then average. Do not infer full-label conditional validity from H_k-conditional validity alone.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions; the reference representation and ordering of steps are not mandatory. The substantive validity and selection arguments must be justified, not merely named.

Do not reward the exact identity dQ_0/dP_0=w without the prevalence factor unless the argument explicitly treats w only up to a constant and correctly explains cancellation. Equal negative-label prevalences are not an assumption.

Do not require distinct covariates, distinct sampled permutations, a nonempty inactive calibration set, or continuity of scores. Do not penalize harmless indexing or tie-convention choices that preserve the claims. Endpoint levels and zero-probability nulls must be covered, at least by a correct brief argument. There is no requirement of independence among the adjusted p-values.

The general claim that arbitrary monotone p-values valid only conditional on their respective H_k automatically remain valid after conditioning on all labels is not an acceptable justification. For this task, the needed conditional property follows from the specified construction and must be established or replaced by another valid argument.
