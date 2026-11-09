# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **Step 1 (3 points):** Uses the independent revealed selector and derives both mutual-information averaging identities. Justifies the needed measurability, integrability, and almost-everywhere admissibility of deterministic sections. The uniform-selector representation is already part of the public setup, so proving a separate representation theorem is not required.
- **Step 2 (2 points):** Constructs a jointly measurable selector time-sharing scheme realizing every finite convex combination of deterministic attainable points and checks its admissibility.
- **Step 3 (3 points):** Proves arbitrary randomized points lie in the closed convex hull using a valid separating-hyperplane contradiction or another complete argument. In the separation proof, verifies integrability of the separating linear functional and uses deterministic membership only almost everywhere.
- **Step 4 (2 points):** Passes to closure, identifies the randomized frontier, proves concavity with potentially infinite values, and proves approximation by at most two deterministic predictors with utility at least phi_R(v)-epsilon and violation at most v+epsilon. A complete method first obtains a finite convex approximation and then maximizes utility over its weights at fixed average violation, proving that an optimizer can have support at most two. Equivalent correct geometric or optimization arguments are accepted.

# Evaluator Notes

Accept any correct alternative proof. Do not require the reference proof's presentation. Do not award credit for merely naming convexification or a separation theorem without establishing the corresponding mathematical steps.

A constant predictor gives (0,0), so all nonnegative-budget feasible slices are nonempty. Individual admissibility does not imply that the frontier is finite everywhere; concavity must be understood in the extended-valued sense. The two-predictor approximation is required only when the frontier value is finite and must include the case v=0.

Do not demand exact attainment, exact-budget approximation without the allowed epsilon slack, or a global compactness assumption. A bare appeal to planar geometry is insufficient unless the argument establishes the hypotheses needed to reduce support to two. General planar convex combinations may require three points; a valid proof must exploit the frontier objective or otherwise justify the two-point reduction. In the finite-support argument, preserving average violation while increasing utility is sufficient; preserving both coordinates of the initial approximation is not required.
