# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Affine best response.** Correctly derives the clipped shifted response `y_g(x)=clip(x+bs/(2c),0,1)` for an affine gate `g(y)=a+s y`, including the constant-gate case.
- **2 points: Strict affine exclusion.** Uses the sign of `L`, the positive mass on both sides of `tau`, and the affine response to prove that every affine gate has value strictly below `W_FB`. Merely asserting that affine gates cannot represent a step earns no credit for this step unless the induced strategic responses and strict welfare loss are justified.
- **4 points: Threshold implementation.** Sets `t=tau+sqrt(b/c)`, verifies admissibility, and compares the best unapproved and approved reports for all type regions. The proof must handle types below `tau`, pooling types between `tau` and `t`, types at or above `t`, and the indifferent boundary type. It must establish almost-sure approval exactly above the value cutoff and the associated report inflation.
- **2 points: Global optimality and consequences.** Establishes the pointwise bound `g(y_g(x))L(x)<=max{L(x),0}`, shows that the threshold attains it, and correctly concludes existence of an optimum and non-affinity of every optimum.

# Evaluator Notes

Accept any complete alternative proof under the stated assumptions. The null boundary type may be assigned either best response. A missing or incorrect threshold incentive comparison is theorem-critical. If the threshold is independently proved optimal, later conclusions may still receive credit even when an earlier affine-response derivation is flawed.
