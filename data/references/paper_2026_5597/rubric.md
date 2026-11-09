# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(3 points) Low-rank quadratic reduction.** Compare the actual and ideal softmax laws; establish a Taylor expansion of the ideal mean action with a universal, dimension-independent remainder; obtain a common term plus a fixed quadratic form and an O(epsilon) residual; symmetrize and prove the full inequality `||W_m^*||_*<=rank(W_m^*)<=2s`. The proof must cover epsilon=0.
2. **(2 points) Bandit gradient estimator.** Differentiate the routing-policy loss and establish conditional unbiasedness under the full information timing. Noise must be averaged conditional on the selected model and sampled item as well as the history and query. Establish a universal conditional bound on `E[sum_m ||hat G_{t,m}||_2^2|history,q_t]`; an almost-sure bounded-gradient claim is not justified by sub-Gaussian noise. Rank at most one includes zero blocks.
3. **(2 points) Hypentropy geometry.** Establish the block decomposition of the potential and divergence, nuclear/spectral norm duality, and the nuclear-norm curvature bound required for OMD. A direct spectral-Hessian and weighted Cauchy-Schwarz derivation is supplied in the reference proof. Merely naming the specialized hypentropy theorem does not complete this step; provide a derivation or a mathematically complete alternative argument yielding the needed geometry. Standard differentiable spectral-function calculus is acceptable with its applicable hypotheses identified.
4. **(3 points) Expected fixed-comparator OMD regret.** Derive the mirror-descent three-point/stability inequality, bound initial divergence for every comparator including zero and arbitrarily small blocks, take expectations for each fixed comparator using conditional unbiasedness, and only then take the comparator supremum. Substitute `tau=2s`, `beta=2s/d_q`, and `eta=sqrt(M log d_q/T)` to obtain the universal upper bound `O(s sqrt(MT log d_q))`.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its numerical constants. The structural and optimization claims are both required; no conversion to exact policy regret is requested.

The public benchmark is `sup_U E[sum_t <grad L_t(W_t),W_t-U>_F]`, where U is a fixed element of the stated product ball. It is not `E[sup_U sum_t ...]`. Do not demand a trajectory-dependent-comparator or martingale-supremum argument. Conversely, conditional unbiasedness alone does not justify exchanging expectation and supremum or conditioning on the completed adaptive query sequence.

The initial-divergence bound `rho log(3rho/beta)` is invalid for sufficiently small positive rho and is undefined as printed at rho=0. Accept bounds such as `rho asinh(rho/beta)` or the uniform `tau asinh(tau/beta)`, followed by the parameter-specific logarithmic estimate. A proof that unnecessarily divides by a comparator norm must handle zero separately.

A solver must establish the substantive quadratic-reduction and OMD steps rather than merely naming softmax expansion, REINFORCE, hypentropy, or mirror descent. The source's specialized hypentropy citation is not an assumed public lemma. No unresolved reference-proof obligation is being treated as a completed scoring step.

Score downstream regret only to the extent that its comparator domain, noise conditioning, expectation order, and dimension-independent constants are correctly established. All finite positive M,s,T and d_q>=2 are covered, including M=1; zero queries and singleton nonempty action sets are permitted.
