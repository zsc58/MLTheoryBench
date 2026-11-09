# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Moment setup and exact task expansion (2 points).** Uses the local moments computed from the prescribed fresh minibatch at a fixed state, then averages over the specified stationary conditional state law at radius \(R\). Uses that this law is supported on actual radius \(R\), including at the selected equilibrium, and derives the conditional task increment \(2\widetilde D_R+\Sigma_R^2/R^2\). Does not fix the embedding direction merely by conditioning on radius, and does not replace an average of squared local means by a squared radius-conditioned mean.
2. **Decay and equilibrium balance (3 points).** Incorporates the actual post-task contribution \(-2\eta\bar\lambda_{\rm rad}(R)R^2\), including task-decay interaction, and obtains the conditional squared-norm drift. Correctly uses the selected zero-drift radius. Conditional second moments justify the finite expected increments at the selected radius. If invoking stationarity, justifies the outer zero-average identity using global finite moments and does not infer pointwise zero drift from stationarity alone. A direct proof at the selected radius need not separately reproduce the unused outer stationarity identity.
3. **Bi-quadratic solution and uniqueness (3 points).** Derives \(2R_{\rm eq}^4-2D_*R_{\rm eq}^2-V_*^2=0\), obtains the displayed root, and proves uniqueness among nonnegative roots with the evaluated coefficients held fixed. Handles the apparent zero-heat boundary using the moment definitions: zero total second moment forces zero radial mean and is incompatible with a positive zero-drift radius under positive damping. Equivalently, establishes \(V_*^2>0\) at the selected equilibrium before comparing the two roots. Merely observing that the other root is nonpositive is insufficient for unconditional uniqueness. No global uniqueness assertion for radius-dependent coefficients is required or justified.
4. **Regime interpretations (2 points).** Proves the heat limit for bounded \(D_*\) and \(V_*\to\infty\), the outward bound when \(D_*>0\) and \(V_*^2/D_*^2\to0\), and the inward asymptotic when \(D_*<0\) and \(V_*^2/|D_*|^2\to0\). Rationalization or equivalent expansions are acceptable. The outward big-O constant may be numerical and independent of the limiting family.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or restatement of definitions already supplied. Do not award credit for merely naming a stationary-drift or NTK method without the necessary algebra and conditioning arguments.

A radius need not be an atom of the stationary radius distribution. Pointwise evaluation is justified by the public fiber-support and minibatch-integration definitions, not by claiming that every regular conditional-distribution version has fiber support at every label. A concise proof that directly uses these definitions is sufficient; no separate disintegration theorem is required. Off-fiber modifications at the selected radius violate the repaired public evaluation domain.

Concentration of a stationary norm distribution is not an exact substitute for the stipulated zero conditional drift. A proof must not claim such an implication without additional quantitative hypotheses.

The formal coefficient example \(V_*^2=0,D_*>0\) does not satisfy the task's moment definitions and is not a valid counterexample. Nevertheless, a proof relying only on nonpositivity of the second root has omitted a real boundary argument.

An NTK interpretation is optional and earns no separately required points. If included, it must retain the source-norm denominator in the ordinary embedding displacement. The simplified transmitted sum describes the rescaled displacement only under an additional comparable-neighbor-norm approximation, alongside differentiability and an SGD-style first-order update. These interpretive assumptions are not requirements for the exact equilibrium proof.
