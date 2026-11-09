# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly models the Shapley vector as a linear Gaussian image and the new observation as an independent noisy coordinate measurement. Establishes the relevant nondegeneracy conditions and derives, or correctly applies with verified hypotheses, the Gaussian entropy/information identity and the rank-one posterior covariance update. Information is conditional on the realized history and fixed parameters; no average over histories or prospective hyperparameter refitting is substituted.
2. **2 points:** Obtains the stated scalar acquisition by the determinant lemma or another valid Gaussian-information argument. Justifies the inverse of the projected covariance and positivity of both logarithm arguments. The exact natural-log information gain is one half of the displayed difference, which satisfies the permitted normalization.
3. **3 points:** Supplies an actual efficient computation of the projected kernel-vector quantities used in the final algorithm. In the reference route, derives the generating-polynomial coefficient interpretation, correctly accounts for the extra degree when a coalition contains the selected player, gives an O(p^2) construction for all components, and applies it to the training vectors as well as the candidate. Award equivalent credit for the corresponding justified algorithmic work in a complete alternative proof.
4. **3 points:** Supplies an actual efficient computation sufficient for the projected quadratic quantity and the final acquisition. In the reference route, derives the four membership cases and their finite weights, covers coincident players, defines the contracted prefix/suffix tables, establishes their initialization and updates including copies across the excluded player, and proves O(p^4) work. Includes training-kernel construction, training-system factorization and solves, projected matrix products, and the p-dimensional solve, and uses t>p to obtain O(p^4+t^3).

# Evaluator Notes

Accept a complete valid alternative proof. The intermediate decompositions, ESP terminology, O(p^2) vector subroutine, and particular prefix/suffix implementation describe the reference route; they are not additional conclusions required by the public task. For an alternative algorithm, allocate the same total credit to its corresponding information-identity and computational obligations, provided its complete cost meets the public bound.

For a proof following the reference route, naming elementary symmetric polynomials, dynamic programming, or prefix/suffix contraction without deriving a suitable algorithm and its cost does not close the computational obligation. Propagate an unsupported projected quadratic-form computation to the final runtime claim. An isolated index or excluded-player update omission can be a readily repairable error when the correct invariant and complete intended construction are otherwise evident, but incorrect computations are not fully correct merely because they match an erroneous source recurrence.

Require finite definitions for padded weights and coefficients; do not interpret a literal reciprocal of a zero binomial coefficient as a valid real number. Distinguish arithmetic-operation complexity from bit complexity and numerical stability. Do not require enumeration of the coalition universe, formation of the full Q matrix, candidate-set optimization, hyperparameter learning, or computation of the posterior mean.

The source-local recurrence repair is fully implemented in the reference proof. No unresolved ground-truth proof obligation is being treated as an assumed rubric step.
