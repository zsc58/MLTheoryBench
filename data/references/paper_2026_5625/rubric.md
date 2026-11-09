# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly formulate the exact Jensen-gap decomposition with the population-minus-empirical sign, establish or correctly justify the simultaneous Gibbs PAC-Bayes inequality for a fixed sample-independent prior, and derive the centered-loss exponential-moment bound with exponent \(\lambda^2\ell^2a_v^2/(2n)\). In the reference route, the PAC-Bayes event follows from Markov's inequality and the entropy/change-of-measure inequality, rather than an unexplained invocation of a nonstandard dependency.
- **4 points:** Establish the characteristic quadratic pseudometric domination for the Jensen-gap class. The loss-gradient difference must be controlled using the exact Gaussian-path quantity \(A_{i,\sigma}\) and the unperturbed Jacobian matrix \(G_i\); the Jacobian-difference contribution must use the integrated Hessian matrix \(B_{i,\sigma}\). Obtain \(M_{S,\sigma}=2\sigma^2\sum_i(\beta^2A_{i,\sigma}G_i+\ell^2B_{i,\sigma})\), or an equally strong justified estimate. Verify a valid process-comparison hypothesis, compute the Gaussian width over the radius-\(R\) ball, and use \(\operatorname{tr}M_{S,\sigma}=2\sigma^2n(\beta^2J_{S,\sigma}+\ell^2H_{S,\sigma})\) to get the stated empirical-complexity dependence.
- **2 points:** Use the fixed Jensen-gap class and its envelope \([-\sigma^2B,\sigma^2B]\) to establish a simultaneous population-minus-empirical bound with twice the empirical Rademacher complexity and concentration no larger than \(8\sigma^2B\sqrt{2\log(8/\delta)/n}\) at failure probability \(\delta/2\). A correctly stated standard bounded-class theorem with verified normalization, measurability, envelope, and confidence hypotheses is acceptable; so is a direct symmetrization and bounded-differences derivation.
- **2 points:** Combine the two events and substitutions to prove the final deterministic bound simultaneously over \(\Theta\), retaining the KL term, the prior exponential moment, and the stated confidence factors. Treat the constant as an existential universal positive constant. Justify risk interchanges in the nonvacuous case and correctly handle infinite KL or infinite prior moment, without adding a new substantive moment assumption. The argument must remain valid for the allowed zero and singular cases.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. The metric/comparison application must be justified, not merely attributed to a named method. A solver may invoke a precisely stated standard-independent process comparison theorem without reproving that general theorem, provided its centering, increment, separability, and finiteness hypotheses are checked. Equivalent Rademacher-to-Gaussian comparison arguments are also acceptable.

Use the empirical Rademacher normalization \(n^{-1}\mathbb E_\varepsilon\sup_w\sum_i\varepsilon_iF_i(w)\), without an absolute value inside the supremum, unless a different convention is explicitly reconciled. No numerical value of the universal constant \(c\) is required. A stronger valid concentration constant earns full credit.

Finite prior exponential moment and finite KL imply the posterior output-bound integrability needed in the reference proof through the entropy inequality. Infinite penalties make the corresponding final inequality vacuous; they do not justify subtracting infinite Gibbs risks. When \(\ell=0\), the common value \(L(0,y)\) makes the loss constant. No inversion of the metric matrix or division by \(R\), \(\beta\), or its eigenvalues is required.

Do not accept a data-dependent prior or data-dependent selection of \(\lambda\), \(\sigma\), or \(R\) as covered by the stated single event without additional justification. Sample-dependent matrices are permitted. Do not replace Gaussian-path controls by controls only on \(\Theta\), or silently truncate the Gaussian perturbation.

The public task intentionally does not provide the auxiliary pseudometric, its dominating matrix, or the Jensen-gap decomposition. These are private proof steps. All reference-proof obligations have been closed; no unresolved dependency is to be scored as if it were established.
