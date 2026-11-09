# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Establishes the necessary projected-operator geometry and regularizer properties. This includes justifying the dual support function, convexity and differentiation, feasibility, dominance, regularizer-increment control, and weighted Bregman smoothness. The regularizer for round k uses the updated matrix T_{k+1}. Routine equivalent derivations are acceptable; no unexplained paper-specific theorem may substitute for these obligations.
2. **2 points:** Derives the exact shifted-regret decomposition with the initial regularizer, terminal dual term, regularizer increments, and negative Bregman divergences, using consistent signs and horizon indexing.
3. **3 points:** Proves the preconditioner-gradient stability inequality and combines it with a justified lower bound on Bregman divergence in terms of gradient differences. Controls the change of regularizer in the correct weighted metric and obtains the shifted-regret bound with the negative squared iterate-difference sum. Handles the initial term, where the gradient at zero vanishes.
4. **2 points:** Converts shifted regret to ordinary regret by weighted Young's inequality, cancels the iterate-difference sum, and proves the trace-square-root telescoping estimate using the updated matrix T_{k+1}. Bounds Phi_0(0)=R tr sqrt(T_1) by R epsilon d+R q_*(h_0). A valid concavity argument or a valid noncommutative factorization is acceptable.
5. **1 point:** Concludes the requested bound with a genuinely universal constant, without a uniform gradient assumption, and explains the arbitrarily small positive initialization choice. Includes the single-round and zero-gradient cases, either explicitly or through formulas that cover them.

# Evaluator Notes

Accept a complete valid alternative proof and allocate credit according to the mathematical obligations it resolves. Do not require the reference proof's incidental presentation, exact constant, or specific intermediate inequalities if another route proves the target.

For a proof following the reference route, merely asserting gradient stability, convexity, the Bregman lower bound, or final telescoping does not close those obligations. In particular, omission of the stability-plus-negative-Bregman absorption is a theorem-critical gap in that route, but its absence is not a defect in an otherwise complete alternative proof.

Do not identify the pre-update T_k with the post-update T_{k+1}. The identity needed for the final telescoping is h_k^T T_{k+1}^{-1/2} h_k=tr[T_{k+1}^{-1/2}(T_{k+1}-T_k)]. Applying the same estimate with T_k^{-1/2} is not justified by the reference argument. Do not assume successive matrices commute. Do not require epsilon=0, since all inverse-square-root operations are justified by epsilon>0.
