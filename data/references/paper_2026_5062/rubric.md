# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Confidence and determinant control (2 points).** Establish correctly allocated estimator confidence, conditional posterior-sample confidence, and the effective-dimension determinant bound for the rank-one design updates, including the squared-norm determinant identity. Derive the specialized prediction-confidence and effective-dimension results rather than merely citing them. Verify the confidence-radius comparison actually used for optimism.
2. **Thompson anti-concentration and saturation (3 points).** Prove the constant optimism probability p on a sufficient, verified confidence event; show optimism plus posterior confidence excludes saturated arms; and derive the unsaturated-selection probability. Respect the Gaussian tail domain, nondegenerate standardization, and the correct posterior-failure event. Naming these methods without the inequalities earns no credit.
3. **One-step regret and super-martingale (2 points).** Derive the conditional expected-regret inequality with the 11g/p coefficient and additive 1/T^2, including the permitted regret bound 2 on posterior failure. Define an adapted confidence-truncated process, prove its conditional-mean property, and apply a valid bounded-increment or conditional-range concentration inequality. Do not assume an unstated lower bound on g/p.
4. **Norm summation and final assembly (3 points).** Use Cauchy-Schwarz, the positive-lambda norm-log inequality on its applicable norm domain, determinant telescoping through the final update, and effective dimension to obtain the cumulative norm bound. Combine concentration with a justified probability allocation to recover the exact high-probability regret expression and leading scaling. Cover small horizons, arbitrary positive regularization, and degenerate parameters by valid arguments.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require incidental presentation choices or the reference proof's particular case split. A correct alternative may establish confidence and optimism differently or close parameter cases directly.

The reference proof handles C=0, T<=4, and lambda>=T deterministically. For T>=5 and lambda<T, it uses a time-uniform confidence event with failure delta/2 and radius beta=R sqrt(2d log(1+T/lambda)+2 log(2/delta))+C. This radius is at most both l and v. The corrected posterior Gaussian bound gives conditional failure at most 1/(2T^2), so the factor-two failure charge is at most 1/T^2. Conditional-range Azuma-Hoeffding avoids the source's unjustified absolute-increment estimate.

Do not accept the unrestricted assertion l/v<=1, the source's incorrect two-sided Gaussian upper coefficient, division by a nonpositive p-1/T^2, charging regret by 1 under only |b_i^T mu|<=1, an unverified replacement of 2 by 2g/p, or telescoping all T updates to B_T. These may be readily repairable in an otherwise complete answer, but they are not correct proof steps as written.

The Thompson anti-concentration/saturation mechanism and effective-dimension summation must be derived, not merely cited. Standard self-normalized concentration, valid Gaussian tails, Azuma-Hoeffding including its conditional-range form, Cauchy-Schwarz, Hadamard's determinant inequality, and the rank-one determinant identity may be used when their relevant statements and hypotheses are verified. No private proof obligation is left unresolved.
