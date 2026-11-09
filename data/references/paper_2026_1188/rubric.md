# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Constructs the odd-stage predecessor strategies, computes their reward-one sets and charge payoffs as 1 - 2^{-n}, and concludes that the value is v_mu = 1 using the upper bound by one.
- **2 points:** From a hypothetical payoff of one, correctly defines the threshold set W and proves that both mu_0(W) and mu_*(W) equal one.
- **4 points:** Establishes the paired-stage identity q_k + q_{k+1} = 1, derives (W intersect E_n) minus 1 subset E_0 minus W for n >= 1, and completes both contradiction cases: some mu_n(W)>0 via translation invariance, or all mu_n(W)=0 via accumulation-point convergence.
- **1 point:** Combines v_mu = 1 with strict inequality for every strategy to conclude that no pure or randomized strategy is optimal.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

Compactness and translation invariance are supplied background facts. Do not require solvers to reproduce the private background derivations of these facts or of the existence of a frequency charge. The proof should correctly use the tail accumulation property to obtain mu_*(E_n)=1 and should justify, explicitly or by an immediate observation, the component support properties used in its payoff calculation.

The paired-stage identity holds pathwise and hence in expectation for every history-dependent behavioral strategy. Do not restrict the strategy domain to stationary or independent stage-by-stage randomization.

Use the bounded-function charge integral in the stated order: aggregate expected rewards. Neither countable additivity nor an interchange of expectation and charge integration is available or needed.
