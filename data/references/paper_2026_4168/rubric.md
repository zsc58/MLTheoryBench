# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

All step indices and sums below range over I_T={2,...,T}.

- **2 points:** Derives the matched-covariance Gaussian likelihood-ratio formula and its conditional N(-m_t,2m_t) lognormal representation. Establishes or correctly invokes the conditional mean-one identity and uniform second- and absolute third-moment controls, including m_t=0. A valid standard lognormal moment argument is acceptable; the reference proof's fourth-moment route is not required.
- **4 points:** Establishes the product-to-sum comparison by Taylor expansion near zero. Controls the aggregate cubic remainder, both generator tails and quadratic tails, and the change from E[(S_T+B_T)^2] to E[S_T^2] using the stated product-remainder bounds. Also justifies the summed per-step Taylor comparison. Equivalent rigorous truncation arguments receive full credit.
- **2 points:** Aggregates the uniform conditional moment estimates to obtain sum_t E[delta_t^2]=2a_T+o(a_T) and sum_t E|delta_t|^3=o(a_T), and uses the assumed cross-moment equalities to identify E[S_T^2]=sum_t E[delta_t^2]. Recognizes that the third moment of S_T and the product-remainder bounds are hypotheses, not consequences that must be established from orthogonality alone.
- **2 points:** Uses conditional expectation and the correct forward pair marginals to identify E_loc G(delta_t)=E_{nu_{T,t}}h_G(m_t), and concludes E_loc G(R_T-1)=L_G+o(a_T) with the stated positive normalization and the necessary finiteness for the asymptotic comparison.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, intermediate labels, or ordering. The public task does not use labels (A1)-(A6) or (D1)-(D4), and no answer should be required to introduce them.

The task concerns the nonendpoint Gaussian reverse steps. Reindexing them as a family of T-1 increments is acceptable. The first reverse step is outside the defined objective and product; no proof of a negligible endpoint contribution is required or authorized. Do not silently replace the actual endpoint posterior by an abstract Gaussian comparison kernel or add an endpoint term to the conclusion.

Cross-step independence is not assumed and must not be silently used. The auxiliary local draws are not identified with the forward-trajectory coordinates. The conclusion concerns the stated auxiliary product, not the full path-space divergence or an upper bound on the marginal data/model divergence.

Treat omission of a necessary nonlinear product-remainder or tail-control argument as a theorem-critical gap. In particular, convergence in probability and control of the generator's tail alone do not justify replacing a truncated quadratic expectation by its full expectation; the quadratic tail must also be controlled, explicitly or by a valid equivalent estimate.

Uniformity of moment constants across timesteps must be justified by the deterministic smallness bound. Do not require global finiteness of h_G(m) for every m>=0: the stated tail assumptions and local estimates supply the finiteness needed at the random mismatches in the asymptotic regime.
