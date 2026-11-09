# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Radial log-sum-exp validity (3 points).** Establishes convexity and positive homogeneity, hence sublinearity, and verifies smoothness away from zero for \(\beta>0\) and positive integer \(m\). A conjugacy proof must justify the needed domain conclusion; a direct LSE variational proof is acceptable.
2. **Convex-body representations (2 points).** Correctly establishes the gauge sublevel representation and differentiable support-gradient representation, including why the displayed gradient image is the entire convex body and has the claimed support function.
3. **Support-family density (3 points).** Uses applicable polytope approximation and the support-function/Hausdorff identity for nonempty compact convex sets, realizes a finite maximum support function, bounds the log-sum-exp error uniformly on the sphere, ensures positivity, and transfers the bound to Hausdorff distance.
4. **Gauge-family density (2 points).** Constructs or justifies an inner polytope containing zero in its interior, represents its gauge as a finite maximum of linear forms, preserves a positive lower bound, controls reciprocal radial functions, and justifies the radial-function Hausdorff bound before concluding by triangle inequalities.

# Evaluator Notes

Accept complete valid alternative proofs and standard convex-geometric results when their relevant statements and hypotheses are made clear. Do not require the reference proof's incidental presentation choices. Count a claimed approximation theorem without the uniform LSE estimate or reciprocal/radial error argument as incomplete. A support-case proof must ensure positivity before using the support-gradient representation.
