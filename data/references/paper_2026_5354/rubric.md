# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points: Affine forcing.** Uses the constant class-sum identity to show that each convex class loss is also concave, and therefore affine on \(\mathbb R^C\).
- **3 points: Coefficient characterization.** Correctly derives the common target coefficient, common off-target coefficient, and common intercept from permutation invariance; then uses symmetry, non-increasingness, and nontriviality to obtain exactly \(a+bU\) with \(b>0\).
- **1 point: Converse direction.** Verifies that every \(a+bU\), \(b>0\), is convex, nontrivial, target-score non-increasing, permutation invariant, and symmetric.
- **3 points: Local characterization.** At an equal-score vector, correctly differentiates permutation invariance and the class-sum identity, proves that the first-order approximation is invariant and symmetric, verifies its monotonicity and nontriviality, and applies or reproduces the affine characterization to conclude \(A=a+bU\) with \(b>0\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Merely asserting that symmetry implies affinity or that the linearization has the required invariances does not earn full credit without the corresponding argument. If the global characterization is established and then validly invoked for the local approximation, award the local step according to whether its hypotheses were actually verified.
