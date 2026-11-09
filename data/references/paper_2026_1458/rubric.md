# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly expands the difference between targeted information gain and the Monte Carlo objective into the numerator nuisance-marginalization gap plus the denominator contrastive gap, with justified expectations. It suffices to control the negative parts and use integrability of their sum; separate integrability of individual log likelihoods must not be assumed without justification.
- **3 points:** Uses the fresh conditional nuisance sampling to prove that the normalized nuisance likelihood average has conditional mean one given the target component and realized history, then applies conditional Jensen to establish nonnegativity of the numerator gap.
- **3 points:** Correctly establishes nonnegativity of the denominator gap. For the symmetry/KL route, defines the product prior and the tilted law, verifies that the average likelihood ratio normalizes the tilted law, and derives the change of measure by averaging over the possible generating coordinates. A complete alternative, such as an equivalent normalized-mixture convexity argument, receives equal credit.
- **2 points:** Uses the bounded likelihood-ratio hypotheses, conditional strong-law convergence of both Monte Carlo averages, and bounded or dominated convergence to prove recovery of targeted information gain whenever both sample counts diverge. Accounts for the vanishing weight of the generating parameter in the denominator rather than treating all denominator samples as conditionally iid.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's notation or presentation. A proof that merely names Jensen, concentration, or a specialized contrastive result without verifying the needed conditional expectation, change-of-measure argument, or convergence conditions does not close that step. A KL representation is not mandatory if another complete argument establishes the denominator inequality. Do not impose a rate, a relation between L and M, uniformity over policies, or assumptions about independence of target and nuisance parameters. Minor omissions in routine integrability details should be distinguished from assuming an unjustified marginal entropy condition or omitting the main denominator argument.
