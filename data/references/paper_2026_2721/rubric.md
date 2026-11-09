# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Constructs localized links with \(N=\Theta(T^{1/3})\) and perturbation height \(\Theta(1/N)\), verifies their range, \(C^1\) regularity, derivative bound, positive \(\mathbb E f'(X)\), and non-monotonicity of the hard instance. Identifies null and single-spike hypotheses. An alternative valid construction is acceptable.
2. **2 points:** With the task's exact \(K=\lceil4T^{1/3}\log T\rceil\), proves universal availability of the relevant plateaus except with probability \(O(T^{-2/3})\).
3. **2 points:** Derives a Gaussian adaptive-history KL bound of order \(\varepsilon^2\mathbb E_0N_j\) for the null and each spike.
4. **3 points:** Uses null-hypothesis counting and a valid testing inequality to find a spike on which the policy selects outside its positive bin on a constant-probability event for a linear number of rounds; establishes a per-round gap of order \(\varepsilon\) for the actual valid links.
5. **1 point:** Accounts for availability failure and constants to conclude the stated \(T^{2/3}\) expected-regret lower bound for every policy and sufficiently large \(T\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's particular smoothing or positivity perturbation. A construction with zero \(\mathbb E f'(X)\), a merely piecewise-differentiable link without a valid repair, or availability justified only for the appendix's larger arm menu does not meet the public contract. Naming an information-theoretic method without its quantitative testing and regret-conversion argument does not earn those steps.
