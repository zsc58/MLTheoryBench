# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Expands the unilateral cost and potential differences using independence and proves the discrepancy bound alpha=(M_b^v+3(M_b^m)^2)C_Q. The argument must apply to all admissible bounded-moment distributed deviations, including nonlinear ones.
2. **2 points:** Establishes the exact affine gain/mean decomposition, gain optimality and normalized gradient dominance, and the 2-strong convexity and finite smoothness constant of the mean functional. Verifies that the affine potential minimizer is globally optimal over all distributed admissible policies, not merely over affine parameters. A direct centered-control completion of squares is sufficient; a specialized verification theorem may not be invoked without its relevant hypotheses being justified.
3. **3 points:** Derives the individual and potential gradients and controls their bias. Establishes the uniform gain and positive variance bounds needed for these estimates, rather than assuming an unproved invariant. Obtains a per-player normalized gain bias O(C_Q) and a full-vector intercept bias O(sqrt(N)C_Q), with explicit finite constants or equivalent estimates. Uses the correct evaluation-ODE signs and accounts for the diagonal and off-diagonal parts of the mean bias.
4. **2 points:** Derives biased gain descent and projected mean contraction under a positive sufficiently-small step threshold and the stated step-ratio condition. Obtains geometric transient terms and nonnegative residuals delta_1,delta_2 bounded by constants times N C_Q^2. The mean distance bound must be converted to an objective bound with its cross term controlled. Uses the actual moment-size assumptions to establish iterate membership in V_b.
5. **1 point:** Combines the component accuracies with total error epsilon and transfers the potential gap through the alpha-potential inequality. Establishes one threshold valid for all later iterates, every player, and every bounded-moment unilateral deviation. Gives logarithmic small-accuracy iteration complexity and vanishing residual at C_Q=0.

# Evaluator Notes

Accept any complete valid alternative proof and do not require the reference proof's particular constants or presentation. The learning algorithm uses exact gradients, not sampled estimators. Gains have strictly positive state variances because the initial variances are strictly positive; no zero-variance extension is part of the task.

Do not award full credit for merely naming gradient dominance, a biased-descent lemma, uniform gain regularization, or a specialized control-verification theorem without closing the required hypotheses and calculations. The full-vector mean bias is important: applying a bound containing sqrt(N) separately to each coordinate can lose an additional factor of N.

The matrices Q^i are symmetric. Accordingly Q^j_ij and Q^j_ji are equal, and either notation is acceptable. The actual source comparison-ODE sign errors must not be reproduced. Potential mean calculations use Q_sym, even when Q is nonsymmetric.

The deviation class is not restricted to affine policies. Proving optimality only within the learning parameterization does not justify the final Nash transfer. Conversely, the global potential minimizer need not lie in V_b; global minimality over V is enough.

The total residual includes the linear term alpha. Do not require or accept an unsupported assertion that the entire residual is O(N C_Q^2) as C_Q decreases to zero. Zero initial gaps, C_Q=0, and large epsilon should be handled without logarithms of zero or negative iteration counts. A routine omission of a max-with-zero or an epsilon/2 allocation is minor if the substantive proof is otherwise complete.
