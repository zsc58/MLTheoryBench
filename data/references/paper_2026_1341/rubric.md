# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **3 points:** Correctly represent every covariance in the unnormalized convex hull as a convex combination and derive the linear decompositions for explained variance and reconstruction loss; use source inclusion to prove the infimum/supremum equalities.
2. **3 points:** Establish the regret equality, including the nontrivial inequality comparing the optimum over one common subspace with the convex combination of the separate source optima, and then use source inclusion for the reverse inequality.
3. **2 points:** Transfer the three source-domain optimizer definitions (variance, reconstruction, regret) to minimax optimality over the unnormalized uncertainty class using the established equalities.
4. **2 points:** Repeat the argument rigorously for trace-normalized covariances and normalized variance, reconstruction, and regret, including the normalized uncertainty class and its optimizer conclusions.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A response that merely names convexity, linearity, or a robustness method without deriving the extremal and regret inequalities should not receive credit for those steps. Minor notation changes are harmless when all six objective cases and both uncertainty classes are covered.
