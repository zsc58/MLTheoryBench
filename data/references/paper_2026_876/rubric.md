# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the normalized power definition on the full simplex. Justifies that the denominator is positive and handles zero coordinates, either directly through the positive support or by a valid boundary-continuity argument.
- **4 points:** Establishes monotonicity of every convex-function sum, or gives an equivalent full majorization argument. For a derivative proof, correctly derives the derivative/covariance expression and its nonnegative sign, and justifies passage from differentiable to arbitrary finite convex functions on R. This is the central bottleneck.
- **2 points:** Correctly concludes $\pi_{\beta_1}\prec\pi_{\beta_2}$ for every simplex vector and every $0<\beta_1<\beta_2$, with the orientation and quantifiers correct. The proof must accommodate ties, singleton support, and $K=1$, whether explicitly or automatically through its argument.
- **2 points:** Correctly derives monotonicity of every symmetric Schur-concave functional and specifically the requested Shannon entropy inequality. Recognizing and correctly using the standard Schur-concavity of Shannon entropy is sufficient; another entropy example does not replace the requested Shannon conclusion.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices, covariance method, explicit averaging approximation, or regularized entropy functions.

The public domain is the entire simplex. Finite logits represent only its strictly positive part. A proof confined to positive coordinates needs a support reduction or a justified limiting argument to cover boundary distributions. Treat a missing boundary extension as a localized gap if the positive-coordinate proof is otherwise complete and extends routinely.

A proof that tests only differentiable convex functions must justify coverage of all convex functions in the public definition, unless it establishes an equivalent full majorization criterion instead. The needed approximation is valid for restrictions of finite convex functions on R; do not require or accept the false general assertion that every finite convex function defined only on a closed interval is uniformly approximable by continuous functions. An omitted routine approximation argument is a localized gap, whereas a missing global majorization argument is theorem-critical.

Do not require separate case splits when the argument already covers ties, singleton support, and $K=1$. Do not award a full proof merely for citing the specialized power-tempering theorem that is itself the target. Standard equivalent majorization criteria and standard Schur-concavity facts may be used correctly.

The entropy direction is $H(\pi_{\beta_1})\geq H(\pi_{\beta_2})$. The opposite sign in the source's explanatory paragraph is a recorded local source error, not an alternative acceptable convention under the public definition.
