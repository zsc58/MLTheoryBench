# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derive the score line-integral identity and construct the bounded Poisson product coin, including its expectation exp(-C)r, the empty-product convention, and the C=0 case. The segment bound justifies the integral identity under differentiability by making the restriction of log p to the segment Lipschitz and absolutely continuous.
- **4 points:** Analyze the fresh independent two-coin trials, prove almost-sure termination of the complete correction, and sum the geometric restarts to obtain eventual acceptance H r/(1+H r).
- **2 points:** Use the reciprocal ratio and the Barker identity, or an equivalent argument, to establish detailed balance, invariance, and reversibility of the accept-or-stay kernel.
- **1 point:** Establish full-support irreducibility, justify Harris recurrence or invoke a valid all-state ergodicity result with its hypotheses verified, establish aperiodicity, and conclude total-variation convergence from every initial state.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular hitting-probability argument. Standard independent results may be invoked when their relevant hypotheses are stated and checked.

Deduct for treating the product coin as an unbiased density-ratio coin without the exp(-C) factor, omitting restart normalization or independence, ignoring the zero-bound or empty-product cases, or treating a terminal rejection as a restart. Recognize that each finite-mean Poisson count is finite almost surely.

Do not demand continuous score derivatives, higher-order score regularity, a small-step regime, a symmetric bound C, or any quadrature approximation: none is an assumption of this task. A concise fundamental-theorem argument may be accepted when its justification under the segment bound is clear.

Irreducibility and existence of an invariant probability alone are not a general justification of Harris recurrence from every state. A convergence argument must use the additional structure of this kernel or another applicable theorem that genuinely provides the all-state conclusion. Positive rejection probability can be used to establish aperiodicity. The standard aperiodic positive-Harris convergence theorem is acceptable after those hypotheses have been verified.
