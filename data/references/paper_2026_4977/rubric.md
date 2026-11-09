# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly establishes row-normalized exact-polar and NS5 alignment and Frobenius norm control, including zero and rank-deficient inputs. For the perturbation argument, justifies NS5's common singular-vector representation rather than inferring alignment from norm closeness alone. Accepts either the requested $(1-\varepsilon)$ and $(1+\varepsilon)$ bounds or stronger bounds that imply the final guarantee.
2. **4 points:** Correctly controls decoupled weight decay and derives smoothness descent with tracking error. Establishes an appropriate $O(t^{1/4})$ iterate envelope, a uniform bound on $\lambda_t\|X_t\|_F$, a bounded update direction, and a positive descent coefficient. Obtains constants sufficient for the displayed conclusion. Does not assume that $\sum t^{-3/4}$ converges, that the iterates have the false constant envelope from the superseded GT, or that $\lambda_t\|X_t\|_F\le\rho t^{-1/4}$ follows from the stated schedule.
3. **2 points:** Proves a valid momentum-tracking recursion for gradients sampled at $X_{t+1}$ with fresh noise. Handles the conditional zero-mean cross term correctly, retains expectation on random drift/update terms in unconditional inequalities, and establishes initialization and the accumulated tracking-error estimate by a justified scalar telescoping argument.
4. **2 points:** Completes the objective telescoping and schedule sums, converts the weighted gradient sum to the unweighted average using $\eta_t\ge T^{-3/4}$ or an equally valid argument, and obtains the displayed constants, positive denominator, logarithmic factor, and $T^{-1/4}$ dependence for both methods. Handles the trajectory-dependent error choice without moving random coefficients outside expectations or conditioning on that error while retaining the unconditional oracle assumptions.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its stronger intermediate bounds, or a separate proof of an approximation-error assumption already supplied in the task.

The trajectory-defined error is generally random. Proving only the deterministic-error special case does not finish the full task. A solution may handle the random-error case by the reference proof's deterministic NS5 bounds and pointwise comparison of constants, or by another valid argument under exactly the stated sampling experiment.

Do not accept an added deterministic uniform spectral-gap assumption, a full-rank assumption, an anticipative choice of the fixed inputs, or an altered sampling point as a repair. A finite maximum of errors below one does not itself yield a deterministic bound strictly below one over every sample path. A lower bound on $\sum_t\eta_t$ alone does not establish a bound on the unweighted average.

The unconditional tracking lemma must average its random squared update norm, or replace it by a proved deterministic bound before taking expectations. The elementary scalar recursion and the specified polynomial estimates can be derived directly; an unsupported citation to a specialized result is not a completed proof step.
