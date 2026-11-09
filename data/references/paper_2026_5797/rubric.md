# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Weighted coupling bound (2 points).** Constructs independent standard Gaussians and the monotone optimal transports to the component laws, verifies that the shared-noise Gaussian projection is standard normal, and expands the centered independent differences to obtain the weighted upper bound. Checks the relevant finite-second-moment and transport hypotheses.
2. **Strictness mechanism (4 points).** Correctly shows that equality would make the constructed coupling optimal and hence give a nondecreasing functional dependence on the Gaussian projection. Justifies the regularity or measure-theoretic steps used to extract constraints from this dependence. Proves that two active coordinates force affine transports with a common slope, uses centering and unit variance to identify the active Gaussian laws, and derives the contradiction with the at-most-one-Gaussian assumption. An everywhere differentiable argument, a justified almost-everywhere argument, or another valid rigidity argument is acceptable.
3. **Orthogonal aggregation (2 points).** Applies the row-wise bound to an arbitrary orthogonal matrix and uses column squared-entry sums to derive the joint contrast upper bound.
4. **Equality characterization (2 points).** Proves equality forbids mixed rows, deduces that orthogonality then gives a signed permutation, and verifies that every signed permutation attains equality, including invariance of the contrast under reflection.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The smooth strictly positive component densities justify smooth Gaussian-to-source quantile maps by the inverse function theorem. No additional tail condition, bounded-density hypothesis, or smoothness assumption on a mixture density is required. A proof differentiating an almost-sure identity must justify that step; a proof concluding affinity from almost-everywhere constant derivatives must supply sufficient regularity, which is available here. Routine omitted justifications should be distinguished from a substantive failure to establish equality rigidity. Do not require a Hessian calculation or an invocation of Caffarelli regularity.

Zero weights, negative weights, and the possibility of one Gaussian source are allowed. Rigidity is required only for active coordinates. All four core steps are closed in the reference proof; there is no unresolved dependency to treat as an assumed lemma.
