# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly decomposes the classifier into signal and orthogonal components and writes the corresponding logits under the signal-plus-noise model, using the same realized base training sample at the compared amplitudes.
- **4 points:** Constructs the inverse orthogonal rescaling for \(t'=\beta\sigma_n\) and proves that every training logit, hence the objective value, is preserved. Uses invertibility to establish a bijection between the complete global-minimizer sets, including nonemptiness at the compared amplitude.
- **3 points:** Applies the same coupling and rescaling to an independent test example and proves pointwise preservation of test logits/classification indicators and equality of the attainable generalization-accuracy sets, conditionally on the fixed training realization.
- **1 point:** Takes suprema of these nonempty subsets of \([0,1]\) and concludes for arbitrary \(\beta>0\) that optimal generalization accuracy is independent of the positive orthogonal-noise amplitude, with all other parameters and base laws fixed.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat failure to establish the minimizer correspondence or test-logit preservation as a theorem-critical gap; merely naming a rescaling argument earns no credit for those steps.

Existence at the reference amplitude is an explicit domain condition, not an additional theorem the solver must prove. Existence at the compared amplitude must follow from the correspondence. Do not accept the unsupported claim that positive alpha and a convex even penalty automatically ensure attainment: constant penalties are permitted by those properties. Do not require nonconstancy, coercivity, strict convexity, full rank, uniqueness, or a specified optimization algorithm.

The public target compares amplitude-indexed versions of one base training realization. Equality of realized accuracies for independently regenerated training samples is neither asserted nor required. Test probability is over the independent test draw only; no training expectation or measurable optimizer selection is required.

The stated tie convention must be respected, but pointwise equality of test logits handles ties automatically. The positive-amplitude domain excludes zero amplitude. The proof must remain valid for zero signal-noise amplitude, one-dimensional inputs, rank-deficient designs, and nonunique minimizers; no separate case analysis is needed if the argument already covers them.
