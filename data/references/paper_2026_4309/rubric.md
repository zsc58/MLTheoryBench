# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Duality and empirical-process reduction (2 points).** Correctly applies one-dimensional W1 duality with finite first moments and normalized one-Lipschitz functions, handles the orthonormal-basis maximum, and reduces to the projected Lipschitz supremum with factor d/sqrt(n). Keeps random suprema distinct from their expectations and supplies or justifies the relevant measurability.
2. **Truncation and tail remainder (2 points).** Defines a valid clipping or other truncation and controls both empirical and population errors. Derives a polynomial remainder of order M^{1-beta}. For exponential tails, a valid route is the exact clipping remainder E[(|X|-M)_+]=integral_M^infinity psi_mu(t)dt, bounded by C0 exp(-delta M)/delta. Alternatively, retain the factor M+1/delta in E[|X|1{|X|>M}] and account for it in the optimization. Do not accept removal of that factor by changing only a multiplicative constant while retaining the same delta.
3. **Product entropy control (3 points).** Verifies the parameter metric and envelope bound, square integrability with constants controlled solely by the stated tail parameters, and a valid entropy estimate for every d>=1. Uses ambient L2 bracket endpoints, correct product-cover radii, and an applicable empirical-process inequality. Evaluates the entropy integral to support a stochastic term of order d^{3/2}sqrt(M/n), or a sufficient sharper bound. Merely naming an entropy method is insufficient. A sphere bound proportional to d-1 must separately handle d=1. A valid explicitly stated standard maximal inequality may be cited without reproving it if its hypotheses are checked.
4. **Optimization and finite-sample conclusions (3 points).** Balances the polynomial terms to obtain exponent (beta-1)/(2beta-1), chooses a positive logarithmic truncation to obtain ell(n)/sqrt(n) in the exponential regime, and derives both sample-size consequences. Addresses all positive integer n and every epsilon>0, with constants independent of d,n,epsilon. For exponential sample-size inversion, provides a uniform argument rather than merely substituting or asserting that constants can fix a zero logarithm. The reference proof uses a crude large-tolerance bound and explicit inversion on the remaining range; any valid alternative is acceptable.

# Evaluator Notes

Accept a complete valid alternative proof, including one proving stronger bounds that imply the targets. Do not require the reference proof's incidental presentation choices. Treat omission of either tail regime or either sample-complexity consequence as a theorem-critical gap; propagate a failed entropy or truncation step only when the corresponding rate is unsupported. The task uses ell(t)=1+max{0,log t}; equivalent positive logarithmic conventions are acceptable when their comparison with the stated bounds is justified. Missing routine measurability details or an easily repaired numerical covering factor need not invalidate an otherwise complete argument, but unverified constant dependence or an unsupported sample-size implication is substantive. The reference proof has no unresolved obligations.
