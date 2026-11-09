# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes a common finite bound for the original trajectory and every warped trajectory, independent of the warp factor. A finite-horizon closed form, a direct convexity induction, or another valid bound is acceptable; the bound must account for the initial value as well as the inputs.
- **3 points:** Gives an explicit one-unit linear-activation LSTM parameter choice whose constant gates are a and 1-a, whose candidate equals the input, and proves that its cell state equals z_t with the prescribed initialization. The construction must work with the given fixed h_0.
- **2 points:** Chooses a finite output-gate bias and proves the uniform error is strictly below epsilon. All sigmoid/logit arguments must lie in their domains, and the argument must cover zero-valued data and every positive tolerance without imposing an extra assumption.
- **3 points:** Changes only the forget- and input-gate biases to the prescribed values encoding a^gamma and 1-a^gamma, proves that the modified cell state equals the warped trajectory, and transfers the same strict tolerance using a base parameter setting independent of gamma.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular bound, or a closed-form calculation when an equivalent direct argument suffices.

Treat failure to establish the stated finite-horizon conclusion, failure to justify a needed common bound, or changing parameters or initial states other than the two permitted biases as theorem-critical gaps. A proof that chooses a new output-gate bias separately for each gamma proves a different quantifier order and does not establish the stated single-base-setting claim. Do not penalize a solver merely for omitting a redundant restatement of a quantifier that the argument actually respects.

No approximation claim at time zero is required. In particular, the initial hidden state need not approximate z_0. All-zero inputs and initial cell value must be covered, but a separate case split is unnecessary when the displayed inequalities already cover them. An isolated strict-versus-nonstrict inequality slip at a zero bound, with an otherwise correct construction and an immediately repairable estimate, is a minor error rather than evidence that the theorem is false.
