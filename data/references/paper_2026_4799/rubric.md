# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the optimal branch values as the complementary binomial probabilities under the actual controlled Markov experiment, and derives the normalized-regret lower bound controlling reference wrong-branch mass on margin-gamma thresholds. Accounts for possibly unsuccessful continuation by the evaluated policy. A complete justification may use independent row-outcome sequences and almost-sure completion under an exploring policy, or another valid argument.
- **4 points:** Carries out the threshold-count/binomial-median argument, including a consistent tie convention, the Cantelli small-margin bound with the specified t_gamma, deterministic endpoint cases, median error, clipping, the half-unit estimator shift, and averaging over n+1 thresholds. Obtains the requested rate with an O_gamma(1/n) remainder uniform in the other quantities. Accept equivalent valid bounds and alternative proofs.
- **2 points:** Transfers the transition estimate to the approximate interventional kernel with the additive epsilon_cMP term, retaining the stated averaging and variance term, and obtains the simplified bound.
- **2 points:** Gives two explicit structural models with identical complete interventional kernels and distinct joint cross-action counterfactual laws. The example must be a well-defined controlled Markov model consistent with the stated environment class; a local coupling example may be completed with identical additional transition rows.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its explicit remainder constant, or its particular structural example.

The evaluated policy is not assumed to complete all attempts almost surely. Conditioning on adaptive completion does not generally preserve the iid outcome law. The required relation is an upper bound on actual value by the mixture of optimal branch values, hence a lower bound on actual regret; an equality requires additional justification and must not be demanded by the evaluator.

An arbitrary optimal policy can choose either marker at a tied threshold. Reference decisions may break ties toward L, provided the proof accounts for this convention and does not infer an unforced policy choice from zero regret.

The specialized branch-optimum citation alone does not close that obligation. Standard Cantelli inequalities and the standard binomial-median bound may be invoked with their applicable hypotheses. Treat omission of the branch-value justification, the median/concentration conversion, or the explicit counterfactual separation as theorem-critical gaps. Minor endpoint or normalization omissions are readily repairable only when the surrounding argument clearly supplies their correction.
