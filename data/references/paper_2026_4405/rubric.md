# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Affinely represent each latent Gaussian using a standard normal, center the individual errors, and give the transformed latent coefficients and bias terms. Handle zero variances without an invalid division.
- **3 points:** Verify that the transformed equations satisfy the standardized-exogenous model definition and preserve the complete specified graph, including its latent-parent lists. Check independence both within and between the exogenous families and the required error covariance structure. A zero coefficient is allowed within the fixed graphical specification.
- **2 points:** Prove equality of the observational distributions, for example by coupling and topological induction or an equivalent distributional structural-recursion argument.
- **2 points:** Prove the intervention conclusion for all cases allowed by the task, with a single constructed model independent of the chosen query. Identifiability can be invoked when the common observational law is positive. For singular laws, justify the conclusion separately, for example by applying the same coupling and recursion after replacing the intervention equations. A direct intervention-recursion argument covering all laws earns full credit without a separate invocation of identifiability.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A derivation of normalization and distribution matching is required; merely naming Gaussian standardization or identifiability is insufficient.

Do not require the solver to prove that arbitrary models with the same singular observational law agree on identifiable intervention queries. The identification definition compares positive observational laws, and the task concerns the particular standardized model whose existence is established. Applying identifiability to a singular law without another argument leaves a gap. A concise assertion that the same verified recursion continues after intervention is sufficient when its justification is clear.

Do not impose positive latent variances, positive error variances, unit error variances, nonzero edge coefficients, or causal minimality. Empty sums and empty variable sets may be handled by the stated conventions rather than separate lengthy cases. Equality of queries means equality of probability measures, not equality of Gaussian point masses.
