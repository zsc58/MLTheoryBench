# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the i.i.d. binary sampling/regeneration model, prefix scores, and weighted vote totals, and applies the strong law to obtain the required almost-sure population limits. Verifies boundedness or integrability of the relevant summands.
- **3 points:** Correctly calculates the population comparison. The reference route derives the probabilities of scores 0, 1/2, and 1 and the decomposition into pooled initial-plus-regenerated mass and self-reproduction. A valid direct calculation of the vote difference or reproduced-answer counts earns equivalent credit without deriving the general decomposition.
- **3 points:** Establishes that the binary correct-versus-wrong comparison has the sign of D=pi(a*)r_C-(1-pi(a*))r_W, using w(1)>0, and derives the threshold pi(a*)>r_W/(r_C+r_W) with the nondegenerate denominator condition. The reference route obtains the exact margin w(1)D; an equivalent strict-comparison calculation is sufficient. Does not impose an unnecessary sign restriction on w(1)-2w(1/2).
- **2 points:** Uses the strict comparison to prove eventual almost-sure correct selection and correctly compares with standard majority voting. Handles p<1/2 and p=1/2 separately or by another valid argument, and identifies the interval r_W/(r_C+r_W)<p<=1/2 and its nonemptiness exactly when r_C>r_W.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, the general population decomposition, a separately named population objective, or an explicitly displayed exact-margin identity when an equivalent calculation establishes the required threshold and convergence. Reallocate the corresponding core-step credit to mathematically equivalent work in an alternative proof.

Failure to establish the strict population or empirical comparison leading to the stated threshold is a theorem-critical gap. Naming a law of large numbers or a voting method without verifying the necessary calculation earns no credit for that missing calculation.

The strong law gives tied limiting initial frequencies at p=1/2 and does not by itself prove the absence of an almost-sure standard-MV correct-selection guarantee. A short valid endpoint argument is required for full credit. For example, a solver may use symmetry to show that standard MV has correct-selection probability 1/2 for every odd sample size, which is incompatible with almost-sure convergence to the correct answer. No specialized random-walk theorem is required.

Tie-breaking cannot affect eventual selection under a strict limiting margin. At the standard-MV endpoint, odd sample sizes have no ties. Do not require a particular tie-breaking convention or an unsupported PC-WMV convergence converse at equality with its threshold.

Rows of T on zero-probability initial states are arbitrary probability distributions as specified in the task. Do not require 0<p<1 or interpret the null-state convention as additional observations or information available to the estimator. Explicitly listing every elementary boundary case is not required when the proof already covers them.
