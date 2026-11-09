# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

The following allocation describes the reference route. Award equivalent credit for a valid alternative proof according to its mathematical completeness, not its use of these particular intermediate statements.

1. **2 points:** Formulates the hard-margin primal and its Lagrange dual, and correctly justifies weak/strong duality, dual attainment, the representation of the primal optimizer, and $\sum_i\beta_i=\|f_S\|^2$. Standard convex duality may be invoked with its hypotheses verified; the finite feature span permits a finite-dimensional application. Minimum-norm solutions exist uniquely under the stated assumptions. Empty training samples have optimizer zero and empty dual multipliers.
2. **3 points:** Derives the partition norm-gap sandwich by comparing the full-sample and in-sample dual optima and allowing arbitrary nonnegative multipliers on the held-out set. A direct derivation for singleton held-out sets receives equivalent credit.
3. **3 points:** Specializes to one omitted point, optimizes the auxiliary multiplier using the positive hinge violation, and obtains $a_i\le\beta_i\|u_i\|^2\le\beta_iR^2$. The argument must be valid when the hinge violation is zero. Division by $\|u_i\|^2$ is justified because feasibility excludes zero feature vectors.
4. **2 points:** Sums over all omitted points using one full-sample optimal multiplier vector and applies the multiplier identity to conclude the stated $R^2\|f_S\|^2/n$ leave-one-out bound.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, a general partition lemma, or explicit optimization of an auxiliary multiplier when another valid argument proves the target. For an answer relying on the reference route, an unproved or incorrectly stated norm-gap comparison, or an unjustified passage from that comparison to the singleton violation bound, is a theorem-critical gap. The proof must cover $n=1$; explicit discussion is unnecessary if its definitions and argument already handle the empty training sample correctly. Routine omitted explanations of optimizer existence or elementary boundary conventions are not automatically theorem-critical when the proof otherwise applies correctly.
