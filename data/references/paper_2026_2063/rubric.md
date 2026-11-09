# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Derives the conditional-mean identity for all four functionals and a second-order remainder consisting of propensity/outcome cross-products and a quadratic outcome-error term. Establishes the uniform bound, exactness at truth, and vanishing when both outcome regressions are correct. A single generic calculation covering all four smooth links is sufficient. An integral Taylor remainder and a justified mean-value remainder are equally acceptable.
- **2 points:** Proves the conditional risk decomposition, identifies the unrestricted population minimizer up to null sets, proves the oracle excess-risk identity, and establishes the stated mixed-derivative orthogonality with justified differentiation or a quadratic difference-quotient argument.
- **1 point:** Verifies the needed uniform boundedness and smoothness for the actual pseudo-outcomes, including any higher link derivatives used, together with squared-loss curvature, Lipschitz control, and mixed-derivative control when using an orthogonal-learning theorem. An alternative proof need only verify the regularity required by its valid statistical argument.
- **3 points:** Obtains the high-probability bound under the explicit localized-complexity condition, with fourth-power L4(l2) nuisance dependence and valid constants. Handles conditioning on each training fold, the independent evaluation-fold ERM, the confidence union bound, and averaging of both prediction errors and fourth-power nuisance errors. Keeps the test-covariate expectation distinct from averaging over training data. If treating the four targets on a joint event, accounts for their finite union as well.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a particular named learning theorem. A valid application of an independent empirical-process or learning theorem must state the relevant result and check its hypotheses against the explicit radius, boundedness, and sample-splitting definitions.

Do not demand vanishing of the remainder when only the propensity is correct. The nonlinear Taylor term generally remains in that case; the source explicitly distinguishes this from exactness when both outcome regressions are correct. The former rubric's phrase 'double-robust vanishing properties' was incorrect.

Do not require m_theta,eta to belong to F at misspecified eta. Do not require the average of the two fits to belong to F, since convexity of F is not assumed. Do not regard the two swapped fits as independent, and do not condition simultaneously on both training folds when asserting evaluation-fold independence.

The standard localized deviation theorem is stated in the reference proof and indexed by theory_003. There is no unresolved private proof obligation. Simply repeating the oracle conclusion as an empirical-process assumption, or citing an unspecified 'standard orthogonal theorem' without resolving its applicable hypotheses, does not establish the final step.
