# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: General one-step control.** Correctly derives a one-step terminal-lengthscale MMD inequality for the actual pushforward update, or the corresponding inequality for an arbitrary square-integrable vector field, including a justified quadratic remainder. Kernel regularity must cover both stated families under Matérn smoothness s>1. An equivalent valid direct Taylor argument receives the same credit.
- **4 points: Cross-lengthscale descent control.** Establishes sufficient comparison between the update-lengthscale and terminal-lengthscale witness gradients to obtain a negative terminal-gradient energy term with a vanishing normalized mismatch error. The reference Fourier route must justify its Gaussian and Matérn spectral multipliers, the positive-definiteness/probability-law construction, the needed noise moment bound, and its use in the descent comparison. Alternatively, a justified uniform gradient-continuity estimate and a valid adjustment of the positive contraction constant earn the full four points without constructing a convolution law. Other complete valid comparisons receive equivalent credit. Merely naming Fourier analysis, Bochner's theorem, continuity, or a convolution method without establishing the comparison used earns at most partial credit.
- **2 points: Contractive recursion.** Combines the one-step estimate with the trajectory-wise gradient-dominance assumption and obtains a recursion with a positive time-independent contraction constant and an additive error of the form gamma_t eta_t, where eta_t tends to zero. Correctly controls all lengthscale and quadratic errors, constants, and the endpoint where current and terminal lengthscales coincide.
- **2 points: Limit argument.** Iterates the recursion and rigorously proves convergence using the divergent step-size sum and a finite-prefix/tail, telescoping, or equivalent discrete Gronwall argument. Does not introduce an unsupported square-summability or error-summability assumption.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the stated assumptions. Constants may be renamed or enlarged. Do not require the reference proof's Fourier normalization conventions or its particular intermediate estimates. Standard Fourier-transform and positive-definiteness theorems may be used when their relevant hypotheses are satisfied; the paper-specific comparison still needs justification.

A complete proof may earn 10 points without a convolution construction. In particular, direct uniform lengthscale continuity can be combined with the bounded factors (r_t/r)^d to obtain a different fixed positive contraction constant. Do not penalize this route for omitting an unused noise representation or noise moment bound.

A proof that assumes its required cross-lengthscale comparison or descent inequality without establishing it has omitted a core obligation and cannot receive full credit for that step. If a later recursion or limit argument is independently established correctly, award those points according to their actual validity. Both kernel choices and the allowed equality r_t=r must be covered, whether explicitly or by estimates that already include them.
