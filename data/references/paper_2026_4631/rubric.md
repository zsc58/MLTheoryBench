# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly identifies the combined box-distance objective, establishes F≥0 and F^{-1}(0)=C, and proves convexity for the componentwise-convex nonlinear inequalities and affine box constraints.
- **2 points:** Establishes the required differentiability and gradient formula, proves that H_k=J_g(y^k)^T J_g(y^k)+lambda I is positive definite, and correctly relates the prescribed step to its gradient and metric quantities. Supplies the operator bounds needed by the chosen proof, including H_k≼(sigma^2+lambda)I once sublevel invariance is known.
- **3 points:** Provides a valid nonlinear majorization argument and proves sufficient descent and sublevel invariance under exactly the stated regularization assumption. In the reference route, retain the combined residual r+Js in the Taylor remainder, use ||r+Js||^2=||r||^2-||Js||^2-2lambda||s||^2, and obtain F(y^{k+1})≤F(y^k)-(1/2)q_k^TH_k^{-1}q_k. A different fully justified estimate sufficient for the requested rate receives the same credit. Merely naming Levenberg–Marquardt, smoothness, or a source-derived descent estimate does not close this step.
- **2 points:** Uses convexity, the distance-radius hypothesis, and the preconditioned metric inequality to obtain F(y^{k+1})≤F(y^k)-F(y^k)^2/[2R^2(sigma^2+lambda)], or establishes an equally strong recurrence by a valid alternative route.
- **1 point:** Telescopes reciprocal objective values to obtain the exact displayed rate and F(y^k)→0. Handles F(y^0)=0, possible later attainment of zero, R>0 when F(y^0)>0, and k=0 without dividing by zero.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular residual identity when an alternative argument closes the same obligations.

The corrected regularization inequality appearing in the public task is part of the benchmark contract. A proof that silently replaces it by a stronger inequality is not a complete proof of this task. In particular, the source's separated Taylor estimate has remainder coefficient LM+L^2M^2/(32lambda); the public condition bounds that coefficient by lambda, not lambda/2. Direct absorption of that separated coefficient into (lambda/2)||s||^2 is invalid. The reference proof repairs the estimate rather than strengthening the hypothesis.

The squared-increment bound has coefficient 1 on ||Js||^2 before application of the outer smoothness factor 1/2. Operator-norm submultiplicativity is an inequality, not a general equality.

Do not require a full-row-rank assumption, compactness of S, a minimizer of a hidden auxiliary optimization problem, or results from the separate linear-convergence branch. The frozen convergence target is F(y^k)→0; do not require an additional proof that the vector sequence converges to a single feasible point. No private proof obligation remains unresolved.
