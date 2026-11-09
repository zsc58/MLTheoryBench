# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points — Differentiation and integrability:** Establishes the finite-recursion first variation, or an equivalent rigorous differentiation argument, and supplies integrable domination sufficient to exchange differentiation and expectation. Bounded derivatives, finite products of Gaussian coordinates, and finite depth suffice. An adapted-adjoint proof may establish its conditional projections and backward moments here, but these constructions are not mandatory for a direct proof.
- **3 points — Reverse-sweep identity and unbiasedness:** Carries out the pathwise reverse-mode or telescoping identity with the correct h-weighted normalization, including the h^{-1/2} diffusion-control term. Identifies the ambient Riesz gradient and proves E[hat g(u)]=nabla J(u). Explains why independent fresh trajectory sampling gives conditional unbiasedness at the current iterate.
- **2 points — Uniform stochastic-gradient control:** Derives a uniform sample second-moment or variance bound sufficient for convergence, with coefficients multiplying 1+V_H(N) and (1+V_H(N))/h. Correctly handles the possible dependence of hat p_{n+1} and xi_n, for example through Holder's inequality and Gaussian fourth moments. A sample second-moment bound is fully acceptable and can be used directly in the SGD proof.
- **3 points — Projected-SGD convergence:** Uses projection non-expansiveness, conditional unbiasedness, and constrained first-order optimality together with strong convexity to derive a valid mean-square recurrence. Closes the diminishing-stepsize argument with mu alpha_0>1, a suitable starting index, and control of the finite initial segment. Obtains the stated bound for every K>=1 with constants independent of K and with the permitted fixed-architecture dependence. Justifies existence and uniqueness of the constrained minimizer, or correctly invokes finite-dimensional coercive strongly convex minimization after checking its hypotheses.

# Evaluator Notes

Accept any complete valid alternative proof under the public assumptions. The task asks for deterministic-parameter unbiasedness and the projected-SGD rate, not for a separate adapted stochastic maximum principle, innovation representation, or backward-equation theorem. Do not deduct points merely because a correct direct pathwise proof omits those intermediate constructions. If a solver uses the adapted route, however, the conditional product with fractional noise must be computed correctly; treating a fractional increment as independent of its past is not valid in general.

Do not award full credit for merely naming reverse differentiation, an adjoint, a moment estimate, or a Robbins–Monro argument without establishing the necessary identities, bounds, and hypotheses. A solver may avoid the smoothness-based gradient estimate by using the uniform sample second-moment bound directly. It is also valid to derive an architecture-dependent moment bound directly from bounded derivatives and Gaussian polynomial domination rather than use the stated moment closure.

The gradient is the ambient gradient on H_det, including at a boundary point of U_det. At a constrained minimizer, the variational inequality replaces the generally false assertion nabla J(u*)=0. The new sample is independent of the algorithmic past; coordinates within one trajectory need not be independent. No uniformity in N, h, or H is required beyond the specified constant dependencies. N=1, H=1/2, V_H(N)=0, and singleton or lower-dimensional feasible sets must not be excluded.

The control-independent-diffusion specialization is not a separate public conclusion and earns no mandatory points. If discussed, its explicit diffusion-control contribution vanishes because sigma_u=0. No minibatch corollary or other unasked source result is required.
