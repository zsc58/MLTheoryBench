# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps for the Pair-Comparison Proof

- **2 points:** Derives theta-uniform all-order finite-horizon moment bounds and a usable one-step pair-kernel stability estimate from the primitive assumptions. Controls the finitely many propagated additive constants. Projector boundedness suffices; a global Lipschitz assertion for the projector is neither supplied nor required.
- **3 points:** Correctly lifts to overlapping pair laws and telescopes through the reverse kernels. Uses the specified terminal pseudo-point or an equivalent explicit terminal-momentum treatment, rather than adding an ordinary forward transition at the terminal time.
- **3 points:** Gives a valid local coupling or conditional argument that bounds the pair discrepancy by a square root of the tangential squared residual plus finite theta-independent terms. Correctly handles the retained coordinate, the full Gaussian mean, normal residual, and potentially singular covariance. An independent Gaussian coupling is sufficient; no Gelbrich formula is required.
- **2 points:** Bounds the terminal discrepancy using the fixed terminal base laws and theta-uniform propagation, and converts local square roots into the stated linear objective plus theta-independent constants. Keeps the terminal training expectation under the forward terminal position law and the fresh conditional momentum prior.

# Evaluator Notes

Accept a complete valid alternative proof and assign credit according to the obligations it actually closes, not according to whether it follows the reference presentation.

In particular, the target only requires finite constants independent of theta on a fixed grid. A proof deriving a uniform second-moment bound for the generated law, then bounding W_2 by independent coupling and taking a sufficiently large C_2, proves the literal target and earns **10 points** if complete. Do not demand a nontrivial dependence on the loss, a sharp C_2, or constants uniform over grid refinement.

Do not treat the propagated terminal discrepancy itself as independent of theta. Only an established uniform upper bound is independent of theta.

Do not identify an expectation under the terminal position prior with an expectation under the forward terminal position law. No domination or density-ratio hypothesis is present. A true forward conditional kernel is specified only almost everywhere under its own conditioning law and cannot be used integrably under an unrelated prior without justification.

A solution must not assume the pair stability or uniform propagated moments that it needs without deriving them or giving another complete argument from the public assumptions. The public task does not grant an unspecified stability theorem.

The unweighted objective is used. Gamma=0 and zero or singular covariance are permitted, so a proof requiring a positive Gaussian density or division by 1-a_j^2 must handle these cases separately. Empty constraint families and rank-deficient projectors are permitted. For N=1, products with no kernels are identities.
