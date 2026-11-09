# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points — Gaussian localization:** Derives a simultaneous event of probability tending to one controlling the normalized head Gram error by O(chi_{n,k}), the tail operator width by O(w_k), the head compression by O(w_k chi_{n,k}), the off-diagonal block by O(w_k), the squared-spectrum operator norm by O(w_k^2), and its trace by (1+o(1))S_k. Uses rank-k interlacing and k w_k^2=o(S_k) to retain a constant fraction of S_k on the tail band. Correct equivalent concentration arguments receive full credit.
- **4 points — Signed-flow upper bound:** Uses the correct conditional mean risk and its head-bias, tail-leakage, head-variance, and tail-variance decomposition. Quantitatively proves the noncontractive localization step, or a valid alternative: the head-map error is O(rho chi_{n,k}+rho^2(1+L)) for rho=w_k/lambda_-, and head-supported exposure is O(1/lambda_-). Controls the ideal head residual using L chi_{n,k}->0, the perturbation using rho L->0, and tail noise by O(V_{T,k}L^2), obtaining the requested total rate. Merely naming invariant graphs, Riccati theory, Duhamel, or a paper-specific upper-bound lemma does not close this step.
- **2 points — Rescaling and positive comparators:** Establishes the ridgeless head-map approximation diag(q_j)+o(1). Justifies uniformity over bounded scalar c and excludes unbounded c by coercivity before taking the rescaling infimum. Proves the positive lower bound uniformly for both all nonnegative ridge parameters and all ordinary gradient-flow times, using a justified empirical head-map argument. Scalar population-eigenvalue substitution or an unsupported squared Loewner-order inequality is insufficient.
- **2 points — Negative endpoints and separation:** Handles the exact class 0<=nu<mu_hat_min^+. Derives tail-band variance and the uniform resolved-head noise floor. Treats admissible nu>a and |a-nu|=O(w_k) through tail variance, and derives the head-bias bound using a positive tail resolvent only when b=a-nu is sufficiently larger than w_k. Obtains the infimum over the deterministic envelope variable b>=0 without confusing that variable with the estimator domain. Proves the simplified rate by a valid two-case bound at b_k^*, and deduces the shape and conditional polynomial-separation conclusions.

# Evaluator Notes

Accept any complete valid alternative proof under the public assumptions; the named source proof architecture is not mandatory. The reference proof reconstructs all theorem-critical source arguments and has no unresolved proof obligations.

Risk is averaged over training noise conditional on X. The estimator itself remains noisy, but its realized error must not be substituted for conditional squared bias and then supplemented by another variance term. Oracle infima are taken after the conditional expectation, pointwise in X; no adaptation to the training-noise realization is part of these comparator definitions.

The restored projected-square-mass assumption is a hypothesis, not a conclusion a solver must establish from the other assumptions. Conversely, r_k->0 follows from the stated hypotheses and need not be imposed again. The cases k=1, coincident head scales, and Delta_shape=0 are allowed: a strictly positive shape defect is required only for the corresponding final separation consequence. No lower-edge asymptotic or additional flat-tail assumption is required.

The endpoint head-bias estimate need not hold near the tail band. A proof must justify the envelope there using variance or another valid argument. The head-noise floor uses the nonnegativity of nu, and cannot be imported unchanged for an enlarged class with arbitrarily negative shifts. All probability and uniformity claims must cover the full stated parameter sets, including zero ridge penalty, zero flow time, unbounded flow times and ridge penalties, and endpoints arbitrarily close to their admissibility boundary.
