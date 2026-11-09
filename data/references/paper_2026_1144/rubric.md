# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the aggregate stale-oracle second-moment bound from the per-agent conditional bound, respecting the stated sampling and delay timing.
- **2 points:** Correctly controls motion and local expected-gradient discrepancies over the scaled delay window, including the factor `p_t=a_{ceil(kappa t)}`.
- **4 points:** Derives a projected smoothness descent recursion by decomposing sampling, stale expected-gradient, and current-time bias errors. The proof must quantitatively control these terms with projection inequalities, Young inequalities, the delay estimates, and the fact that `F` is `mL`-smooth. Merely naming a delayed-SGD argument earns no credit for this step.
- **2 points:** Telescopes the weighted stationarity inequality, uses the ratio condition and monotone stepsizes to obtain the stated average bound, and establishes the polynomial-stepsize specialization.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A solution may use different valid constants. It must justify the stale-sampling, delay, bias, and projection controls rather than assuming them as intermediate results.
