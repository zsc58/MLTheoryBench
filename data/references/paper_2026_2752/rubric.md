# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **1 point:** Correctly sets up the binary support class, the residual-loss comparison, and the relation \(|S\triangle S^\star|=2m\).
- **4 points:** Derives a valid heterogeneous two-block Chernoff/MGF bound using centered noise independent of the design. For the reference route, this includes conditional Gaussian integration, an admissible choice \(\vartheta=1/(4\tau_2^2)\), and the corrected \(2\tau_2^4\) denominator in the high-quality factor.
- **3 points:** Applies a valid union bound over competing supports, obtains the exponential failure estimate in terms of the logarithmic tradeoff \(A\), and explains why its complement guarantees the required error bound for every minimizer.
- **2 points:** Controls the combinatorial term in both sparsity regimes using valid entropy bounds or Stirling estimates, obtains the stated exponential rate, and verifies that the failure probability tends to zero.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The heterogeneous probability calculation and its dependence on both noise blocks are theorem-critical; merely naming a concentration or union-bound argument is insufficient.

An upper bound on \(\log\binom ps\) is sufficient; an asymptotic equality or explicit use of Stirling's formula is not required. In the sublinear regime, \(\log\binom ps\le s\log(p/s)+s\) yields the required \(\varepsilon+o(1)\) coefficient. In the linear regime, the entropy bound \(\log\binom ps\le h(\alpha)p\) already suffices.

The signal and noise variances are deterministic parameters, and the variances may depend on dimension. The probability is over the design and noise for each fixed true signal; a simultaneous recovery event over every signal is not required. Empty blocks contribute a product factor of one, and an empty collection of bad supports presents no difficulty. Do not demand separate discussions of these cases when the submitted argument already covers them.
