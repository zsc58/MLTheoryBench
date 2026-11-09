# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly express the intrinsic profile using the cumulative clock and generalized inverse, and derive `q=gamma/(gamma+1)` by integrating both sides of the terminal tail estimate. The argument must allow zeros or flat portions before the tail and use a valid terminal interval.
- **3 points:** Obtain two-sided forgetting-convolution estimates in all three regimes, including the logarithmic equality case and `alpha=min{beta,gamma+1}`. A valid early/terminal split uses a cutoff where the intrinsic tail holds. An upper bound on the early part and a matching terminal lower bound suffice. The polynomial-growth case is `q-p>-1`, and the bounded-integral case is `q-p<-1`.
- **2 points:** Combine the assumed signal and noise terms into the stated full loss scaling, accounting for the fixed mass `m` and uniformity in the admissible peak rate for large intrinsic horizon.
- **3 points:** Prove matching optimal-order lower and upper bounds under the fixed stability cap. Cover `s<1-1/alpha`, `s>=1-1/alpha`, the equality `s=1-1/alpha`, and both logarithmic and nonlogarithmic cases. Obtain the displayed peak and risk orders and verify the proposed rates are admissible and have diverging intrinsic horizons.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The FSL is a primitive assumption; solvers need not derive an external SDE or SGD theorem.

A solution that merely names an intrinsic-time change of variables, kernel asymptotics, or balancing argument without carrying out the exponent comparisons should not receive credit for those steps. Propagate a missing intrinsic-tail derivation to the convolution step when the latter depends on it; independently correct later optimization may still receive its own credit.

Do not require a positive early contribution: the terminal region supplies the needed lower bounds. Do not accept application of the terminal comparison on an arbitrary half-horizon interval without justification.

The correct peak-rate balances have right side `N^(r-s)`, where `r=1-1/alpha`. An isolated sign transcription error with otherwise correct reasoning may be minor, but an incorrect optimization argument is not a completed step.

An optimal-order claim requires both achievability and a lower bound for competing admissible sequences. A concise monotonicity or two-region argument is sufficient. Replacing `log T_N` by `log N` at all admissible rates is unjustified; establishing that comparison at the proposed optimal scale is sufficient when accompanied by a valid lower bound elsewhere.

The public task concerns optimal orders, not existence or uniqueness of an exact minimizer of an arbitrary loss comparable to the FSL. Do not require the exact equality `eta_0^*=eta_max`. At the nonlogarithmic boundary `s=1-1/alpha`, allow a constant-order choice capped by the stability bound.
