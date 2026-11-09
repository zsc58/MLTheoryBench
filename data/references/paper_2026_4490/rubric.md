# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly models the reset process and derives \(\mathbb E[T_\tau]=G(\tau)/F(\tau)\) using the block survival probabilities and the tail-sum identity.
- **3 points:** Correctly expands \(\mathbb E[T_{\tau+1}]-\mathbb E[T_\tau]\) and reduces its numerator to the weighted covariance expression involving \(p\) and \(h_\tau=(1-p)^\tau/u_\tau(p)\).
- **3 points:** Proves that \(h_\tau\) is nonincreasing and applies a valid covariance/association argument to establish the numerator is nonnegative. Merely naming covariance or a restart method without deriving the reduction earns no credit for this step.
- **2 points:** Concludes that the mean is nondecreasing in integer \(\tau\), hence resetting after every attempt (\(\tau=1\)) is the optimal deterministic interval for every admissible difficulty distribution.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat failure to justify the weighted monotonicity or covariance sign as a theorem-critical gap.
