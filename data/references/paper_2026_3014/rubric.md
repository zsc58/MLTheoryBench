# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the source-faithful, unhalved loss normalization and the dataset-conditional experiment. Derives the empirical cutoff ELBO bound from monotonicity and the generalized inverse, obtains the population bound under alternatives 1 or 2, and handles zero tolerance without division by zero. It suffices to use w(t)>=32 varepsilon for t>delta; attainment at delta is not required.
- **3 points:** Establishes the conditional reverse-process KL inequalities with the correct energy coefficient and the same generated law. Justifies terminal population and expected empirical KL control for both kappa>0 and kappa=0, and treats the almost-sure third alternative correctly. A standard localized Girsanov entropy estimate may be invoked if its relevant statement and hypotheses are supplied and verified.
- **3 points:** Uses Pinsker and the metric/L2 triangle inequality to obtain expected squared TV at most 1/8. Establishes Gaussian-ball separation, including contraction of the centers, iid small-ball averaging, and a union bound, yielding n rho(8 sqrt(d) sigma_delta)>=(2-sqrt(2))/3 for sufficiently small delta, or an equally strong valid estimate.
- **2 points:** Applies the lower order-2 Renyi-dimension definition with the correct sign when dividing by log r, absorbs the fixed positive constant through exponent slack, and concludes n>=(8 sqrt(d) sigma_delta)^(-d'/2). Handles d'<=0 and dimension zero using n>=1 and a cutoff scale below one. The small-cutoff threshold must not depend on n or the trained score.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular positive constants when another argument proves the stated numerical target for sufficiently small delta.

Do not require a Fisher-information lower bound as a theorem-critical step. The preceding deterministic-score lemma is optional background. Its unconditional marginal substitution is not valid for an arbitrary dataset-dependent score, and a proof using that substitution without a valid replacement has a genuine gap.

The public losses are unhalved squared-error losses. For drift difference 2 times the score error and diffusion coefficient sqrt(2), the entropy cost equals this loss. Using a factor 1/2 in the loss without correcting the rest of the argument is an error.

Treat omission of the terminal-KL justification, misuse of dataset conditioning, a wrong Girsanov coefficient, failure to justify the common-law TV comparison, or an incorrect Renyi-dimension conversion as theorem-critical gaps. For kappa=0, the elementary bound sigma^2/(4T) is sufficient; a stationary-OU argument containing kappa^{-1} is not defined.

The third alternative holds almost surely over S. A KL inequality on only one favorable realized dataset is not the stated assumption. An expected population KL bound may be used in a proof because the public almost-sure bound implies it, but the evaluator must not silently replace the public assumption with a different experiment.

An inverse cutoff need not attain the level at its endpoint. Endpoint values are irrelevant to the Lebesgue integral. Zero tolerance is included and must be addressed; positivity of the density almost everywhere supplies the necessary local argument.
