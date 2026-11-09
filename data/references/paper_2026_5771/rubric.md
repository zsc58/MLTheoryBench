# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points: Uniform mixing, adaptive blocks, and confidence.** Derives suffix-uniform canonical endpoint lower bounds for both displayed block lengths from common-stationary spectral contraction; uses the canonical component to obtain conditional block-end visitation rates despite reward-adaptive movement; and justifies confidence intervals under adaptive counts via fixed reward-table prefixes or an equivalent argument. Merely naming mixing or concentration without supplying the needed conditional bounds does not earn full credit. The proof must not rely on an unproved ordering between the two block lengths.
- **2 points: Worst-case identification and stopping.** Applies adapted lower-tail concentration to obtain all gap-dependent sample counts, proves that these counts force the confidence certificate with the optimal arm as leader, excludes any earlier incorrect certificate on the uniform confidence event, and transfers the result from perpetual exploration to the stopped procedure, including the learning-regret bound. Handles zero observations and the horizon endpoint consistently.
- **2 points: Navigation and sublinear expected regret.** Establishes a suffix-uniform geometric hitting-time bound conditional on the actual stopping history. Correctly combines learning, navigation, and failure-event costs to obtain the displayed expected-regret bound and its o(T) consequence. A pseudo-regret decomposition is sufficient; a realized-regret argument must justify all conditioning involving reward noise rather than assuming zero-mean noise persists after conditioning on a confidence event.
- **3 points: Conditional gain and global complexity reduction.** Repeats the adapted count/stopping argument using the stated coefficients and pre-block filtration, without assuming that the gain condition survives conditioning on the entire graph sequence. Proves the factor (1+zeta)^-1 bound by treating arms both inside and outside the near-bottleneck set, and justifies the displayed time estimate including integer rounding under the horizon condition. Improving only exact maximizers, or asserting the gain without controlling every possible bottleneck arm, is insufficient.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the stated assumptions. The canonical-component coupling, reward-table construction, and particular numerical confidence thresholds may be replaced by equivalent rigorous arguments. The same sufficiently large universal constant must work in both stopping claims; no particular numerical value is required. The endpoint concentration argument does not require independent block indicators. At epsilon_0=1 the exploration kernel is canonical and no residual mixture kernel need be defined.

The gain comparison is against the baseline using the same h1 and coefficients vartheta_1 pi_i. It does not claim an identical multiplicative improvement over the h0 bound, or over burn-in and rounding costs. The horizon condition guarantees that at least one gain block is applicable, allowing probability bounds to imply kappa_i<=1 when needed. A failure in an earlier step should affect later credit only when the later conclusion remains unsupported.
